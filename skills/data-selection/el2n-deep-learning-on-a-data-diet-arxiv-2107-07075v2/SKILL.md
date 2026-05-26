# EL2N: Deep Learning on a Data Diet

## One-line decision
Use this skill when you want to prune training data using early-epoch error norms (EL2N scores) to select the most informative examples. Avoid it when you cannot compute early training predictions or all data is equally important.

## Skill metadata
- **Skill type**: error-based-data-pruning
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Select the most informative training examples using EL2N scores — the L2 norm of error vectors computed early in training — enabling a 'data diet' where models train on less data without losing performance.

## Problem signature
- Modality: any modality with softmax predictions.
- Data state: training data scored by EL2N at early training epochs.
- Scale regime: standard to large datasets.
- Model requirement: Any model with softmax outputs for early-epoch EL2N computation.

## Use when
- You want to select the most informative training examples.
- You can compute predictions at early training epochs.
- You want data-efficient training.

## Do not use when
- All data is equally important for your task.
- You cannot compute early-epoch predictions.
- Your dataset is already small.

## Required inputs
- **training_data**: Dataset to score for pruning.
- **early_model**: Model at early training epoch for computing EL2N scores.
- **el2n_scorer**: Code for computing L2 norm of error vectors.

## Optional inputs
- **pruning_fraction**: Fraction of data to keep.

## Outputs
- **el2n_scores**: Per-example EL2N scores.
- **selected_subset**: High-EL2N examples selected for training.

## Assumptions and prerequisites
- Examples with high EL2N scores early in training are more informative.
- Low-EL2N examples are easy and redundant.
- Early-epoch scores predict long-term utility.

## Procedure
1. **Train for a few epochs**
   Action: Train the model for 5-10 epochs.
   Why: Early training provides the signal for EL2N scoring.
   Note: See paper for details.
2. **Compute EL2N scores**
   Action: For each example, compute the L2 norm of (prediction - one_hot_label).
   Why: EL2N captures example difficulty relative to the model.
   Note: See paper for details.
3. **Select high-EL2N examples**
   Action: Keep examples with the highest EL2N scores.
   Why: High-EL2N examples are most informative.
   Note: See paper for details.
4. **Train on selected subset**
   Action: Train from scratch on the selected examples.
   Why: Data diet maintains performance with less data.
   Note: See paper for details.

## Parameters to set
- **early_epochs** — Role: Number of epochs for EL2N computation. How to set: 5-10 epochs. Default/range: 10. Effect: More epochs provide more stable scores.
- **keep_fraction** — Role: Fraction of data to keep. How to set: 50-75% for typical datasets. Default/range: 50-75%. Effect: Lower fraction is more aggressive pruning.

## Validation checks
- Training on high-EL2N examples should match full-data performance.
- EL2N scores should be stable across random seeds.
- Low-EL2N examples should be verifiably easy.

## Failure modes
- Early-epoch scores may not be stable for all datasets.
- Aggressive pruning may remove important rare examples.
- The method requires initial training for scoring.

## Adaptation notes for VLM training
- Apply EL2N scoring to VLM pretraining data selection.
- Use early-epoch VLM predictions to score image-text pairs.
- Combine with CLIP-score filtering for multimodal data selection.

## Implementation notes
- Average EL2N scores across multiple early-epoch checkpoints.
- Compute scores efficiently in batches.
- Validate pruning on a held-out set.

## Evidence from the paper
- EL2N scores computed at early epochs identify the most informative training examples.
- 50-75% of data can be pruned with minimal performance loss.
- The approach enables 'data diets' that reduce training compute.
- EL2N is simpler and more efficient than influence functions.

## Source paper
- **Title**: EL2N: Deep Learning on a Data Diet
- **Year**: 2021
- **Venue**: NeurIPS
- **Paper ID**: arxiv-2107.07075v2
- **URL**: http://arxiv.org/abs/2107.07075v2
- **arXiv ID**: 2107.07075v2
