"""ARDS baseline: select ARDS-chosen samples from LLaVA-665K, then subsample.

Paper: https://github.com/xyang583/ARDS
Source: Google Drive (ards_selected.json downloaded via gdown)

The ARDS JSON contains ~200K entries with `global_id` fields that index into
the original llava_v1_5_mix665k.json. We use these IDs to select from our
LLaVA-665K Arrow dataset, then subsample at each budget.

Usage:
    uv run python dataset/ards.py \
        --selection dataset/ards_selected.json \
        --source /path/to/llava665k_ds \
        --budgets 10000 20000 50000 100000 200000 \
        --output_dir dataset/
"""

from __future__ import annotations

import argparse
import json
import random as rng
import secrets
from pathlib import Path

from datasets import DatasetDict, concatenate_datasets, load_from_disk

SEED = 42


def make_ards_subsets(
    selection_path: str,
    source_path: str,
    budgets: list[int],
    output_dir: str,
    seed: int | None,
) -> None:
    # Load the ARDS selection JSON
    print(f"Loading ARDS selection from {selection_path}...")
    with open(selection_path) as f:
        ards_data = json.load(f)

    # Extract global_ids (1-indexed in ARDS, convert to 0-indexed)
    global_ids = sorted(set(int(d["global_id"]) - 1 for d in ards_data if "global_id" in d))
    print(f"ARDS selected {len(global_ids)} unique samples")

    # Load the full LLaVA-665K dataset
    print(f"Loading LLaVA-665K from {source_path}...")
    ds = load_from_disk(source_path, keep_in_memory=True)
    if isinstance(ds, DatasetDict):
        ds = concatenate_datasets([ds[k] for k in sorted(ds.keys())])

    total = len(ds)
    print(f"Total LLaVA-665K rows: {total}")

    # Filter to only valid indices
    valid_ids = [i for i in global_ids if i < total]
    print(f"Valid indices: {len(valid_ids)} (dropped {len(global_ids) - len(valid_ids)} out-of-range)")

    # Select ARDS subset from full dataset
    ards_ds = ds.select(valid_ids)
    print(f"ARDS full subset: {len(ards_ds)} rows")

    seed = secrets.randbits(32) if seed is None else seed
    print(f"Using seed: {seed}")
    rng.seed(seed)

    for n in budgets:
        if n > len(ards_ds):
            print(f"SKIP: budget {n} > ARDS total {len(ards_ds)}")
            continue

        name = f"ards_random_{n // 1000}k"
        out_path = Path(output_dir) / name
        if out_path.exists():
            print(f"EXISTS: {out_path} — skipping")
            continue

        print(f"Sampling {n} from {len(ards_ds)}...")
        indices = sorted(rng.sample(range(len(ards_ds)), n))
        subset = ards_ds.select(indices)

        out_path.mkdir(parents=True, exist_ok=True)
        subset.save_to_disk(str(out_path))
        print(f"Saved {name} ({len(subset)} rows) → {out_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--selection", default="dataset/ards_selected.json",
                        help="Path to ARDS selection JSON (from Google Drive)")
    parser.add_argument("--source", required=True,
                        help="Path to full LLaVA-665K Arrow dataset")
    parser.add_argument("--budgets", nargs="+", type=int,
                        default=[10000, 20000, 50000, 100000, 200000])
    parser.add_argument("--output_dir", default="dataset/")
    parser.add_argument("--seed", type=int, default=None,
                        help=f"Sampling seed. If omitted, generate a random seed. Legacy v1 seed was {SEED}.")
    args = parser.parse_args()

    make_ards_subsets(args.selection, args.source, args.budgets, args.output_dir, args.seed)
