from __future__ import annotations

from pathlib import Path
from typing import Any

from ..core.dataset_store import load_dataset_from_disk

REQUIRED_COLUMNS = {"images", "texts"}


def validate_submission(path: str | Path, *, target_rows: int | None = None) -> dict[str, Any]:
    submission_path = Path(path).expanduser().resolve()
    if not submission_path.exists() or not submission_path.is_dir():
        return {"status": "failed", "error": f"Submission path does not exist: {submission_path}"}
    try:
        dataset = load_dataset_from_disk(submission_path, split="train")
    except Exception as exc:
        return {"status": "failed", "error": f"Could not load dataset from disk: {exc}"}
    columns = set(dataset.column_names)
    missing = sorted(REQUIRED_COLUMNS - columns)
    if missing:
        return {"status": "failed", "error": f"Missing required columns: {missing}", "columns": sorted(columns)}
    rows = len(dataset)
    payload: dict[str, Any] = {
        "status": "submitted",
        "submission_path": str(submission_path),
        "rows": rows,
        "columns": list(dataset.column_names),
        "required_columns": sorted(REQUIRED_COLUMNS),
    }
    if target_rows is not None:
        payload["target_rows"] = target_rows
        payload["matches_budget"] = rows == target_rows
        if rows != target_rows:
            payload["status"] = "failed"
            payload["error"] = f"Submission row count must equal target_rows: rows={rows}, target_rows={target_rows}"
    return payload
