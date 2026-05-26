"""SmolVLM-Base training entrypoint for curation-train.

Targets `HuggingFaceTB/SmolVLM-Base` specifically — the pre-instruct variant has
no chat template baked in, so we install one that matches the prompt format used
by VLMEvalKit's `vlm/smolvlm.py` eval wrapper (`<|im_start|>User:<image>...
<end_of_utterance>\\nAssistant:`). The trained checkpoint ships this template,
so downstream eval via VLMEvalKit will see a consistent prompt format.

Launched via accelerate (single GPU) or torchrun (multi-GPU); see runner.py.
"""

from __future__ import annotations

import json
import logging
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import torch
from datasets import DatasetDict, concatenate_datasets, load_from_disk
from PIL import Image
from torch.utils.data import Dataset
from transformers import (
    AutoProcessor,
    HfArgumentParser,
    Idefics3ForConditionalGeneration,
    Trainer,
    TrainingArguments,
)

logger = logging.getLogger(__name__)

# Chat template for SmolVLM-Base. The Base model has no chat template, so we
# install one that:
#   * mirrors the prompt format used in VLMEvalKit's SmolVLM wrapper, and
#   * marks the assistant text with `{% generation %}` so the assistant-token
#     mask returned by `apply_chat_template(return_assistant_tokens_mask=True)`
#     can supervise the answer (and its `<end_of_utterance>`) only.
# The leading space inside the generation block lets eval-time prompts that end
# in exactly "Assistant:" (no trailing space) trigger generation that starts with
# the same " ANSWER..." pattern the model saw during training.
SMOLVLM_CHAT_TEMPLATE_WITH_EOS = (
    "<|im_start|>"
    "{% for message in messages %}"
    "{% if message['role'] == 'user' %}"
    "{{ 'User' }}"
    "{% if message['content'][0]['type'] == 'image' %}{{ ':' }}{% else %}{{ ': ' }}{% endif %}"
    "{% for content in message['content'] %}"
    "{% if content['type'] == 'image' %}{{ '<image>' }}"
    "{% elif content['type'] == 'text' %}{{ content['text'] }}"
    "{% endif %}"
    "{% endfor %}"
    "{{ '<end_of_utterance>\n' }}"
    "{% elif message['role'] == 'assistant' %}"
    "{{ 'Assistant:' }}"
    "{% for content in message['content'] | selectattr('type', 'equalto', 'text') %}"
    "{% generation %}{{ ' ' + content['text'] + '<end_of_utterance>\n' }}{% endgeneration %}"
    "{% endfor %}"
    "{% endif %}"
    "{% endfor %}"
    "{% if add_generation_prompt %}{{ 'Assistant:' }}{% endif %}"
)


@dataclass
class ScriptArguments:
    config_json: str = field(metadata={"help": "Path to JSON config file"})


def _as_pil_image(value: Any) -> Image.Image:
    """Convert a dataset image cell into a PIL RGB image.

    SmolVLM's image processor handles its own aspect-aware splitting and
    padding, so we do NOT pad to square here (unlike the LLaVA-1.5 path).
    """
    if isinstance(value, Image.Image):
        return value.convert("RGB")
    if isinstance(value, dict):
        if "bytes" in value and value["bytes"] is not None:
            from io import BytesIO

            return Image.open(BytesIO(value["bytes"])).convert("RGB")
        if "path" in value and value["path"]:
            return Image.open(value["path"]).convert("RGB")
    if hasattr(value, "convert"):
        return value.convert("RGB")
    raise TypeError(f"Unsupported image value type: {type(value)!r}")


def _normalize_turns(texts: Any) -> list[dict[str, str]]:
    if isinstance(texts, str):
        texts = json.loads(texts)
    if isinstance(texts, dict):
        texts = [texts]
    if not isinstance(texts, list):
        return [{"user": str(texts), "assistant": ""}]

    turns: list[dict[str, str]] = []
    for turn in texts:
        if isinstance(turn, dict):
            user = str(turn.get("user", turn.get("human", "")))
            assistant = str(turn.get("assistant", turn.get("gpt", "")))
            turns.append({"user": user, "assistant": assistant})
        else:
            turns.append({"user": str(turn), "assistant": ""})
    return turns or [{"user": "", "assistant": ""}]


