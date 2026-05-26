# Curation-Bench Protocol

> Variant of `BENCHMARK.md`. The agent is given exactly one of `protocols/plain.md`, `protocols/instruction.md`, or `protocols/skill.md` at launch, depending on the chosen launch profile. The instruction variant adds prescriptive step-by-step guidance on top of the canonical protocol.

You are an AI agent working inside a dataset-curation benchmark. Your goal is to curate training data based on the task to maximize downstream evaluation performance after fine-tuning.

The benchmark manages the suite lifecycle, training, and evaluation. You manage the data curation strategy.

**Read only this file as protocol.** No other protocol files are available to you.

## Session initialization

`BENCHMARK_CURRENT_TASK` tells you which task you own — only that task, not any other task in the suite.

```bash
echo "My assigned task: $BENCHMARK_CURRENT_TASK"
```

If `datacuration-bench next` ever returns a `task_id` different from `$BENCHMARK_CURRENT_TASK`, exit immediately — that's another agent session's responsibility.

**At the start of every session**, clear all previous git history and start fresh:

```bash
PROJECT_ROOT=$(pwd)
cd $PROJECT_ROOT
rm -rf .git
git init
git add -A
git commit -m "fresh start: $BENCHMARK_CURRENT_TASK"
```

This ensures each session starts with a clean single-commit history. `runs/`, `.venv/`, and `*.log` are in `.gitignore` and must NEVER be committed to git (they contain run artifacts, model checkpoints, and venvs).

## Setup

To set up a new experiment:

1. **Run tag**: use `$BENCHMARK_CURRENT_TASK` (or a date-based tag like `apr21`). The branch `autoresearch/<tag>` must not already exist.
2. **Create the branch**: `git checkout -b autoresearch/<tag>`
3. **Read the in-scope files**:
   - `run_prompt.md` — current run's tasks and strategy
   - `datacuration-bench task` — task definition: `task_id`, `goal`, `target_rows`, `model_key`, `target_evals`, `strategy_timeout_seconds`, `dataset_path`, `default_submission_path`
4. **Verify vendor venvs** (see "Venv setup" below).
5. **Initialize results.tsv**: create `<suite_dir>/results.tsv` with the header row (see **Logging results**).
6. **Confirm and go**.

Once you get confirmation **yourself**, kick off the experimentation. **Do not stop waiting for the user's input.**

## The Dataset

The LLaVA-665K dataset is a multimodal instruction-following dataset with ~665K samples. Each sample has:
- `images`: list of PIL images
- `texts`: list of conversation turns (user/assistant pairs)
- `source_subset`: which subset the sample came from

You are selecting a subset (of size `target_rows`) that maximizes downstream VLM benchmark performance after fine-tuning on the selected data.

**IMPORTANT**: The dataset is on a read-only mount. Do NOT use `ds.filter()` — it tries to write temp/cache files to the dataset directory and will fail. Instead, use fast column-level access like `ds["source_subset"]` to get indices, then `ds.select(indices)`. This is also much faster (~seconds vs ~40 minutes).

## Venv setup (one-time)

There are three separate Python venvs. Each persists across runs — you only set them up once. First-time setup is slow (compiling flash-attn, downloading torch, etc.) but subsequent runs skip it.

**CRITICAL**: You MUST set `UV_PROJECT_ENVIRONMENT` to the correct venv path when running any `uv sync` or `uv pip install`. If you forget, uv will modify the wrong venv and break it. This is the #1 cause of environment breakage.

### Benchmark CLI

```bash
PROJECT_ROOT=$(pwd)
if ! uv run datacuration-bench --help > /dev/null 2>&1; then
    uv sync --project $PROJECT_ROOT
fi
```

### curation-train

```bash
TRAIN_VENV=$PROJECT_ROOT/vendor/curation-train/.venv
if ! $TRAIN_VENV/bin/python -c "print('ok')" 2>/dev/null; then
    rm -rf $TRAIN_VENV
    UV_PROJECT_ENVIRONMENT=$TRAIN_VENV \
      uv sync --project $PROJECT_ROOT/vendor/curation-train
fi
```

