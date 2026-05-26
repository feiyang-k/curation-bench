# Beyond Neural Scaling Laws: Beating Power Law Scaling via Data Pruning

## One-line decision
Use this skill when you want to beat standard scaling laws by pruning low-quality or redundant data points using perplexity or EL2N scores. Avoid it when you do not have compute for data quality scoring or your data is already curated.

## Skill metadata
- **Skill type**: data-pruning-for-scaling
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Demonstrate that intelligently pruning training data using quality metrics (perplexity, EL2N scores) can beat the standard power law scaling, achieving better performance with less data.

## Problem signature
- Modality: any modality; demonstrated on vision and language data.
- Data state: large training datasets with quality scores for each example.
- Scale regime: datasets from millions to billions of examples.
- Model requirement: Pre-trained model for computing quality scores; any model architecture for training.

## Use when
- You have a large dataset and want to train on a higher-quality subset.
- You can compute per-example quality scores (perplexity, EL2N).
- You want to reduce training compute while maintaining or improving quality.

## Do not use when
- Your data is already curated and high-quality.
- You cannot afford the cost of scoring all examples.
- You need all data for coverage of rare concepts.

## Required inputs
- **training_data**: Large training dataset to be pruned.
- **quality_scorer**: Model or metric for scoring example quality (perplexity, EL2N, etc.).
- **pruning_threshold**: Threshold or fraction for data pruning.

## Optional inputs
- **stratification**: Strategy for balanced pruning across data subgroups.

## Outputs
- **pruned_dataset**: Higher-quality subset of the training data.
- **improved_model**: Model trained on pruned data with better efficiency.

## Assumptions and prerequisites
- Training data contains examples of varying quality and utility.
- Quality metrics can identify examples worth keeping.
- Pruning low-quality data improves the scaling law exponent.

## Procedure
1. **Score all training examples**
   Action: Compute quality scores (perplexity, EL2N, loss) for each example using a pre-trained model.
   Why: Quality scores identify which examples to keep or prune.
   Note: See paper for details.
2. **Rank and prune**
   Action: Sort examples by quality score and prune the lowest-quality fraction.
   Why: Removing low-quality examples improves the dataset.
   Note: See paper for details.
3. **Train on pruned data**
   Action: Train the target model on the pruned dataset.
   Why: Higher-quality data yields better models per training step.
   Note: See paper for details.
4. **Compare to unpruned baseline**
   Action: Compare pruned training to full-data baseline at same compute.
   Why: Demonstrates that pruning beats standard scaling.
   Note: See paper for details.

## Parameters to set
- **pruning_fraction** — Role: Fraction of data to remove. How to set: Prune 20-50% of lowest-quality examples. Default/range: 20-50%. Effect: More aggressive pruning increases quality but reduces diversity.
- **scoring_metric** — Role: Metric for example quality. How to set: Use perplexity, EL2N, or loss-based scores. Default/range: Perplexity or EL2N. Effect: Different metrics identify different aspects of quality.
- **scoring_model** — Role: Model used to compute quality scores. How to set: Use a pre-trained model of similar or smaller size. Default/range: Pre-trained baseline. Effect: Better scoring models produce better pruning decisions.

## Validation checks
- Pruned training should achieve better performance per compute step.
- The scaling law exponent should improve with pruning.
- Pruning should not systematically remove rare but important examples.

## Failure modes
- Aggressive pruning may remove rare but valuable examples.
- The scoring model may not accurately assess quality for all examples.
- Pruning decisions may not transfer across model architectures.

## Adaptation notes for VLM training
- Apply data pruning to VLM pretraining and instruction tuning data.
- Use CLIP scores as quality metrics for image-text data pruning.
- Combine pruning with deduplication for maximum efficiency.

## Implementation notes
- Pre-compute and cache all quality scores.
- Experiment with different pruning fractions to find the optimum.
- Monitor coverage of rare concepts after pruning.

## Evidence from the paper
- Data pruning can beat standard neural scaling laws by improving the scaling exponent.
- Pruning 20-50% of low-quality data maintains or improves model performance.
- The approach works across vision and language modalities.
- Quality-based pruning is more effective than random subsampling.

## Source paper
- **Title**: Beyond Neural Scaling Laws: Beating Power Law Scaling via Data Pruning
- **Year**: 2022
- **Venue**: NeurIPS
- **Paper ID**: arxiv-2206.14486v2
- **URL**: http://arxiv.org/abs/2206.14486v2
- **arXiv ID**: 2206.14486v2
