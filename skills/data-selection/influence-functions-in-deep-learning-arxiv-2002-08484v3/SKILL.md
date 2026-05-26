# Influence Functions in Deep Learning

## One-line decision
Use this skill when you want to estimate the influence of individual training examples on model predictions for data debugging and selection. Avoid it when you cannot afford the compute for influence estimation or have too many training examples.

## Skill metadata
- **Skill type**: influence-based-data-valuation
- **Paper kind**: operational-method
- **Actionability**: medium
- **Evidence quality**: full_paper

## Goal
Use influence functions to estimate the effect of individual training examples on model predictions, enabling data debugging, mislabel detection, and targeted data selection.

## Problem signature
- Modality: any modality; applicable to image-text data.
- Data state: training data where per-example influence on predictions needs to be estimated.
- Scale regime: thousands to millions of examples (compute-intensive beyond that).
- Model requirement: Differentiable model with accessible gradients.

## Use when
- You want to identify which training examples most affect specific predictions.
- You need to detect mislabeled or harmful training examples.
- You want influence-based data selection for targeted improvement.

## Do not use when
- You have too many training examples for tractable influence computation.
- You need a simple, fast data selection method.
- Your model is not differentiable or gradients are unavailable.

## Required inputs
- **training_data**: Training dataset with per-example gradient access.
- **trained_model**: Model trained on the data with stored gradients or checkpoints.
- **target_predictions**: Specific predictions or loss values to trace influences to.

## Optional inputs
- **approximation_method**: Efficient approximation for scaling (e.g., Arnoldi, EK-FAC).

## Outputs
- **influence_scores**: Per-example influence scores for each training example.
- **influential_examples**: Ranked list of most influential training examples.

## Assumptions and prerequisites
- Influence functions approximate leave-one-out retraining.
- Per-example influences provide actionable insights for data curation.
- Approximations make influence estimation tractable.

## Procedure
1. **Train model and store checkpoints**
   Action: Train the model and store necessary gradients or checkpoints.
   Why: Influence computation requires gradient information.
   Note: See paper for details.
2. **Compute per-example gradients**
   Action: Calculate gradients for each training example.
   Why: Gradients are the basis for influence estimation.
   Note: See paper for details.
3. **Estimate influence scores**
   Action: Use the influence function formula with Hessian approximation.
   Why: Estimates the effect of each example on target predictions.
   Note: See paper for details.
4. **Analyze influential examples**
   Action: Examine the most positively and negatively influential examples.
   Why: Reveals data quality issues and important training patterns.
   Note: See paper for details.

## Parameters to set
- **approximation_method** — Role: Method for approximating the Hessian inverse. How to set: Use Arnoldi iteration or EK-FAC for scalability. Default/range: Arnoldi. Effect: Better approximations improve accuracy but increase compute.
- **target_set** — Role: Which predictions to compute influence for. How to set: Choose validation errors or specific failure cases. Default/range: Validation set. Effect: Different targets reveal different influential examples.

## Validation checks
- Removing high-influence negative examples should improve predictions.
- Mislabeled examples should have high negative influence.
- Influence estimates should correlate with leave-one-out retraining.

## Failure modes
- Influence computation is expensive for large datasets.
- Hessian approximations may be inaccurate.
- Non-convex loss landscapes may make influence estimates unreliable.

## Adaptation notes for VLM training
- Apply influence functions to debug VLM training data.
- Identify image-text pairs that harm specific benchmark performance.
- Use influence scores for targeted data selection in VLM fine-tuning.

## Implementation notes
- Use efficient influence implementations (e.g., FastIF, TRAK).
- Start with a small target set for tractable computation.
- Compare influence-selected data to random baselines.

## Evidence from the paper
- Influence functions identify training examples most responsible for specific predictions.
- The approach enables data debugging by finding mislabeled or harmful examples.
- Approximation methods make influence estimation tractable for deep learning.
- Influence-based data selection can improve targeted model performance.

## Source paper
- **Title**: Influence Functions in Deep Learning
- **Year**: 2020
- **Venue**: ICML
- **Paper ID**: arxiv-2002.08484v3
- **URL**: http://arxiv.org/abs/2002.08484v3
- **arXiv ID**: 2002.08484v3
