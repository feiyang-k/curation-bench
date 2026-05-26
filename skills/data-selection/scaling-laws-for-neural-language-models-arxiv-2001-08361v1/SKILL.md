# Scaling Laws for Neural Language Models

## One-line decision
Use this skill when you want to understand power-law relationships between model size, data size, and compute for optimal resource allocation. Avoid it when you are not making scaling decisions.

## Skill metadata
- **Skill type**: neural-scaling-laws
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Establish power-law scaling relationships between language model performance and three factors: model size, dataset size, and compute budget, providing guidance for optimal resource allocation.

## Problem signature
- Modality: text data scaling analysis; principles apply to multimodal.
- Data state: training data at various scales for scaling studies.
- Scale regime: millions to billions of tokens.
- Model requirement: Transformer models at various scales.

## Use when
- You are making scaling decisions about data vs model size.
- You want to predict performance at larger scales.
- You need to optimize resource allocation.

## Do not use when
- You are not making scaling decisions.
- Your task does not follow power-law scaling.
- You have fixed resources without flexibility.

## Required inputs
- **training_data**: Data at various scales.
- **model_variants**: Models at multiple sizes.
- **compute_budget**: Available compute for scaling studies.

## Optional inputs
- **downstream_tasks**: Tasks for evaluating scaling predictions.

## Outputs
- **scaling_laws**: Power-law relationships between performance and resources.
- **optimal_allocation**: Recommended split between model size and data.

## Assumptions and prerequisites
- Performance follows power-law relationships with scale.
- Scaling laws are consistent across model families.
- Small-scale experiments predict large-scale behavior.

## Procedure
1. **Train at multiple scales**
   Action: Train models at various data and model sizes.
   Why: Empirical data for fitting scaling laws.
   Note: See paper for details.
2. **Fit power laws**
   Action: Fit power-law functions to the results.
   Why: Mathematical relationships enable prediction.
   Note: See paper for details.
3. **Derive compute-optimal allocation**
   Action: Find the optimal model/data split for a given compute budget.
   Why: Optimizes resource allocation.
   Note: See paper for details.
4. **Validate at larger scale**
   Action: Verify predictions hold at larger scales.
   Why: Ensures extrapolation accuracy.
   Note: See paper for details.

## Parameters to set
- **model_range** — Role: Range of model sizes tested. How to set: 6 orders of magnitude. Default/range: 1M-1B parameters. Effect: Wider range improves law accuracy.
- **data_range** — Role: Range of data sizes tested. How to set: 3 orders of magnitude. Default/range: 1M-1B tokens. Effect: Wider range captures scaling behavior.

## Validation checks
- Power laws should fit the empirical data well.
- Predictions should hold at larger scales.
- Compute-optimal allocations should improve efficiency.

## Failure modes
- Scaling laws may break at very large scales.
- Different architectures may have different laws.
- Quality-dependent effects may not be captured.

## Adaptation notes for VLM training
- Scaling laws guide VLM data collection and model sizing decisions.
- Apply to multimodal scaling: vision encoder, LLM, and data.
- Consider data quality effects on scaling (Chinchilla, D4).

## Implementation notes
- Use logarithmic axes for power-law fitting.
- Run experiments at cleanly separated scales.
- Report confidence intervals on scaling law parameters.

## Evidence from the paper
- Performance follows power-law relationships with model size, data size, and compute.
- Scaling laws enable accurate prediction of performance at larger scales.
- Compute-optimal allocation splits resources between model and data size.
- These laws have shaped the development of modern LLMs and VLMs.

## Source paper
- **Title**: Scaling Laws for Neural Language Models
- **Year**: 2020
- **Venue**: arXiv
- **Paper ID**: arxiv-2001.08361v1
- **URL**: http://arxiv.org/abs/2001.08361v1
- **arXiv ID**: 2001.08361v1