### VLMEvalKit

```bash
EVAL_VENV=$PROJECT_ROOT/vendor/VLMEvalKit/.venv
if ! $EVAL_VENV/bin/python -c "import vlmeval; print('ok')" 2>/dev/null; then
    rm -rf $EVAL_VENV
    UV_PROJECT_ENVIRONMENT=$EVAL_VENV \
      uv sync --project $PROJECT_ROOT/vendor/VLMEvalKit
fi
```

## Pre-init baseline

Before the iter loop, evaluate the **base model** (no training) once. These scores are the pre-init reference row — the "what happens if you do nothing" baseline. The harness's `datacuration-bench eval` subcommand requires a fine-tuned checkpoint, so this one step calls the vendored VLMEvalKit directly.

Pull the base-model path from `profiles/example.yaml` → `model_path_map[<model_key>]`, the benchmark list from `datacuration-bench task` → `target_evals`, and pick a suite-level work dir (e.g. `<suite_dir>/preinit_eval`). Then:

This is a blocking call — see the **Monitoring** section for what's allowed during the wait.

```bash
PROJECT_ROOT=$(pwd)
SUITE_DIR=$(cat .bench_active_suite)
BASE_MODEL=/path/to/data-curation/models/llava15-7b-hf-init  # from profile
PREINIT_DIR=$SUITE_DIR/preinit_eval
mkdir -p $PREINIT_DIR

LMUData=/path/to/LMUData \
BENCHMARK_VLMEVAL_TRUST_LOCAL_TSV=1 \
CUDA_VISIBLE_DEVICES=0 \  # literal 0 (container GPUs are always 0-indexed); do NOT substitute profile value
VLLM_WORKER_MULTIPROC_METHOD=spawn \
OPENAI_API_BASE=http://localhost:8001/v1/chat/completions \
OPENAI_API_KEY=dummy \
UV_PROJECT_ENVIRONMENT=$PROJECT_ROOT/vendor/VLMEvalKit/.venv \
uv run --no-sync --project $PROJECT_ROOT/vendor/VLMEvalKit \
  python $PROJECT_ROOT/vendor/VLMEvalKit/run.py \
  --model llava-1.5-7b-hf \
  --model-path $BASE_MODEL \
  --data HallusionBench LLaVABench MMBench MMMU_DEV_VAL MMStar MMVet MathVista_MINI OCRBench \
  --work-dir $PREINIT_DIR \
  --mode all \
  --use-vllm \                    # REQUIRED — 10× faster; without it eval falls back to per-sample transformers
  --judge Qwen3.5-27B \
  --api-nproc 4 \
  2>&1 | tee $PREINIT_DIR/eval.log
```

Parse `$PREINIT_DIR/results.json` (keyed by model name) the same way as an iter eval. Record the result as the first row of the suite TSV with `commit=0000000` and description `pre-init baseline (no finetune)` (see **Logging results**). If `results.tsv` already contains a pre-init row, skip this step. Only after pre-init finishes do you enter the iter loop.

## Running an experiment

Each iteration has three stages: curate, train, evaluate. You run each stage via the `datacuration-bench` CLI — **one stage and one iter at a time; no overlapping stages within or across iters**. The harness owns the run directory and all paths.

### Activate the next iteration

```bash
datacuration-bench next
```

Returns JSON with `status`, `target_key`, `task_id`, `iteration`, `run_dir`, `task_goal`, `default_submission_path`, `dataset_path`.

- `status == "target_activated"` and `task_id == $BENCHMARK_CURRENT_TASK`: proceed.
- `status == "task_done"`: exit.
- Anything else: exit immediately.

### Stage 1: Curate

Your working directory is `curation/`. Use the `dataset_path` from the JSON as input, write the curated HuggingFace dataset (`save_to_disk`, with `images` and `texts` columns, row count == `target_rows`) to `default_submission_path`. The reference script takes three positional args:

