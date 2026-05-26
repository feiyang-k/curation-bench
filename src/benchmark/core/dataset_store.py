from __future__ import annotations

from pathlib import Path

from datasets import Dataset, DatasetDict, load_from_disk


def load_dataset_from_disk(path: str | Path, split: str | None = None) -> Dataset:
    obj = load_from_disk(str(Path(path).expanduser().resolve()))
    if isinstance(obj, DatasetDict):
        if split and split in obj:
            return obj[split]
        return next(iter(obj.values()))
    return obj
