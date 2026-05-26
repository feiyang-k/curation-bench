"""Parser for run_prompt.md files.

A run_prompt.md has two parts:
1. YAML frontmatter (between --- delimiters): tasks, iterations, profile
2. Markdown body: strategy text for the agent
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

import yaml


@dataclass
class RunPrompt:
    """Parsed content of a run_prompt.md file."""

    tasks: list[str]
    iterations: int = 1
    profile: str | None = None
    strategy_text: str = ""

    # Original path for error messages
    source_path: str | None = None


def parse_run_prompt(path: str | Path) -> RunPrompt:
    """Parse a run_prompt.md file into a RunPrompt.

    Raises ValueError for missing/invalid frontmatter.
    """
    path = Path(path)
    text = path.read_text(encoding="utf-8")
    return parse_run_prompt_text(text, source_path=str(path))


def parse_run_prompt_text(text: str, *, source_path: str | None = None) -> RunPrompt:
    """Parse run_prompt.md content from a string."""
    frontmatter, body = _split_frontmatter(text, source_path=source_path)
    tasks = _extract_tasks(frontmatter, source_path=source_path)
    iterations = _extract_iterations(frontmatter, source_path=source_path)
    profile = frontmatter.get("profile")
    if profile is not None:
        profile = str(profile)

    return RunPrompt(
        tasks=tasks,
        iterations=iterations,
        profile=profile,
        strategy_text=body.strip(),
        source_path=source_path,
    )


def _split_frontmatter(
    text: str, *, source_path: str | None = None
) -> tuple[dict, str]:
    """Split text into (frontmatter_dict, body_text).

    Frontmatter is delimited by --- at the start and end.
    """
    stripped = text.lstrip("\n")
    if not stripped.startswith("---"):
        raise ValueError(
            f"run_prompt.md must start with YAML frontmatter (---).{_src(source_path)}"
        )
    # Find the closing ---
    rest = stripped[3:]
    # Skip the first newline after opening ---
    if rest.startswith("\n"):
        rest = rest[1:]
    closing = rest.find("\n---")
    if closing < 0:
        raise ValueError(
            f"run_prompt.md frontmatter is missing closing ---.{_src(source_path)}"
        )
    yaml_text = rest[:closing]
    body = rest[closing + 4:]  # skip \n---
    # Skip the newline right after closing ---
    if body.startswith("\n"):
        body = body[1:]

    try:
        data = yaml.safe_load(yaml_text)
    except yaml.YAMLError as exc:
        raise ValueError(
            f"Invalid YAML in frontmatter: {exc}.{_src(source_path)}"
        ) from exc

    if not isinstance(data, dict):
        raise ValueError(
            f"Frontmatter must be a YAML mapping, got {type(data).__name__}.{_src(source_path)}"
        )

    return data, body


def _extract_tasks(
    frontmatter: dict, *, source_path: str | None = None
) -> list[str]:
    """Extract and validate the tasks list from frontmatter."""
    if "tasks" not in frontmatter:
        raise ValueError(
            f"Frontmatter must include 'tasks' (list of task IDs).{_src(source_path)}"
        )
    tasks = frontmatter["tasks"]
    if not isinstance(tasks, list) or len(tasks) == 0:
        raise ValueError(
            f"'tasks' must be a non-empty list of task IDs.{_src(source_path)}"
        )
    for i, t in enumerate(tasks):
        if not isinstance(t, str) or not t.strip():
            raise ValueError(
                f"tasks[{i}] must be a non-empty string.{_src(source_path)}"
            )
    return [t.strip() for t in tasks]


def _extract_iterations(
    frontmatter: dict, *, source_path: str | None = None
) -> int:
    """Extract iteration count, defaulting to 1."""
    iterations = frontmatter.get("iterations", 1)
    if not isinstance(iterations, int) or iterations < 1:
        raise ValueError(
            f"'iterations' must be a positive integer, got {iterations!r}.{_src(source_path)}"
        )
    return iterations


def _src(source_path: str | None) -> str:
    return f" (in {source_path})" if source_path else ""
