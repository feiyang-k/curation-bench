# Are More LLM Calls All You Need? Towards Scaling Laws for Compound AI Systems

## One-line decision
Use this skill when you want to understand scaling behavior when using multiple LLM calls in compound systems for tasks like data generation or evaluation. Avoid it when you use single LLM calls and do not build compound systems.

## Skill metadata
- **Skill type**: compound-system-scaling
- **Paper kind**: operational-method
- **Actionability**: medium
- **Evidence quality**: full_paper

## Goal
Study scaling laws for compound AI systems that use multiple LLM calls, understanding when more calls improve quality and when they hit diminishing returns.

## Problem signature
- Modality: any task processed by compound LLM systems.
- Data state: tasks processed with varying numbers of LLM calls.
- Scale regime: 1 to hundreds of LLM calls per task.
- Model requirement: Any LLM used in compound system configurations.

## Use when
- You build systems that make multiple LLM calls.
- You want to understand scaling of compound AI systems.
- You need to optimize the number of LLM calls.

## Do not use when
- You use single LLM calls.
- Scaling analysis is not relevant.
- You have a fixed, non-compound pipeline.

## Required inputs
- **compound_system**: System making multiple LLM calls per task.
- **task_suite**: Tasks for evaluating compound system performance.
- **call_budget**: Budget of LLM calls to study scaling.

## Optional inputs
- **aggregation_strategy**: Strategy for combining multiple LLM outputs.

## Outputs
- **scaling_analysis**: How performance scales with number of calls.
- **optimal_calls**: Recommended number of calls for different tasks.

## Assumptions and prerequisites
- More LLM calls can improve quality up to a point.
- Diminishing returns eventually set in.
- The optimal number of calls varies by task.

## Procedure
1. **Define compound system**
   Action: Design a system that uses multiple LLM calls per task.
   Why: Multiple calls enable voting, refinement, or parallel processing.
   Note: See paper for details.
2. **Vary number of calls**
   Action: Run the system with different numbers of LLM calls.
   Why: Maps the performance-cost tradeoff.
   Note: See paper for details.
3. **Analyze scaling behavior**
   Action: Fit scaling curves to the results.
   Why: Identifies optimal call counts and diminishing returns.
   Note: See paper for details.
4. **Recommend configurations**
   Action: Determine the optimal number of calls per task type.
   Why: Provides actionable guidance for compound system design.
   Note: See paper for details.

## Parameters to set
- **max_calls** — Role: Maximum LLM calls to test. How to set: Up to hundreds per task. Default/range: 1-100. Effect: Shows scaling and saturation behavior.
- **aggregation** — Role: How to combine multiple outputs. How to set: Majority voting, best-of-n, or refinement. Default/range: Task-dependent. Effect: Aggregation strategy affects scaling behavior.

## Validation checks
- Performance should improve with more calls (up to a point).
- Diminishing returns should be quantifiable.
- Optimal call counts should be task-dependent.

## Failure modes
- More calls increase cost without proportional benefit.
- Poor aggregation may not improve with more calls.
- The analysis may not generalize across models.

## Adaptation notes for VLM training
- Apply compound scaling to VLM data generation pipelines.
- Understand when more generation calls improve synthetic data quality.
- Optimize the cost-quality tradeoff in data generation.

## Implementation notes
- Track quality at each call count.
- Plot scaling curves for visual analysis.
- Compare different aggregation strategies.

## Evidence from the paper
- Compound AI systems show diminishing returns with more LLM calls.
- The optimal number of calls varies by task complexity.
- Aggregation strategy significantly affects scaling behavior.
- Understanding compound scaling helps optimize data generation pipelines.

## Source paper
- **Title**: Are More LLM Calls All You Need? Towards Scaling Laws for Compound AI Systems
- **Year**: 2024
- **Venue**: arXiv
- **Paper ID**: arxiv-2403.02419v2
- **URL**: http://arxiv.org/abs/2403.02419v2
- **arXiv ID**: 2403.02419v2
