# TRAK: Attributing Model Behavior at Scale

## One-line decision
Use this skill when you want to efficiently attribute model behavior to training data at scale using random projections and ensembling. Avoid it when you do not need per-example attribution or simple quality metrics suffice.

## Skill metadata
- **Skill type**: scalable-data-attribution
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Provide a scalable method for attributing model predictions to individual training examples using random projections of gradients, enabling data valuation and selection at scale.

## Problem signature
- Modality: any modality; validated on vision and language tasks.
- Data state: training data needing per-example attribution scores.
- Scale regime: millions of training examples (more scalable than influence functions).
- Model requirement: Differentiable model with gradient access.

## Use when
- You need per-example data attribution at scale.
- Influence functions are too expensive for your dataset size.
- You want to identify which training examples matter for specific capabilities.

## Do not use when
- Simple quality metrics suffice for your needs.
- You have a very small dataset where exact influence is feasible.
- You do not need per-example granularity.

## Required inputs
- **training_data**: Dataset to compute attributions for.
- **trained_models**: Multiple model checkpoints for ensembling.
- **projection_matrix**: Random projection matrix for dimensionality reduction.

## Optional inputs
- **target_examples**: Specific examples to compute attributions for.

## Outputs
- **attribution_scores**: Per-training-example attribution scores.
- **data_valuation**: Ranking of training examples by attribution value.

## Assumptions and prerequisites
- Random projections preserve enough gradient information for attribution.
- Ensembling over multiple checkpoints improves attribution quality.
- TRAK scales to millions of examples where influence functions cannot.

## Procedure
1. **Train multiple model checkpoints**
   Action: Train the model and save checkpoints at different stages or with different seeds.
   Why: Ensembling over checkpoints improves attribution stability.
   Note: See paper for details.
2. **Compute projected gradients**
   Action: Project per-example gradients using random projection matrices.
   Why: Projection makes computation tractable at scale.
   Note: See paper for details.
3. **Compute attribution scores**
   Action: Calculate TRAK scores for each training example.
   Why: Scores indicate each example's contribution.
   Note: See paper for details.
4. **Select or prune by attribution**
   Action: Use attribution scores for data selection or pruning.
   Why: High-attribution examples are most valuable.
   Note: See paper for details.

## Parameters to set
- **projection_dim** — Role: Dimensionality of random projections. How to set: 2K-4K for good accuracy. Default/range: 4096. Effect: Higher dimension improves accuracy but increases cost.
- **num_checkpoints** — Role: Number of model checkpoints for ensembling. How to set: 10-20 checkpoints. Default/range: 10. Effect: More checkpoints improve stability.

## Validation checks
- Attribution scores should correlate with leave-one-out retraining effects.
- High-attribution examples should be more valuable than random examples.
- TRAK should match or exceed influence function accuracy at lower cost.

## Failure modes
- Random projections may lose important gradient information.
- Many checkpoints are needed for stable attributions.
- The method may not capture complex data interactions.

## Adaptation notes for VLM training
- Use TRAK for VLM training data attribution and selection.
- Identify which image-text pairs contribute most to specific VLM capabilities.
- Combine TRAK with other data selection methods.

## Implementation notes
- Use the TRAK library for efficient implementation.
- Pre-compute and cache projected gradients.
- Compare TRAK to random selection baselines.

## Evidence from the paper
- TRAK provides scalable data attribution using random projections of gradients.
- The method matches influence function accuracy while being orders of magnitude faster.
- TRAK enables data valuation at scales of millions of training examples.
- The approach has been validated on both vision and language tasks.

## Source paper
- **Title**: TRAK: Attributing Model Behavior at Scale
- **Year**: 2023
- **Venue**: ICML
- **Paper ID**: arxiv-2303.14186v2
- **URL**: http://arxiv.org/abs/2303.14186v2
- **arXiv ID**: 2303.14186v2
