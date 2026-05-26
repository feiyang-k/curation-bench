"""SuiteController: manages a multi-task, multi-iteration benchmark suite.

Responsibilities:
- Parse run_prompt.md and profile to build the target queue
- State machine: PENDING → ACTIVE → COMPLETED / FAILED
- Persist state to suite_state.json for crash recovery
- Create Session instances per target
"""

from __future__ import annotations

import json
import logging
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from ..core.profile import Profile, find_default_profile, load_profile, resolve_profile_path
from ..core.prompt import parse_run_prompt
from ..core.task import render_task_for_run, resolve_task_template

logger = logging.getLogger(__name__)

# Target states
PENDING = "pending"
ACTIVE = "active"
COMPLETED = "completed"
FAILED = "failed"


class _AgentMismatch(Exception):
    """Signal: the recorded suite agent differs from the current agent.

    Raised inside the resume check to bail out to the fresh-suite branch
    without inventing new control flow (caught by the existing except clause).
    """


class Target:
    """One (task_id, iteration) combination in the suite."""

    __slots__ = ("task_id", "iteration", "state", "run_dir", "task_path", "eval_result")

    def __init__(self, task_id: str, iteration: int) -> None:
        self.task_id = task_id
        self.iteration = iteration
        self.state: str = PENDING
        self.run_dir: Path | None = None
        self.task_path: Path | None = None
        self.eval_result: dict | None = None

    @property
    def key(self) -> str:
        return f"{self.task_id}_iter{self.iteration}"

    def to_dict(self) -> dict[str, Any]:
        return {
            "task_id": self.task_id,
            "iteration": self.iteration,
            "state": self.state,
            "key": self.key,
            "run_dir": str(self.run_dir) if self.run_dir else None,
            "eval_result": self.eval_result,
        }


