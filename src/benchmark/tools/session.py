from __future__ import annotations

from copy import deepcopy
import json
import os
import shutil
import subprocess
import time
import uuid
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from .submission import validate_submission
from ..core.task import load_task_spec
from ..core.uv_runtime import resolve_uv_command


class Session:
    def __init__(
        self,
        task_path: str | Path,
        *,
        run_dir: str | Path | None = None,
        default_submission_path: str | Path | None = None,
    ) -> None:
        self.task_path = str(Path(task_path).expanduser().resolve())
        self.task = load_task_spec(self.task_path)
        if run_dir:
            self.run_dir = Path(run_dir).expanduser().resolve()
        else:
            from datetime import UTC, datetime
            base = Path.cwd() / "runs"
            stamp = datetime.now(tz=UTC).strftime("%Y%m%dT%H%M%S_%f")
            self.run_dir = base / stamp
        self.run_dir.mkdir(parents=True, exist_ok=True)
        self.archive_submission_path = self.run_dir / self.task.default_submission_dir
        if default_submission_path is not None:
            self.default_submission_path = Path(default_submission_path).expanduser().resolve()
        else:
            self.default_submission_path = self.archive_submission_path
        self.events_path = self.run_dir / "events.jsonl"
        self.last_submission_path: str | None = None
        self.finetune_model_path: str | None = None
        self._finetune_submission_path: str | None = None
        self._finetune_result: dict[str, Any] | None = None
        self.event_seq: int = 0
        self.iteration: int = 1
        self._eval_data_dir: str | None = None
        self._strategy_started_at_epoch = time.time()

    def summarize_task(self) -> dict[str, Any]:
        summary = self.task.to_summary(self.default_submission_path)
        if self.iteration > 1:
            summary["iteration"] = self.iteration
        return summary

    def get_time_budget(self) -> dict[str, Any]:
        elapsed_seconds = max(0.0, time.time() - self._strategy_started_at_epoch)
        strategy_timeout_seconds = self.task.strategy_timeout_seconds
        if strategy_timeout_seconds is None:
            return {
                "strategy_timeout_seconds": None,
                "elapsed_seconds": elapsed_seconds,
                "remaining_seconds": None,
                "expired": False,
            }
        remaining_seconds = max(0.0, strategy_timeout_seconds - elapsed_seconds)
        return {
            "strategy_timeout_seconds": strategy_timeout_seconds,
            "elapsed_seconds": elapsed_seconds,
            "remaining_seconds": remaining_seconds,
            "expired": elapsed_seconds >= strategy_timeout_seconds,
        }

    def _strategy_timeout_result(self) -> dict[str, Any] | None:
        budget = self.get_time_budget()
        if not budget["expired"]:
            return None
        limit = budget["strategy_timeout_seconds"]
        elapsed = budget["elapsed_seconds"]
        return {
            "status": "failed",
            "error": (
                "Data strategy time limit exceeded before successful submission: "
                f"elapsed={elapsed:.1f}s limit={limit}s."
            ),
            **budget,
        }

    def dispatch(self, tool_name: str, args: dict[str, Any]) -> dict[str, Any]:
        handler = getattr(self, f"_tool_{tool_name}", None)
        if handler is None:
            raise KeyError(f"Unknown tool: {tool_name}")

        result = handler(**args)
        self._log_event(tool_name, args, result)
        self.save_state()
        return result

    # ------------------------------------------------------------------
    # State persistence (for CLI mode: each command is a separate process)
    # ------------------------------------------------------------------

    def save_state(self) -> None:
        """Persist mutable session state to session_state.json."""
        state = {
            "event_seq": self.event_seq,
            "last_submission_path": self.last_submission_path,
            "finetune_model_path": self.finetune_model_path,
            "_finetune_submission_path": self._finetune_submission_path,
            "_finetune_result": self._finetune_result,
            "strategy_started_at_epoch": self._strategy_started_at_epoch,
        }
        state_path = self.run_dir / "session_state.json"
        state_path.write_text(json.dumps(state, indent=2), encoding="utf-8")

    def load_state(self) -> None:
        """Restore mutable session state from session_state.json (if it exists)."""
        state_path = self.run_dir / "session_state.json"
        if not state_path.exists():
            return
        state = json.loads(state_path.read_text(encoding="utf-8"))
        self.event_seq = state.get("event_seq", 0)
        self.last_submission_path = state.get("last_submission_path")
        self.finetune_model_path = state.get("finetune_model_path")
        self._finetune_submission_path = state.get("_finetune_submission_path")
        self._finetune_result = state.get("_finetune_result")
        epoch = state.get("strategy_started_at_epoch")
        if epoch is not None:
            self._strategy_started_at_epoch = epoch

    def _log_event(self, tool_name: str, args: dict[str, Any], result: dict[str, Any]) -> None:
        self.event_seq += 1
        event = {"seq": self.event_seq, "tool": tool_name, "args": args, "result": result}
        with open(self.events_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(event, ensure_ascii=False) + "\n")

    def _tool_audit_contamination(self, submission_path: str) -> dict[str, Any]:
        from .contamination import audit_contamination

        eval_dir = self._eval_data_dir
        if not eval_dir:
            return {"status": "skipped", "error": "eval_data_dir not configured"}
        try:
            return audit_contamination(
                submission_path,
                eval_dir,
                self.task.target_evals,
            )
        except Exception as exc:
            return {"status": "error", "error": f"{type(exc).__name__}: {exc}"}

    def _tool_submit_curated_dataset(self, submission_path: str) -> dict[str, Any]:
        timeout_result = self._strategy_timeout_result()
        if timeout_result is not None:
            return timeout_result

        result = validate_submission(
            submission_path,
            target_rows=self.task.target_rows,
        )
        if result.get("status") == "submitted":
            source_submission_path = Path(result.get("submission_path", submission_path)).expanduser().resolve()
            archived_submission_path = self.archive_submission_path.expanduser().resolve()
            try:
                if source_submission_path != archived_submission_path:
                    archived_submission_path.parent.mkdir(parents=True, exist_ok=True)
                    if archived_submission_path.exists():
                        shutil.rmtree(archived_submission_path)
                    shutil.copytree(source_submission_path, archived_submission_path)
                self.last_submission_path = str(archived_submission_path)
                # A new successful submission invalidates any previous finetune result,
                # even though the archived path is reused within the same run.
                self.finetune_model_path = None
                self._finetune_submission_path = None
                self._finetune_result = None
            except Exception as exc:
                return {
                    "status": "failed",
                    "error": f"Could not archive submission into run directory: {type(exc).__name__}: {exc}",
                    "submission_path": str(source_submission_path),
                }
            result["source_submission_path"] = str(source_submission_path)
            result["submission_path"] = str(archived_submission_path)
        return result

    def _tool_submit_finetune(self) -> dict[str, Any]:
        if self.last_submission_path is None:
            return {"status": "failed", "error": "No successful submission. Call submit_curated_dataset first."}
        if self.task.training_config is None:
            return {"status": "failed", "error": "No training_config in task spec."}
        if self._finetune_submission_path == self.last_submission_path and self._finetune_result is not None:
            cached_result = deepcopy(self._finetune_result)
            if cached_result.get("status") == "completed":
                self.finetune_model_path = cached_result.get("model_path")
            return cached_result

        tc = self.task.training_config
        job_id = f"ft-{uuid.uuid4().hex[:8]}"
        output_dir = self.run_dir / "finetune" / job_id
        output_dir.mkdir(parents=True, exist_ok=True)

        from ..core.model_registry import get_model

        model_config = get_model(self.task.model_key)
        if model_config.finetuning_method is None:
            result = {
                "status": "failed",
                "job_id": job_id,
                "model_path": str(output_dir),
                "metrics": {},
                "error": f"model_key {self.task.model_key!r} has no finetuning_method",
            }
        else:
            result = self._run_curation_train(tc, job_id, output_dir, model_config.finetuning_method)

        self._finetune_submission_path = self.last_submission_path
        self._finetune_result = deepcopy(result)
        return result

    def _run_curation_train(
        self, tc: "TrainingConfig", job_id: str, output_dir: Path,
        method: str,
    ) -> dict[str, Any]:
        config: dict[str, Any] = {
            "method": method,
            "data_path": self.last_submission_path,
            "output_dir": str(output_dir),
            "model_name_or_path": self.task.model_name_or_path,
        }
        if tc.max_steps is not None:
            config["max_steps"] = tc.max_steps
        if tc.save_steps is not None:
            config["save_steps"] = tc.save_steps
        if tc.logging_steps is not None:
            config["logging_steps"] = tc.logging_steps
        if tc.num_processes is not None:
            config["num_processes"] = tc.num_processes

        config_path = output_dir / "benchmark_train_config.json"
        config_path.write_text(json.dumps(config, indent=2), encoding="utf-8")

        train_project = Path(__file__).resolve().parents[3] / "vendor" / "curation-train"
        try:
            uv_cmd = resolve_uv_command()
        except RuntimeError as exc:
            return {
                "status": "failed",
                "job_id": job_id,
                "model_path": str(output_dir),
                "metrics": {},
                "error": str(exc),
            }

        cmd = [*uv_cmd, "run", "--no-sync", "--project", str(train_project), "curation-train", str(config_path)]

        stdout_path = output_dir / "train_stdout.txt"
        stderr_path = output_dir / "train_stderr.txt"

        train_env = os.environ.copy()
        train_gpus_override = train_env.get("BENCHMARK_TRAIN_GPUS")
        if train_gpus_override:
            train_env["CUDA_VISIBLE_DEVICES"] = train_gpus_override

        try:
            with open(stdout_path, "w", encoding="utf-8") as out_f, \
                 open(stderr_path, "w", encoding="utf-8") as err_f:
                proc = subprocess.run(
                    cmd,
                    stdout=out_f,
                    stderr=err_f,
                    text=True,
                    timeout=tc.timeout_seconds,
                    env=train_env,
                )
        except FileNotFoundError as exc:
            return {
                "status": "failed",
                "job_id": job_id,
                "model_path": str(output_dir),
                "metrics": {},
                "error": f"Training launcher not found: {exc.filename}",
            }
        except subprocess.TimeoutExpired:
            return {
                "status": "failed",
                "job_id": job_id,
                "model_path": str(output_dir),
                "metrics": {},
                "error": f"Training timed out after {tc.timeout_seconds}s",
            }

        metrics: dict[str, Any] = {}
        stdout_text = stdout_path.read_text(encoding="utf-8").strip()
        if not stdout_text and getattr(proc, "stdout", None):
            # Support test doubles that return captured stdout instead of writing
            # to the redirected log file.
            stdout_text = str(proc.stdout).strip()
        if stdout_text:
            last_line = stdout_text.splitlines()[-1]
            try:
                metrics = json.loads(last_line)
            except json.JSONDecodeError:
                pass

        if proc.returncode != 0:
            return {
                "status": "failed",
                "job_id": job_id,
                "model_path": str(output_dir),
                "metrics": metrics,
                "error": f"Training exited with code {proc.returncode}",
            }

        training_status = str(metrics.get("status", "")).lower()
        if training_status == "failed":
            return {
                "status": "failed",
                "job_id": job_id,
                "model_path": str(output_dir),
                "metrics": metrics,
                "error": str(metrics.get("error") or "Training reported failure."),
            }

        self.finetune_model_path = str(output_dir)
        return {
            "status": "completed",
            "job_id": job_id,
            "model_path": str(output_dir),
            "metrics": metrics,
            "error": None,
        }

    def _tool_submit_eval(self) -> dict[str, Any]:
        if self.finetune_model_path is None:
            return {"status": "failed", "error": "No fine-tuned model. Call submit_finetune first."}
        if self.task.eval_config is None:
            return {"status": "failed", "error": "No eval_config in task spec."}

        from .evaluation import run_evaluation

        eval_dir = self.run_dir / "eval"
        return run_evaluation(
            self.finetune_model_path,
            self.task.model_key,
            self.task.eval_config,
            eval_dir,
            eval_data_dir=self._eval_data_dir,
        )
