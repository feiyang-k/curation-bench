# Curation-Bench

A fixed-flow benchmark for dataset-curation agents. The benchmark owns task definitions, training, evaluation, and suite orchestration. Agents choose only what data to keep.

## How It Works

1. You declare a suite in `run_prompt.md`: which tasks, how many iterations per task, which profile.
2. You start the suite with `datacuration-bench run <agent>`. This launches one Docker container per task.
3. Inside each container the agent reads `BENCHMARK.md` and follows its protocol: `next → task → curate → audit → submit → finetune → eval`, then `next` to the next iteration.
4. The benchmark records per-iteration scores to `runs/<timestamp>/suite_state.json` and `suite_result.json`.

Each iteration runs independently: a failed iteration does not cancel subsequent iterations of the same task.

## Built-in Tasks

Nine task YAMLs under `src/benchmark/tasks/`. All evaluate on 8 benchmarks: HallusionBench, LLaVABench, MMBench, MMMU_DEV_VAL, MMStar, MMVet, MathVista_MINI, OCRBench.

| Task ID | Dataset | Model | Select | Strategy Timeout |
|---------|---------|-------|--------|------------------|
| `llava665k_llava_8bench_10k_unlimited` | LLaVA-665K | LLaVA-1.5-7B | 10K | unlimited |
| `llava665k_llava_8bench_20k_unlimited` | LLaVA-665K | LLaVA-1.5-7B | 20K | unlimited |
| `llava665k_llava_8bench_50k_unlimited` | LLaVA-665K | LLaVA-1.5-7B | 50K | unlimited |
| `llava665k_qwen_8bench_10k_unlimited` | LLaVA-665K | Qwen2.5-VL-3B-Instruct | 10K | unlimited |
| `llava665k_qwen2vl2b_8bench_10k_unlimited` | LLaVA-665K | Qwen2-VL-2B | 10K | unlimited |
| `llava665k_smolvlm_8bench_10k_unlimited` | LLaVA-665K | SmolVLM-Base (2.2B) | 10K | unlimited |
| `llava665k_smolvlm500m_8bench_10k_unlimited` | LLaVA-665K | SmolVLM-500M-Base | 10K | unlimited |
| `visionflan_llava_8bench_20k_unlimited` | VisionFlan | LLaVA-1.5-7B | 20K | unlimited |
| `visionflan_smolvlm_8bench_10k_unlimited` | VisionFlan | SmolVLM-Base (2.2B) | 10K | unlimited |

Varies the dataset (`llava665k` / `visionflan`), the target model (LLaVA-1.5-7B / Qwen2.5-VL-3B-Instruct / Qwen2-VL-2B / SmolVLM-Base / SmolVLM-500M-Base), and the selection budget (10K / 20K / 50K). `_unlimited` in the task ID means there is no per-iteration strategy-time budget.

## Training / Eval Backends

- LLaVA and Qwen fine-tuning → `vendor/curation-train`
- Evaluation → `vendor/VLMEvalKit`

## Repository Layout

```text
BENCHMARK.md                  Agent-facing protocol (mounted into container)
run_prompt.md                 Suite declaration: tasks + iterations + profile
curation/                     Agent's curation code — curate.py entry point + helpers
profiles/                     Machine-local paths (dataset/model/eval dirs, env, GPUs)
  example.yaml
configs/docker.yaml           Docker runner config (mounts, env)
docker/claude.Dockerfile      Container image for claude-code agent
src/benchmark/
  cli.py                      datacuration-bench entrypoint
  runner/docker_runner.py     Per-task container orchestration
  tools/suite.py              Suite state machine
  tools/session.py            Per-target tool dispatch
  tools/evaluation.py         VLMEvalKit launcher
  tasks/                      Built-in task YAMLs
vendor/
  curation-train/             LLaVA + Qwen trainer (uv project)
  VLMEvalKit/                 Evaluator (uv project)
tests/
```