class SuiteController:
    """Manages the lifecycle of a benchmark suite."""

    def __init__(
        self,
        *,
        targets: list[Target],
        suite_dir: Path,
        profile: Profile,
        strategy_text: str = "",
        prompt_source: str | None = None,
        agent: str | None = None,
    ) -> None:
        self.targets = targets
        self.suite_dir = suite_dir
        self.profile = profile
        self.strategy_text = strategy_text
        self.prompt_source = prompt_source
        self.agent = agent
        self._active_index: int | None = None
        self._session: Any = None  # Current Session instance (lazy import)
        self._state_path = suite_dir / "suite_state.json"
        self._resumed_active = False  # True if loaded from state file with ACTIVE target

    # ------------------------------------------------------------------
    # Factory: build from run_prompt.md + profile
    # ------------------------------------------------------------------

    @classmethod
    def from_prompt(
        cls,
        prompt_path: str | Path = "run_prompt.md",
        profile_path: str | None = None,
        *,
        profiles_dir: str | Path | None = None,
        output_root: str | Path | None = None,
        suite_stamp: str | None = None,
        agent: str | None = None,
        new_suite: bool = False,
    ) -> "SuiteController":
        """Initialize a suite from run_prompt.md and a profile.

        If a suite_state.json already exists in the resolved suite_dir,
        the suite is resumed from that state instead — unless the recorded
        agent differs from ``agent`` or ``new_suite`` is True, in which case
        a fresh suite is created.
        """
        prompt = parse_run_prompt(prompt_path)

        # Resolve profile
        resolved_profile_path = _resolve_profile(
            profile_path, prompt.profile, profiles_dir
        )
        profile = load_profile(resolved_profile_path)

        # Inject profile env vars into os.environ so training/eval subprocesses see them.
        # Use setdefault: do NOT override values already set by the ambient environment
        # (e.g., docker_runner remaps host GPU IDs to container-local IDs before launch).
        if profile.env:
            import os
            for key, val in profile.env.items():
                os.environ.setdefault(key, val)

        # Build target queue: all iterations of task A, then all of task B, etc.
        targets = _build_target_queue(prompt.tasks, prompt.iterations)

        # Idempotent resume: if an active-suite pointer exists and points at an
        # unfinished suite whose tasks+iterations match the current prompt,
        # resume that suite instead of creating a new one. If the iteration
        # count was bumped up (same tasks, strict superset), extend the suite.
        # Skipped when --new-suite is requested, or when the recorded suite
        # was run by a different agent (claude vs codex must not collide).
        pointer = Path.cwd() / ".bench_active_suite"
        if pointer.exists() and not new_suite:
            try:
                existing_dir = Path(pointer.read_text(encoding="utf-8").strip())
                existing_state = existing_dir / "suite_state.json"
                if existing_state.exists():
                    data = json.loads(existing_state.read_text(encoding="utf-8"))
                    if agent is not None and data.get("agent") != agent:
                        logger.info(
                            "Ignoring active-suite pointer: recorded agent %r != current agent %r",
                            data.get("agent"), agent,
                        )
                        raise _AgentMismatch
                    existing_targets = data.get("targets", [])
                    all_done = existing_targets and all(
                        t.get("state") in (COMPLETED, FAILED) for t in existing_targets
                    )
                    existing_pairs = {(t["task_id"], t["iteration"]) for t in existing_targets}
                    expected_pairs = {(t.task_id, t.iteration) for t in targets}
                    if existing_pairs == expected_pairs and not all_done:
                        logger.info("Resuming existing suite at %s", existing_dir)
                        ctrl = cls.from_state_file(existing_state)
                        ctrl.profile = profile  # honor current-process profile changes
                        return ctrl
                    if existing_pairs and expected_pairs > existing_pairs:
                        logger.info(
                            "Extending existing suite at %s (+%d targets)",
                            existing_dir, len(expected_pairs - existing_pairs),
                        )
                        ctrl = cls.from_state_file(existing_state)
                        ctrl.profile = profile  # honor current-process profile changes
                        ctrl._resumed_active = False  # extension only, not a crash resume
                        existing_keys = {(t.task_id, t.iteration) for t in ctrl.targets}
                        for t in targets:
                            if (t.task_id, t.iteration) in existing_keys:
                                continue
                            t.run_dir = ctrl.suite_dir / t.key
                            t.run_dir.mkdir(parents=True, exist_ok=True)
                            template_path = resolve_task_template(t.task_id)
                            dataset_path = _resolve_dataset_path(t.task_id, ctrl.profile, template_path)
                            model_path = _resolve_model_path(t.task_id, ctrl.profile, template_path)
                            t.task_path = render_task_for_run(template_path, dataset_path, model_path, t.run_dir)
                            ctrl.targets.append(t)
                        ctrl._save_state()
                        return ctrl
            except _AgentMismatch:
                pass  # fall through to create a fresh suite for this agent
            except (json.JSONDecodeError, OSError, KeyError) as exc:
                logger.warning("Ignoring stale active-suite pointer: %s", exc)

        # Create suite directory
        if not suite_stamp:
            suite_stamp = datetime.now(tz=UTC).strftime("%Y%m%dT%H%M%S_%f")
            if agent:
                suite_stamp = f"{suite_stamp}_{agent}"
        base = Path(output_root) if output_root else Path.cwd() / "runs"
        suite_dir = base / suite_stamp
        suite_dir.mkdir(parents=True, exist_ok=True)

        # Resolve task templates and create per-target directories
        for target in targets:
            target.run_dir = suite_dir / target.key
            target.run_dir.mkdir(parents=True, exist_ok=True)
            template_path = resolve_task_template(target.task_id)
            dataset_path = _resolve_dataset_path(target.task_id, profile, template_path)
            model_path = _resolve_model_path(target.task_id, profile, template_path)
            target.task_path = render_task_for_run(
                template_path, dataset_path, model_path, target.run_dir
            )

        ctrl = cls(
            targets=targets,
            suite_dir=suite_dir,
            profile=profile,
            strategy_text=prompt.strategy_text,
            prompt_source=str(prompt_path),
            agent=agent,
        )
        ctrl._save_state()
        return ctrl

    @classmethod
    def from_state_file(cls, state_path: str | Path) -> "SuiteController":
        """Resume a suite from a persisted suite_state.json."""
        state_path = Path(state_path)
        data = json.loads(state_path.read_text(encoding="utf-8"))
        suite_dir = Path(data["suite_dir"])

        # Reconstruct profile (it was saved alongside)
        profile_path = data.get("profile_path")
        profile = load_profile(profile_path) if profile_path else Profile()

        # Inject profile env vars into os.environ so training/eval subprocesses see them.
        # Use setdefault: do NOT override values already set by the ambient environment
        # (e.g., docker_runner remaps host GPU IDs to container-local IDs before launch).
        if profile.env:
            import os
            for key, val in profile.env.items():
                os.environ.setdefault(key, val)

        targets = []
        for td in data["targets"]:
            t = Target(td["task_id"], td["iteration"])
            t.state = td["state"]
            t.run_dir = Path(td["run_dir"]) if td.get("run_dir") else None
            t.task_path = Path(td["task_path"]) if td.get("task_path") else None
            t.eval_result = td.get("eval_result")
            targets.append(t)

        ctrl = cls(
            targets=targets,
            suite_dir=suite_dir,
            profile=profile,
            strategy_text=data.get("strategy_text", ""),
            prompt_source=data.get("prompt_source"),
            agent=data.get("agent"),
        )
        persisted_idx = data.get("active_index")
        if isinstance(persisted_idx, int) and 0 <= persisted_idx < len(targets):
            ctrl._active_index = persisted_idx
        else:
            for i, t in enumerate(targets):
                if t.state == ACTIVE:
                    ctrl._active_index = i
                    break
        # Flag so begin_next_target() restarts this target instead of failing it
        if ctrl._active_index is not None and targets[ctrl._active_index].state == ACTIVE:
            ctrl._resumed_active = True
        return ctrl

    # ------------------------------------------------------------------
    # Suite-level operations
    # ------------------------------------------------------------------

    def get_run_plan(self) -> dict[str, Any]:
        """Return the full target queue with states and progress."""
        active = self.active_target
        completed = sum(1 for t in self.targets if t.state == COMPLETED)
        failed = sum(1 for t in self.targets if t.state == FAILED)
        pending = sum(1 for t in self.targets if t.state == PENDING)
        return {
            "suite_dir": str(self.suite_dir),
            "total_targets": len(self.targets),
            "completed": completed,
            "failed": failed,
            "pending": pending,
            "active_target": active.to_dict() if active else None,
            "targets": [t.to_dict() for t in self.targets],
        }

    def begin_next_target(self) -> dict[str, Any]:
        """Advance to the next pending target.

        If the current ACTIVE target was not completed by submit_eval(),
        it is marked FAILED. Remaining iterations of the same task still run.

        If BENCHMARK_CURRENT_TASK env var is set, only targets belonging to
        that task are considered — and the current active target is only
        failed if it belongs to this caller's task.

        Returns the new target's context, a task-done marker, or suite completion.
        """
        import os as _os
        current_task_filter = _os.environ.get("BENCHMARK_CURRENT_TASK")

        # Resume: if the ACTIVE target was inherited from a prior process,
        # restart it (fresh session) instead of marking it FAILED.
        if self._resumed_active and self._active_index is not None:
            current = self.targets[self._active_index]
            if current.state == ACTIVE and (
                current_task_filter is None
                or current.task_id == current_task_filter
            ):
                self._resumed_active = False
                stale_session = current.run_dir / "session_state.json" if current.run_dir else None
                if stale_session and stale_session.exists():
                    stale_session.unlink()
                self._session = self._create_session(current)
                self._session.save_state()
                self._save_state()
                return self._build_target_context(current)

        # Handle current active target — only fail it if it's ours to fail
        if self._active_index is not None:
            current = self.targets[self._active_index]
            if current.state == ACTIVE:
                owns_current = (
                    current_task_filter is None
                    or current.task_id == current_task_filter
                )
                if owns_current:
                    # Not completed by submit_eval — mark FAILED
                    current.state = FAILED
                    self._save_state()

        # Find next PENDING target (within our task if filter is set)
        next_idx = None
        for i, t in enumerate(self.targets):
            if t.state == PENDING:
                if current_task_filter and t.task_id != current_task_filter:
                    continue
                next_idx = i
                break

        if next_idx is None:
            # No more targets for this caller (or the whole suite, if no filter)
            if current_task_filter:
                # Only this task is done; suite may still have other tasks
                return {
                    "status": "task_done",
                    "task_id": current_task_filter,
                    "message": f"All iterations of {current_task_filter} are processed.",
                }
            self._write_suite_result()
            return {
                "status": "suite_completed",
                "message": "All targets processed.",
                "summary": self.get_run_plan(),
            }

        # Activate next target
        target = self.targets[next_idx]
        target.state = ACTIVE
        self._active_index = next_idx

        # Create Session immediately and persist — strategy_started_at_epoch
        # is fixed at this moment, not when the agent first calls a tool.
        self._session = self._create_session(target)
        self._session.save_state()

        self._save_state()

        # Build context for the agent
        context = self._build_target_context(target)

        return context

    # ------------------------------------------------------------------
    # Target-level: completion via submit_eval
    # ------------------------------------------------------------------

    def mark_target_completed(self, eval_result: dict) -> None:
        """Called by submit_eval() on success to immediately mark target COMPLETED."""
        if self._active_index is None:
            return
        target = self.targets[self._active_index]
        if target.state == ACTIVE:
            target.state = COMPLETED
            target.eval_result = eval_result
            self._save_state()
            logger.info("Target %s marked COMPLETED", target.key)

    @property
    def active_target(self) -> Target | None:
        if self._active_index is not None:
            return self.targets[self._active_index]
        return None

    def get_active_session(self) -> Any:
        """Return the Session for the current active target, creating it if needed."""
        if self._active_index is None:
            raise RuntimeError("No active target. Call begin_next_target() first.")
        target = self.targets[self._active_index]
        if self._session is None:
            self._session = self._create_session(target)
        return self._session

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _create_session(self, target: Target) -> Any:
        """Create a Session instance for the given target."""
        from .session import Session

        session = Session(
            task_path=str(target.task_path),
            run_dir=str(target.run_dir),
            default_submission_path=str(target.run_dir / "curated" / "final_submission"),
        )
        # Override env-var based fields with suite-level config
        session.iteration = target.iteration
        session._eval_data_dir = self.profile.eval_data_dir

        # Restore persisted state (for CLI mode: each command is a separate process)
        session.load_state()

        return session

    def _build_target_context(self, target: Target) -> dict[str, Any]:
        """Build the context dict returned by begin_next_target."""
        from ..core.task import load_task_spec

        task = load_task_spec(str(target.task_path))
        return {
            "status": "target_activated",
            "target_key": target.key,
            "task_id": target.task_id,
            "iteration": target.iteration,
            "run_dir": str(target.run_dir),
            "task_goal": task.goal,
            "default_submission_path": str(
                target.run_dir / task.default_submission_dir
            ),
            "dataset_path": task.dataset.local_path,
        }

    def _save_state(self) -> None:
        """Persist suite state to suite_state.json."""
        data = {
            "suite_dir": str(self.suite_dir),
            "profile_path": self.profile.source_path,
            "strategy_text": self.strategy_text,
            "prompt_source": self.prompt_source,
            "agent": self.agent,
            "active_index": self._active_index,
            "targets": [],
        }
        for t in self.targets:
            td = t.to_dict()
            td["task_path"] = str(t.task_path) if t.task_path else None
            data["targets"].append(td)
        self._state_path.write_text(
            json.dumps(data, indent=2) + "\n", encoding="utf-8"
        )

    def _write_suite_result(self) -> None:
        """Write suite_result.json when all targets are processed."""
        completed = [t.to_dict() for t in self.targets if t.state == COMPLETED]
        failed = [t.to_dict() for t in self.targets if t.state == FAILED]
        payload = {
            "status": "completed" if completed else "failed",
            "suite_dir": str(self.suite_dir),
            "total_targets": len(self.targets),
            "completed_targets": len(completed),
            "failed_targets": len(failed),
            "completed": completed,
            "failed": failed,
        }
        result_path = self.suite_dir / "suite_result.json"
        result_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


