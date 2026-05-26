"""Multimodal finetune execution logic for Qwen and LLaVA methods."""

from __future__ import annotations

import json
import logging
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any

from curation_train.defaults import (
    DEFAULT_LLAVA_MODEL,
    DEFAULT_QWEN_MODEL,
    DEFAULT_QWEN2VL_2B_MODEL,
    DEFAULT_SMOLVLM_MODEL,
    DEFAULT_SMOLVLM_256M_MODEL,
    DEFAULT_SMOLVLM_500M_MODEL,
    LLAVA_FULL_FT_TRAINING_ARGS,
    QWEN_FIXED_TRAINING_ARGS,
    QWEN2VL_2B_FIXED_TRAINING_ARGS,
    SMOLVLM_FULL_FT_TRAINING_ARGS,
)

# All SmolVLM Base variants share the same training script + hyperparams; only
# the default model_name_or_path differs. Keeping effective batch identical
# across sizes also keeps autoresearch comparisons size-controlled.
_SMOLVLM_DEFAULT_MODEL: dict[str, str] = {
    "smolvlm": DEFAULT_SMOLVLM_MODEL,
    "smolvlm-256m": DEFAULT_SMOLVLM_256M_MODEL,
    "smolvlm-500m": DEFAULT_SMOLVLM_500M_MODEL,
}

logger = logging.getLogger(__name__)

_PKG_DIR = Path(__file__).parent
_ALLOWED_OVERRIDES = {
    "max_steps",
    "save_steps",
    "logging_steps",
    "per_device_train_batch_size",
    "gradient_accumulation_steps",
}


def _resolve_method(raw: object) -> str:
    method = str(raw or "qwen").lower().strip()
    if method in {"qwen", "qwen2.5", "qwen25"}:
        return "qwen"
    if method in {"qwen2vl_2b", "qwen2-vl-2b", "qwen2vl2b", "qwen2", "qwen2vl", "qwen2-vl"}:
        return "qwen2vl_2b"
    if method in {"llava", "llava1.5", "llava-1.5"}:
        return "llava"
    if method in {"smolvlm", "smolvlm-base", "smolvlm_base", "smol"}:
        return "smolvlm"
    if method in {"smolvlm-256m", "smolvlm-256m-base", "smolvlm_256m", "smol-256m"}:
        return "smolvlm-256m"
    if method in {"smolvlm-500m", "smolvlm-500m-base", "smolvlm_500m", "smol-500m"}:
        return "smolvlm-500m"
    raise ValueError(
        f"Unsupported training method '{method}'. Use 'qwen', 'qwen2vl_2b', 'llava', "
        "'smolvlm', 'smolvlm-256m', or 'smolvlm-500m'."
    )


