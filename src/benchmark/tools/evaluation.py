from __future__ import annotations

import logging
import os
import subprocess
from pathlib import Path
from typing import Any

from ..core.model_registry import get_model
from ..core.task import EvalConfig
from ..core.uv_runtime import resolve_uv_command

logger = logging.getLogger(__name__)


def _query_gpus() -> list[dict[str, int]]:
    try:
        proc = subprocess.run(
            [
                "nvidia-smi",
                "--query-gpu=index,memory.total,memory.free",
                "--format=csv,noheader,nounits",
            ],
            capture_output=True,
            text=True,
            check=True,
        )
    except Exception:
        logger.debug("Failed to query GPUs via nvidia-smi", exc_info=True)
        return []

    gpus: list[dict[str, int]] = []
    for line in proc.stdout.splitlines():
        parts = [part.strip() for part in line.split(",")]
        if len(parts) != 3:
            continue
        try:
            gpus.append({
                "index": int(parts[0]),
                "total_mb": int(parts[1]),
                "free_mb": int(parts[2]),
            })
        except ValueError:
            continue
    return gpus


def _pick_eval_gpu(preferred_gpu: int) -> int | None:
    gpus = _query_gpus()
    if not gpus:
        return preferred_gpu

    # BENCHMARK_EVAL_GPUS takes priority, then CUDA_VISIBLE_DEVICES
    gpu_filter = os.environ.get("BENCHMARK_EVAL_GPUS") or os.environ.get("CUDA_VISIBLE_DEVICES")
    if gpu_filter:
        allowed = {int(x.strip()) for x in gpu_filter.split(",") if x.strip().isdigit()}
        gpus = [g for g in gpus if g["index"] in allowed]
        if not gpus:
            return None

    by_index = {gpu["index"]: gpu for gpu in gpus}
    preferred = by_index.get(preferred_gpu)
    if preferred:
        return preferred_gpu

    gpus.sort(key=lambda item: (-item["free_mb"], item["index"]))
    return gpus[0]["index"]


def _vlmeval_dir() -> Path:
    return Path(__file__).resolve().parents[3] / "vendor" / "VLMEvalKit"


def run_evaluation(
    model_path: str,
    model_key: str,
    eval_config: EvalConfig,
    output_dir: Path,
    *,
    eval_data_dir: str | None = None,
) -> dict[str, Any]:
    vlmeval_dir = _vlmeval_dir()
    if not vlmeval_dir.exists():
        return {"status": "failed", "error": f"VLMEvalKit not found at {vlmeval_dir}"}

    try:
        model_config = get_model(model_key)
    except ValueError:
        return {"status": "failed", "error": f"Unknown model_key: {model_key}"}
    model_name = model_config.vlmeval_model_name

    benchmarks = eval_config.benchmarks or []
    if not benchmarks:
        return {"status": "failed", "error": "No benchmarks specified in eval_config"}

    output_dir.mkdir(parents=True, exist_ok=True)
    results_dir = output_dir / "results"
    results_dir.mkdir(parents=True, exist_ok=True)

    try:
        uv_cmd = resolve_uv_command()
    except RuntimeError as exc:
        return {"status": "failed", "error": str(exc)}

    cmd = [
        *uv_cmd, "run", "--no-sync", "--project", str(vlmeval_dir),
        "python", str(vlmeval_dir / "run.py"),
        "--model", model_name,
        "--model-path", model_path,
        "--data", *benchmarks,
        "--work-dir", str(results_dir),
        "--mode", eval_config.mode,
    ]
    if eval_config.use_vllm:
        cmd.append("--use-vllm")
    if eval_config.judge_model:
        cmd.extend(["--judge", eval_config.judge_model])
    if eval_config.api_nproc:
        cmd.extend(["--api-nproc", str(eval_config.api_nproc)])

    env = os.environ.copy()
    if eval_data_dir:
        env["LMUData"] = eval_data_dir
        env["BENCHMARK_VLMEVAL_TRUST_LOCAL_TSV"] = "1"
    selected_gpu = _pick_eval_gpu(eval_config.gpu_id)
    if selected_gpu is None:
        return {"status": "failed", "error": "No eligible GPU is currently available for evaluation."}
    env["CUDA_VISIBLE_DEVICES"] = str(selected_gpu)
    env["VLLM_WORKER_MULTIPROC_METHOD"] = "spawn"
    if eval_config.judge_api_base:
        env["OPENAI_API_BASE"] = eval_config.judge_api_base
        env.setdefault("OPENAI_API_KEY", "dummy")

    logger.info("Running VLMEvalKit: %s", " ".join(cmd))

    stdout_path = output_dir / "eval_stdout.txt"
    stderr_path = output_dir / "eval_stderr.txt"

    try:
        with open(stdout_path, "w", encoding="utf-8") as out_f, \
             open(stderr_path, "w", encoding="utf-8") as err_f:
            proc = subprocess.run(
                cmd,
                stdout=out_f,
                stderr=err_f,
                text=True,
                timeout=eval_config.timeout_seconds,
                env=env,
            )

        if proc.returncode != 0:
            return {
                "status": "failed",
                "error": f"VLMEvalKit exited with code {proc.returncode}",
                "results_dir": str(results_dir),
            }
    except FileNotFoundError as exc:
        return {"status": "failed", "error": f"Evaluation launcher not found: {exc.filename}"}
    except subprocess.TimeoutExpired:
        return {
            "status": "failed",
            "error": f"Evaluation timed out after {eval_config.timeout_seconds}s",
        }

    return {
        "status": "completed",
        "results_dir": str(results_dir),
        "error": None,
    }
