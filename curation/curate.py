from __future__ import annotations

import json
import os
import random
import sys
import time

import pyarrow.ipc as ipc


SEED = 123


def curate(dataset_path: str, output_path: str, target_n: int) -> dict:
    """Select target_n random samples from the dataset."""
    t0 = time.time()

    shard_files = sorted(
        f for f in os.listdir(dataset_path)
        if f.startswith("data-") and f.endswith(".arrow")
    )
    total = 0
    for sf in shard_files:
        with open(os.path.join(dataset_path, sf), "rb") as f:
            reader = ipc.open_stream(f)
            for batch in reader:
                total += batch.num_rows
    print(f"Total: {total} rows (scanned in {time.time()-t0:.1f}s)")

    rng = random.Random(SEED)
    selected = sorted(rng.sample(range(total), min(target_n, total)))
    print(f"Selected {len(selected)} samples")

    from datasets import load_from_disk
    t1 = time.time()
    ds = load_from_disk(dataset_path)
    curated = ds.select(selected)
    curated.save_to_disk(output_path)
    print(f"Dataset saved in {time.time()-t1:.1f}s")

    return {
        "strategy": f"random {target_n}",
        "total_rows": total,
        "selected_rows": len(curated),
        "seed": SEED,
    }


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python curate.py <dataset_path> <output_path> <target_n>", file=sys.stderr)
        sys.exit(1)
    result = curate(sys.argv[1], sys.argv[2], int(sys.argv[3]))
    print(json.dumps(result, indent=2))
