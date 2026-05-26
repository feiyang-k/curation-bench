# Curriculum Learning

## One-line decision
Use this skill when you want to order training examples from easy to hard during training to improve convergence and final performance. Avoid it when random data ordering works well for your task.

## Skill metadata
- **Skill type**: curriculum-data-ordering
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Order training examples from easy to hard during training, mimicking human curriculum-based learning, to improve convergence speed and potentially final model performance.

## Problem signature
- Modality: any modality; the principle is general.
- Data state: training data ordered by difficulty for curriculum-based training.
- Scale regime: any dataset size.
- Model requirement: Any model; curriculum is a training strategy.

## Use when
- You want to improve training convergence.
- Your data has meaningful difficulty variation.
- Easy-to-hard ordering is feasible.

## Do not use when
- Random ordering works well for your task.
- You cannot define a meaningful difficulty ordering.
- Your data has uniform difficulty.

## Required inputs
- **training_data**: Dataset with definable difficulty levels.
- **difficulty_measure**: Metric for ordering examples by difficulty.
- **training_schedule**: Schedule for introducing harder examples.

## Optional inputs
- **anti_curriculum**: Reversed ordering for comparison.

## Outputs
- **curriculum_schedule**: Training schedule with difficulty ordering.
- **improved_model**: Model trained with curriculum learning.

## Assumptions and prerequisites
- Easy-to-hard ordering improves learning.
- Difficulty can be meaningfully defined.
- Curriculum learning mimics effective human learning.

## Procedure
1. **Define difficulty measure**
   Action: Choose a metric for ranking example difficulty.
   Why: Difficulty ordering is the key to curriculum learning.
   Note: See paper for details.
2. **Sort examples by difficulty**
   Action: Order training data from easy to hard.
   Why: Progressive difficulty improves learning.
   Note: See paper for details.
3. **Train with progressive introduction**
   Action: Start with easy examples and progressively add harder ones.
   Why: Easy examples provide a foundation for harder learning.
   Note: See paper for details.
4. **Compare to random ordering**
   Action: Benchmark against random and anti-curriculum ordering.
   Why: Validates the curriculum benefit.
   Note: See paper for details.

## Parameters to set
- **difficulty_metric** — Role: How to measure example difficulty. How to set: Use loss, confidence, or domain-specific metrics. Default/range: Task-dependent. Effect: The metric defines the curriculum.
- **pacing_function** — Role: How quickly to introduce harder examples. How to set: Linear, exponential, or step-based pacing. Default/range: Linear. Effect: Faster pacing reaches full data sooner.

## Validation checks
- Curriculum should converge faster than random ordering.
- Final performance should match or exceed random ordering.
- The difficulty metric should meaningfully order examples.

## Failure modes
- Some tasks may not benefit from curriculum ordering.
- Poor difficulty metrics produce bad curricula.
- Anti-curriculum (hard-first) sometimes works better.

## Adaptation notes for VLM training
- Apply curriculum learning to VLM training (easy then complex instructions).
- Use CLIP scores or LLM complexity as difficulty metrics for VLM data.
- Combine with data selection for curriculum + selection benefits.

## Implementation notes
- Implement curriculum in the data sampler.
- Track training loss for curriculum progression analysis.
- Compare multiple difficulty metrics.

## Evidence from the paper
- Curriculum learning improves convergence speed on multiple tasks.
- Easy-to-hard ordering mimics effective human learning.
- The principle applies across modalities and architectures.
- Curriculum learning has been rediscovered in many forms for LLM and VLM training.

## Source paper
- **Title**: Curriculum Learning
- **Year**: 2009
- **Venue**: ICML
- **Paper ID**: crossref-icml-2009-curriculum
- **URL**: https://dl.acm.org/doi/10.1145/1553374.1553380
- **arXiv ID**: N/A
