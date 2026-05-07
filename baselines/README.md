# Baseline Data Generation

This folder contains the data-generation scripts for the non-agent baselines used
in the LLaVA-665K to LLaVA-1.5-7B baseline study.

Included baseline families:

- `llava665k_random`: uniformly sample from the LLaVA-665K Arrow dataset.
- `icons_random`: sample from the released ICONS selected-example pool after
  mapping it back to LLaVA-665K.
- `ards_random`: sample from the released ARDS selected-example pool after
  mapping it back to LLaVA-665K.
- `template_rewrite`: sample from LLaVA-665K and apply the programmatic Template
  Matters rewrite.

The one-command setup and data-generation entrypoint is:

```bash
uv run python scripts/setup_baselines.py --output-dir dataset_run_vX --seed 123
```

This initializes the Template Matters submodule, downloads the small external
metadata files, checks the configured LLaVA-665K Arrow dataset, and generates
Random, ICONS, ARDS, and Template Matters subsets with a shared run seed.

Each family can also be generated independently:

```bash
uv run python scripts/generate_random.py --output-dir dataset_run_vX --seed 123
uv run python scripts/generate_icons.py --output-dir dataset_run_vX --seed 123
uv run python scripts/generate_ards.py --output-dir dataset_run_vX --seed 123
uv run python scripts/generate_template_rewrite.py --output-dir dataset_run_vX --seed 123
```

The setup script calls these four family scripts by default. Use `--families` to
run a subset, for example `--families random template_rewrite`.

To only download/configure external artifacts:

```bash
uv run python scripts/download_llava665k.py
```

The downloader reads `.env`. By default it fetches only
`dataset/llava_v1_5_mix665k.json` and `dataset/ards_selected.json`; the image
archives are large and are skipped unless `DOWNLOAD_IMAGES=true` or
`--download-images` is set.

By default it expects the local LLaVA-665K Arrow dataset at:

```text
/path/to/llava665k_ds
```

Large external artifacts are intentionally not checked into this folder:

- `dataset/llava_v1_5_mix665k.json` from `liuhaotian/LLaVA`.
- `dataset/ards_selected.json` from the ARDS release.
- The local LLaVA-665K Arrow dataset.

Place those artifacts at the paths expected by the scripts, or pass explicit
paths with the script arguments.

For a small smoke test, pass temporary paths and tiny budgets:

```bash
uv run python scripts/setup_baselines.py \
  --output-dir /tmp/dataset_run_smoke \
  --seed 123 \
  --budgets 1000 \
  --skip-downloads
```
