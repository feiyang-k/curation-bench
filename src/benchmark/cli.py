from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any



# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

_ACTIVE_SUITE_FILE = ".bench_active_suite"


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def _resolve_suite_dir(args: argparse.Namespace) -> Path:
    """Resolve suite_dir from --suite-dir arg, then .bench_active_suite fallback."""
    explicit = getattr(args, "suite_dir", None)
    if explicit:
        return Path(explicit)
    active_file = Path.cwd() / _ACTIVE_SUITE_FILE
    if active_file.exists():
        return Path(active_file.read_text(encoding="utf-8").strip())
    raise SystemExit(
        f"Error: no active suite. Run 'datacuration-bench init' first, "
        f"or pass --suite-dir explicitly."
    )


def _load_suite(args: argparse.Namespace) -> Any:
    """Load SuiteController from suite_state.json."""
    from .tools.suite import SuiteController

    suite_dir = _resolve_suite_dir(args)
    state_path = suite_dir / "suite_state.json"
    if not state_path.exists():
        raise SystemExit(f"Error: suite_state.json not found in {suite_dir}")
    return SuiteController.from_state_file(state_path)


def _add_suite_dir_arg(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "--suite-dir", default=None,
        help="Suite directory (default: read from .bench_active_suite)",
    )


# ---------------------------------------------------------------------------
# Benchmark commands
# ---------------------------------------------------------------------------


def cmd_init(args: argparse.Namespace) -> None:
    """Initialize a benchmark suite from run_prompt.md and profile."""
    import os
    from .tools.suite import SuiteController

    kwargs: dict[str, Any] = {"prompt_path": args.prompt}
    if args.profile:
        kwargs["profile_path"] = args.profile
    # docker_runner sets these when it invokes `datacuration-bench init` so the
    # suite can segregate by agent and honor --new-suite across the subprocess.
    agent_env = os.environ.get("BENCHMARK_AGENT")
    if agent_env:
        kwargs["agent"] = agent_env
    if os.environ.get("BENCHMARK_NEW_SUITE"):
        kwargs["new_suite"] = True

    suite = SuiteController.from_prompt(**kwargs)

    # Write active suite pointer
    active_file = Path.cwd() / _ACTIVE_SUITE_FILE
    active_file.write_text(str(suite.suite_dir), encoding="utf-8")

    print(json.dumps(suite.get_run_plan(), indent=2))


def cmd_next(args: argparse.Namespace) -> None:
    """Advance to the next target."""
    suite = _load_suite(args)
    result = suite.begin_next_target()
    print(json.dumps(result, indent=2))


def cmd_plan(args: argparse.Namespace) -> None:
    """Show all targets and their current states."""
    suite = _load_suite(args)
    print(json.dumps(suite.get_run_plan(), indent=2))


def cmd_task(args: argparse.Namespace) -> None:
    """Show the active target's task details."""
    suite = _load_suite(args)
    session = suite.get_active_session()
    print(json.dumps(session.summarize_task(), indent=2))


def cmd_time_budget(args: argparse.Namespace) -> None:
    """Show remaining strategy time budget."""
    suite = _load_suite(args)
    session = suite.get_active_session()
    print(json.dumps(session.get_time_budget(), indent=2))


def cmd_audit(args: argparse.Namespace) -> None:
    """Run contamination check on a candidate dataset."""
    suite = _load_suite(args)
    session = suite.get_active_session()
    result = session.dispatch("audit_contamination", {"submission_path": args.path})
    print(json.dumps(result, indent=2))


def cmd_submit(args: argparse.Namespace) -> None:
    """Validate and finalize a curated dataset submission."""
    suite = _load_suite(args)
    session = suite.get_active_session()
    result = session.dispatch("submit_curated_dataset", {"submission_path": args.path})
    print(json.dumps(result, indent=2))


def cmd_finetune(args: argparse.Namespace) -> None:
    """Fine-tune the target model on the submitted dataset."""
    suite = _load_suite(args)
    session = suite.get_active_session()
    result = session.dispatch("submit_finetune", {})
    print(json.dumps(result, indent=2))


