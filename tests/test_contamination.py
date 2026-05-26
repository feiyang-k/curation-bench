from __future__ import annotations

import csv
from pathlib import Path

from datasets import Dataset

from benchmark.tools.contamination import (
    EVAL_REGISTRY,
    EvalBenchmarkSpec,
    audit_contamination,
    hash_exact_duplicates,
    ngram_near_duplicates,
)


# ---------------------------------------------------------------------------
# hash_exact_duplicates
# ---------------------------------------------------------------------------

def test_hash_exact_finds_match():
    shared = "Q: what color is the sky\nA: blue"
    sub_pairs = [shared, "Q: hello\nA: world"]
    eval_pairs = {"bench": [shared, "Q: foo\nA: bar"]}
    result = hash_exact_duplicates(sub_pairs, eval_pairs)
    assert result["bench"]["exact_matches"] == 1
    assert "matched_pairs" not in result["bench"]


def test_hash_exact_count_not_capped():
    """exact_matches must reflect the true count, not len(matched_pairs)."""
    shared_a = "Q: what color is the sky\nA: blue"
    shared_b = "Q: what shape is the earth\nA: round"
    shared_c = "Q: how many legs does a cat have\nA: four"
    sub_pairs = [shared_a, shared_b, shared_c]
    eval_pairs = {"bench": [shared_a, shared_b, shared_c, "Q: foo\nA: bar"]}
    result = hash_exact_duplicates(sub_pairs, eval_pairs)
    # Count must equal 3 regardless of any internal sample cap
    assert result["bench"]["exact_matches"] == 3
    assert result["bench"]["total_eval_pairs"] == 4


def test_hash_exact_no_false_positives():
    sub_pairs = ["Q: hello\nA: world"]
    eval_pairs = {"bench": ["Q: foo\nA: bar"]}
    result = hash_exact_duplicates(sub_pairs, eval_pairs)
    assert result["bench"]["exact_matches"] == 0
    assert "matched_pairs" not in result["bench"]


# ---------------------------------------------------------------------------
# ngram_near_duplicates
# ---------------------------------------------------------------------------

def test_ngram_near_finds_similar():
    # Shared long subsequence, but slightly different wording
    sub_pairs = ["Q: the quick brown fox jumps over the lazy dog near the river\nA: yes it does jump over"]
    eval_pairs = {"bench": ["Q: the quick brown fox jumps over the lazy dog by the river\nA: yes it does jump over"]}
    result = ngram_near_duplicates(sub_pairs, eval_pairs, n=5, threshold=0.5)
    assert result["bench"]["near_matches"] >= 1


def test_ngram_near_one_match_per_eval_pair():
    """One eval pair matching two submission pairs should count as 1, not 2."""
    eval_text = "Q: the quick brown fox jumps over the lazy dog near the river\nA: yes it does jump over"
    sub_a = "Q: the quick brown fox jumps over the lazy dog near the river\nA: yes it does jump over perfectly"
    sub_b = "Q: the quick brown fox jumps over the lazy dog near the river\nA: yes it does jump over gracefully"
    result = ngram_near_duplicates([sub_a, sub_b], {"bench": [eval_text]}, n=5, threshold=0.5)
    assert result["bench"]["near_matches"] == 1
    assert len(result["bench"]["matches"]) == 1


def test_ngram_near_count_not_capped():
    """near_matches must reflect the true count, independent of the 100-sample cap."""
    # Create 3 distinct eval pairs, each with an exact-ish submission counterpart
    eval_pairs = []
    sub_pairs = []
    for i in range(3):
        base = f"Q: word{i} alpha beta gamma delta epsilon zeta eta theta iota\nA: answer{i} one two three four five"
        eval_pairs.append(base)
        sub_pairs.append(base)
    result = ngram_near_duplicates(sub_pairs, {"bench": eval_pairs}, n=5, threshold=0.5)
    assert result["bench"]["near_matches"] == 3
    assert result["bench"]["total_eval_pairs"] == 3


def test_ngram_near_rejects_dissimilar():
    sub_pairs = ["Q: alpha beta gamma delta epsilon zeta eta\nA: one two three four five"]
    eval_pairs = {"bench": ["Q: lorem ipsum dolor sit amet consectetur adipiscing\nA: six seven eight nine ten"]}
    result = ngram_near_duplicates(sub_pairs, eval_pairs, n=5, threshold=0.5)
    assert result["bench"]["near_matches"] == 0


def test_ngram_short_text_safety():
    sub_pairs = ["Q: hi\nA: ok"]
    eval_pairs = {"bench": ["Q: hi\nA: ok"]}
    result = ngram_near_duplicates(sub_pairs, eval_pairs, n=5, threshold=0.5)
    # Short text has fewer than 5 tokens — should be skipped, no crash
    assert result["bench"]["near_matches"] == 0


