"""Tests for SuiteController state machine."""

import json
import pytest
from pathlib import Path
from unittest.mock import patch, MagicMock

from benchmark.tools.suite import (
    ACTIVE,
    COMPLETED,
    FAILED,
    PENDING,
    SuiteController,
    Target,
    _build_target_queue,
)
from benchmark.core.profile import Profile


# ---------------------------------------------------------------------------
# Target queue building
# ---------------------------------------------------------------------------


class TestBuildTargetQueue:
    def test_single_task_single_iter(self):
        targets = _build_target_queue(["taskA"], 1)
        assert len(targets) == 1
        assert targets[0].task_id == "taskA"
        assert targets[0].iteration == 1
        assert targets[0].state == PENDING

    def test_single_task_multi_iter(self):
        targets = _build_target_queue(["taskA"], 3)
        assert len(targets) == 3
        assert [t.key for t in targets] == [
            "taskA_iter1", "taskA_iter2", "taskA_iter3"
        ]

    def test_multi_task_multi_iter(self):
        targets = _build_target_queue(["taskA", "taskB"], 2)
        assert len(targets) == 4
        assert [t.key for t in targets] == [
            "taskA_iter1", "taskA_iter2",
            "taskB_iter1", "taskB_iter2",
        ]


# ---------------------------------------------------------------------------
# Helpers for building a controller without real tasks
# ---------------------------------------------------------------------------


def _make_controller(
    task_ids: list[str],
    iterations: int = 1,
    suite_dir: Path | None = None,
    profile: Profile | None = None,
) -> SuiteController:
    """Build a SuiteController with fake targets (no real task resolution)."""
    targets = _build_target_queue(task_ids, iterations)
    if suite_dir is None:
        raise ValueError("suite_dir required")
    for t in targets:
        t.run_dir = suite_dir / t.key
        t.run_dir.mkdir(parents=True, exist_ok=True)
        # Write a minimal task YAML so load_task_spec works
        t.task_path = t.run_dir / "task.resolved.yaml"
        t.task_path.write_text(
            _minimal_task_yaml(t.task_id),
            encoding="utf-8",
        )
    return SuiteController(
        targets=targets,
        suite_dir=suite_dir,
        profile=profile or Profile(),
    )


def _minimal_task_yaml(task_id: str) -> str:
    return f"""\
task:
  task_id: {task_id}
  goal: "Test goal for {task_id}"
  target_rows: 10000
  model_key: llava-1.5-7b-hf
  model_name_or_path: /fake/model
  training_stage: finetuning
  target_evals: [HallusionBench]
  default_submission_dir: curated/final_submission
  dataset:
    dataset_id: test_ds
    local_path: /fake/dataset
    image_column: images
    text_column: texts
"""


# ---------------------------------------------------------------------------
# State machine tests
# ---------------------------------------------------------------------------


class TestStateMachine:
    def test_initial_state_all_pending(self, tmp_path):
        ctrl = _make_controller(["a", "b"], iterations=2, suite_dir=tmp_path)
        assert all(t.state == PENDING for t in ctrl.targets)
        assert ctrl.active_target is None

    def test_begin_next_target_activates_first(self, tmp_path):
        ctrl = _make_controller(["a"], iterations=1, suite_dir=tmp_path)
        result = ctrl.begin_next_target()
        assert result["status"] == "target_activated"
        assert result["task_id"] == "a"
        assert result["iteration"] == 1
        assert ctrl.active_target.state == ACTIVE

    def test_mark_completed_then_advance(self, tmp_path):
        ctrl = _make_controller(["a"], iterations=2, suite_dir=tmp_path)

        # Activate first target
        ctrl.begin_next_target()
        assert ctrl.active_target.key == "a_iter1"

        # Mark it completed (simulates submit_eval success)
        ctrl.mark_target_completed({"status": "completed", "accuracy": 0.5})
        assert ctrl.targets[0].state == COMPLETED

        # Advance to next
        result = ctrl.begin_next_target()
        assert result["status"] == "target_activated"
        assert result["task_id"] == "a"
        assert result["iteration"] == 2

    def test_uncompleted_target_becomes_failed(self, tmp_path):
        ctrl = _make_controller(["a"], iterations=3, suite_dir=tmp_path)

        # Activate first target
        ctrl.begin_next_target()
        # Don't call mark_target_completed

        # Try to advance — current should fail
        ctrl.begin_next_target()
        assert ctrl.targets[0].state == FAILED

    def test_failed_iteration_does_not_cancel_next(self, tmp_path):
        ctrl = _make_controller(["a"], iterations=3, suite_dir=tmp_path)

        # Activate iter1
        ctrl.begin_next_target()
        # Don't complete it — advance (marks iter1 FAILED, activates iter2)
        result = ctrl.begin_next_target()

        assert ctrl.targets[0].state == FAILED
        assert ctrl.targets[1].state == ACTIVE
        assert ctrl.targets[2].state == PENDING
        assert result["status"] == "target_activated"
        assert result["task_id"] == "a"

    def test_failed_iteration_independent_across_tasks(self, tmp_path):
        ctrl = _make_controller(["a", "b"], iterations=2, suite_dir=tmp_path)

        # Activate a_iter1, don't complete — advance activates a_iter2
        ctrl.begin_next_target()
        result = ctrl.begin_next_target()

        assert ctrl.targets[0].state == FAILED   # a_iter1
        assert ctrl.targets[1].state == ACTIVE   # a_iter2 still runs
        assert result["status"] == "target_activated"
        assert result["task_id"] == "a"

    def test_suite_completes_when_all_done(self, tmp_path):
        ctrl = _make_controller(["a"], iterations=1, suite_dir=tmp_path)

        ctrl.begin_next_target()
        ctrl.mark_target_completed({"status": "completed"})
        result = ctrl.begin_next_target()

        assert result["status"] == "suite_completed"
        # suite_result.json should be written
        assert (tmp_path / "suite_result.json").exists()

    def test_get_run_plan(self, tmp_path):
        ctrl = _make_controller(["a", "b"], iterations=1, suite_dir=tmp_path)

        ctrl.begin_next_target()
        plan = ctrl.get_run_plan()

        assert plan["total_targets"] == 2
        assert plan["pending"] == 1
        assert plan["completed"] == 0
        assert plan["active_target"]["task_id"] == "a"

    def test_completed_and_failed_counts(self, tmp_path):
        ctrl = _make_controller(["a", "b"], iterations=2, suite_dir=tmp_path)

        # Complete a_iter1
        ctrl.begin_next_target()
        ctrl.mark_target_completed({"status": "completed"})

        # Complete a_iter2
        ctrl.begin_next_target()
        ctrl.mark_target_completed({"status": "completed"})

        # Fail b_iter1 (don't complete, advance)
        ctrl.begin_next_target()
        ctrl.begin_next_target()  # b_iter1 FAILED, b_iter2 now ACTIVE
        # Fail b_iter2 too
        ctrl.begin_next_target()  # b_iter2 FAILED → suite done

        plan = ctrl.get_run_plan()
        assert plan["completed"] == 2
        assert plan["failed"] == 2


