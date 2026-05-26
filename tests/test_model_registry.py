from benchmark.core.model_registry import (
    MODEL_REGISTRY,
    ModelConfig,
    get_model,
)

import pytest


def test_all_models_have_required_fields():
    for key, config in MODEL_REGISTRY.items():
        assert isinstance(config, ModelConfig)
        assert config.vlmeval_model_name
        assert config.vlmeval_model_class
        assert config.training_stage in ("finetuning", "posttraining")


def test_get_model_valid():
    assert get_model("qwen2.5-vl-3b-instruct").vlmeval_model_name == "Qwen2.5-VL-3B-Instruct"
    assert get_model("llava-1.5-7b-hf").vlmeval_model_name == "llava-1.5-7b-hf"


def test_get_model_invalid():
    with pytest.raises(ValueError, match="Unknown model_key"):
        get_model("nonexistent")


def test_training_stage_is_explicit():
    assert get_model("qwen2.5-vl-3b-instruct").training_stage == "posttraining"
    assert get_model("llava-1.5-7b-hf").training_stage == "finetuning"


def test_finetuning_method_set():
    assert get_model("llava-1.5-7b-hf").finetuning_method == "llava"
    assert get_model("qwen2.5-vl-3b-instruct").finetuning_method == "qwen"


def test_qwen_vlmeval_name():
    assert MODEL_REGISTRY["qwen2.5-vl-3b-instruct"].vlmeval_model_name == "Qwen2.5-VL-3B-Instruct"