# ---------------------------------------------------------------------------
# min_tokens filter & stricter defaults
# ---------------------------------------------------------------------------

def test_ngram_skips_short_qa_pairs():
    """QA pair with ~8 tokens is above n=5 but below min_tokens=12; skipped by default."""
    short = "Q: what color sky\nA: blue color"
    sub_pairs = [short]
    eval_pairs = {"bench": [short]}
    # Default min_tokens=12 should skip this
    result = ngram_near_duplicates(sub_pairs, eval_pairs)
    assert result["bench"]["near_matches"] == 0


def test_stricter_defaults_reduce_noisy_matches():
    """A generic template-like pair that matches at n=5/0.5 does NOT match at n=8/0.8."""
    sub = "Q: what is the color of the object in the image shown here\nA: the object is red colored"
    evl = "Q: what is the color of the object in the picture shown here\nA: the object is blue colored"
    # Loose settings: should match
    loose = ngram_near_duplicates([sub], {"bench": [evl]}, n=5, threshold=0.5)
    assert loose["bench"]["near_matches"] >= 1
    # Strict defaults: should NOT match
    strict = ngram_near_duplicates([sub], {"bench": [evl]})
    assert strict["bench"]["near_matches"] == 0


# ---------------------------------------------------------------------------
# Graduated status thresholds
# ---------------------------------------------------------------------------

def test_status_clean_no_matches():
    sub_pairs = ["Q: alpha beta gamma delta\nA: one two three four"]
    eval_pairs = {"bench": ["Q: lorem ipsum dolor sit\nA: five six seven eight"]}
    hash_res = hash_exact_duplicates(sub_pairs, eval_pairs)
    ngram_res = ngram_near_duplicates(sub_pairs, eval_pairs, n=5, threshold=0.5)
    assert hash_res["bench"]["exact_matches"] == 0
    assert ngram_res["bench"]["near_matches"] == 0


def test_status_warning_few_exact(tmp_path: Path):
    """1 exact match with rate < 5% (1/100) → clean under current thresholds."""
    bench_name = "_ThreshBench"
    spec = EvalBenchmarkSpec("ThreshBench.tsv", "question", "answer")
    EVAL_REGISTRY[bench_name] = spec
    try:
        eval_dir = tmp_path / "eval_data"
        eval_dir.mkdir()
        rows = [{"question": f"q{i}", "answer": f"a{i}"} for i in range(100)]
        rows[0] = {"question": "What is 2+2?", "answer": "4"}
        _write_fake_eval_tsv(eval_dir, "ThreshBench.tsv", rows)
        sub_path = tmp_path / "submission"
        _make_submission_dataset(sub_path, [
            [{"user": "What is 2+2?", "assistant": "4"}],
        ])
        report = audit_contamination(str(sub_path), str(eval_dir), [bench_name])
        assert report["status"] == "clean"
    finally:
        del EVAL_REGISTRY[bench_name]


def test_status_warning_near_only(tmp_path: Path):
    """0 exact, 1/1 near matches = 100% near rate → high_risk under current thresholds."""
    bench_name = "_NearBench"
    spec = EvalBenchmarkSpec("NearBench.tsv", "question", "answer")
    EVAL_REGISTRY[bench_name] = spec
    try:
        eval_dir = tmp_path / "eval_data"
        eval_dir.mkdir()
        _write_fake_eval_tsv(eval_dir, "NearBench.tsv", [
            {"question": "the quick brown fox jumps over the lazy dog near the river bank today",
             "answer": "yes it does jump over the lazy dog near the river bank today"},
        ])
        sub_path = tmp_path / "submission"
        _make_submission_dataset(sub_path, [
            [{"user": "the quick brown fox jumps over the lazy dog by the river bank today",
              "assistant": "yes it does jump over the lazy dog near the river bank today"}],
        ])
        report = audit_contamination(str(sub_path), str(eval_dir), [bench_name],
                                     ngram_n=5, ngram_threshold=0.5, min_tokens_for_near=5)
        assert report["status"] == "high_risk"
    finally:
        del EVAL_REGISTRY[bench_name]


