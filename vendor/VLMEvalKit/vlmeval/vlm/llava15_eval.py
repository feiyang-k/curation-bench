"""LLaVA-1.5 evaluation wrapper using HuggingFace transformers.

Supports both vLLM (batched, 10-20x faster) and HF generate backends.
Does NOT require the separate `llava` package — uses HF
`LlavaForConditionalGeneration` directly.
"""

import os

import torch
from .base import BaseModel


class LLaVA15Eval(BaseModel):
    INSTALL_REQ = False
    INTERLEAVE = True
    _cached_llm = None
    _cached_model_path = None

    def __init__(self, model_path, use_vllm=False, **kwargs):
        self.model_path = model_path
        self.use_vllm = use_vllm

        if self.use_vllm:
            from vllm import LLM
            from transformers import AutoProcessor

            os.environ.setdefault("VLLM_WORKER_MULTIPROC_METHOD", "spawn")
            self.processor = AutoProcessor.from_pretrained(model_path)
            if (
                LLaVA15Eval._cached_llm is not None
                and LLaVA15Eval._cached_model_path == model_path
            ):
                self.llm = LLaVA15Eval._cached_llm
            else:
                gpu_mem_util = float(os.environ.get("VLLM_GPU_MEMORY_UTILIZATION", "0.9"))
                self.llm = LLM(
                    model=model_path,
                    dtype="bfloat16",
                    trust_remote_code=True,
                    limit_mm_per_prompt={"image": 5},
                    gpu_memory_utilization=gpu_mem_util,
                )
                LLaVA15Eval._cached_llm = self.llm
                LLaVA15Eval._cached_model_path = model_path
        else:
            from transformers import AutoProcessor, LlavaForConditionalGeneration

            self.processor = AutoProcessor.from_pretrained(model_path)
            try:
                import flash_attn  # noqa: F401
                attn = {"attn_implementation": "flash_attention_2"}
            except ImportError:
                attn = {}
            model = LlavaForConditionalGeneration.from_pretrained(
                model_path,
                torch_dtype=torch.bfloat16,
                low_cpu_mem_usage=True,
                **attn,
            )
            self.model = model.eval().cuda()
            self.hf_kwargs = dict(
                do_sample=False,
                temperature=0,
                max_new_tokens=128,
                top_p=None,
                num_beams=1,
            )

    @staticmethod
    def _pad_to_square(image):
        """Pad image to square matching original LLaVA expand2square()."""
        from PIL import Image

        w, h = image.size
        if w == h:
            return image
        s = max(w, h)
        # CLIP image mean as background color (matches original LLaVA)
        bg = (122, 116, 104)
        result = Image.new("RGB", (s, s), bg)
        result.paste(image, ((s - w) // 2, (s - h) // 2))
        return result

    def _parse_message(self, message):
        from PIL import Image

        images, prompt_parts = [], []
        for item in message:
            if item["type"] == "image":
                img = Image.open(item["value"]).convert("RGB")
                images.append(self._pad_to_square(img))
            elif item["type"] == "text":
                prompt_parts.append(item["value"])
        prompt = "\n".join(prompt_parts)
        conversation = [
            {
                "role": "user",
                "content": [
                    *[{"type": "image"} for _ in images],
                    {"type": "text", "text": prompt},
                ],
            },
        ]
        text = self.processor.apply_chat_template(
            conversation, add_generation_prompt=True, tokenize=False
        )
        return text, images

    def generate_inner(self, message, dataset=None):
        if self.use_vllm:
            return self._generate_vllm(message, dataset=dataset)
        return self._generate_hf(message, dataset=dataset)

    def generate_inner_vllm_batch(self, messages, dataset=None):
        """Batch generate for vLLM — process all messages in one call."""
        from vllm import SamplingParams

        inputs = []
        for msg in messages:
            text, images = self._parse_message(msg)
            inputs.append({"prompt": text, "multi_modal_data": {"image": images}})
        sampling_params = SamplingParams(temperature=0, max_tokens=128)
        outputs = self.llm.generate(inputs, sampling_params=sampling_params)
        return [out.outputs[0].text for out in outputs]

    def _generate_vllm(self, message, dataset=None):
        from vllm import SamplingParams

        text, images = self._parse_message(message)
        sampling_params = SamplingParams(temperature=0, max_tokens=128)
        outputs = self.llm.generate(
            {"prompt": text, "multi_modal_data": {"image": images}},
            sampling_params=sampling_params,
        )
        return outputs[0].outputs[0].text

    def _generate_hf(self, message, dataset=None):
        text, images = self._parse_message(message)
        inputs = self.processor(
            text=text, images=images or None, return_tensors="pt"
        ).to(self.model.device)
        with torch.no_grad():
            output = self.model.generate(**inputs, **self.hf_kwargs)
        input_len = inputs["input_ids"].shape[1]
        return self.processor.decode(
            output[0][input_len:], skip_special_tokens=True
        )
