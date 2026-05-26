# Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance

## One-line decision
Use this skill when you want to predict LLM performance from data mixing ratios and optimize the mix without expensive full-scale training. Avoid it when you have a single data source or cannot run ablation experiments.

## Skill metadata
- **Skill type**: data-mixing-optimization
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Derive mathematical laws that predict language model performance as a function of data mixing ratios, enabling optimization of data mixes without expensive full-scale training runs.

## Problem signature
- Modality: text data from multiple sources with different mixing ratios.
- Data state: multiple data sources with configurable mixing ratios for pretraining.
- Scale regime: experiments from 1B to 100B+ tokens.
- Model requirement: Any transformer LLM for ablation experiments.

## Use when
- You have multiple data sources and need to optimize mixing ratios.
- You want to predict performance without training at full scale.
- You need principled guidance for data recipe design.

## Do not use when
- You have a single data source.
- You cannot run small-scale ablation experiments.
- Your data sources are not cleanly separable.

## Required inputs
- **data_sources**: Multiple text data sources with independent mixing controls.
- **ablation_budget**: Compute for running small-scale mixing experiments.
- **performance_metric**: Target metric for optimization (perplexity, downstream accuracy).

## Optional inputs
- **constraint_set**: Constraints on minimum/maximum ratios per source.

## Outputs
- **mixing_law**: Mathematical function predicting performance from mixing ratios.
- **optimal_mix**: Optimized mixing ratios for maximum performance.

## Assumptions and prerequisites
- Performance is a smooth function of mixing ratios.
- Small-scale experiments predict full-scale performance.
- The optimal mix can be found mathematically.

## Procedure
1. **Design mixing experiments**
   Action: Choose a set of mixing ratio configurations to test.
   Why: Experiments sample the mixing ratio space.
   Note: See paper for details.
2. **Run small-scale ablations**
   Action: Train small models at each configuration and measure performance.
   Why: Small-scale runs are cheap and informative.
   Note: See paper for details.
3. **Fit mixing law**
   Action: Fit a mathematical function to the ablation results.
   Why: The law enables prediction without training.
   Note: See paper for details.
4. **Optimize mixing ratios**
   Action: Find the mixing ratios that maximize predicted performance.
   Why: Optimization identifies the best data recipe.
   Note: See paper for details.
5. **Validate at full scale**
   Action: Train a full-scale model with the optimized mix.
   Why: Confirms that the prediction holds at scale.
   Note: See paper for details.

## Parameters to set
- **num_experiments** — Role: Number of mixing configurations to test. How to set: 10-50 configurations for good coverage. Default/range: 20-50. Effect: More experiments improve law accuracy.
- **ablation_scale** — Role: Size of ablation models. How to set: 1/10th to 1/100th of target scale. Default/range: 1B tokens. Effect: Larger ablations are more predictive but more expensive.
- **optimization_objective** — Role: What to optimize (perplexity, accuracy, etc.). How to set: Choose the most relevant downstream metric. Default/range: Perplexity. Effect: Different objectives may yield different optimal mixes.

## Validation checks
- The mixing law should accurately predict held-out experiments.
- The optimized mix should outperform uniform mixing.
- Full-scale results should match predictions.

## Failure modes
- The mixing law may not capture complex interactions between sources.
- Small-scale predictions may not transfer perfectly to full scale.
- The optimal mix may be sensitive to the performance metric.

## Adaptation notes for VLM training
- Apply mixing laws to VLM data recipes (image-text, interleaved, text-only).
- Optimize the ratio of pretraining data types for multimodal models.
- Use mixing laws for instruction tuning data recipe optimization.

## Implementation notes
- Use Latin hypercube or random sampling for mixing configurations.
- Fit polynomial or exponential mixing functions.
- Validate predictions on at least 5 held-out configurations.

## Evidence from the paper
- Data mixing laws accurately predict LLM performance from mixing ratios.
- Optimized mixes outperform uniform mixing by meaningful margins.
- Small-scale experiments (1B tokens) predict full-scale results.
- The approach provides principled guidance for data recipe design.

## Source paper
- **Title**: Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance
- **Year**: 2024
- **Venue**: arXiv
- **Paper ID**: arxiv-2403.16952v2
- **URL**: http://arxiv.org/abs/2403.16952v2
- **arXiv ID**: 2403.16952v2