```bash
uv run python curation/curate.py <dataset_path> <default_submission_path> <target_rows>
```

**Avoid row-by-row Python iteration on the dataset** — e.g. `for i in range(len(ds))`, `for row in ds:`, etc.

For iter2+ (before editing `curation/curate.py`), you **MUST** read in full:
- The full `<suite_dir>/results.tsv` (every row, not just the tail).
- **EVERY** `<suite_dir>/<commit>-curate.py` snapshot — one per prior iter (`keep` AND `discard` alike). Glob: `<suite_dir>/*-curate.py`.
- **EVERY** `<suite_dir>/<commit>-research.md` snapshot — one per prior iter from iter2+ (iter1 baseline has none). Glob: `<suite_dir>/*-research.md`.
- **EVERY** prior aggregate score: `<run_dir>/../<task_id>_iter<i>/eval/results/results.json` for `i` in `1..N-1`.
- (Optional, recommended) Per-question predictions: `<run_dir>/../<task_id>_iter<N-1>/eval/results/<model_name>/*.xlsx`.

Skipping any of the four required reads above is a protocol violation.

If the task has `strategy_timeout_seconds`, check `datacuration-bench time-budget` frequently — before any long op, after each major step, before submitting. If low, simplify. If `strategy_timeout_seconds: null`, ignore the timer.

Then audit and submit:
```bash
datacuration-bench audit --path <default_submission_path>
datacuration-bench submit --path <default_submission_path>
```

### Stage 2: Train

Run as a **blocking foreground** Bash call. Do NOT use `run_in_background`, `&`, or `nohup`. See the **Monitoring** section.

```bash
uv run datacuration-bench finetune 2>&1
```

Success signal: `"status": "completed"` with `model_path` printed after training ends. Model files land under `<run_dir>/finetune/`.

### Stage 3: Evaluate

Run as a **blocking foreground** Bash call. Do NOT use `run_in_background`, `&`, or `nohup`. See the **Monitoring** section.

```bash
uv run datacuration-bench eval 2>&1
```

VLMEvalKit writes per-benchmark scores to `<run_dir>/eval/results/`. On success, the target is automatically marked COMPLETED by the harness.

## Scoring

After evaluation, extract raw scores from `<run_dir>/eval/results/`. VLMEvalKit writes per-benchmark result files under `<run_dir>/eval/results/<model_name>/` (JSON, xlsx, or CSV). Look for keys like `overall`, `score`, `accuracy`, or `avg`. The aggregate `<run_dir>/eval/results/results.json` (keyed by model name) is also available.

For HallusionBench, the score is the average of aAcc, fAcc, and qAcc.

For MMMU_DEV_VAL, use the **validation** split score (not the dev split score). The eval outputs both; report the val score.

Normalization:

| Benchmark      | Max score |
|----------------|-----------|
| MMVet          | 100       |
| LLaVABench     | 100       |
| OCRBench       | 1000      |
| HallusionBench | 100       |
| MMMU_DEV_VAL   | 100       |
| MathVista_MINI | 100       |
| MMStar         | 100       |
| MMBench        | 100       |

**accuracy** = mean of (MMVet/100, LLaVABench/100, OCRBench/1000, HallusionBench/100, MMMU_DEV_VAL/100, MathVista_MINI/100, MMStar/100, MMBench/100) across the task's `target_evals`.

## Experimentation rules

**Research-first mandate**: Every iteration starts with *data research*, not a code change. The goal is a specific, testable hypothesis about why a benchmark behaves the way it does, grounded in the actual contents of the dataset or in the eval outputs — not in generic intuition.

The following patterns are out. They have all been tried, they don't generalize, and they don't teach us anything about the data:

