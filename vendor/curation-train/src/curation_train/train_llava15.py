"""LLaVA-1.5 training entrypoint for curation-train.

Launched via accelerate:
    accelerate launch train_llava15.py --config_json path/to/config.json
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
    LlavaForConditionalGeneration,
    Trainer,
    TrainingArguments,
)

logger = logging.getLogger(__name__)

VICUNA_SYSTEM_MSG = (
    "A chat between a curious user and an artificial intelligence assistant. "
    "The assistant gives helpful, detailed, and polite answers to the user's questions."
)

# Chat template matching the base model's template, but with `</s>` appended
# INSIDE the {% generation %} block so EOS is part of the assistant span and
# gets supervised by the assistant-token mask. Without this, the model never
# sees EOS as a prediction target and fails to stop cleanly at inference —
# which breaks MC benchmarks that rely on strict answer extraction.
LLAVA_CHAT_TEMPLATE_WITH_EOS = (
    "{% for message in messages %}"
    "{% if message['role'] != 'system' %}{{ message['role'].upper() + ': '}}{% endif %}"
    "{% for content in message['content'] | selectattr('type', 'equalto', 'image') %}"
    "{{ '<image>\n' }}"
    "{% endfor %}"
    "{% if message['role'] != 'assistant' %}"
    "{% for content in message['content'] | selectattr('type', 'equalto', 'text') %}"
    "{{ content['text'] + ' '}}"
    "{% endfor %}"
    "{% else %}"
    "{% for content in message['content'] | selectattr('type', 'equalto', 'text') %}"
    "{% generation %}{{ content['text'] + '</s>' }}{% endgeneration %}"
    "{% endfor %}"
    "{% endif %}"
    "{% endfor %}"
    "{% if add_generation_prompt %}{{ 'ASSISTANT:' }}{% endif %}"
)


@dataclass
class ScriptArguments:
    config_json: str = field(metadata={"help": "Path to JSON config file"})


def _pad_to_square(image: Image.Image) -> Image.Image:
    """Pad image to square matching original LLaVA expand2square().

    HF's CLIPImageProcessor does resize→center_crop which loses edge content.
    Original LLaVA pads to square first using CLIP image mean as background,
    so center_crop becomes a no-op on the spatial dimension.
    """
    w, h = image.size
    if w == h:
        return image
    s = max(w, h)
    # CLIP image mean: [0.48145466, 0.4578275, 0.40821073] * 255
    bg = (122, 116, 104)
    result = Image.new("RGB", (s, s), bg)
    result.paste(image, ((s - w) // 2, (s - h) // 2))
    return result


def _as_pil_image(value: Any) -> Image.Image:
    """Convert a dataset image cell into PIL RGB, then pad to square."""
    if isinstance(value, Image.Image):
        return _pad_to_square(value.convert("RGB"))
    if isinstance(value, dict):
        if "bytes" in value and value["bytes"] is not None:
            from io import BytesIO

            return _pad_to_square(Image.open(BytesIO(value["bytes"])).convert("RGB"))
        if "path" in value and value["path"]:
            return _pad_to_square(Image.open(value["path"]).convert("RGB"))
    if hasattr(value, "convert"):
        return _pad_to_square(value.convert("RGB"))
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
) -> torch.Tensor:
    """Build labels using the chat template's `{% generation %}` markers.

    The chat template wraps assistant text in {% generation %}...{% endgeneration %},
    so `apply_chat_template(..., return_assistant_tokens_mask=True)` returns a
    1/0 mask aligned with the *pre-image-expansion* token sequence (one <image>
    token per image). We then expand the mask in lockstep with the processor's
    image-token expansion to align with `expanded_input_ids`.
    """
    tokenizer = processor.tokenizer
    image_token_id = tokenizer.convert_tokens_to_ids("<image>")
    image_seq_len = int(getattr(processor, "image_seq_length", 576))

    encoded = tokenizer.apply_chat_template(
        conversation,
        add_generation_prompt=False,
        tokenize=True,
        return_dict=True,
        return_assistant_tokens_mask=True,
    )
    pre_ids = encoded["input_ids"]
    pre_mask = encoded["assistant_masks"]  # 1 where assistant generation, else 0

    # Expand: each <image> in pre_ids becomes image_seq_len tokens (all masked-out).
    expanded_mask: list[int] = []
    for tok, m in zip(pre_ids, pre_mask):
        if tok == image_token_id:
            expanded_mask.extend([0] * image_seq_len)
        else:
            expanded_mask.append(int(m))

    # The processor's tokenizer call adds BOS while tokenizer.apply_chat_template
    # (tokenize=True) does not (add_bos_token=False in tokenizer_config). Prepend a
    # 0 mask entry so lengths align and the BOS itself is never supervised.
    bos_id = tokenizer.bos_token_id
    if (
        bos_id is not None
        and expanded_input_ids.shape[0] == len(expanded_mask) + 1
        and int(expanded_input_ids[0]) == bos_id
    ):
        expanded_mask.insert(0, 0)

    if len(expanded_mask) != expanded_input_ids.shape[0]:
        # Length mismatch (e.g. processor adds a BOS the chat template did not,
        # or image expansion size differs). Fall back to all-masked rather than
        # silently training on prompt tokens.
        return torch.full_like(expanded_input_ids, -100)

    mask_t = torch.tensor(expanded_mask, dtype=torch.bool)
    labels = expanded_input_ids.clone()
    labels[~mask_t] = -100
    return labels


class Llava15Dataset(Dataset):
    """Arrow dataset wrapper for LLaVA-1.5 HF training."""

    def __init__(self, arrow_dataset, processor: AutoProcessor) -> None:
        self.dataset = arrow_dataset
        self.processor = processor

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
            # Text-only sample: use a blank image + an <image> token so the
            # processor produces matching pixel_values and image tokens.
            # Transformers 5.x asserts feature/token counts match, so we
            # can't drop the token while still passing pixel_values.
            image = Image.new("RGB", (336, 336), (0, 0, 0))

        turns = _normalize_turns(texts)

        conversation: list[dict[str, Any]] = []
        for turn_idx, turn in enumerate(turns):
            user_content: list[dict[str, Any]] = []
            if turn_idx == 0:
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
            images=image,
            return_tensors="pt",
        )

        input_ids = model_inputs["input_ids"].squeeze(0)
        attention_mask = model_inputs["attention_mask"].squeeze(0)

        labels = _build_assistant_labels(conversation, self.processor, input_ids)

        # Truncate after image-token expansion to avoid breaking the
        # image/text token count invariant that the processor checks.
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


class DataCollatorForLlava15:
    """Pad token sequences and stack image tensors."""

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
                try:
                    batch[key] = torch.stack(values)
                except RuntimeError:
                    batch[key] = values
            else:
                batch[key] = values

        return batch


def train() -> None:
    parser = HfArgumentParser((ScriptArguments, TrainingArguments))
    script_args, training_args = parser.parse_args_into_dataclasses(return_remaining_strings=False)

    config = json.loads(Path(script_args.config_json).read_text())
    data_path = config["data_path"]
    model_name = config.get("model_name_or_path", "llava-hf/llava-1.5-7b-hf")

    logger.info("Loading model: %s", model_name)
    torch_dtype = torch.bfloat16 if torch.cuda.is_available() else torch.float32
    model = LlavaForConditionalGeneration.from_pretrained(
        model_name,
        torch_dtype=torch_dtype,
        attn_implementation="sdpa",
    )
    model.config.use_cache = False

    # Liger Kernel: fused RoPE, RMSNorm, SwiGLU, CrossEntropy on Llama backbone
    try:
        from liger_kernel.transformers import apply_liger_kernel_to_llava

        apply_liger_kernel_to_llava(model=model)
        logger.info("Liger kernel applied to LLaVA model")
    except ImportError:
        logger.warning("liger-kernel not installed, skipping kernel optimization")

    # Full finetune: freeze vision tower (matches original LLaVA recipe)
    model.model.vision_tower.requires_grad_(False)
    trainable = sum(p.numel() for p in model.parameters() if p.requires_grad)
    frozen = sum(p.numel() for p in model.model.vision_tower.parameters())
    logger.info("Full finetune: %d trainable, %d frozen (vision tower)", trainable, frozen)

    if training_args.gradient_checkpointing and hasattr(model, "enable_input_require_grads"):
        model.enable_input_require_grads()

    processor = AutoProcessor.from_pretrained(model_name)
    # Override chat template to supervise EOS at end of each assistant turn.
    processor.chat_template = LLAVA_CHAT_TEMPLATE_WITH_EOS
    processor.tokenizer.chat_template = LLAVA_CHAT_TEMPLATE_WITH_EOS

    logger.info("Loading dataset from: %s", data_path)
    ds = load_from_disk(data_path)
    if isinstance(ds, DatasetDict):
        if "train" in ds:
            ds = ds["train"]
        else:
            ds = concatenate_datasets([ds[k] for k in sorted(ds.keys())])

    train_dataset = Llava15Dataset(ds, processor)
    collator = DataCollatorForLlava15(processor)

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

    # Patch tokenizer_config.json for compatibility with transformers 4.x
    # (used by VLMEvalKit's conda env). Transformers 5.x writes
    # "tokenizer_class": "TokenizersBackend" which 4.x doesn't recognize.
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