def _build_assistant_labels(
    conversation: list[dict[str, Any]],
    processor: AutoProcessor,
    expanded_input_ids: torch.Tensor,
    image_token_id: int,
) -> torch.Tensor:
    """Align pre-expansion assistant mask with the processor's expanded input_ids.

    Strategy: tokenize via `tokenizer.apply_chat_template(...,
    return_assistant_tokens_mask=True)` to get the assistant mask on the
    pre-expansion sequence (each `<image>` placeholder is a single token).
    Then map text-token positions to expanded-token positions: non-image
    tokens map 1:1; the image placeholder at position P expands to a
    contiguous block of length `expansion_len` starting at P. The total
    expansion length is derived from the post- vs pre-expansion length
    difference and the number of image placeholders.

    LLaVA665K samples carry at most one image, so we keep this simple and
    fall back to all-masked for unexpected multi-image cases or any
    alignment failure.
    """
    tokenizer = processor.tokenizer

    encoded = tokenizer.apply_chat_template(
        conversation,
        add_generation_prompt=False,
        tokenize=True,
        return_dict=True,
        return_assistant_tokens_mask=True,
    )
    text_ids = list(encoded["input_ids"])
    text_mask = list(encoded["assistant_masks"])
    full_ids = expanded_input_ids.tolist()

    n_images_text = sum(1 for t in text_ids if t == image_token_id)
    if n_images_text == 0:
        # No image placeholder in the rendered prompt; just align directly.
        expansion_len = 0
    elif n_images_text == 1:
        # Each <image> placeholder expands into `expansion_len` tokens; the
        # placeholder itself contributes 1 to text_ids, so:
        #   len(full_ids) = len(text_ids) - n + n * expansion_len
        # With n = 1 this is exact regardless of per-image variation.
        diff = len(full_ids) - len(text_ids)
        if diff < 0:
            return torch.full_like(expanded_input_ids, -100)
        expansion_len = diff + 1
    else:
        # Multi-image: would need per-image expansion lengths to split `diff`
        # across placeholders. LLaVA665K is single-image, so fall back rather
        # than implement the harder case here.
        return torch.full_like(expanded_input_ids, -100)

    full_mask = [0] * len(full_ids)
    t_idx = 0
    f_idx = 0

    while t_idx < len(text_ids):
        t = int(text_ids[t_idx])
        if t == image_token_id:
            # The processor replaced this placeholder with `expansion_len`
            # tokens in full_ids — skip the whole block (mask stays 0).
            f_idx += expansion_len
            t_idx += 1
        else:
            if f_idx >= len(full_ids) or int(full_ids[f_idx]) != t:
                return torch.full_like(expanded_input_ids, -100)
            full_mask[f_idx] = int(text_mask[t_idx])
            t_idx += 1
            f_idx += 1

    if f_idx != len(full_ids):
        return torch.full_like(expanded_input_ids, -100)

    mask_t = torch.tensor(full_mask, dtype=torch.bool)
    labels = expanded_input_ids.clone()
    labels[~mask_t] = -100
    return labels