- Turn-count bonuses / penalties.
- Response-length or user-length scoring.
- Keyword-regex "reasoning" or "complexity" detection.
- Hand-tuned per-subset quotas (hard-coded `ALLOCATIONS` dicts, pool-multiplier knobs).
- Round-number thresholds (`MIN_RESP_LEN = 50`, `SHORT_ANSWER_THRESHOLD = 50`, etc.) picked by feel.
- Superficial reasoning from subset names alone ("the OCR subset must help OCRBench").
- Plain deduplication as a strategy in itself.
- Empirical mixing / ratio tweaking without a data-grounded reason.

A strategy is research-grounded only if you can point to an observation in `<run_dir>/research.md` that directly motivates it. "Reasoning-heavy samples are probably better" does not qualify. "62% of MathVista errors involve multi-step counting; training set contains 0.3% of counting samples with >2 steps" does.

**What you CAN do:**
- Modify any `.py` files under `curation/` — this is the only directory you edit. Everything is fair game: selection criteria, filtering, subset balancing, deduplication, quality scoring, diversity sampling, metadata-based selection, etc.

**What you CANNOT do:**
- Modify the vendor projects (`vendor/curation-train/`, `vendor/VLMEvalKit/`).
- Modify anything under `.venv/`, `src/`, `configs/`, `docker/`, `profiles/`, or task YAMLs (`src/benchmark/tasks/`).
- Create new files under `vendor/`, `src/`, `.venv/`, `configs/`, `docker/`, or `profiles/` — creating a file there counts as modification.
- Change training hyperparameters or evaluation benchmarks.
- Run `uv sync`, `uv pip install`, or `uv add` without explicitly setting `UV_PROJECT_ENVIRONMENT` to the correct vendor venv path.

**Use discretion for new packages**: try what's already in `pyproject.toml` first.

**The goal**: highest accuracy (average normalized score across MMVet, LLaVABench, OCRBench, HallusionBench, MMMU_DEV_VAL, MathVista_MINI, MMStar, MMBench).

**Data fraction**: at most `target_rows` samples. Fewer is fine if your strategy benefits.

**Simplicity criterion**: all else being equal, simpler is better. A small improvement that adds ugly complexity is not worth it. Removing something and getting equal or better results is a great outcome.

**Pre-init baseline**: Before training anything, first run evaluation on the base model (without any fine-tuning) to establish the pre-init baseline — see the **Pre-init baseline** section. Log this in results.tsv with commit `0000000` and description `pre-init baseline (no finetune)`. **If results.tsv already contains a pre-init baseline row, skip it and move on — do not re-run it.**

**First run (iter1)**: Always establish the baseline first — run with the default random selection. The baseline is randomly selecting `target_rows` examples from the original dataset by running `curation/curate.py` unchanged — note that `curate.py` may not have been updated at initialization (i.e., it may already contain a non-baseline strategy from a previous session). **You MUST NOT modify `curation/curate.py` for iter1 — run it exactly as-is, even if it looks non-baseline.** **If results.tsv already contains a baseline row, skip it and move on — do not re-run it.**

**Research artifact**: Before modifying `curation/curate.py` on any iteration (other than the baselines above), write `<run_dir>/research.md` containing:

1. **Observation** — a concrete finding from the dataset or from eval outputs. Tie it to a specific benchmark behavior, not generic descriptive stats. Examples: distribution of question types in a subset, breakdown of failure modes on a specific benchmark, a clustering result, retrieval of training samples similar to hard benchmark items.
2. **Hypothesis** — a testable claim that follows from the observation, naming which benchmark(s) it is expected to move and roughly by how much.
3. **Minimal change** — the smallest `curation/curate.py` modification that tests the hypothesis.

After committing the change, save a copy of `research.md` alongside the `curation/curate.py` snapshot (see "Logging results" below) — do this for **every** iteration so the research trail is preserved even when a commit is later reset.

## Logging results

When an iter is done, append a row to `<suite_dir>/results.tsv` (tab-separated, NOT comma-separated). The header row is created in Setup; each iter (including the pre-init baseline) adds one data row.

Header and columns:

