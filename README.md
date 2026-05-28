# Curation-Bench

*A fixed-flow benchmark for dataset-curation agents.*

---

## What is Curation-Bench?

Data curation is the highest-leverage decision in vision-language model training, yet most prior "data selection" benchmarks confound it with training-recipe variation and model choice. Curation-Bench fixes everything except the subset itself.

The harness owns the full pipeline. For each *task* you pick a `(dataset, base model, selection budget, evaluation suite)`. The agent's only job is to submit a curated subset of the requested size. Curation-Bench fine-tunes a single base model for one epoch under a frozen recipe, evaluates with [VLMEvalKit](https://github.com/open-compass/VLMEvalKit) on eight benchmarks, and writes a score. Differences between runs are attributable to the curation strategy alone.

You can drive Curation-Bench in two modes:

- **Manual** — write `curation/curate.py` yourself, then run the harness commands to score it.
- **Agent** — let an LLM agent (Claude Code, Codex CLI, or OpenHands) iterate over `curation/curate.py` inside a sandboxed container that has access only to the harness CLI, the dataset, and a built-in protocol document.

Each iteration runs independently; a failed iteration does not cancel subsequent iterations of the same task.

---

## How It Works

Each iteration follows a fixed seven-step loop. The harness owns step transitions; the agent only edits curation code between steps.

1. `next` — the harness advances to the next pending `(task, iteration)` target and writes a per-iteration run directory.
2. `task` — returns the task spec (dataset path, model path, target row count, evaluation list).
3. *(agent edits `curation/curate.py` and produces an Arrow dataset of `target_rows` rows)*
4. `audit` — flags exact-match and 8-gram overlaps between the submission and the eight evaluation benchmarks.
5. `submit` — validates row count and registers the dataset as this iteration's accepted submission.
6. `finetune` — trains the base model on the submitted data for one epoch under the frozen recipe.
7. `eval` — runs VLMEvalKit on the fine-tuned model and writes the eight per-benchmark scores plus a normalized aggregate.

Per-iteration scores land in `runs/<timestamp>/suite_state.json`; final results in `suite_result.json`.

---

## Built-in Tasks

Eight task YAMLs under `src/benchmark/tasks/`. All evaluate on eight benchmarks: HallusionBench, LLaVABench, MMBench, MMMU_DEV_VAL, MMStar, MMVet, MathVista_MINI, OCRBench.

| Task ID | Dataset | Model | Select | Strategy Timeout |
|---|---|---|---|---|
| `llava665k_llava_8bench_10k_unlimited` | LLaVA-665K | LLaVA-1.5-7B | 10K | unlimited |
| `llava665k_llava_8bench_20k_unlimited` | LLaVA-665K | LLaVA-1.5-7B | 20K | unlimited |
| `llava665k_llava_8bench_50k_unlimited` | LLaVA-665K | LLaVA-1.5-7B | 50K | unlimited |
| `llava665k_qwen_8bench_10k_unlimited` | LLaVA-665K | Qwen2.5-VL-3B-Instruct | 10K | unlimited |
| `llava665k_qwen2vl2b_8bench_10k_unlimited` | LLaVA-665K | Qwen2-VL-2B | 10K | unlimited |
| `llava665k_smolvlm_8bench_10k_unlimited` | LLaVA-665K | SmolVLM-Base (2.2B) | 10K | unlimited |
| `visionflan_llava_8bench_20k_unlimited` | VisionFlan | LLaVA-1.5-7B | 20K | unlimited |
| `visionflan_smolvlm_8bench_10k_unlimited` | VisionFlan | SmolVLM-Base (2.2B) | 10K | unlimited |

Tasks vary the dataset (`llava665k` / `visionflan`), the target model, and the selection budget (10K / 20K / 50K). `_unlimited` in the task ID means there is no per-iteration strategy-time budget.

---

## Repository Layout

```text
BENCHMARK.md                Agent-facing protocol (canonical text mounted into container)
AGENTS.md                   One-line pointer at BENCHMARK.md for autonomous-agent tooling
run_prompt.md               Suite declaration: tasks + iterations + profile
curation/                   Agent's curation code — curate.py entry point + helpers
profiles/                   Machine-local paths (datasets, models, eval dir, env, GPUs)
  example.yaml
configs/docker.yaml         Docker runner config (mounts, agent model/effort)
docker/                     Agent images (claude / codex / openhands)
protocols/                  Variant protocol documents (plain / instruction / skill)
skills/                     Paper-derived skill cards (data-acquisition / data-curation /
                            data-selection / data-synthesis) — used by the skill protocol
src/benchmark/
  cli.py                    datacuration-bench entrypoint
  core/                     Profile, prompt, task, model registry
  runner/docker_runner.py   Per-task container orchestration
  tools/suite.py            Suite state machine
  tools/session.py          Per-target tool dispatch
  tools/evaluation.py       VLMEvalKit launcher
  tools/contamination.py    Eval-overlap audit
  tasks/                    Built-in task YAMLs
vendor/
  curation-train/           LLaVA / Qwen / SmolVLM trainers (uv project)
  VLMEvalKit/               Evaluator (uv project)
tests/                      Pytest suite
```

