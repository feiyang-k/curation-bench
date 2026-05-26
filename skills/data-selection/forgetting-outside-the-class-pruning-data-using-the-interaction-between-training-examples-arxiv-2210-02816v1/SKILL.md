# Forgetting Outside the Class: Pruning Data Using the Interaction Between Training Examples

## One-line decision
Use this skill when you want to prune training data by identifying examples that are frequently forgotten during training, using forgetting events as a data quality signal. Avoid it when you cannot train a model first to measure forgetting events.

## Skill metadata
- **Skill type**: forgetting-based-pruning
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Prune training data by tracking forgetting events — transitions from correct to incorrect prediction during training — identifying examples that interact beneficially or detrimentally with the training process.

## Problem signature
- Modality: any modality; demonstrated on image classification.
- Data state: training data with per-example forgetting statistics from initial training.
- Scale regime: standard dataset sizes (10K-1M+ examples).
- Model requirement: Any model trained for multiple epochs with per-example tracking.

## Use when
- You want to identify dispensable training examples.
- You can train a model and track per-example predictions.
- You want data-efficient training through pruning.

## Do not use when
- You cannot afford initial training for forgetting statistics.
- Your dataset is too large for per-example tracking.
- All data is equally important.

## Required inputs
- **training_data**: Dataset to prune.
- **training_model**: Model trained for multiple epochs with per-example tracking.
- **forgetting_tracker**: Code to track correct-to-incorrect transitions.

## Optional inputs
- **pruning_fraction**: Fraction of data to prune.

## Outputs
- **forgetting_statistics**: Per-example forgetting event counts.
- **pruned_dataset**: Dataset with dispensable examples removed.

## Assumptions and prerequisites
- Examples that are never forgotten are easy and potentially redundant.
- Frequently forgotten examples may be noisy or mislabeled.
- Forgetting events reveal training dynamics useful for pruning.

## Procedure
1. **Train with per-example tracking**
   Action: Train a model and track whether each example is correctly or incorrectly predicted at each epoch.
   Why: Forgetting events are transitions from correct to incorrect.
   Note: See paper for details.
2. **Count forgetting events**
   Action: For each example, count the number of forgetting events during training.
   Why: Forgetting counts characterize example difficulty.
   Note: See paper for details.
3. **Identify dispensable examples**
   Action: Examples never forgotten are candidates for pruning.
   Why: Never-forgotten examples may be redundant.
   Note: See paper for details.
4. **Prune and retrain**
   Action: Remove dispensable examples and retrain.
   Why: Validates that pruning maintains performance.
   Note: See paper for details.

## Parameters to set
- **num_epochs_tracking** — Role: Epochs for tracking forgetting. How to set: Full training duration. Default/range: Full training. Effect: More epochs capture more forgetting events.
- **pruning_strategy** — Role: How to select examples for pruning. How to set: Remove never-forgotten examples first. Default/range: Never-forgotten. Effect: Removes redundant easy examples.

## Validation checks
- Pruning never-forgotten examples should maintain performance.
- Frequently forgotten examples should be examined for mislabeling.
- The pruned dataset should be more efficient for training.

## Failure modes
- Forgetting computation requires full training.
- Some never-forgotten examples may be important for rare classes.
- The method is not applicable before initial training.

## Adaptation notes for VLM training
- Apply forgetting-based pruning to VLM instruction tuning data.
- Use forgetting events to identify low-quality image-text pairs.
- Combine with other data selection methods for comprehensive pruning.

## Implementation notes
- Track per-example predictions at every epoch.
- Store forgetting statistics for analysis.
- Visualize forgetting distributions for insights.

## Evidence from the paper
- Examples that are never forgotten during training can be removed without performance loss.
- Forgetting events identify mislabeled and noisy examples.
- The approach enables significant data reduction with minimal performance impact.
- Forgetting-based pruning is complementary to other data selection methods.

## Source paper
- **Title**: Forgetting Outside the Class: Pruning Data Using the Interaction Between Training Examples
- **Year**: 2022
- **Venue**: NeurIPS
- **Paper ID**: arxiv-2210.02816v1
- **URL**: http://arxiv.org/abs/2210.02816v1
- **arXiv ID**: 2210.02816v1