```
commit	accuracy	MMVet	LLaVABench	OCRBench	HallusionBench	MMMU_DEV_VAL	MathVista_MINI	MMStar	MMBench	status	description	skill_ref	failure_mode	next_skill_candidate
```

1. git commit hash (short, 7 chars) — use `0000000` for the pre-init row
2. accuracy (normalized average, e.g. 0.456700) — 0.000000 for crashes
3. MMVet raw score (e.g. 35.2) — 0.0 for crashes
4. LLaVABench raw score (e.g. 62.1) — 0.0 for crashes
5. OCRBench raw score (e.g. 310.0) — 0.0 for crashes
6. HallusionBench raw score (avg of aAcc, fAcc, qAcc; e.g. 42.5) — 0.0 for crashes
7. MMMU_DEV_VAL raw score (validation split; e.g. 34.0) — 0.0 for crashes
8. MathVista_MINI raw score (e.g. 28.5) — 0.0 for crashes
9. MMStar raw score (e.g. 35.0) — 0.0 for crashes
10. MMBench raw score (dev split Overall; e.g. 65.0) — 0.0 for crashes
11. status: `keep` (new best accuracy so far), `discard` (worse), or `crash` (run failed)
12. short text description
13. `skill_ref`: the commit hash of the prior `research.md` this iteration built on, or `none` for the baselines / an independent start. This is a citation, not a summary.
14. `failure_mode`: what **this run** revealed about the data or model — a *new* finding, tied to specific benchmarks. Not a restatement of the description or of prior failure modes. Example: "upsampled counting-chain samples but MathVista counting still fails — suggests the chains lack grounding to image regions".
15. `next_skill_candidate`: the next research question to investigate, phrased as something `research.md` could answer.

Example:

```
commit	accuracy	MMVet	LLaVABench	OCRBench	HallusionBench	MMMU_DEV_VAL	MathVista_MINI	MMStar	MMBench	status	description	skill_ref	failure_mode	next_skill_candidate
0000000	0.420000	32.0	58.0	295.0	40.0	32.5	27.0	33.0	62.0	keep	pre-init baseline (no finetune)	none	weak on multi-step math and OCR-heavy questions	what distinguishes MathVista-like samples in the training set?
a1b2c3d	0.456700	35.2	62.1	310.0	42.5	34.0	28.5	35.0	65.0	keep	baseline random 10k	none	HallusionBench gains came from VD-illusion items; MMBench instance-reasoning unmoved	which subsets contribute samples similar to MMBench instance-reasoning?
b2c3d4e	0.478200	37.1	64.3	320.0	44.0	35.5	30.0	36.5	67.0	keep	upsample samples with chart-like images (from research on MathVista failure clusters)	a1b2c3d	MMBench unmoved despite chart gains; visual-reasoning transfer is narrower than expected	do chart gains come from image content or answer format?
c3d4e5f	0.412000	30.5	58.2	290.0	38.0	32.0	26.0	33.0	60.0	discard	drop text_only after clustering showed it as a distinct failure mode	b2c3d4e	removing text_only also drops general-instruction coverage; LLaVABench regresses	which text_only clusters actually hurt vs. help?
d4e5f6g	0.000000	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	crash	dedup bug caused empty dataset	c3d4e5f	n/a (crash)	fix dedup then retry
```

Then, also save copies of `curation/curate.py` and `<run_dir>/research.md` to `<suite_dir>/[commit]-*` — do this for **every** iteration so the research trail is preserved.
Example: for commit `a1b2c3d`,
```bash
cp curation/curate.py <suite_dir>/a1b2c3d-curate.py
cp <run_dir>/research.md <suite_dir>/a1b2c3d-research.md
```

## The experiment loop

The experiment runs on a dedicated branch (e.g. `autoresearch/apr21`).

LOOP UNTIL `datacuration-bench next` RETURNS `task_done`:

