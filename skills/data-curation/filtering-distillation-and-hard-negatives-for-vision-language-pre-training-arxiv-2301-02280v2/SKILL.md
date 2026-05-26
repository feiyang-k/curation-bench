# Filtering, Distillation, and Hard Negatives for Vision-Language Pre-Training

## One-line decision
Use this skill when you want to filter web-crawled image-text data using a learned data filtering network (DFN) trained to predict which pairs improve downstream performance. Avoid it when you do not have labeled data for training a filtering network or prefer simple threshold-based filtering.

## Skill metadata
- **Skill type**: data-filtering-and-distillation
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Train a data filtering network (DFN) that learns to predict which image-text pairs from a web-crawled pool are most useful for CLIP training, then use it to curate high-quality training data.

## Problem signature
- Modality: image-text pairs scored by a learned filtering network.
- Data state: large web-crawled pool of image-text pairs that need learned quality filtering.
- Scale regime: 2 billion candidate pairs filtered down to hundreds of millions for training.
- Model requirement: A trained data filtering network (small CLIP variant); standard CLIP architecture for training.

## Use when
- You have a very large pool of web-crawled image-text pairs and need learned filtering beyond simple thresholds.
- You have a small set of high-quality training data to bootstrap the filtering network.
- You want to outperform CLIP score filtering and MetaCLIP curation.

## Do not use when
- You lack a high-quality reference dataset to train the filtering network.
- Simple CLIP score filtering already meets your quality requirements.
- Your candidate pool is small enough that filtering would leave insufficient training data.

## Required inputs
- **candidate_pool**: Large web-crawled image-text pair pool.
- **reference_quality_data**: Small high-quality dataset for training the filtering network.
- **filtering_network_architecture**: Small CLIP-like model trained to score pairs.

## Optional inputs
- **hard_negative_mining**: Strategy for generating hard negatives during CLIP training.
- **distillation_teacher**: Larger CLIP model for knowledge distillation.

## Outputs
- **filtered_training_data**: High-quality subset of the candidate pool selected by the DFN.
- **dfn_clip_model**: CLIP model trained on DFN-filtered data with state-of-the-art performance.

## Assumptions and prerequisites
- A small model can learn to predict which pairs are useful for CLIP training.
- High-quality reference data provides sufficient signal for training the filter.
- Learned filtering outperforms heuristic or score-based approaches.

## Procedure
1. **Train the data filtering network**
   Action: Train a small CLIP model on a mix of high-quality and random web data, using quality labels derived from the high-quality reference set.
   Why: The DFN learns to distinguish useful from noisy pairs.
   Note: See paper for details.
2. **Score the candidate pool**
   Action: Apply the trained DFN to score all pairs in the candidate pool.
   Why: Assigns a quality score to each candidate pair.
   Note: See paper for details.
3. **Filter by DFN score**
   Action: Keep pairs above a DFN score threshold to form the training set.
   Why: Selects the highest quality subset for CLIP training.
   Note: See paper for details.
4. **Train CLIP on filtered data**
   Action: Train the target CLIP model on the DFN-filtered dataset.
   Why: High-quality filtered data produces better CLIP models.
   Note: See paper for details.
5. **Apply hard negatives and distillation**
   Action: Optionally add hard negative mining and knowledge distillation to further improve training.
   Why: These techniques complement data filtering for additional gains.
   Note: See paper for details.

## Parameters to set
- **dfn_score_threshold** — Role: Minimum DFN score for keeping a pair. How to set: Sweep thresholds on validation. Default/range: Dataset-dependent. Effect: Higher threshold keeps fewer but higher quality pairs.
- **dfn_model_size** — Role: Size of the filtering network. How to set: Use a small, efficient model (e.g., ViT-B/16). Default/range: ViT-B/16. Effect: Smaller models are faster to apply but may have lower accuracy.
- **hard_negative_ratio** — Role: Fraction of hard negatives in each batch. How to set: Start with 50% hard negatives. Default/range: 0.5. Effect: More hard negatives improve discrimination but may destabilize training.

## Validation checks
- DFN-filtered data should outperform CLIP score filtering and MetaCLIP on downstream benchmarks.
- The DFN should assign high scores to clean, well-aligned pairs and low scores to noisy ones.
- Zero-shot ImageNet accuracy should set a new state-of-the-art for the given model scale.

## Failure modes
- The DFN may overfit to the reference data distribution, rejecting valid out-of-distribution pairs.
- Training the DFN requires careful curation of the reference quality labels.
- Hard negatives may be too difficult early in training, causing instability.

## Adaptation notes for VLM training
- The DFN approach can be adapted to filter data for any VLM pretraining pipeline.
- Train domain-specific DFNs using domain-specific reference data.
- Combine DFN filtering with metadata curation for best results.

## Implementation notes
- Pre-compute DFN scores for the entire pool and store them for rapid threshold sweeping.
- Use efficient inference (half-precision, batched) for scoring billions of pairs.
- Monitor the score distribution to set thresholds meaningfully.

## Evidence from the paper
- DFN CLIP ViT-H/14 achieves 83.0% zero-shot ImageNet accuracy, setting a new state-of-the-art.
- Learned data filtering (DFN) outperforms CLIP score filtering and MetaCLIP curation.
- Hard negatives and knowledge distillation provide additional gains on top of data filtering.
- The key insight is that learning to filter is more effective than using fixed heuristics.

## Source paper
- **Title**: Filtering, Distillation, and Hard Negatives for Vision-Language Pre-Training
- **Year**: 2023
- **Venue**: CVPR
- **Paper ID**: arxiv-2301.02280v2
- **URL**: http://arxiv.org/abs/2301.02280v2
- **arXiv ID**: 2301.02280v2