def run_finetune(config: dict[str, Any]) -> dict[str, Any]:
    """Run multimodal finetune via accelerate launch.

    Config JSON schema:
        method: str                 — qwen (default) or llava
        data_path: str              — path to Arrow dataset on disk
        output_dir: str             — where to write model outputs
        model_name_or_path: str     — base model (method-dependent default)
        num_processes: int           — number of GPUs (default: auto-detect)

    Returns:
        dict with keys: status, metrics, error
    """
    try:
        method = _resolve_method(config.get("method", "qwen"))
        data_path = config["data_path"]
        output_dir = config["output_dir"]

        if method == "qwen":
            model_name = config.get("model_name_or_path", DEFAULT_QWEN_MODEL)
            train_script = str(_PKG_DIR / "train_qwen2vl.py")
            fixed_args = dict(QWEN_FIXED_TRAINING_ARGS)
        elif method == "qwen2vl_2b":
            model_name = config.get("model_name_or_path", DEFAULT_QWEN2VL_2B_MODEL)
            train_script = str(_PKG_DIR / "train_qwen2vl_2b.py")
            fixed_args = dict(QWEN2VL_2B_FIXED_TRAINING_ARGS)
        elif method in _SMOLVLM_DEFAULT_MODEL:
            # SmolVLM Base variants (2.2B / 500M / 256M) — full finetune,
            # vision tower frozen. Same script + args; only the default model
            # path differs. The user can override via model_name_or_path.
            model_name = config.get("model_name_or_path", _SMOLVLM_DEFAULT_MODEL[method])
            train_script = str(_PKG_DIR / "train_smolvlm.py")
            fixed_args = dict(SMOLVLM_FULL_FT_TRAINING_ARGS)
        else:  # llava — full finetune (vision tower frozen)
            model_name = config.get("model_name_or_path", DEFAULT_LLAVA_MODEL)
            train_script = str(_PKG_DIR / "train_llava15.py")
            fixed_args = dict(LLAVA_FULL_FT_TRAINING_ARGS)

        for key in _ALLOWED_OVERRIDES:
            if key in config:
                fixed_args[key] = config[key]

        # Write the config JSON that the training script reads
        Path(output_dir).mkdir(parents=True, exist_ok=True)
        train_config = {
            "method": method,
            "data_path": data_path,
            "model_name_or_path": model_name,
        }
        train_config_path = str(Path(output_dir) / "train_config.json")
        Path(train_config_path).write_text(json.dumps(train_config, ensure_ascii=False))

        import os as _os
        run_env = _os.environ.copy()
        # Ensure consistent GPU ordering between CUDA runtime and NCCL
        run_env["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"

        num_processes = config.get("num_processes")
        if num_processes is None:
            cuda_devs = run_env.get("CUDA_VISIBLE_DEVICES", "")
            if cuda_devs:
                num_processes = len(cuda_devs.split(","))
            else:
                num_processes = 1

        if num_processes > 1:
            # Use torchrun for reliable multi-GPU DDP
            cmd = [
                sys.executable, "-m", "torch.distributed.run",
                "--nproc_per_node", str(num_processes),
                "--master_port", "29500",
                train_script,
                "--config_json", train_config_path,
                "--output_dir", output_dir,
            ]
        else:
            # Single-GPU: use accelerate launch
            accelerate_bin = shutil.which("accelerate") or f"{sys.executable} -m accelerate"
            cmd = [
                accelerate_bin, "launch",
                "--num_processes", "1",
                "--gpu_ids", "0",
                train_script,
                "--config_json", train_config_path,
                "--output_dir", output_dir,
            ]

        for key, value in fixed_args.items():
            flag = f"--{key}"
            if isinstance(value, bool):
                if value:
                    cmd.append(flag)
            else:
                cmd.extend([flag, str(value)])

        logger.info("Running: %s", " ".join(cmd))

        output_path = Path(output_dir)

        # Let accelerate output flow through to parent's stdout/stderr
        # so the outer caller (session.py) can capture it to files in real-time.
        result = subprocess.run(
            cmd,
            text=True,
            env=run_env,
        )

        # Persist structured log for post-mortem debugging
        log_path = output_path / "train.log"
        with open(log_path, "w") as f:
            f.write(f"=== COMMAND ===\n{' '.join(cmd)}\n\n")
            f.write(f"=== RETURNCODE ===\n{result.returncode}\n")

        # Check for saved model as the success signal
        model_saved = (
            (output_path / "model.safetensors").exists()
            or any(output_path.glob("model-*.safetensors"))
            or (output_path / "adapter_model.safetensors").exists()
            or (output_path / "pytorch_model.bin").exists()
        )

        if result.returncode != 0 and not model_saved:
            raise RuntimeError(
                f"accelerate launch exited with code {result.returncode} "
                f"(full log: {log_path})"
            )

        if not model_saved:
            raise RuntimeError(
                f"Training process exited 0 but no model found in {output_dir} "
                f"(full log: {log_path})"
            )

        # Parse metrics from trainer output
        metrics: dict[str, Any] = {
            "method": method,
            "model_name_or_path": model_name,
            "output_dir": output_dir,
        }

        trainer_state = output_path / "trainer_state.json"
        if trainer_state.exists():
            state = json.loads(trainer_state.read_text())
            log_history = state.get("log_history", [])
            if log_history:
                last = log_history[-1]
                if "train_loss" in last:
                    metrics["train_loss"] = last["train_loss"]
                if "train_runtime" in last:
                    metrics["train_runtime"] = last["train_runtime"]

        return {
            "status": "completed",
            "metrics": metrics,
            "error": None,
        }

    except Exception as exc:
        logger.exception("Finetune failed")
        return {
            "status": "failed",
            "metrics": {},
            "error": str(exc),
        }