# ------------------------------------------------------------------
# Module-level helpers
# ------------------------------------------------------------------


def _build_target_queue(task_ids: list[str], iterations: int) -> list[Target]:
    """Build an ordered target queue: all iterations of task A, then task B, etc."""
    targets = []
    for task_id in task_ids:
        for i in range(1, iterations + 1):
            targets.append(Target(task_id, i))
    return targets


def _resolve_profile(
    explicit_path: str | None,
    frontmatter_name: str | None,
    profiles_dir: str | Path | None,
) -> Path:
    """Resolve profile from explicit path, frontmatter name, or default."""
    if explicit_path:
        return resolve_profile_path(explicit_path, profiles_dir)
    if frontmatter_name:
        return resolve_profile_path(frontmatter_name, profiles_dir)
    default = find_default_profile(profiles_dir)
    if default:
        return default
    raise FileNotFoundError(
        "No profile specified and no default found in profiles/. "
        "Pass profile_path or set 'profile:' in run_prompt.md frontmatter."
    )


def _resolve_dataset_path(
    task_id: str, profile: Profile, template_path: Path
) -> str:
    """Resolve dataset path from profile's dataset_path_map."""
    from ..core.task import _read_yaml

    raw = _read_yaml(template_path)
    dataset_id = raw["task"]["dataset"].get("dataset_id", "")

    if dataset_id in profile.dataset_path_map:
        return profile.dataset_path_map[dataset_id]

    # Fallback: check if there's a single entry in the map
    if len(profile.dataset_path_map) == 1:
        return next(iter(profile.dataset_path_map.values()))

    raise ValueError(
        f"Cannot resolve dataset path for task {task_id!r} (dataset_id={dataset_id!r}). "
        f"Available in profile: {list(profile.dataset_path_map.keys())}"
    )


def _resolve_model_path(
    task_id: str, profile: Profile, template_path: Path
) -> str:
    """Resolve model path from profile's model_path_map."""
    from ..core.task import _read_yaml

    raw = _read_yaml(template_path)
    model_key = raw["task"].get("model_key", "")

    if model_key in profile.model_path_map:
        return profile.model_path_map[model_key]

    # Fallback: check if there's a single entry
    if len(profile.model_path_map) == 1:
        return next(iter(profile.model_path_map.values()))

    raise ValueError(
        f"Cannot resolve model path for task {task_id!r} (model_key={model_key!r}). "
        f"Available in profile: {list(profile.model_path_map.keys())}"
    )
