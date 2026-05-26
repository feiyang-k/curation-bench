"""Print a per-subset word/turn summary of an Arrow dataset.

Usage:
    python analyze_subsets.py <dataset_path>

Or set DATASET_PATH in the environment and run with no args.
"""

import pyarrow.ipc as ipc
import os
import sys
from collections import defaultdict

if len(sys.argv) > 1:
    dataset_path = sys.argv[1]
elif os.environ.get("DATASET_PATH"):
    dataset_path = os.environ["DATASET_PATH"]
else:
    sys.exit("usage: python analyze_subsets.py <dataset_path>  (or set DATASET_PATH)")

shard_files = sorted(f for f in os.listdir(dataset_path) if f.startswith("data-") and f.endswith(".arrow"))

subset_data = defaultdict(lambda: {"count": 0, "total_words": 0, "total_turns": 0})
total = 0

for sf in shard_files:
    with open(os.path.join(dataset_path, sf), "rb") as f:
        reader = ipc.open_stream(f)
        for batch in reader:
            subsets_col = batch.column("source_subset").to_pylist()
            texts_col = batch.column("texts").to_pylist()
            for j in range(len(subsets_col)):
                s = subsets_col[j]
                turns = texts_col[j]
                word_count = sum(len(turn.get("assistant", "").split()) for turn in turns)
                subset_data[s]["count"] += 1
                subset_data[s]["total_words"] += word_count
                subset_data[s]["total_turns"] += len(turns)
            total += len(subsets_col)

# Print all subsets sorted by avg words (ascending)
print(f"Total: {total} samples, {len(subset_data)} subsets\n")
print(f"{'Subset':<65} {'Count':>6} {'AvgWords':>8} {'AvgTurns':>8}")
print("-" * 95)
for s in sorted(subset_data, key=lambda s: subset_data[s]["total_words"]/subset_data[s]["count"]):
    d = subset_data[s]
    avg_words = d["total_words"] / d["count"]
    avg_turns = d["total_turns"] / d["count"]
    print(f"{s:<65} {d['count']:>6} {avg_words:>8.1f} {avg_turns:>8.1f}")
