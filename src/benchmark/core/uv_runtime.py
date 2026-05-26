from __future__ import annotations

import importlib.util
import shutil
import sys


def resolve_uv_command() -> list[str]:
    uv_path = shutil.which("uv")
    if uv_path:
        return [uv_path]

    if importlib.util.find_spec("uv") is not None:
        return [sys.executable, "-m", "uv"]

    raise RuntimeError(
        "uv is required for benchmark-owned train/eval tools but was not found. "
        "Install the `uv` package or ensure the `uv` executable is on PATH."
    )
