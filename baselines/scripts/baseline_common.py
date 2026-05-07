"""Shared helpers for baseline data-generation entrypoints."""

from __future__ import annotations

import os
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

DEFAULT_ENV = {
    "LLAVA_ARROW_DIR": "/path/to/llava665k_ds",
    "LLAVA_JSON_PATH": "dataset/llava_v1_5_mix665k.json",
    "ARDS_SELECTION_PATH": "dataset/ards_selected.json",
}


def load_env() -> dict[str, str]:
    env = dict(DEFAULT_ENV)
    env_path = ROOT / ".env"
    if not env_path.exists():
        return env

    for raw_line in env_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        env[key.strip()] = value.strip().strip('"').strip("'")
    return env


def resolve_path(value: str | Path) -> Path:
    path = Path(os.path.expandvars(os.path.expanduser(str(value))))
    return path if path.is_absolute() else ROOT / path


def budget_args(budgets: list[int] | None) -> list[str]:
    if not budgets:
        return []
    return ["--budgets", *(str(n) for n in budgets)]


def run_command(cmd: list[str], *, dry_run: bool = False) -> int:
    print("$ " + " ".join(cmd), flush=True)
    if dry_run:
        return 0
    return subprocess.run(cmd, cwd=ROOT, check=False).returncode
