from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml


@dataclass(slots=True)
class DatasetSpec:
    dataset_id: str
    local_path: str
    split: str | None
    image_column: str
    text_column: str


@dataclass(slots=True)
class TrainingConfig:
    max_steps: int | None = None
    save_steps: int | None = None
    logging_steps: int | None = None
    num_processes: int | None = None
    timeout_seconds: int = 3600


@dataclass(slots=True)
class EvalConfig:
    benchmarks: list[str] | None = None
    use_vllm: bool = False
    mode: str = "all"
    judge_model: str = ""
    judge_api_base: str = ""
    api_nproc: int = 4
    gpu_id: int = 0
    timeout_seconds: int = 14400


@dataclass(slots=True)
class TaskSpec:
    task_id: str
    goal: str
    target_rows: int
    model_key: str
    training_stage: str
    model_name_or_path: str
    target_evals: list[str]
    strategy_timeout_seconds: int | None
    dataset: DatasetSpec
    default_submission_dir: str
    eval_data_dir: str | None = None
    training_config: TrainingConfig | None = None
    eval_config: EvalConfig | None = None

    def to_summary(self, default_submission_path: str | Path) -> dict[str, Any]:
        return {
            "task_id": self.task_id,
            "goal": self.goal,
            "target_rows": self.target_rows,
            "model_key": self.model_key,
            "training_stage": self.training_stage,
            "model_name_or_path": self.model_name_or_path,
            "target_evals": list(self.target_evals),
            "strategy_timeout_seconds": self.strategy_timeout_seconds,
            "has_training": self.training_config is not None,
            "has_eval": self.eval_config is not None,
            "candidate_datasets": [
                {
                    "dataset_id": self.dataset.dataset_id,
                    "local_path": self.dataset.local_path,
                    "split": self.dataset.split,
                    "image_column": self.dataset.image_column,
                    "text_column": self.dataset.text_column,
                }
            ],
            "default_submission_output_path": str(Path(default_submission_path).expanduser().resolve()),
        }


def _tasks_dir() -> Path:
    """Return the built-in tasks directory."""
    return Path(__file__).resolve().parent.parent / "tasks"


def discover_tasks(tasks_dir: Path | None = None) -> dict[str, Path]:
    """Return {task_id: template_path} for all .yaml files in tasks_dir."""
    d = tasks_dir or _tasks_dir()
    result = {}
    for p in sorted(d.glob("*.yaml")):
        raw = _read_yaml(p)
        task_id = raw["task"]["task_id"]
        result[task_id] = p
    return result


def resolve_task_template(task_id: str, tasks_dir: Path | None = None) -> Path:
    """Look up one task template by task_id. Raises KeyError if not found."""
    tasks = discover_tasks(tasks_dir)
    if task_id not in tasks:
        available = ", ".join(sorted(tasks))
        raise KeyError(f"Unknown task: {task_id!r}. Available: {available}")
    return tasks[task_id]


def _read_yaml(path: str | Path) -> dict[str, Any]:
    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    if not isinstance(data, dict):
        raise ValueError(f"Task file must be a mapping: {path}")
    return data


def _parse_training_config(raw: dict[str, Any] | None) -> TrainingConfig | None:
    if raw is None:
        return None
    return TrainingConfig(
        max_steps=raw.get("max_steps"),
        save_steps=raw.get("save_steps"),
        logging_steps=raw.get("logging_steps"),
        num_processes=raw.get("num_processes"),
        timeout_seconds=int(raw.get("timeout_seconds", 3600)),
    )


def _parse_eval_config(raw: dict[str, Any] | None, target_evals: list[str]) -> EvalConfig | None:
    if raw is None:
        return None
    benchmarks = raw.get("benchmarks")
    if benchmarks is None:
        benchmarks = list(target_evals)
    return EvalConfig(
        benchmarks=[str(b) for b in benchmarks],
        use_vllm=bool(raw.get("use_vllm", False)),
        mode=str(raw.get("mode", "all")),
        judge_model=str(raw.get("judge_model", "")),
        judge_api_base=str(raw.get("judge_api_base", "")),
        api_nproc=int(raw.get("api_nproc", 4)),
        gpu_id=int(raw.get("gpu_id", 0)),
        timeout_seconds=int(raw.get("timeout_seconds", 14400)),
    )


def load_task_spec(path: str | Path) -> TaskSpec:
    raw = _read_yaml(path)
    task = raw["task"]
    dataset = task["dataset"]

    from .model_registry import MODEL_REGISTRY, get_model

    model_key = str(task["model_key"])
    training_stage = str(task["training_stage"])

    if model_key not in MODEL_REGISTRY:
        raise ValueError(
            f"Unknown model_key {model_key!r}. "
            f"Available: {', '.join(sorted(MODEL_REGISTRY))}"
        )
    if training_stage not in ("finetuning", "posttraining"):
        raise ValueError(
            f"training_stage must be 'finetuning' or 'posttraining', got: {training_stage!r}"
        )
    model_config = get_model(model_key)
    if model_config.training_stage != training_stage:
        raise ValueError(
            f"model_key {model_key!r} expects training_stage={model_config.training_stage!r}, "
            f"but task YAML says {training_stage!r}"
        )

    target_evals = [str(x) for x in task["target_evals"]]

    return TaskSpec(
        task_id=str(task["task_id"]),
        goal=str(task["goal"]),
        target_rows=int(task["target_rows"]),
        model_key=model_key,
        training_stage=training_stage,
        model_name_or_path=str(task["model_name_or_path"]),
        target_evals=target_evals,
        strategy_timeout_seconds=(
            int(task["strategy_timeout_seconds"])
            if task.get("strategy_timeout_seconds") is not None
            else None
        ),
        dataset=DatasetSpec(
            dataset_id=str(dataset["dataset_id"]),
            local_path=str(dataset["local_path"]),
            split=dataset.get("split"),
            image_column=str(dataset.get("image_column", "images")),
            text_column=str(dataset.get("text_column", "texts")),
        ),
        default_submission_dir=str(task["default_submission_dir"]),
        eval_data_dir=task.get("eval_data_dir"),
        training_config=_parse_training_config(task.get("training_config")),
        eval_config=_parse_eval_config(task.get("eval_config"), target_evals),
    )


def render_task_for_run(
    template_path: str | Path,
    dataset_path: str | Path,
    model_path: str,
    run_dir: str | Path,
) -> Path:
    raw = _read_yaml(template_path)
    raw["task"]["dataset"]["local_path"] = str(Path(dataset_path).expanduser().resolve())
    raw["task"]["model_name_or_path"] = model_path
    # Never write the real eval_data_dir into the resolved task file.
    if raw["task"].get("eval_data_dir") == "__EVAL_DATA_DIR__":
        raw["task"]["eval_data_dir"] = None
    out_path = Path(run_dir) / "task.resolved.yaml"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        yaml.safe_dump(raw, f, sort_keys=False)
    return out_path
