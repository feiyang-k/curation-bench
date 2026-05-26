# Scaling Data-Constrained Language Models

## One-line decision
Use this skill when you want to understand how to optimally train when data is limited and must be repeated, and how to trade off epochs vs model size. Avoid it when you have unlimited unique data and do not need to repeat data.

## Skill metadata
- **Skill type**: data-constrained-scaling
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Establish scaling laws for data-constrained regimes where unique data is limited and must be repeated, showing how to optimally allocate compute between model size and data repetition.

## Problem signature
- Modality: text data (principles apply to multimodal training).
- Data state: fixed-size unique data that may need to be repeated for training.
- Scale regime: varying unique data sizes with compute budgets up to 900B tokens.
- Model requirement: Any transformer LLM; principles apply to VLMs.

## Use when
- You have a fixed amount of unique training data.
- You need to decide whether to repeat data or use a smaller model.
- You want to understand diminishing returns from data repetition.

## Do not use when
- You have unlimited unique data.
- You are not constrained by data availability.
- You need task-specific rather than scaling guidance.

## Required inputs
- **unique_data**: Fixed pool of unique training data.
- **compute_budget**: Available compute for training.
- **model_size_options**: Range of model sizes to consider.

## Optional inputs
- **data_augmentation**: Methods to increase effective data diversity.

## Outputs
- **scaling_recommendations**: Optimal model size and epochs given data constraints.
- **scaling_laws**: Mathematical relationships for data-constrained scaling.

## Assumptions and prerequisites
- Data repetition has diminishing returns.
- There is an optimal trade-off between model size and data repetition.
- These scaling laws transfer across model families.

## Procedure
1. **Measure scaling with repetition**
   Action: Train models at various sizes with different amounts of data repetition.
   Why: Establishes empirical scaling curves.
   Note: See paper for details.
2. **Fit scaling laws**
   Action: Fit power law relationships to the empirical data.
   Why: Mathematical models enable extrapolation.
   Note: See paper for details.
3. **Derive optimal allocations**
   Action: Calculate optimal model size for a given compute budget and data size.
   Why: Provides actionable recommendations.
   Note: See paper for details.
4. **Validate predictions**
   Action: Verify scaling law predictions at larger scales.
   Why: Ensures extrapolation accuracy.
   Note: See paper for details.

## Parameters to set
- **unique_tokens** — Role: Amount of unique training data. How to set: Count unique tokens in your dataset. Default/range: Variable. Effect: Less unique data means more repetition needed.
- **compute_budget** — Role: Total compute available. How to set: Measured in FLOPs or GPU-hours. Default/range: Variable. Effect: Larger budgets enable larger models.
- **max_epochs** — Role: Maximum data repetitions. How to set: 4-16 epochs before severe diminishing returns. Default/range: 4-16. Effect: Beyond 4 epochs, returns diminish significantly.

## Validation checks
- Scaling law predictions should match empirical results.
- Diminishing returns from repetition should be quantified.
- Recommendations should generalize across model sizes.

## Failure modes
- Scaling laws may not hold for very small or very large data.
- Data quality may interact with repetition effects.
- The laws may not transfer perfectly to multimodal data.

## Adaptation notes for VLM training
- Apply data-constrained scaling laws to VLM pretraining data budgets.
- These insights guide decisions about data collection vs. model scaling.
- Relevant for VLM domains with limited paired data (medical, scientific).

## Implementation notes
- Use the paper's scaling formulas for compute-optimal training.
- Monitor validation loss across epochs for diminishing returns.
- Consider data augmentation as a way to increase effective uniqueness.

## Evidence from the paper
- Training with up to 4 epochs of repeated data causes minimal degradation.
- Beyond 4-16 epochs, significant diminishing returns occur.
- The optimal strategy allocates excess compute to model size rather than more epochs.
- These scaling laws provide actionable guidance for data-constrained training.

## Source paper
- **Title**: Scaling Data-Constrained Language Models
- **Year**: 2023
- **Venue**: NeurIPS
- **Paper ID**: arxiv-2305.16264v3
- **URL**: http://arxiv.org/abs/2305.16264v3
- **arXiv ID**: 2305.16264v3