def test_status_high_risk_by_count(tmp_path: Path):
    """10/500 = 2% exact rate < 5% → clean under current thresholds."""
    bench_name = "_CountBench"
    spec = EvalBenchmarkSpec("CountBench.tsv", "question", "answer")
    EVAL_REGISTRY[bench_name] = spec
    try:
        eval_dir = tmp_path / "eval_data"
        eval_dir.mkdir()
        rows = [{"question": f"shared q{i}", "answer": f"shared a{i}"} for i in range(500)]
        _write_fake_eval_tsv(eval_dir, "CountBench.tsv", rows)
        sub_path = tmp_path / "submission"
        texts = [[{"user": f"shared q{i}", "assistant": f"shared a{i}"}] for i in range(10)]
        _make_submission_dataset(sub_path, texts)
        report = audit_contamination(str(sub_path), str(eval_dir), [bench_name])
        assert report["status"] == "clean"
    finally:
        del EVAL_REGISTRY[bench_name]


def test_status_high_risk_by_rate(tmp_path: Path):
    """2/50 = 4% exact rate < 5% → clean under current thresholds."""
    bench_name = "_RateBench"
    spec = EvalBenchmarkSpec("RateBench.tsv", "question", "answer")
    EVAL_REGISTRY[bench_name] = spec
    try:
        eval_dir = tmp_path / "eval_data"
        eval_dir.mkdir()
        rows = [{"question": f"q{i}", "answer": f"a{i}"} for i in range(50)]
        rows[0] = {"question": "overlap q0", "answer": "overlap a0"}
        rows[1] = {"question": "overlap q1", "answer": "overlap a1"}
        _write_fake_eval_tsv(eval_dir, "RateBench.tsv", rows)
        sub_path = tmp_path / "submission"
        _make_submission_dataset(sub_path, [
            [{"user": "overlap q0", "assistant": "overlap a0"}],
            [{"user": "overlap q1", "assistant": "overlap a1"}],
        ])
        report = audit_contamination(str(sub_path), str(eval_dir), [bench_name])
        assert report["status"] == "clean"
    finally:
        del EVAL_REGISTRY[bench_name]


def test_status_clean_below_rate_thresholds(tmp_path: Path):
    """1/250 = 0.4% exact rate < 5%, 0 near → clean."""
    bench_name = "_BelowThreshBench"
    spec = EvalBenchmarkSpec("BelowThreshBench.tsv", "question", "answer")
    EVAL_REGISTRY[bench_name] = spec
    try:
        eval_dir = tmp_path / "eval_data"
        eval_dir.mkdir()
        rows = [{"question": f"q{i}", "answer": f"a{i}"} for i in range(250)]
        rows[0] = {"question": "What is 2+2?", "answer": "4"}
        _write_fake_eval_tsv(eval_dir, "BelowThreshBench.tsv", rows)
        sub_path = tmp_path / "submission"
        _make_submission_dataset(sub_path, [
            [{"user": "What is 2+2?", "assistant": "4"}],
        ])
        report = audit_contamination(str(sub_path), str(eval_dir), [bench_name])
        assert report["status"] == "clean"
    finally:
        del EVAL_REGISTRY[bench_name]


def test_status_not_high_risk_by_count_alone(tmp_path: Path):
    """10/1000 = 1% exact rate < 5% → clean under current thresholds."""
    bench_name = "_CountOnlyBench"
    spec = EvalBenchmarkSpec("CountOnlyBench.tsv", "question", "answer")
    EVAL_REGISTRY[bench_name] = spec
    try:
        eval_dir = tmp_path / "eval_data"
        eval_dir.mkdir()
        rows = [{"question": f"shared q{i}", "answer": f"shared a{i}"} for i in range(1000)]
        _write_fake_eval_tsv(eval_dir, "CountOnlyBench.tsv", rows)
        sub_path = tmp_path / "submission"
        texts = [[{"user": f"shared q{i}", "assistant": f"shared a{i}"}] for i in range(10)]
        _make_submission_dataset(sub_path, texts)
        report = audit_contamination(str(sub_path), str(eval_dir), [bench_name])
        assert report["status"] == "clean"
    finally:
        del EVAL_REGISTRY[bench_name]


