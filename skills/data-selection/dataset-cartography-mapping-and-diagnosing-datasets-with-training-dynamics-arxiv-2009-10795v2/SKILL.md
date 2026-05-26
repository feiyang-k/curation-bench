# Dataset Cartography: Mapping and Diagnosing Datasets with Training Dynamics

## One-line decision
Use this skill when you want to map training examples as easy, ambiguous, or hard based on training dynamics (confidence, variability) for data selection. Avoid it when you cannot afford to train a model first to compute training dynamics.

## Skill metadata
- **Skill type**: training-dynamics-analysis
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Map training examples into easy, ambiguous, and hard regions based on training dynamics (confidence and variability across epochs), enabling targeted data selection and curriculum learning.

## Problem signature
- Modality: any modality; applied to text classification and NLI.
- Data state: training data with per-example confidence and variability tracked across epochs.
- Scale regime: standard dataset sizes (10K-500K examples).
- Model requirement: Any model trained for multiple epochs to compute training dynamics.

## Use when
- You want to understand which training examples are easy, ambiguous, or hard.
- You can train a model for multiple epochs to compute dynamics.
- You want to select examples for curriculum learning or debugging.

## Do not use when
- You cannot afford to train a model for dynamics computation.
- Your dataset is too large for per-example tracking.
- You need a one-pass selection method.

## Required inputs
- **training_data**: Dataset to analyze.
- **training_model**: Model trained for multiple epochs with per-example predictions logged.
- **dynamics_computer**: Code to compute confidence and variability from training logs.

## Optional inputs
- **selection_strategy**: Strategy for selecting examples based on their map region.

## Outputs
- **dataset_map**: Visualization mapping examples to easy/ambiguous/hard regions.
- **selected_subset**: Subset of examples selected based on map regions.

## Assumptions and prerequisites
- Training dynamics reveal intrinsic properties of examples.
- Easy examples are learned quickly and consistently; hard examples are never learned; ambiguous examples show high variability.
- Ambiguous examples are often most valuable for training.

## Procedure
1. **Train with per-example logging**
   Action: Train a model for multiple epochs, logging per-example predictions at each epoch.
   Why: Training dynamics require multi-epoch prediction histories.
   Note: See paper for details.
2. **Compute confidence and variability**
   Action: Calculate mean confidence and prediction variability for each example across epochs.
   Why: These metrics define the dataset map coordinates.
   Note: See paper for details.
3. **Map examples to regions**
   Action: Plot examples on the confidence-variability map and identify easy/ambiguous/hard regions.
   Why: The map reveals dataset composition and potential issues.
   Note: See paper for details.
4. **Select based on map**
   Action: Choose examples from specific regions for training (e.g., ambiguous examples).
   Why: Targeted selection can improve training efficiency.
   Note: See paper for details.

## Parameters to set
- **num_epochs_for_dynamics** — Role: Epochs to train for dynamics computation. How to set: 3-5 epochs capture stable dynamics. Default/range: 3-5. Effect: More epochs provide more stable dynamics.
- **confidence_threshold** — Role: Threshold for easy vs. hard classification. How to set: Tune based on map distribution. Default/range: 0.5-0.9. Effect: Separates confidently learned from struggling examples.
- **variability_threshold** — Role: Threshold for ambiguous classification. How to set: High variability indicates ambiguity. Default/range: Dataset-dependent. Effect: Identifies examples the model is uncertain about.

## Validation checks
- Easy examples should be learned quickly and consistently.
- Hard examples should remain incorrectly classified throughout training.
- Training on ambiguous examples should improve over training on easy ones.

## Failure modes
- Dynamics computation requires full training, which is expensive.
- The map may not be stable across different model initializations.
- Hard examples may be mislabeled rather than genuinely difficult.

## Adaptation notes for VLM training
- Apply dataset cartography to VLM instruction tuning data.
- Use dynamics to identify mislabeled or ambiguous image-text pairs.
- Select challenging examples for targeted VLM improvement.

## Implementation notes
- Log predictions at every epoch for dynamics computation.
- Use the 2D map for visual diagnosis of data quality.
- Implement efficient per-example tracking for large datasets.

## Evidence from the paper
- Dataset cartography maps examples into easy, ambiguous, and hard regions based on training dynamics.
- Training on ambiguous examples is more valuable than training on easy or hard ones.
- The approach reveals mislabeled examples and dataset artifacts.
- Data maps provide actionable insights for dataset curation and selection.

## Source paper
- **Title**: Dataset Cartography: Mapping and Diagnosing Datasets with Training Dynamics
- **Year**: 2020
- **Venue**: EMNLP
- **Paper ID**: arxiv-2009.10795v2
- **URL**: http://arxiv.org/abs/2009.10795v2
- **arXiv ID**: 2009.10795v2