class SmolVLMDataset(Dataset):
    """Arrow dataset wrapper for SmolVLM training on LLaVA665K-style data."""

    def __init__(self, arrow_dataset, processor: AutoProcessor) -> None:
        self.dataset = arrow_dataset
        self.processor = processor
        image_token = getattr(processor, "image_token", "<image>")
        self.image_token_id = int(processor.tokenizer.convert_tokens_to_ids(image_token))

    def __len__(self) -> int:
        return len(self.dataset)

    def __getitem__(self, idx: int) -> dict[str, Any]:
        example = self.dataset[idx]
        images = example.get("images")
        texts = example.get("texts")

        if isinstance(images, list):
            image_value = images[0] if images else None
        else:
            image_value = images
        has_image = image_value is not None

        if has_image:
            image = _as_pil_image(image_value)
        else:
            # Text-only sample: feed a tiny black image + an <image> placeholder
            # in the first user turn so the processor produces matching
            # pixel_values and image tokens. SmolVLM asserts feature/token
            # counts match.
            image = Image.new("RGB", (384, 384), (0, 0, 0))

        turns = _normalize_turns(texts)

        conversation: list[dict[str, Any]] = []
        for turn_idx, turn in enumerate(turns):
            user_content: list[dict[str, Any]] = []
            if turn_idx == 0:
                # Image always goes in the FIRST user turn (LLaVA665K
                # convention). The chat template handles the
                # `User:<image>` vs `User: text` spacing.
                user_content.append({"type": "image"})
            user_content.append({"type": "text", "text": turn["user"]})
            conversation.append({"role": "user", "content": user_content})
            conversation.append(
                {
                    "role": "assistant",
                    "content": [{"type": "text", "text": turn["assistant"]}],
                }
            )

        prompt = self.processor.apply_chat_template(
            conversation,
            add_generation_prompt=False,
            tokenize=False,
        )

        model_inputs = self.processor(
            text=prompt,
            images=[image],
            return_tensors="pt",
        )

        input_ids = model_inputs["input_ids"].squeeze(0)
        attention_mask = model_inputs["attention_mask"].squeeze(0)

        labels = _build_assistant_labels(
            conversation,
            self.processor,
            input_ids,
            self.image_token_id,
        )

        # Truncate AFTER image expansion to avoid breaking the image-token
        # count invariant the model checks at forward time.
        max_length = 2048
        if input_ids.shape[0] > max_length:
            input_ids = input_ids[:max_length]
            attention_mask = attention_mask[:max_length]
            labels = labels[:max_length]

        batch: dict[str, Any] = {
            "input_ids": input_ids,
            "attention_mask": attention_mask,
            "labels": labels,
        }
        for key, value in model_inputs.items():
            if key in {"input_ids", "attention_mask"}:
                continue
            batch[key] = value.squeeze(0) if hasattr(value, "squeeze") else value
        return batch


class DataCollatorForSmolVLM:
    """Pad token sequences and stack per-sample image tensors.

    SmolVLM emits `pixel_values` of shape (num_tiles, 3, H, W) and
    `pixel_attention_mask` of shape (num_tiles, H, W); num_tiles varies per
    sample, so we pad along the tile dim before stacking.
    """

    def __init__(self, processor: AutoProcessor) -> None:
        tokenizer = processor.tokenizer
        pad_id = tokenizer.pad_token_id
        if pad_id is None:
            tokenizer.pad_token = tokenizer.eos_token
            pad_id = tokenizer.pad_token_id
        self.pad_token_id = int(pad_id)

    def __call__(self, features: list[dict[str, Any]]) -> dict[str, Any]:
        max_len = max(f["input_ids"].shape[0] for f in features)

        input_ids_list = []
        attention_mask_list = []
        labels_list = []

        for feature in features:
            seq_len = feature["input_ids"].shape[0]
            pad_len = max_len - seq_len
            input_ids_list.append(
                torch.nn.functional.pad(feature["input_ids"], (0, pad_len), value=self.pad_token_id)
            )
            attention_mask_list.append(
                torch.nn.functional.pad(feature["attention_mask"], (0, pad_len), value=0)
            )
            labels_list.append(torch.nn.functional.pad(feature["labels"], (0, pad_len), value=-100))

        batch: dict[str, Any] = {
            "input_ids": torch.stack(input_ids_list),
            "attention_mask": torch.stack(attention_mask_list),
            "labels": torch.stack(labels_list),
        }

        extra_keys = sorted(
            {k for f in features for k in f} - {"input_ids", "attention_mask", "labels"}
        )
        for key in extra_keys:
            values = [f[key] for f in features if key in f]
            if len(values) != len(features):
                continue
            if all(torch.is_tensor(v) for v in values):
                # Pad along the leading "tiles" axis if shapes mismatch
                # (pixel_values: [T, 3, H, W]; pixel_attention_mask: [T, H, W]).
                shapes = [v.shape for v in values]
                if all(s == shapes[0] for s in shapes):
                    batch[key] = torch.stack(values)
                elif len(shapes[0]) >= 1 and all(s[1:] == shapes[0][1:] for s in shapes):
                    max_tiles = max(s[0] for s in shapes)
                    padded = []
                    for v in values:
                        pad_amount = max_tiles - v.shape[0]
                        if pad_amount == 0:
                            padded.append(v)
                        else:
                            zeros_shape = (pad_amount,) + tuple(v.shape[1:])
                            padded.append(torch.cat([v, torch.zeros(zeros_shape, dtype=v.dtype)], dim=0))
                    batch[key] = torch.stack(padded)
                else:
                    batch[key] = values
            else:
                batch[key] = values

        return batch