1. Check git state: current branch/commit.
2. `datacuration-bench next`, check `status` and `task_id`.
3. **Research** — write `<run_dir>/research.md` (observation → hypothesis → minimal change). See **Research artifact** above. Skip for the pre-init baseline and iter1.
4. Modify `curation/curate.py` to implement the minimal change from step 3 (iter1: run unchanged — see **First run**; iter2+ ground each change in research.md).
5. `git add -A && git commit -m "<short strategy description>"`. Then copy `curation/curate.py` and `<run_dir>/research.md` to `<suite_dir>/[commit]-curate.py` and `<suite_dir>/[commit]-research.md`.
6. Run the three stages in sequence (curate → train → evaluate), redirecting all output to log files in the `run_dir`. **Do NOT let output flood your context.**
7. Extract results from eval output files.
8. If any stage failed or results are missing: tail the matching stderr to diagnose — finetune failure: `tail -n 50 <run_dir>/finetune/train_stderr.txt`; eval failure: `tail -n 50 <run_dir>/eval/eval_stderr.txt`.
9. Record results in TSV. `failure_mode` must be a *new* finding from this run (not a restatement of description or prior failure modes); `next_skill_candidate` is the next research question.
10. If accuracy improved (higher): keep the commit ("advance").
11. If accuracy equal or worse: `git reset --hard HEAD~1` back to where you started. (The iter's official eval score is already recorded by the harness and cannot be undone; resetting git only affects the `curation/` starting point for the next iter. The `<suite_dir>/[commit]-*` snapshots and TSV row persist — a negative result is still data and feeds the next iteration's research.)

## Monitoring

**Don't check anything excessively — every tool call re-reads your full context. Keep checks sparse and reasonable regardless of what file or mechanism you're using: tailing logs, listing directories (ls), grepping output files, watching step counts, counting benchmark completions, reading intermediate state, probing background task progress, etc., all count. Don't spawn Monitor watchers to poll progress.**

**ETA for curation**: for data curation operations, always compute and print an ETA, and check proactively while it is running — do not wait on scripts that do not finish quickly without an ETA. If a curation script is running without producing progress/ETA output, kill it, add ETA logging, and re-run. Harness commands (`finetune` / `eval` / pre-init baseline) don't need progress monitoring — the harness owns the wall-clock.

**Crashes**: if it's something dumb and easy to fix, fix and re-run. If fundamentally broken, log `"crash"` and move on.

**NEVER STOP**: once the experiment loop begins, do NOT pause to ask the human if you should continue. Do NOT ask "should I keep going?" or "is this a good stopping point?". The human might be asleep and expects you to continue working *indefinitely* until `datacuration-bench next` returns `task_done`. You are autonomous. If you run out of ideas, think harder — analyze the dataset distribution, study which samples help which benchmarks, try combining previous near-misses, try more radical strategies. The loop runs until `task_done`, period.

**NO ITERATION-END SUMMARY**: After every iter's TSV append + git commit + snapshot copy, your next action MUST be a tool call (typically the harness `next` command or starting the next curate). Do NOT write a chat message summarizing iter results, "current state", "best so far", or progress reports — that information is already in results.tsv. Every iteration boundary must transition to the next tool call without intermediate reflection text.

Before any chat message, check yourself:
- Did I just commit / append TSV / save snapshot?
- If yes: replace the urge to summarize with `uv run datacuration-bench next`.



## Data Isolation (MANDATORY)

Your results are only valid if you plan strategies from scratch. Accessing
another run's work is cheating and invalidates your results.

You are PROHIBITED from:

1. Reading, listing, scanning, or referencing any files, scores, strategies,
   curation code, evaluation outputs, or any other artifacts produced by a
   benchmark run, session, or agent other than your own active session.

2. Enumerating directories (via ls, find, glob, or shell loops) to discover
   what other work exists outside your current active suite.

3. Accessing git commits, branches, reflog, or history outside your current
   autoresearch branch. This includes viewing branches from past sessions,
   looking up external commit hashes, or using --all flags.

4. Delegating the above to tools, sub-agents, or scripts.
