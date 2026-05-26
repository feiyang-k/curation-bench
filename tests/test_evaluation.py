from __future__ import annotations

import json
import math
import subprocess
from pathlib import Path

from benchmark.tools.evaluation import run_evaluation
from benchmark.core.task import EvalConfig


def _fake_vlmeval_dir(tmp_path: Path) -> Path:
    vlmeval_dir = tmp_path / "vendor" / "VLMEvalKit"
    vlmeval_dir.mkdir(parents=True, exist_ok=True)
    (vlmeval_dir / "run.py").write_text("print('stub')\n", encoding="utf-8")
    return vlmeval_dir


def test_run_evaluation_reads_nested_results_summary(tmp_path: Path, monkeypatch) -> None:
    import benchmark.tools.evaluation as evaluation

    vlmeval_dir = _fake_vlmeval_dir(tmp_path)
    monkeypatch.setattr(evaluation, "_vlmeval_dir", lambda: vlmeval_dir)
    monkeypatch.setattr(evaluation, "resolve_uv_command", lambda: ["uv"])
    monkeypatch.setattr(
        subprocess,
        "run",
        lambda *args, **kwargs: subprocess.CompletedProcess(args[0], 0, stdout="ok\n", stderr=""),
    )

    output_dir = tmp_path / "eval"
    results_dir = output_dir / "results"
    results_dir.mkdir(parents=True, exist_ok=True)
    (results_dir / "results.json").write_text(
        json.dumps(
            {
                "llava-1.5-7b-hf": {
                    "MMVet": {"score": 75.0},
                    "OCRBench": {"accuracy": 640.0},
                }
            }
        ),
        encoding="utf-8",
    )

    result = run_evaluation(
        model_path="/tmp/fake-model",
        model_key="llava-1.5-7b-hf",
        eval_config=EvalConfig(benchmarks=["MMVet", "OCRBench"], timeout_seconds=30),
        output_dir=output_dir,
    )

    assert result["status"] == "completed"
    assert result["results"] == {"MMVet": 75.0, "OCRBench": 640.0}
    assert result["normalized"] == {"MMVet": 0.75, "OCRBench": 0.64}
    assert math.isclose(result["accuracy"], 0.695)


def test_qwen_vlmeval_model_name() -> None:
    from benchmark.core.model_registry import MODEL_REGISTRY

    assert MODEL_REGISTRY["qwen2.5-vl-3b-instruct"].vlmeval_model_name == "Qwen2.5-VL-3B-Instruct"


def test_pope_and_mmbench_in_benchmark_max() -> None:
    from benchmark.tools.evaluation import _BENCHMARK_MAX

    assert "POPE" in _BENCHMARK_MAX
    assert "MMBench_DEV_EN" in _BENCHMARK_MAX
    assert _BENCHMARK_MAX["POPE"] == 100.0
    assert _BENCHMARK_MAX["MMBench_DEV_EN"] == 100.0


def test_run_evaluation_fails_when_no_scores_can_be_extracted(tmp_path: Path, monkeypatch) -> None:
    import benchmark.tools.evaluation as evaluation

    vlmeval_dir = _fake_vlmeval_dir(tmp_path)
    monkeypatch.setattr(evaluation, "_vlmeval_dir", lambda: vlmeval_dir)
    monkeypatch.setattr(evaluation, "resolve_uv_command", lambda: ["uv"])
    monkeypatch.setattr(
        subprocess,
        "run",
        lambda *args, **kwargs: subprocess.CompletedProcess(args[0], 0, stdout="ok\n", stderr=""),
    )

    result = run_evaluation(
        model_path="/tmp/fake-model",
        model_key="llava-1.5-7b-hf",
        eval_config=EvalConfig(benchmarks=["MMVet"], timeout_seconds=30),
        output_dir=tmp_path / "eval",
    )

    assert result["status"] == "failed"
    assert result["results"] == {}
    assert result["accuracy"] == 0.0
    assert "no benchmark scores could be extracted" in result["error"].lower()
