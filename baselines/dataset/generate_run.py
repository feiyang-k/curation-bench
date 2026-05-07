#!/usr/bin/env python3
"""Generate one complete dataset run with a shared recorded random seed."""

from __future__ import annotations

import argparse
import json
import os
import secrets
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SOURCE_DEFAULT = Path("/path/to/llava665k_ds")
LLAVA_JSON_DEFAULT = Path("dataset/llava_v1_5_mix665k.json")
ARDS_SELECTION_DEFAULT = Path("dataset/ards_selected.json")

GENERATORS = [
    ("llava665k_random", ["dataset/make_random.py"]),
    ("icons_random", ["dataset/icons.py"]),
    ("ards_random", ["dataset/ards.py"]),
    ("template_rewrite", ["dataset/template_rewrite.py"]),
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--source", type=Path, default=None)
    parser.add_argument(
        "--llava-json",
        type=Path,
        default=None,
        help="Path to llava_v1_5_mix665k.json. Defaults to LLAVA_JSON_PATH in .env.",
    )
    parser.add_argument(
        "--ards-selection",
        type=Path,
        default=None,
        help="Path to ards_selected.json. Defaults to ARDS_SELECTION_PATH in .env.",
    )
    parser.add_argument(
        "--budgets",
        nargs="+",
        type=int,
        default=None,
        help="Optional budgets forwarded to every generator. Defaults match each generator script.",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=None,
        help="Shared seed for every generator. If omitted, create or reuse the output manifest seed.",
    )
    parser.add_argument(
        "--force-new-seed",
        action="store_true",
        help="Ignore an existing manifest seed and generate a new one.",
    )
    return parser.parse_args()


def load_env() -> dict[str, str]:
    env = {
        "LLAVA_ARROW_DIR": str(SOURCE_DEFAULT),
        "LLAVA_JSON_PATH": str(LLAVA_JSON_DEFAULT),
        "ARDS_SELECTION_PATH": str(ARDS_SELECTION_DEFAULT),
    }
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


def resolve_seed(manifest_path: Path, requested_seed: int | None, force_new_seed: bool) -> int:
    if requested_seed is not None:
        return requested_seed
    if manifest_path.exists() and not force_new_seed:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        if "seed" in manifest:
            return int(manifest["seed"])
    return secrets.randbits(32)


def main() -> None:
    args = parse_args()
    env = load_env()
    output_dir = args.output_dir
    if not output_dir.is_absolute():
        output_dir = ROOT / output_dir
    source = resolve_path(args.source or env["LLAVA_ARROW_DIR"])
    llava_json = resolve_path(args.llava_json or env["LLAVA_JSON_PATH"])
    ards_selection = resolve_path(args.ards_selection or env["ARDS_SELECTION_PATH"])
    budget_args = ["--budgets", *(str(n) for n in args.budgets)] if args.budgets else []

    output_dir.mkdir(parents=True, exist_ok=True)
    manifest_path = output_dir / "dataset_run_manifest.json"
    seed = resolve_seed(manifest_path, args.seed, args.force_new_seed)

    manifest = {
        "ards_selection": str(ards_selection),
        "budgets": args.budgets,
        "llava_json": str(llava_json),
        "output_dir": str(output_dir),
        "source": str(source),
        "seed": seed,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "generators": [],
    }
    manifest_path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"Dataset run seed: {seed}")
    print(f"Manifest: {manifest_path}")

    for name, script_args in GENERATORS:
        extra_args: list[str] = []
        if name == "icons_random":
            extra_args.extend(["--llava-json", str(llava_json)])
        elif name == "ards_random":
            extra_args.extend(["--selection", str(ards_selection)])
        cmd = [
            "uv",
            "run",
            "python",
            *script_args,
            *extra_args,
            "--source",
            str(source),
            "--output_dir",
            str(output_dir),
            "--seed",
            str(seed),
            *budget_args,
        ]
        print("\n$ " + " ".join(cmd), flush=True)
        completed = subprocess.run(cmd, cwd=ROOT)
        manifest["generators"].append(
            {
                "name": name,
                "command": cmd,
                "returncode": completed.returncode,
            }
        )
        manifest_path.write_text(
            json.dumps(manifest, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        if completed.returncode != 0:
            raise SystemExit(completed.returncode)


if __name__ == "__main__":
    main()