## Setup

### 1. Install `uv`

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
export PATH="$HOME/.local/bin:$PATH"
uv python install 3.11
```

### 2. Sync the benchmark and vendor venvs

```bash
uv sync
uv sync --project vendor/curation-train
uv sync --project vendor/VLMEvalKit
```

### 3. Build the agent Docker image

```bash
docker build -f docker/claude.Dockerfile -t datacuration-bench-claude:latest .
```

### 4. Configure a profile

Copy `profiles/example.yaml` and fill in your machine's paths:

```yaml
dataset_path_map:
  llava665k: /path/to/llava665k_merged
  visionflan: /path/to/vision_flan

model_path_map:
  llava-1.5-7b-hf: /path/to/llava15-7b-hf-init
  qwen2.5-vl-3b-instruct: /path/to/Qwen2.5-VL-3B-Instruct

eval_data_dir: /path/to/LMUData

env:
  CUDA_VISIBLE_DEVICES: "2,3"
  BENCHMARK_TRAIN_GPUS: "2,3"
  BENCHMARK_EVAL_GPUS: "2"
  OPENAI_API_KEY: "..."
  OPENAI_API_BASE: "..."
```

`CUDA_VISIBLE_DEVICES` picks the host GPUs; inside the container they are remapped to consecutive IDs starting at 0 (`BENCHMARK_TRAIN_GPUS`/`BENCHMARK_EVAL_GPUS` are remapped automatically).

## Running a Suite

Declare the suite in `run_prompt.md`:

```yaml
---
tasks:
  - llava665k_qwen_8bench_10k_unlimited
  - llava665k_llava_8bench_10k_unlimited
iterations: 3
profile: example
---
```

Launch:

```bash
uv run datacuration-bench run claude --profile example
```

This initializes the suite and launches one container per task. Each container runs the agent through all iterations of its assigned task, then exits.

Dry run (print the docker command, don't execute):

```bash
uv run datacuration-bench run claude --profile example --dry-run
```

Force image rebuild:

```bash
uv run datacuration-bench run claude --profile example --rebuild
```

## Suite CLI (inside or outside the container)

These commands operate on the active suite (`.bench_active_suite` pointer file in CWD):

```bash
datacuration-bench init --prompt run_prompt.md --profile example  # create suite
datacuration-bench plan                                           # show all targets + states
datacuration-bench next                                           # advance to next target
datacuration-bench task                                           # describe active target
datacuration-bench time-budget                                    # remaining strategy time
datacuration-bench audit --path <dataset-dir>                     # contamination check
datacuration-bench submit --path <dataset-dir>                    # finalize submission
datacuration-bench finetune                                       # train on submitted data
datacuration-bench eval                                           # evaluate fine-tuned model
```

Outside a container, `init` is usually done automatically by the `run` command. You rarely need to call these manually unless debugging.

## Run Output Layout

```text
runs/<timestamp>/
  suite_state.json                       Suite state + per-target state
  suite_result.json                      Written when suite completes
  <task_id>_iter1/
    task.resolved.yaml
    events.jsonl                         Per-tool event log
    session_state.json
    curated/final_submission/            Agent's submitted dataset
    finetune/ft-<job>/
      benchmark_train_config.json        (llava + qwen)
      train_stdout.txt / train_stderr.txt
      model weights
    eval/
      eval_stdout.txt / eval_stderr.txt
      results/                           VLMEvalKit results (xlsx + json)
    output/run.jsonl                     Agent's full thinking + tool-call log
  <task_id>_iter2/
  ...
```

## Contamination Audit

`datacuration-bench audit --path <dir>` compares the submission against eval benchmarks using:

1. exact hash matching
2. n-gram near-duplicate detection

Status levels: `clean`, `warning`, `high_risk`.

## Tests

```bash
uv run pytest -q
```

More test details in [tests/README.md](tests/README.md).