# ---------------------------------------------------------------------------
# Crash recovery tests
# ---------------------------------------------------------------------------


class TestCrashRecovery:
    def test_state_persisted_after_activation(self, tmp_path):
        ctrl = _make_controller(["a"], iterations=1, suite_dir=tmp_path)
        ctrl.begin_next_target()

        state_file = tmp_path / "suite_state.json"
        assert state_file.exists()
        data = json.loads(state_file.read_text())
        assert data["targets"][0]["state"] == ACTIVE

    def test_state_persisted_after_completion(self, tmp_path):
        ctrl = _make_controller(["a"], iterations=1, suite_dir=tmp_path)
        ctrl.begin_next_target()
        ctrl.mark_target_completed({"status": "completed", "accuracy": 0.5})

        data = json.loads((tmp_path / "suite_state.json").read_text())
        assert data["targets"][0]["state"] == COMPLETED

    def test_resume_from_state_file(self, tmp_path):
        # Create a controller and advance to a state
        ctrl = _make_controller(["a", "b"], iterations=1, suite_dir=tmp_path)
        ctrl.begin_next_target()
        ctrl.mark_target_completed({"status": "completed"})
        # a_iter1 is COMPLETED, b_iter1 is PENDING

        # Resume from state
        ctrl2 = SuiteController.from_state_file(tmp_path / "suite_state.json")
        assert ctrl2.targets[0].state == COMPLETED
        assert ctrl2.targets[1].state == PENDING
        assert ctrl2.suite_dir == tmp_path

    def test_completed_target_preserved_after_crash(self, tmp_path):
        """Simulates: target COMPLETED via submit_eval, then crash before begin_next_target."""
        ctrl = _make_controller(["a", "b"], iterations=1, suite_dir=tmp_path)
        ctrl.begin_next_target()
        ctrl.mark_target_completed({"status": "completed"})
        # Crash here — don't call begin_next_target

        # Resume
        ctrl2 = SuiteController.from_state_file(tmp_path / "suite_state.json")
        # a_iter1 should still be COMPLETED
        assert ctrl2.targets[0].state == COMPLETED
        # b_iter1 should still be PENDING
        assert ctrl2.targets[1].state == PENDING

    def test_active_target_after_crash_stays_in_state(self, tmp_path):
        """If crash happens while target is ACTIVE (no eval), it stays ACTIVE in state file.
        The resuming code can decide to mark it FAILED or restart."""
        ctrl = _make_controller(["a"], iterations=2, suite_dir=tmp_path)
        ctrl.begin_next_target()
        # Crash — target is ACTIVE

        ctrl2 = SuiteController.from_state_file(tmp_path / "suite_state.json")
        assert ctrl2.targets[0].state == ACTIVE
        # Calling begin_next_target will mark it FAILED
        ctrl2.begin_next_target()
        assert ctrl2.targets[0].state == FAILED


# ---------------------------------------------------------------------------
# Target.to_dict
# ---------------------------------------------------------------------------


class TestTargetSerialization:
    def test_to_dict(self):
        t = Target("my_task", 2)
        t.state = COMPLETED
        t.eval_result = {"accuracy": 0.8}
        d = t.to_dict()
        assert d["task_id"] == "my_task"
        assert d["iteration"] == 2
        assert d["state"] == "completed"
        assert d["key"] == "my_task_iter2"
        assert d["eval_result"]["accuracy"] == 0.8
