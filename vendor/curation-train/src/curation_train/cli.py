"""CLI entry point for curation-train.

Usage:
    curation-train <config.json>

Reads a JSON config file, runs multimodal finetune (Qwen, LLaVA, or SmolVLM),
writes result JSON to stdout.
"""

from __future__ import annotations

import json
import sys

from curation_train.runner import run_finetune


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: curation-train <config.json>", file=sys.stderr)
        sys.exit(1)

    config_path = sys.argv[1]
    with open(config_path) as f:
        config = json.load(f)

    result = run_finetune(config)

    # Write result JSON to stdout for the executor to capture
    print(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    main()