def cmd_eval(args: argparse.Namespace) -> None:
    """Evaluate the fine-tuned model. Marks target COMPLETED on success."""
    suite = _load_suite(args)
    session = suite.get_active_session()
    result = session.dispatch("submit_eval", {})
    if isinstance(result, dict) and result.get("status") == "completed":
        suite.mark_target_completed(result)
    print(json.dumps(result, indent=2))


# ---------------------------------------------------------------------------
# Utility commands
# ---------------------------------------------------------------------------


def cmd_run(args: argparse.Namespace) -> None:
    """Launch benchmark agent in a Docker container."""
    from .runner.docker_runner import run_agent
    exit_code = run_agent(
        args.agent,
        profile_name=args.profile,
        docker_config_path=args.docker_config,
        rebuild=args.rebuild,
        dry_run=args.dry_run,
        new_suite=args.new_suite,
        prompt=args.prompt,
    )
    raise SystemExit(exit_code)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="datacuration-bench",
        description="Data-curation benchmark CLI",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    # --- Benchmark commands ---

    p_init = sub.add_parser("init", help="Initialize a benchmark suite")
    p_init.add_argument("--prompt", default="run_prompt.md", help="Path to run_prompt.md")
    p_init.add_argument("--profile", default=None, help="Profile name or path")

    p_next = sub.add_parser("next", help="Advance to the next target")
    _add_suite_dir_arg(p_next)

    p_plan = sub.add_parser("plan", help="Show all targets and states")
    _add_suite_dir_arg(p_plan)

    p_task = sub.add_parser("task", help="Show active target's task details")
    _add_suite_dir_arg(p_task)

    p_budget = sub.add_parser("time-budget", help="Show remaining strategy time")
    _add_suite_dir_arg(p_budget)

    p_audit = sub.add_parser("audit", help="Run contamination check")
    _add_suite_dir_arg(p_audit)
    p_audit.add_argument("--path", required=True, help="Path to candidate dataset")

    p_submit = sub.add_parser("submit", help="Validate and submit curated dataset")
    _add_suite_dir_arg(p_submit)
    p_submit.add_argument("--path", required=True, help="Path to curated dataset")

    p_finetune = sub.add_parser("finetune", help="Fine-tune the target model")
    _add_suite_dir_arg(p_finetune)

    p_eval = sub.add_parser("eval", help="Evaluate the fine-tuned model")
    _add_suite_dir_arg(p_eval)

    # --- Utility commands ---

    p_run = sub.add_parser("run", help="Run benchmark agent in Docker container")
    p_run.add_argument(
        "agent",
        choices=["claude", "claude-deepseek", "codex", "openhands-kimi", "openhands-qwen"],
        help="Agent to run",
    )
    p_run.add_argument("--profile", default=None, help="Profile name or path")
    p_run.add_argument("--docker-config", default="configs/docker.yaml", help="Docker runner config")
    p_run.add_argument("--rebuild", action="store_true", help="Force rebuild Docker image")
    p_run.add_argument("--dry-run", action="store_true", help="Show Docker command without running")
    p_run.add_argument(
        "--new-suite", action="store_true",
        help="Force creating a fresh suite instead of resuming the active one",
    )
    p_run.add_argument(
        "--prompt", choices=["plain", "instruction", "skill"], default="plain",
        help="Which protocol .md the agent reads (default: plain)",
    )

    args = parser.parse_args()

    _dispatch = {
        "init": cmd_init,
        "next": cmd_next,
        "plan": cmd_plan,
        "task": cmd_task,
        "time-budget": cmd_time_budget,
        "audit": cmd_audit,
        "submit": cmd_submit,
        "finetune": cmd_finetune,
        "eval": cmd_eval,
        "run": cmd_run,
    }

    handler = _dispatch.get(args.command)
    if handler:
        handler(args)
