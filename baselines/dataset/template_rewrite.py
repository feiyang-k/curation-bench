"""TemplateMatters baseline: apply programmatic template rewriting to LLaVA-665K subsets.

Paper: https://github.com/shijian2001/TemplateMatters
Method: Rewrites instruction templates using a programmatic generator (CPU only, no LLM).
        We apply templates to random subsets at each budget.

Usage:
    uv run python dataset/template_rewrite.py \
        --source /path/to/llava665k_ds \
        --budgets 10000 20000 50000 100000 200000 \
        --output_dir dataset/
"""

from __future__ import annotations

import argparse
import json
import random as rng
import secrets
import sys
from pathlib import Path

from datasets import DatasetDict, concatenate_datasets, load_from_disk

# Add vendor TemplateMatters to path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "vendor" / "TemplateMatters"))
from tm.template_generator import QuestionTemplateGenerator, generate_templates_set, assign_templates

SEED = 42
NUM_TEMPLATES = 15000


def _apply_templates(texts_list: list, templates: list[str]) -> list:
    """Apply template rewrites to the instruction portion of each sample."""
    rewritten = []
    for i, texts in enumerate(texts_list):
        if isinstance(texts, str):
            texts = json.loads(texts)
        if isinstance(texts, dict):
            texts = [texts]

        template = templates[i % len(templates)]
        new_texts = []
        for turn in texts:
            user = turn.get("user", turn.get("human", ""))
            assistant = turn.get("assistant", turn.get("gpt", ""))
            # Prepend template to user instruction
            new_user = f"{template} {user}" if template else user
            new_texts.append({"user": new_user, "assistant": assistant})
        rewritten.append(new_texts)
    return rewritten


def make_template_subsets(
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

    # Generate template set
    print(f"Generating {NUM_TEMPLATES} templates...")
    templates_set = generate_templates_set(QuestionTemplateGenerator, num_templates=NUM_TEMPLATES)
    print(f"Generated {len(templates_set)} unique templates")

    seed = secrets.randbits(32) if seed is None else seed
    print(f"Using seed: {seed}")
    rng.seed(seed)

    for n in budgets:
        if n > total:
            print(f"SKIP: budget {n} > total {total}")
            continue

        name = f"template_rewrite_{n // 1000}k"
        out_path = Path(output_dir) / name
        if out_path.exists():
            print(f"EXISTS: {out_path} — skipping")
            continue

        # Random subset first
        print(f"Sampling {n} from {total}...")
        indices = sorted(rng.sample(range(total), n))
        subset = ds.select(indices)

        # Assign templates to this subset (num_templates <= num_data required)
        num_t = min(len(templates_set), n)
        subset_templates = templates_set[:num_t]
        assigned = assign_templates(
            num_data=n,
            templates_set=subset_templates,
        )

        # Apply templates to the texts column
        print(f"Applying templates to {n} samples...")
        texts_col = subset["texts"]
        rewritten = _apply_templates(texts_col, assigned)
        subset = subset.remove_columns(["texts"])
        subset = subset.add_column("texts", rewritten)

        out_path.mkdir(parents=True, exist_ok=True)
        subset.save_to_disk(str(out_path))
        print(f"Saved {name} ({len(subset)} rows) → {out_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True,
                        help="Path to full LLaVA-665K Arrow dataset")
    parser.add_argument("--budgets", nargs="+", type=int,
                        default=[10000, 20000, 50000, 100000, 200000])
    parser.add_argument("--output_dir", default="dataset/")
    parser.add_argument("--seed", type=int, default=None,
                        help=f"Sampling seed. If omitted, generate a random seed. Legacy v1 seed was {SEED}.")
    args = parser.parse_args()

    make_template_subsets(args.source, args.budgets, args.output_dir, args.seed)
