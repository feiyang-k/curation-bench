#!/usr/bin/env python3
"""One-command setup for generating non-agent baseline datasets."""

from __future__ import annotations

import argparse
import json
import os
import secrets
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_MATTERS_COMMIT = "4aef84c8e38b997610120de288c993dff848832a"
FAMILY_SCRIPTS = {
    "random": "scripts/generate_random.py",
    "icons": "scripts/generate_icons.py",
    "ards": "scripts/generate_ards.py",
    "template_rewrite": "scripts/generate_template_rewrite.py",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("dataset_run"),
        help="Output directory for generated baseline subsets.",
    )
    parser.add_argument(
        "--source",
        type=Path,
        default=None,
        help="Override LLaVA-665K Arrow dataset path. Defaults to LLAVA_ARROW_DIR in .env.",
    )
    parser.add_argument(
        "--llava-json",
        type=Path,
        default=None,
        help="Override llava_v1_5_mix665k.json path. Defaults to LLAVA_JSON_PATH in .env.",
    )
    parser.add_argument(
        "--ards-selection",
        type=Path,
        default=None,
        help="Override ards_selected.json path. Defaults to ARDS_SELECTION_PATH in .env.",
    )
    parser.add_argument(
        "--budgets",
        nargs="+",
        type=int,
        default=None,
        help="Optional budgets forwarded to all baseline generators.",
    )
    parser.add_argument("--seed", type=int, default=None)
    parser.add_argument("--force-new-seed", action="store_true")
    parser.add_argument(
        "--families",
        nargs="+",
        choices=sorted(FAMILY_SCRIPTS),
        default=list(FAMILY_SCRIPTS),
        help="Baseline families to generate. Defaults to all non-uniform families.",
    )
    parser.add_argument("--download-images", action="store_true")
    parser.add_argument("--skip-downloads", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def load_env() -> dict[str, str]:
    env = {
        "LLAVA_ARROW_DIR": "/path/to/llava665k_ds",
        "LLAVA_JSON_PATH": "dataset/llava_v1_5_mix665k.json",
        "ARDS_SELECTION_PATH": "dataset/ards_selected.json",
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


def run(cmd: list[str], *, dry_run: bool = False, check: bool = True) -> int:
    print("$ " + " ".join(cmd), flush=True)
    if dry_run:
        return 0
    completed = subprocess.run(cmd, cwd=ROOT, check=False)
    if check and completed.returncode != 0:
        raise SystemExit(completed.returncode)
    return completed.returncode


def template_matters_ready() -> bool:
    module_dir = ROOT / "vendor" / "TemplateMatters" / "tm"
    repo_dir = ROOT / "vendor" / "TemplateMatters"
    if not module_dir.exists():
        return False
    completed = subprocess.run(
        ["git", "-C", str(repo_dir), "rev-parse", "HEAD"],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        check=False,
    )
    return completed.returncode == 0 and completed.stdout.strip() == TEMPLATE_MATTERS_COMMIT


def ensure_template_matters(*, dry_run: bool) -> None:
    if template_matters_ready():
        print(f"ok: Template Matters submodule pinned at {TEMPLATE_MATTERS_COMMIT}")
        return
    run(
        [
            "git",
            "-C",
            str(ROOT.parent),
            "submodule",
            "update",
            "--init",
            "--recursive",
            "baselines/vendor/TemplateMatters",
        ],
        dry_run=dry_run,
    )


def assert_exists(path: Path, description: str, *, dry_run: bool = False) -> None:
    if path.exists():
        print(f"ok: {description}: {path}")
        return
    if dry_run:
        print(f"check: {description}: {path}")
        return
    raise SystemExit(f"missing {description}: {path}")


def resolve_seed(manifest_path: Path, requested_seed: int | None, force_new_seed: bool) -> int:
    if requested_seed is not None:
        return requested_seed
    if manifest_path.exists() and not force_new_seed:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        if "seed" in manifest:
            return int(manifest["seed"])
    return secrets.randbits(32)


def write_manifest(manifest_path: Path, payload: dict) -> None:
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> None:
    args = parse_args()
    env = load_env()

    ensure_template_matters(dry_run=args.dry_run)

    if not args.skip_downloads:
        cmd = [sys.executable, "scripts/download_llava665k.py"]
        if args.download_images:
            cmd.append("--download-images")
        if args.dry_run:
            cmd.append("--dry-run")
        run(cmd, dry_run=False)

    source = resolve_path(args.source or env["LLAVA_ARROW_DIR"])
    llava_json = resolve_path(args.llava_json or env["LLAVA_JSON_PATH"])
    ards_selection = resolve_path(args.ards_selection or env["ARDS_SELECTION_PATH"])

    assert_exists(source, "LLaVA-665K Arrow dataset", dry_run=args.dry_run)
    assert_exists(llava_json, "LLaVA instruction JSON", dry_run=args.dry_run)
    assert_exists(ards_selection, "ARDS selected-result JSON", dry_run=args.dry_run)
    assert_exists(ROOT / "vendor" / "TemplateMatters" / "tm", "Template Matters submodule", dry_run=args.dry_run)

    output_dir = resolve_path(args.output_dir)
    manifest_path = output_dir / "dataset_run_manifest.json"
    seed = resolve_seed(manifest_path, args.seed, args.force_new_seed)
    manifest = {
        "ards_selection": str(ards_selection),
        "budgets": args.budgets,
        "families": args.families,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "generators": [],
        "llava_json": str(llava_json),
        "output_dir": str(output_dir),
        "seed": seed,
        "source": str(source),
    }
    if not args.dry_run:
        write_manifest(manifest_path, manifest)

    for family in args.families:
        cmd = [
            sys.executable,
            FAMILY_SCRIPTS[family],
            "--output-dir",
            str(output_dir),
            "--source",
            str(source),
            "--seed",
            str(seed),
        ]
        if family == "icons":
            cmd.extend(["--llava-json", str(llava_json)])
        elif family == "ards":
            cmd.extend(["--ards-selection", str(ards_selection)])
        if args.budgets:
            cmd.extend(["--budgets", *(str(n) for n in args.budgets)])
        returncode = run(cmd, dry_run=args.dry_run, check=False)
        manifest["generators"].append(
            {
                "family": family,
                "script": FAMILY_SCRIPTS[family],
                "command": cmd,
                "returncode": returncode,
            }
        )
        if not args.dry_run:
            write_manifest(manifest_path, manifest)
        if returncode != 0:
            raise SystemExit(returncode)


if __name__ == "__main__":
    main()