def train() -> None:
    parser = HfArgumentParser((ScriptArguments, TrainingArguments))
    script_args, training_args = parser.parse_args_into_dataclasses(return_remaining_strings=False)

    config = json.loads(Path(script_args.config_json).read_text())
    data_path = config["data_path"]
    model_name = config.get("model_name_or_path", "HuggingFaceTB/SmolVLM-Base")

    logger.info("Loading model: %s", model_name)
    torch_dtype = torch.bfloat16 if torch.cuda.is_available() else torch.float32
    # SmolVLM-Base ships with `model_type: idefics3` in its config; using the
    # Idefics3 class also matches VLMEvalKit's `vlm/smolvlm.py` eval wrapper,
    # avoiding any class-vs-config mismatch between train and eval.
    model = Idefics3ForConditionalGeneration.from_pretrained(
        model_name,
        torch_dtype=torch_dtype,
        attn_implementation="sdpa",
    )
    model.config.use_cache = False

    # Full finetune: freeze the SigLIP vision encoder (matches the LLaVA-1.5
    # recipe and the original SmolVLM training procedure).
    model.model.vision_model.requires_grad_(False)
    trainable = sum(p.numel() for p in model.parameters() if p.requires_grad)
    frozen = sum(p.numel() for p in model.model.vision_model.parameters())
    logger.info("Full finetune: %d trainable, %d frozen (vision tower)", trainable, frozen)

    if training_args.gradient_checkpointing and hasattr(model, "enable_input_require_grads"):
        model.enable_input_require_grads()

    processor = AutoProcessor.from_pretrained(model_name)
    # SmolVLM-Base has no chat template — install ours (with `{% generation %}`
    # markers so assistant tokens can be identified for the loss mask).
    processor.chat_template = SMOLVLM_CHAT_TEMPLATE_WITH_EOS
    processor.tokenizer.chat_template = SMOLVLM_CHAT_TEMPLATE_WITH_EOS

    # Align tokenizer.eos_token with the turn-ending token the chat template
    # actually trains the model to emit. SmolVLM-Base inherits eos_token =
    # <|im_end|> (id 2) from SmolLM2, but our template ends each assistant
    # turn with <end_of_utterance>. Without this fix, the saved checkpoint's
    # eos disagrees with what the model emits, so eval-time generators (vLLM
    # in particular) never see EOS and run all the way to max_new_tokens —
    # which makes every benchmark sample take ~17s instead of ~0.2s.
    # SmolVLM-Instruct sets it this way too (HuggingFaceTB confirmed).
    eou_id = processor.tokenizer.convert_tokens_to_ids("<end_of_utterance>")
    if eou_id is not None and eou_id != processor.tokenizer.unk_token_id:
        processor.tokenizer.eos_token = "<end_of_utterance>"
        model.config.eos_token_id = eou_id
        if getattr(model, "generation_config", None) is not None:
            model.generation_config.eos_token_id = eou_id
        logger.info("Set eos_token to <end_of_utterance> (id=%d)", eou_id)
    else:
        logger.warning(
            "Could not resolve <end_of_utterance> to a real token id; "
            "eos_token left as %r. vLLM-based eval may not stop cleanly.",
            processor.tokenizer.eos_token,
        )

    logger.info("Loading dataset from: %s", data_path)
    ds = load_from_disk(data_path)
    if isinstance(ds, DatasetDict):
        if "train" in ds:
            ds = ds["train"]
        else:
            ds = concatenate_datasets([ds[k] for k in sorted(ds.keys())])

    train_dataset = SmolVLMDataset(ds, processor)
    collator = DataCollatorForSmolVLM(processor)

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        data_collator=collator,
    )
    trainer.train()

    output_dir = training_args.output_dir
    trainer.save_model(output_dir)

    processor.save_pretrained(output_dir)

    # Patch tokenizer_config.json for transformers 4.x compatibility
    # (same workaround as train_llava15.py for older eval venvs).
    tok_config_path = Path(output_dir) / "tokenizer_config.json"
    if tok_config_path.exists():
        tok_config = json.loads(tok_config_path.read_text())
        if tok_config.get("tokenizer_class") == "TokenizersBackend":
            tok_config.pop("tokenizer_class")
            tok_config.pop("model_specific_special_tokens", None)
            tok_config_path.write_text(json.dumps(tok_config, indent=2, ensure_ascii=False))

    logger.info("Training complete. Model saved to %s", output_dir)


if __name__ == "__main__":
    train()
