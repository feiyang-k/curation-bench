from __future__ import annotations

import csv
import hashlib
import re
import sys
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from ..core.dataset_store import load_dataset_from_disk


@dataclass(slots=True)
class EvalBenchmarkSpec:
    filename: str
    question_column: str
    answer_column: str


EVAL_REGISTRY: dict[str, EvalBenchmarkSpec] = {
    "MMVet": EvalBenchmarkSpec("MMVet.tsv", "question", "answer"),
    "LLaVABench": EvalBenchmarkSpec("LLaVABench.tsv", "question", "gpt4_ans"),
    "OCRBench": EvalBenchmarkSpec("OCRBench.tsv", "question", "answer"),
    "HallusionBench": EvalBenchmarkSpec("HallusionBench.tsv", "question", "answer"),
    "MMBench": EvalBenchmarkSpec("MMBench.tsv", "question", "answer"),
    "MMMU_DEV_VAL": EvalBenchmarkSpec("MMMU_DEV_VAL.tsv", "question", "answer"),
    "MMStar": EvalBenchmarkSpec("MMStar.tsv", "question", "answer"),
    "MathVista_MINI": EvalBenchmarkSpec("MathVista_MINI.tsv", "question", "answer"),
}


def _normalize(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def _make_qa_pair(question: str, answer: str) -> str:
    return f"Q: {_normalize(question)}\nA: {_normalize(answer)}"


def _word_ngrams(tokens: list[str], n: int) -> list[tuple[str, ...]]:
    if len(tokens) < n:
        return []
    return [tuple(tokens[i : i + n]) for i in range(len(tokens) - n + 1)]


def _load_eval_qa_pairs(eval_dir: Path, spec: EvalBenchmarkSpec) -> list[str]:
    csv.field_size_limit(sys.maxsize)
    tsv_path = eval_dir / spec.filename
    pairs: list[str] = []
    with open(tsv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter="\t")
        for row in reader:
            pairs.append(_make_qa_pair(row[spec.question_column], row[spec.answer_column]))
    return pairs


def _extract_submission_qa_pairs(submission_path: str | Path) -> list[str]:
    ds = load_dataset_from_disk(submission_path)
    pairs: list[str] = []
    for texts in ds["texts"]:
        for turn in texts:
            pairs.append(_make_qa_pair(turn["user"], turn["assistant"]))
    return pairs


def hash_exact_duplicates(
    submission_pairs: list[str],
    eval_pairs_by_benchmark: dict[str, list[str]],
) -> dict[str, Any]:
    unique_pairs = set(submission_pairs)
    hash_set = {hashlib.sha256(p.encode("utf-8")).hexdigest() for p in unique_pairs}
    results: dict[str, Any] = {}
    for bench_name, eval_pairs in eval_pairs_by_benchmark.items():
        exact_count = 0
        for ep in eval_pairs:
            h = hashlib.sha256(ep.encode("utf-8")).hexdigest()
            if h in hash_set:
                exact_count += 1
        results[bench_name] = {
            "total_eval_pairs": len(eval_pairs),
            "exact_matches": exact_count,
        }
    return results


def ngram_near_duplicates(
    submission_pairs: list[str],
    eval_pairs_by_benchmark: dict[str, list[str]],
    *,
    n: int = 8,
    threshold: float = 0.8,
    min_tokens: int = 12,
) -> dict[str, Any]:
    unique_pairs = list(set(submission_pairs))

    # Build inverted index: ngram -> set of indices into unique_pairs
    inverted: dict[tuple[str, ...], set[int]] = defaultdict(set)
    sub_ngrams_cache: list[set[tuple[str, ...]]] = []
    for idx, pair in enumerate(unique_pairs):
        tokens = pair.split()
        ngrams = _word_ngrams(tokens, n)
        ngram_set = set(ngrams)
        sub_ngrams_cache.append(ngram_set)
        for ng in ngram_set:
            inverted[ng].add(idx)

    results: dict[str, Any] = {}
    for bench_name, eval_pairs in eval_pairs_by_benchmark.items():
        near_count = 0
        matches: list[dict[str, Any]] = []
        for ep in eval_pairs:
            tokens = ep.split()
            if len(tokens) < min_tokens:
                continue
            eval_ngram_set = set(_word_ngrams(tokens, n))
            # Find candidate submission pairs via index
            candidates: set[int] = set()
            for ng in eval_ngram_set:
                if ng in inverted:
                    candidates.update(inverted[ng])
            best_sim = 0.0
            best_idx = -1
            for cand_idx in candidates:
                sub_ngram_set = sub_ngrams_cache[cand_idx]
                overlap = len(eval_ngram_set & sub_ngram_set)
                denom = min(len(eval_ngram_set), len(sub_ngram_set))
                if denom == 0:
                    continue
                similarity = overlap / denom
                if similarity > best_sim:
                    best_sim = similarity
                    best_idx = cand_idx
            if best_sim >= threshold:
                near_count += 1
                if len(matches) < 100:
                    matches.append({
                        "submission_text": unique_pairs[best_idx],
                        "similarity": round(best_sim, 4),
                    })
        results[bench_name] = {
            "total_eval_pairs": len(eval_pairs),
            "near_matches": near_count,
            "matches": matches,
        }
    return results


def audit_contamination(
    submission_path: str | Path,
    eval_dir: str | Path,
    benchmarks: list[str],
    *,
    ngram_n: int = 8,
    ngram_threshold: float = 0.8,
    min_tokens_for_near: int = 12,
) -> dict[str, Any]:
    eval_dir = Path(eval_dir)
    if not eval_dir.exists():
        return {"status": "skipped", "error": "eval_data_dir does not exist"}

    submission_pairs = _extract_submission_qa_pairs(submission_path)

    eval_pairs_by_benchmark: dict[str, list[str]] = {}
    skipped_benchmarks: dict[str, str] = {}

    for bench in benchmarks:
        spec = EVAL_REGISTRY.get(bench)
        if spec is None:
            skipped_benchmarks[bench] = "not in registry"
            continue
        tsv_path = eval_dir / spec.filename
        if not tsv_path.exists():
            skipped_benchmarks[bench] = "file not found"
            continue
        eval_pairs_by_benchmark[bench] = _load_eval_qa_pairs(eval_dir, spec)

    hash_results = hash_exact_duplicates(submission_pairs, eval_pairs_by_benchmark)
    ngram_results = ngram_near_duplicates(
        submission_pairs, eval_pairs_by_benchmark,
        n=ngram_n, threshold=ngram_threshold, min_tokens=min_tokens_for_near,
    )

    status = "clean"
    for bench_name in eval_pairs_by_benchmark:
        exact = hash_results[bench_name]["exact_matches"]
        total = hash_results[bench_name]["total_eval_pairs"]
        near = ngram_results[bench_name]["near_matches"]
        exact_rate = exact / total if total > 0 else 0.0
        near_rate = near / total if total > 0 else 0.0
        if exact_rate >= 0.10 or near_rate >= 0.20:
            status = "high_risk"
            break
        if exact_rate >= 0.05 or near_rate >= 0.10:
            status = "warning"

    if status == "high_risk":
        recommendation = "Contamination appears material; revise selection before submission."
    elif status == "warning":
        recommendation = "A small number of exact overlaps or near-duplicates were detected; review before final submission."
    else:
        recommendation = "No contamination detected."

    return {
        "status": status,
        "submission_path": str(submission_path),
        "submission_qa_pair_count": len(submission_pairs),
        "benchmarks_checked": list(eval_pairs_by_benchmark.keys()),
        "skipped_benchmarks": skipped_benchmarks,
        "hash_exact": hash_results,
        "ngram_near": ngram_results,
        "ngram_params": {"n": ngram_n, "threshold": ngram_threshold, "min_tokens_for_near": min_tokens_for_near},
        "recommendation": recommendation,
    }