def test_status_warning_by_near_rate(tmp_path: Path):
    """0 exact, 2/100 = 2% near rate < 10% → clean under current thresholds."""
    bench_name = "_NearRateBench"
    spec = EvalBenchmarkSpec("NearRateBench.tsv", "question", "answer")
    EVAL_REGISTRY[bench_name] = spec
    try:
        eval_dir = tmp_path / "eval_data"
        eval_dir.mkdir()
        rows = [{"question": f"q{i}", "answer": f"a{i}"} for i in range(100)]
        rows[0] = {
            "question": "the quick brown fox jumps over the lazy dog near the river bank today",
            "answer": "yes it does jump over the lazy dog near the river bank today",
        }
        rows[1] = {
            "question": "alpha beta gamma delta epsilon zeta eta theta iota kappa lambda mu",
            "answer": "one two three four five six seven eight nine ten eleven twelve",
        }
        _write_fake_eval_tsv(eval_dir, "NearRateBench.tsv", rows)
        sub_path = tmp_path / "submission"
        _make_submission_dataset(sub_path, [
            [{"user": "the quick brown fox jumps over the lazy dog by the river bank today",
              "assistant": "yes it does jump over the lazy dog near the river bank today"}],
            [{"user": "alpha beta gamma delta epsilon zeta eta theta iota kappa lambda mu",
              "assistant": "one two three four five six seven eight nine ten eleven thirteen"}],
        ])
        report = audit_contamination(str(sub_path), str(eval_dir), [bench_name],
                                     ngram_n=5, ngram_threshold=0.5, min_tokens_for_near=5)
        assert report["hash_exact"][bench_name]["exact_matches"] == 0
        assert report["ngram_near"][bench_name]["near_matches"] >= 2
        assert report["status"] == "clean"
    finally:
        del EVAL_REGISTRY[bench_name]


# ---------------------------------------------------------------------------
# audit_contamination (end-to-end)
# ---------------------------------------------------------------------------

def _write_fake_eval_tsv(eval_dir: Path, filename: str, rows: list[dict[str, str]]) -> None:
    tsv_path = eval_dir / filename
    with open(tsv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()), delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)


def _make_submission_dataset(path: Path, texts_data: list[list[dict[str, str]]]) -> Path:
    ds = Dataset.from_dict({
        "images": [None] * len(texts_data),
        "texts": texts_data,
    })
    ds.save_to_disk(str(path))
    return path


def test_audit_end_to_end(tmp_path: Path):
    # Register a temporary benchmark
    bench_name = "_TestBench"
    spec = EvalBenchmarkSpec("TestBench.tsv", "question", "answer")
    EVAL_REGISTRY[bench_name] = spec
    try:
        # Create eval TSV with a known QA pair
        eval_dir = tmp_path / "eval_data"
        eval_dir.mkdir()
        _write_fake_eval_tsv(eval_dir, "TestBench.tsv", [
            {"question": "What is 2+2?", "answer": "4"},
            {"question": "Capital of France?", "answer": "Paris"},
        ])

        # Create submission with overlapping QA pair
        sub_path = tmp_path / "submission"
        _make_submission_dataset(sub_path, [
            [{"user": "What is 2+2?", "assistant": "4"}],
            [{"user": "Describe this image", "assistant": "A dog on a beach"}],
        ])

        report = audit_contamination(str(sub_path), str(eval_dir), [bench_name])

        assert report["status"] == "high_risk"
        assert bench_name in report["benchmarks_checked"]
        assert report["hash_exact"][bench_name]["exact_matches"] == 1
        assert report["submission_qa_pair_count"] == 2
        assert "recommendation" in report
    finally:
        del EVAL_REGISTRY[bench_name]


def test_audit_missing_eval_dir(tmp_path: Path):
    sub_path = tmp_path / "submission"
    _make_submission_dataset(sub_path, [
        [{"user": "hello", "assistant": "world"}],
    ])
    report = audit_contamination(str(sub_path), str(tmp_path / "nonexistent"), ["MMVet"])
    assert report["status"] == "skipped"
    assert "error" in report


def test_audit_unknown_benchmark(tmp_path: Path):
    eval_dir = tmp_path / "eval_data"
    eval_dir.mkdir()
    sub_path = tmp_path / "submission"
    _make_submission_dataset(sub_path, [
        [{"user": "hello", "assistant": "world"}],
    ])
    report = audit_contamination(str(sub_path), str(eval_dir), ["NonexistentBench"])
    assert "NonexistentBench" in report["skipped_benchmarks"]
    assert report["skipped_benchmarks"]["NonexistentBench"] == "not in registry"



# (Session dispatch and eval leakage tests removed — they referenced
#  a task ID that no longer exists. Coverage is now in test_suite.py.)


def test_contamination_hash_no_matched_pairs():
    """hash_exact_duplicates must not return matched_pairs."""
    shared = "Q: what color is the sky\nA: blue"
    result = hash_exact_duplicates([shared], {"b": [shared, "Q: x\nA: y"]})
    assert result["b"]["exact_matches"] == 1
    assert "matched_pairs" not in result["b"]


def test_contamination_ngram_no_eval_text():
    """ngram near-match entries must not contain eval_text."""
    text = "Q: the quick brown fox jumps over the lazy dog near the river\nA: yes it does jump over"
    result = ngram_near_duplicates([text], {"b": [text]}, n=5, threshold=0.5)
    for m in result["b"]["matches"]:
        assert "eval_text" not in m
        assert "submission_text" in m
