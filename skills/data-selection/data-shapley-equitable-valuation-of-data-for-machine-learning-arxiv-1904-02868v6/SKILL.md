# Data Shapley: Equitable Valuation of Data for Machine Learning

## One-line decision
Use this skill when you want to assign fair value to individual training examples based on their marginal contribution using Shapley value theory. Avoid it when you cannot afford the computational cost of data Shapley estimation.

## Skill metadata
- **Skill type**: cooperative-data-valuation
- **Paper kind**: operational-method
- **Actionability**: medium
- **Evidence quality**: full_paper

## Goal
Assign equitable values to individual training examples based on their marginal contribution to model performance using Shapley value theory from cooperative game theory.

## Problem signature
- Modality: any modality; the framework is general.
- Data state: training data where per-example value needs to be estimated.
- Scale regime: thousands to tens of thousands of examples (compute-intensive).
- Model requirement: Any differentiable model; retraining required for Shapley estimation.

## Use when
- You want a theoretically grounded value for each training example.
- You need to identify high-value and low-value training data.
- Fairness in data valuation matters (e.g., for data markets).

## Do not use when
- You have too many training examples for Shapley estimation.
- Simple quality heuristics suffice for your needs.
- You cannot afford the retraining cost.

## Required inputs
- **training_data**: Dataset to compute Shapley values for.
- **model**: Model that can be retrained on subsets.
- **performance_metric**: Metric for measuring model performance (accuracy, loss, etc.).

## Optional inputs
- **approximation_method**: Monte Carlo or KNN approximation for scalability.

## Outputs
- **data_shapley_values**: Per-example Shapley values.
- **data_ranking**: Ranking of examples by value.

## Assumptions and prerequisites
- Shapley values provide fair, unique data valuation.
- Marginal contribution captures example value.
- Approximation methods make computation tractable.

## Procedure
1. **Define performance metric**
   Action: Choose the model performance metric for value computation.
   Why: The metric defines what 'valuable' means.
   Note: See paper for details.
2. **Estimate Shapley values**
   Action: Use Monte Carlo or KNN approximation to estimate per-example values.
   Why: Exact computation is infeasible; approximation is necessary.
   Note: See paper for details.
3. **Rank examples by value**
   Action: Sort training examples by their Shapley value.
   Why: Ranking enables data selection and debugging.
   Note: See paper for details.
4. **Validate valuation**
   Action: Verify that removing low-value examples doesn't hurt performance.
   Why: Confirms the valuation is meaningful.
   Note: See paper for details.

## Parameters to set
- **num_permutations** — Role: Monte Carlo samples for Shapley estimation. How to set: More permutations improve accuracy. Default/range: 1000-10000. Effect: More permutations improve estimation accuracy.
- **approximation_method** — Role: Method for efficient Shapley computation. How to set: KNN-Shapley or TMC-Shapley. Default/range: TMC-Shapley. Effect: Different methods trade accuracy for speed.

## Validation checks
- Removing low-Shapley-value examples should not degrade performance.
- High-value examples should be informative for the task.
- The valuation should be stable across different approximation runs.

## Failure modes
- Computation is expensive even with approximation.
- Shapley values may not be stable with few permutations.
- The valuation depends on the specific model and metric.

## Adaptation notes for VLM training
- Apply Data Shapley to VLM training data valuation.
- Use Shapley values to identify the most valuable image-text pairs.
- Combine with TRAK or influence functions for scalable alternatives.

## Implementation notes
- Use efficient implementations (OpenDataVal, pyDVL).
- Start with a small subset for feasibility assessment.
- Compare Shapley-selected data to random baselines.

## Evidence from the paper
- Data Shapley provides theoretically fair data valuation using cooperative game theory.
- The approach identifies mislabeled and low-value training examples.
- Monte Carlo and KNN approximations make computation tractable.
- Data selection based on Shapley values improves model efficiency.

## Source paper
- **Title**: Data Shapley: Equitable Valuation of Data for Machine Learning
- **Year**: 2019
- **Venue**: ICML
- **Paper ID**: arxiv-1904.02868v6
- **URL**: http://arxiv.org/abs/1904.02868v6
- **arXiv ID**: 1904.02868v6
