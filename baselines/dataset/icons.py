"""ICONS-133K baseline: match ICONS selection to LLaVA-665K Arrow dataset.

ICONS (xindiw/LLAVA-ICONS-133K) provides a curated 133K subset of LLaVA-665K.
Entries are matched to our Arrow dataset by ID or image path via the original
llava_v1_5_mix665k.json, then subsampled at each budget.

Usage:
    uv run python dataset/icons.py \
        --source /path/to/llava665k_ds \
        --llava-json dataset/llava_v1_5_mix665k.json \
        --budgets 10000 20000 50000 100000 \
        --output_dir dataset/
"""

from __future__ import annotations

import argparse
import json
import random as rng
import secrets
from pathlib import Path

from datasets import DatasetDict, concatenate_datasets, load_dataset, load_from_disk

SEED = 42
HF_DATASET_ID = "xindiw/LLAVA-ICONS-133K"


def make_icons_subsets(
    source_path: str,
    llava_json_path: str,
    budgets: list[int],
    output_dir: str,
    seed: int | None,
) -> None:
    # Load the original LLaVA-665K JSON to build ID/path -> index mapping
    print(f"Loading LLaVA JSON from {llava_json_path}...")
    with open(llava_json_path) as f:
        llava_json = json.load(f)

    # Build lookup: ID or image path -> Arrow index
    # Arrow dataset only has image entries (624,610 of 665,298)
    lookup: dict[str, int] = {}
    arrow_idx = 0
    for entry in llava_json:
        if "image" not in entry:
            continue
        eid = str(entry["id"])
        lookup[eid] = arrow_idx
        lookup[entry["image"]] = arrow_idx
        arrow_idx += 1
    print(f"Built lookup with {len(lookup)} keys for {arrow_idx} Arrow rows")

    # Load ICONS from HuggingFace
    print(f"Loading {HF_DATASET_ID} from HuggingFace...")
    icons = load_dataset(HF_DATASET_ID, split="train")
    print(f"ICONS total: {len(icons)} rows")

    # Match ICONS entries to Arrow indices
    matched_indices = []
    missed = 0
    for row in icons:
        icon_id = str(row["id"])
        icon_img = row.get("image", "")
        idx = lookup.get(icon_id) or lookup.get(icon_img)
        if idx is not None:
            matched_indices.append(idx)
        else:
            missed += 1

    matched_indices = sorted(set(matched_indices))
    print(f"Matched {len(matched_indices)} ICONS entries to Arrow indices (missed {missed})")

    # Load our Arrow dataset
    print(f"Loading LLaVA-665K Arrow from {source_path}...")
    ds = load_from_disk(source_path, keep_in_memory=True)
    if isinstance(ds, DatasetDict):
        ds = concatenate_datasets([ds[k] for k in sorted(ds.keys())])

    # Select ICONS subset from Arrow
    icons_ds = ds.select(matched_indices)
    print(f"ICONS Arrow subset: {len(icons_ds)} rows")

    seed = secrets.randbits(32) if seed is None else seed
    print(f"Using seed: {seed}")
    rng.seed(seed)

    for n in budgets:
        if n > len(icons_ds):
            print(f"SKIP: budget {n} > ICONS total {len(icons_ds)}")
            continue

        name = f"icons_random_{n // 1000}k"
        out_path = Path(output_dir) / name
        if out_path.exists():
            print(f"EXISTS: {out_path} — skipping")
            continue

        print(f"Sampling {n} from {len(icons_ds)}...")
        indices = sorted(rng.sample(range(len(icons_ds)), n))
        subset = icons_ds.select(indices)

        out_path.mkdir(parents=True, exist_ok=True)
        subset.save_to_disk(str(out_path))
        print(f"Saved {name} ({len(subset)} rows) → {out_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True,
                        help="Path to full LLaVA-665K Arrow dataset")
    parser.add_argument("--llava-json", default="dataset/llava_v1_5_mix665k.json",
                        help="Path to llava_v1_5_mix665k.json")
    parser.add_argument("--budgets", nargs="+", type=int,
                        default=[10000, 20000, 50000, 100000])
    parser.add_argument("--output_dir", default="dataset/")
    parser.add_argument("--seed", type=int, default=None,
                        help=f"Sampling seed. If omitted, generate a random seed. Legacy v1 seed was {SEED}.")
    args = parser.parse_args()

    make_icons_subsets(args.source, args.llava_json, args.budgets, args.output_dir, args.seed)