---

## Prerequisites

Before running anything, make sure the host has:

- **Docker Engine** ≥ 20.10
- **NVIDIA Container Toolkit** (for GPU access inside containers)
- **At least one NVIDIA GPU** — ≥ 24 GB VRAM for the 7B targets, ≥ 16 GB suffices for SmolVLM-Base, ≥ 8 GB suffices for SmolVLM-500M / 256M
- **[`uv`](https://docs.astral.sh/uv/)** — Python project manager; Python 3.12 itself is bootstrapped by `uv`
- **Git**
- **≥ 1 TB free disk** (the datasets dominate)
- **Exactly one of these agent credentials** (pick the agent you plan to use):
  - Claude Code: `CLAUDE_CODE_OAUTH_TOKEN` env var, *or* `~/.claude/.credentials.json` from `claude login`
  - Codex: `~/.codex/auth.json`
  - OpenHands (via Together AI): `TOGETHER_API_KEY` env var

---

## Setup

### Step 1 — Clone and install the CLI

```bash
git clone <repo-url> Curation-Bench
cd Curation-Bench
uv sync
```

That builds the host venv (`./.venv`) used to invoke the `datacuration-bench` CLI. The vendor venvs under `vendor/curation-train` and `vendor/VLMEvalKit` are *not* built on the host — they're built inside the agent container on its first run.

### Step 2 — Download the datasets

The benchmark expects HuggingFace Arrow datasets saved via `datasets.save_to_disk()`, with two columns:

- `images` — `PIL.Image` or a `{bytes, path}` dict
- `texts` — a list of `{user, assistant}` turns

| `dataset_id` (profile key) | Source | On-disk size | Used by |
|---|---|---|---|
| `llava665k` | LLaVA-1.5 visual-instruction-tuning data, repacked as a 665K-row Arrow dataset | ~500 GB | 6 of 8 tasks |
| `visionflan` | [`Vision-Flan/Vision-Flan_jsons_split`](https://huggingface.co/datasets/Vision-Flan/Vision-Flan_jsons_split) repacked into the same `(images, texts)` schema | ~300 GB | 2 of 8 tasks |

Place each dataset wherever you have room and remember the path; you'll wire it up in your profile in Step 5. If you only need one task family, you only need that family's dataset.

> **Tip:** if you already have raw LLaVA / VisionFlan jsons, you can convert them to the expected Arrow layout with a small script using `datasets.Dataset.save_to_disk`. The exact column shapes the harness expects are documented in `vendor/curation-train/src/curation_train/train_smolvlm.py` (`_as_pil_image()` and `_normalize_turns()`).

### Step 3 — Download the base models

| `model_key` (profile key) | HuggingFace id | Tasks |
|---|---|---|
| `llava-1.5-7b-hf` | `llava-hf/llava-1.5-7b-hf` | All LLaVA tasks |
| `qwen2.5-vl-3b-instruct` | `Qwen/Qwen2.5-VL-3B-Instruct` | `llava665k_qwen_8bench_10k_unlimited` |
| `qwen2-vl-2b` | `Qwen/Qwen2-VL-2B` | `llava665k_qwen2vl2b_8bench_10k_unlimited` |
| `smolvlm` | `HuggingFaceTB/SmolVLM-Base` (2.2B) | SmolVLM 2.2B tasks |
| `smolvlm-500m` | `HuggingFaceTB/SmolVLM-500M-Base` | supported but not in the default task set |
| `smolvlm-256m` | `HuggingFaceTB/SmolVLM-256M-Base` | supported but not in the default task set |

A typical download:

```bash
huggingface-cli download llava-hf/llava-1.5-7b-hf --local-dir /path/to/llava-1.5-7b-hf
```

You only need the models that the tasks you plan to run actually use.

### Step 4 — Prepare evaluation data and the judge model

**LMUData.** VLMEvalKit auto-downloads all eight evaluation TSVs into your `LMUData/` directory on the first eval run, so the user just needs to create a directory and point the profile at it:

```bash
mkdir -p /path/to/LMUData
```

**Judge model.** Three of the eight benchmarks (LLaVABench, MMVet, MathVista_MINI) need an LLM judge. The default is `Qwen3.5-27B` served over an OpenAI-compatible endpoint. Two options:

1. **Local vLLM** (recommended for cost). Reserve one GPU and serve:
   ```bash
   vllm serve Qwen/Qwen3.5-27B \
     --host 127.0.0.1 --port 8001 \
     --served-model-name Qwen3.5-27B \
     --api-key YOUR_LOCAL_KEY
   ```
   Then set `OPENAI_API_BASE=http://host.docker.internal:8001/v1` and `OPENAI_API_KEY=YOUR_LOCAL_KEY` in your profile. (Inside the container, `localhost` won't reach the host vLLM — use `host.docker.internal`.)

2. **Cloud OpenAI-compatible endpoint.** Set `OPENAI_API_BASE` and `OPENAI_API_KEY` to whatever provider you use.

### Step 5 — Create your profile

Copy the template and fill in real paths:

```bash
cp profiles/example.yaml profiles/my-machine.yaml
```

A typical `profiles/my-machine.yaml`:

```yaml
dataset_path_map:
  llava665k:   /data/curation/llava665k
  visionflan:  /data/curation/visionflan

model_path_map:
  llava-1.5-7b-hf:         /data/models/llava-1.5-7b-hf
  qwen2.5-vl-3b-instruct:  /data/models/Qwen2.5-VL-3B-Instruct
  qwen2-vl-2b:             /data/models/Qwen2-VL-2B
  smolvlm:                 /data/models/SmolVLM-Base
  smolvlm-500m:            /data/models/SmolVLM-500M-Base

eval_data_dir: /data/LMUData

env:
  CUDA_VISIBLE_DEVICES:  "0,1"
  BENCHMARK_TRAIN_GPUS:  "0"
  BENCHMARK_EVAL_GPUS:   "1"
  OPENAI_API_KEY:        "YOUR_LOCAL_KEY"
  OPENAI_API_BASE:       "http://host.docker.internal:8001/v1"
```

Field reference:

- `dataset_path_map` — every `dataset_id` the tasks you'll run mention must appear here. Missing keys surface as `Cannot resolve dataset path for task X` at suite init.
- `model_path_map` — same, for `model_key`. Note that the *key* names look like model IDs but the *value* is a directory of model weights — pick weights consistent with the key (e.g., point `qwen2.5-vl-3b-instruct` at the 3B variant, not the 7B).
- `eval_data_dir` — the `LMUData/` from Step 4. Mounted read-write into the container; VLMEvalKit writes its decoded images there on first run.
- `env` — environment variables passed into the training and eval subprocesses. The harness remaps GPU IDs for you: `CUDA_VISIBLE_DEVICES` lists the host GPUs to expose, and `BENCHMARK_TRAIN_GPUS` / `BENCHMARK_EVAL_GPUS` are **container-local** indices into that list (0-based). For example, `CUDA_VISIBLE_DEVICES="0,1"` + `BENCHMARK_TRAIN_GPUS="0"` means "expose host GPUs 0 and 1; pin training to the *first* of those (= host GPU 0)."
- `env.OPENAI_API_KEY` / `OPENAI_API_BASE` — judge endpoint from Step 4.

### Step 6 — Configure your agent

Pick one:

**Claude Code**
```bash
export CLAUDE_CODE_OAUTH_TOKEN="<your-token>"
# or, if you've run `claude login` on the host:
#   ~/.claude/.credentials.json will be mounted into the container automatically.
```

**Codex CLI**
```bash
# Make sure ~/.codex/auth.json exists. Either run `codex login` once, or
# create it manually per OpenAI's Codex CLI docs.
```

**OpenHands (Together AI)**
```bash
export TOGETHER_API_KEY="<your-key>"
# OpenHands spawns sibling containers via Docker-out-of-Docker; pre-pull
# its agent-server image so the first run isn't slowed by a network fetch:
docker pull ghcr.io/openhands/agent-server:latest-python
```

Per-agent model and reasoning-effort defaults live in `configs/docker.yaml` under `agents.<name>`; edit there if you want to override.

### Step 7 — Build the agent's Docker image (optional but recommended)

`datacuration-bench run` builds the image automatically on first launch, but pre-building catches build errors before you commit to a long run:

```bash
docker build -f docker/claude.Dockerfile     -t datacuration-bench-claude:latest    .
docker build -f docker/codex.Dockerfile      -t datacuration-bench-codex:latest     .
docker build -f docker/openhands.Dockerfile  -t datacuration-bench-openhands:latest .
```

Only build the image for the agent you'll use.

### Step 8 — Declare the suite

The suite manifest lives in `run_prompt.md`:

```yaml
---
tasks:
  - llava665k_llava_8bench_10k_unlimited
iterations: 1
profile: my-machine
---
```

Frontmatter fields:

- `tasks` *(required, list)* — task IDs from the table above. All iterations of `tasks[0]` run before `tasks[1]`.
- `iterations` *(optional, int, default 1)* — number of iterations *per task*. Applies uniformly; per-task overrides are not supported.
- `profile` *(optional, str)* — profile file name without `.yaml`. May be overridden on the command line.

Anything after the closing `---` is *strategy text*: free-form Markdown the agent will read at the start of every iteration as a hint, but the harness itself does not interpret.

### Step 9 — Launch

```bash
uv run datacuration-bench run claude --profile my-machine
```

Replace `claude` with `codex`, `openhands-kimi`, or `openhands-qwen` for the other agents. Useful flags:

- `--protocol plain|instruction|skill` — which protocol document the agent reads (default `plain`).
- `--rebuild` — force a fresh image build.
- `--dry-run` — print the Docker invocation without executing.
- `--new-suite` — discard `.bench_active_suite` and start a fresh run; without this flag, `run` resumes the existing active suite when possible.

The launcher initializes the suite, builds the image if needed, and starts one Docker container per task. Each container walks all iterations of its assigned task and then exits.

---

## Run Output Layout

```text
runs/<timestamp>_<agent>/
  suite_state.json                       Suite state + per-target state
  suite_result.json                      Written when the suite completes
  <task_id>_iter1/
    task.resolved.yaml                   Profile-resolved task spec (paths filled in)
    events.jsonl                         Per-tool event log
    session_state.json
    curated/final_submission/            Agent's submitted Arrow dataset
    finetune/ft-<job>/                   Training run: stdout/stderr + model weights
    eval/
      eval_stdout.txt / eval_stderr.txt
      results/                           VLMEvalKit results (xlsx + json)
    output/run.jsonl                     Agent's full thinking + tool-call log
  <task_id>_iter2/
  ...
```

---

## Manual / Suite CLI Reference

The `run` command does end-to-end orchestration. For debugging, replay, or running outside Docker, the individual harness commands are also exposed:

```bash
datacuration-bench init --prompt run_prompt.md --profile my-machine   # create + activate a suite
datacuration-bench plan                                                # list all targets + states
datacuration-bench next                                                # advance to next target
datacuration-bench task                                                # print active target spec
datacuration-bench time-budget                                         # remaining strategy time
datacuration-bench audit    --path <dataset-dir>                       # contamination check
datacuration-bench submit   --path <dataset-dir>                       # finalize submission
datacuration-bench finetune                                            # train on submitted data
datacuration-bench eval                                                # evaluate fine-tuned model
```

All commands except `init` read the active suite from `.bench_active_suite` in the current working directory; pass `--suite-dir` to override.

---

## Contamination Audit

`datacuration-bench audit --path <dir>` compares each submission against the eight evaluation benchmarks (loaded from `LMUData/`, the same TSVs VLMEvalKit auto-downloads on first eval) using two passes:

1. **Exact hash matching** — SHA-256 of normalized question/answer pairs.
2. **8-gram near-duplicate detection** — token-set overlap ≥ 0.8.

Status levels: `clean`, `warning`, `high_risk`. The agent's `submit` step refuses high-risk submissions.

---

## Tests

```bash
uv run pytest -q
```

The test suite covers profile parsing, suite-state transitions, the Docker runner config, contamination detection, and basic evaluation plumbing. See `tests/` for the full layout.

---

## Troubleshooting

- **`Cannot resolve dataset path for task X (dataset_id=Y)`** — `Y` isn't in your profile's `dataset_path_map`. Add it.
- **`Cannot resolve model path for task X (model_key=Y)`** — same, but `model_path_map` / `model_key`.
- **`permission denied: /var/run/docker.sock`** (OpenHands only) — add your host user to the `docker` group, or run with `sudo`.
- **Training appears to hang with no `train_runtime` line** — usually GPU memory. SmolVLM uses per-device batch 16, LLaVA uses 1×16-accum, both at bf16; see `vendor/curation-train/src/curation_train/defaults.py` for the full recipes.
- **VLMEvalKit can't reach the judge** — from inside the container, `localhost` is the container itself. Use `host.docker.internal` (Docker Desktop / recent Linux Docker) or your host's LAN IP, and make sure `OPENAI_API_BASE` ends in `/v1` (not `/v1/chat/completions`).
- **Out-of-memory during eval** — bring up the judge on a separate GPU and assign it via `BENCHMARK_EVAL_GPUS` in the profile.

---

## License

*Not yet specified — coming soon.*
