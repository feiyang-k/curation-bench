"""Random baseline: uniform random sampling from LLaVA-665K.

Usage:
    uv run python dataset/make_random.py --source /data/nvidia/datasets/llava665k_full \
        --budgets 10000 20000 50000 100000 200000 \
        --output_dir dataset/
"""

from __future__ import annotations

import argparse
import os
import random as rng
import secrets
import tempfile
from pathlib import Path

os.environ.setdefault("HF_DATASETS_CACHE", tempfile.mkdtemp(prefix="hf_cache_"))

from datasets import DatasetDict, concatenate_datasets, load_from_disk

SEED = 42


def make_random_subsets(
    source_path: str,
    budgets: list[int],
    output_dir: str,
    seed: int | None,
) -> None:
    print(f"Loading dataset from {source_path}...")
    ds = load_from_disk(source_path, keep_in_memory=True)
    if isinstance(ds, DatasetDict):
        ds = concatenate_datasets([ds[k] for k in sorted(ds.keys())])

    total = len(ds)
    print(f"Total rows: {total}")
    print(f"Columns: {ds.column_names}")

    seed = secrets.randbits(32) if seed is None else seed
    print(f"Using seed: {seed}")
    rng.seed(seed)

    for n in budgets:
        if n > total:
            print(f"SKIP: budget {n} > total {total}")
            continue

        name = f"llava665k_random_{n // 1000}k"
        out_path = Path(output_dir) / name
        if out_path.exists():
            print(f"EXISTS: {out_path} — skipping")
            continue

        print(f"Sampling {n} from {total}...")
        indices = sorted(rng.sample(range(total), n))
        subset = ds.select(indices)

        out_path.mkdir(parents=True, exist_ok=True)
        subset.save_to_disk(str(out_path))
        print(f"Saved {name} ({len(subset)} rows) → {out_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True, help="Path to LLaVA-665K Arrow dataset")
    parser.add_argument("--budgets", nargs="+", type=int,
                        default=[10000, 20000, 50000, 100000, 200000])
    parser.add_argument("--output_dir", default="dataset/")
    parser.add_argument("--seed", type=int, default=None,
                        help=f"Sampling seed. If omitted, generate a random seed. Legacy v1 seed was {SEED}.")
    args = parser.parse_args()

    make_random_subsets(args.source, args.budgets, args.output_dir, args.seed)
