#!/usr/bin/env python3
"""Generate ICONS baseline subsets."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from baseline_common import budget_args, load_env, resolve_path, run_command


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--source", type=Path, default=None)
    parser.add_argument("--llava-json", type=Path, default=None)
    parser.add_argument("--seed", type=int, default=None)
    parser.add_argument("--budgets", nargs="+", type=int, default=None)
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    env = load_env()
    source = resolve_path(args.source or env["LLAVA_ARROW_DIR"])
    llava_json = resolve_path(args.llava_json or env["LLAVA_JSON_PATH"])
    output_dir = resolve_path(args.output_dir)

    cmd = [
        sys.executable,
        "dataset/icons.py",
        "--llava-json",
        str(llava_json),
        "--source",
        str(source),
        "--output_dir",
        str(output_dir),
        *budget_args(args.budgets),
    ]
    if args.seed is not None:
        cmd.extend(["--seed", str(args.seed)])

    raise SystemExit(run_command(cmd, dry_run=args.dry_run))


if __name__ == "__main__":
    main()
