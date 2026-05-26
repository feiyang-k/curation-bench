"""Centralized model registry for the benchmark.

Maps model_key (a stable benchmark-side identifier) to downstream tool
names and the curation-train training method.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ModelConfig:
    """Registry entry for a concrete model used in the benchmark."""

    vlmeval_model_name: str  # VLMEvalKit --model name
    vlmeval_model_class: str  # VLMEvalKit model class (documentation)
    training_stage: str  # "finetuning" or "posttraining"
    finetuning_method: str | None = None  # curation-train method name


MODEL_REGISTRY: dict[str, ModelConfig] = {
    # ── Finetuning (curation-train, method="llava") ──────────────────
    "llava-1.5-7b-hf": ModelConfig(
        vlmeval_model_name="llava-1.5-7b-hf",
        vlmeval_model_class="LLaVA15Eval",
        training_stage="finetuning",
        finetuning_method="llava",
    ),
    # ── Finetuning (curation-train, method="smolvlm-256m") ───────────
    # SmolVLM-256M-Base (Idefics3 architecture). Training script installs
    # a custom chat template at train time (Base has none), so the trained
    # checkpoint ships with the prompt format VLMEvalKit's SmolVLM wrapper
    # expects.
    "smolvlm-256m": ModelConfig(
        vlmeval_model_name="SmolVLM-256M",
        vlmeval_model_class="SmolVLM",
        training_stage="finetuning",
        finetuning_method="smolvlm-256m",
    ),
    "smolvlm-500m": ModelConfig(
        vlmeval_model_name="SmolVLM-500M",
        vlmeval_model_class="SmolVLM",
        training_stage="finetuning",
        finetuning_method="smolvlm-500m",
    ),
    # SmolVLM-Base (2.2B). model_key is "smolvlm" (matches runner.py
    # _resolve_method default for the 2.2B variant).
    "smolvlm": ModelConfig(
        vlmeval_model_name="SmolVLM",
        vlmeval_model_class="SmolVLM",
        training_stage="finetuning",
        finetuning_method="smolvlm",
    ),
    # ── Posttraining (curation-train, method="qwen") ─────────────────
    "qwen2.5-vl-3b-instruct": ModelConfig(
        vlmeval_model_name="Qwen2.5-VL-3B-Instruct",
        vlmeval_model_class="Qwen2VLChat",
        training_stage="posttraining",
        finetuning_method="qwen",
    ),
}


def get_model(model_key: str) -> ModelConfig:
    """Look up a model config by key. Raises ValueError if not found."""
    if model_key not in MODEL_REGISTRY:
        raise ValueError(
            f"Unknown model_key {model_key!r}. "
            f"Available: {', '.join(sorted(MODEL_REGISTRY))}"
        )
    return MODEL_REGISTRY[model_key]
