# DataComp: In Search of the Next Generation of Multimodal Datasets

## One-line decision
Use this skill when you need a systematic benchmark-driven approach to evaluate and compare data filtering strategies for CLIP-style vision-language pretraining. Avoid it when you already have a fixed, curated dataset and do not intend to experiment with filtering.

## Skill metadata
- **Skill type**: data-filtering-benchmark
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Provide a standardized competition framework for designing better training datasets for CLIP models by fixing the model architecture and training code while allowing participants to innovate on data filtering and selection strategies.

## Problem signature
- Modality: image-text pairs from web crawl (CommonPool).
- Data state: a large unfiltered pool of image-text pairs is available; filtering must be applied to produce a training set.
- Scale regime: multiple scales from 12.8M to 12.8B candidate pairs.
- Model requirement: CLIP ViT-B/32 or ViT-L/14 with fixed training recipe.

## Use when
- You have a large pool of uncurated image-text pairs and need to decide which filtering strategy yields the best downstream CLIP performance.
- You want to benchmark a novel filtering method against established baselines (CLIP score, text-based, image-based filters).
- You want to understand the interaction between dataset scale and filtering aggressiveness.

## Do not use when
- You are training a generative VLM rather than a contrastive CLIP model and need instruction-tuning data.
- Your data pool is already small and curated; filtering would reduce it below a viable training set size.
- You need a filtering method for non-English or domain-specific data and the CommonPool does not cover your domain.

## Required inputs
- **candidate_pool**: Large pool of image-text pairs (e.g., CommonPool derived from Common Crawl).
- **filtering_strategy**: A function that takes the candidate pool and returns a subset for training.
- **evaluation_suite**: Downstream benchmarks (ImageNet, 38 transfer datasets) to measure CLIP zero-shot performance.

## Optional inputs
- **clip_score_model**: Pre-trained CLIP model used to compute image-text alignment scores for CLIP score filtering baseline.
- **text_complexity_features**: Perplexity, caption length, vocabulary richness features for text-based filtering.
- **image_quality_features**: Resolution, aesthetic score, NSFW probability for image-based filtering.

## Outputs
- **filtered_training_set**: Subset of the candidate pool selected by the filtering strategy.
- **benchmark_scores**: Zero-shot accuracy on ImageNet and 38 transfer datasets for the CLIP model trained on the filtered set.
- **filtering_analysis**: Comparison of the filtering strategy against DataComp baselines.

## Assumptions and prerequisites
- The CLIP architecture and training hyperparameters are fixed; only the data varies.
- CommonPool or an equivalent large-scale image-text pool is accessible.
- Compute budget is sufficient to train a CLIP model at the chosen scale.

## Procedure
1. **Obtain the candidate pool**
   Action: Download or construct a large pool of image-text pairs at the desired scale (small, medium, large, xlarge).
   Why: The pool defines the universe of candidates from which filtering selects a subset.
2. **Apply the filtering strategy**
   Action: Run the filtering function on the candidate pool. Common baselines include CLIP score thresholding, text-based filtering (English-only, caption length, deduplication), and image-based filtering (resolution, NSFW removal).
   Why: The filtering strategy is the variable under study.
3. **Train a CLIP model on the filtered set**
   Action: Train a CLIP ViT-B/32 (or ViT-L/14) using the fixed DataComp training recipe on the filtered subset.
   Why: Fixed training ensures differences in performance are attributable to data.
4. **Evaluate on downstream benchmarks**
   Action: Run zero-shot evaluation on ImageNet and 38 additional datasets.
   Why: These benchmarks provide a standardized measure of the data's quality.
5. **Compare against baselines**
   Action: Compare results to DataComp baselines: no filtering, random subset, CLIP score filtering, and best-published strategies.
   Why: Relative performance contextualizes the filtering method's contribution.

## Parameters to set
- **clip_score_threshold** — Role: Minimum CLIP similarity score for keeping an image-text pair. How to set: Sweep thresholds (e.g., 0.25, 0.28, 0.30) and pick the best on validation. Default/range: ~0.28 for medium scale. Effect: Higher threshold keeps fewer but better-aligned pairs.
- **pool_scale** — Role: Size of the candidate pool. How to set: Choose based on compute budget: small (12.8M), medium (128M), large (1.28B), xlarge (12.8B). Default/range: medium (128M). Effect: Larger pools allow more aggressive filtering.
- **text_filter_config** — Role: Language detection, caption length, and deduplication settings. How to set: English-only, min 5 words, near-dedup by text. Default/range: English, ≥5 words. Effect: Removes noise but may discard valid short captions.

## Validation checks
- Filtered set size should be reported alongside accuracy to characterize the precision-recall tradeoff.
- ImageNet zero-shot accuracy should be compared to the no-filtering and CLIP-score baselines at the same scale.
- Training loss curves should be monitored for overfitting on small filtered sets.

## Failure modes
- Overly aggressive filtering can reduce the training set below viable size, causing underfitting.
- CLIP score filtering inherits biases of the reference CLIP model used for scoring.
- Text-only filtering may keep visually irrelevant pairs with good captions.

## Adaptation notes for VLM training
- The filtering strategies (CLIP score, text quality, image quality) transfer directly to VLM pretraining data pipelines.
- For generative VLMs, augment CLIP score filtering with caption faithfulness checks.
- When a representation space is needed, prefer a joint image-text embedding rather than a unimodal feature space.

## Implementation notes
- Cache CLIP embeddings for the full candidate pool to enable rapid iteration on score thresholds.
- Use the DataComp evaluation toolkit for reproducible benchmark comparisons.
- Keep structured audit logs with timestamps, scorer versions, and exported manifests.

## Evidence from the paper
- DataComp is a testbed for dataset experiments centered around a new candidate pool of 12.8 billion image-text pairs from Common Crawl.
- Participants innovate by proposing new filtering techniques or new data sources while the model architecture and training code are fixed.
- The best methods found involve CLIP score filtering combined with text-based filtering, achieving a new state-of-the-art ImageNet zero-shot accuracy of 79.2% with a ViT-L/14.
- Filtering based on CLIP scores consistently outperforms no filtering and random subsets across all pool scales.

## Source paper
- **Title**: DataComp: In Search of the Next Generation of Multimodal Datasets
- **Year**: 2023
- **Venue**: NeurIPS
- **Paper ID**: arxiv-2304-14108v2
- **URL**: http://arxiv.org/abs/2304.14108v2
- **arXiv ID**: 2304.14108v2
