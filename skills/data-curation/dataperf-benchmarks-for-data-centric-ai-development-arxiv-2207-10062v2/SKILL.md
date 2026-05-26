# DataPerf: Benchmarks for Data-Centric AI Development

## One-line decision
Use this skill when you need benchmarks for evaluating data-centric AI tasks including data selection, labeling, and slice discovery. Avoid it when you need model-centric benchmarks rather than data-centric ones.

## Skill metadata
- **Skill type**: data-centric-benchmarks
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Provide standardized benchmarks for evaluating data-centric AI tasks, shifting focus from model improvement to data improvement as the variable under study.

## Problem signature
- Modality: various benchmarks across data-centric tasks.
- Data state: benchmark tasks where data quality is the variable.
- Scale regime: benchmark-specific scales.
- Model requirement: Fixed models with variable data for benchmarking.

## Use when
- You want to benchmark data-centric methods.
- You need standardized evaluation for data quality techniques.
- You want to participate in data-centric competitions.

## Do not use when
- You need model-centric benchmarks.
- You have your own evaluation methodology.
- Data-centric evaluation is not your focus.

## Required inputs
- **benchmark_tasks**: DataPerf benchmark task definitions.
- **fixed_models**: Fixed model architectures for fair comparison.
- **data_strategies**: Data curation strategies to evaluate.

## Optional inputs
- **leaderboard**: Competition leaderboard for comparing strategies.

## Outputs
- **benchmark_scores**: Scores on DataPerf benchmark tasks.
- **data_strategy_comparison**: Comparison of data curation strategies.

## Assumptions and prerequisites
- Data quality improvements can be benchmarked like model improvements.
- Fixed models ensure data is the variable.
- Standardized benchmarks enable fair comparison.

## Procedure
1. **Select benchmark tasks**
   Action: Choose from DataPerf's data-centric benchmark tasks.
   Why: Standardized tasks enable comparison.
   Note: See paper for details.
2. **Apply data strategies**
   Action: Apply different data curation strategies to the benchmark data.
   Why: The strategy is the variable under study.
   Note: See paper for details.
3. **Train with fixed models**
   Action: Train fixed models on the curated data.
   Why: Fixed models ensure differences are data-driven.
   Note: See paper for details.
4. **Evaluate and compare**
   Action: Compare strategies on the benchmark metrics.
   Why: Standardized evaluation enables fair comparison.
   Note: See paper for details.

## Parameters to set
- **benchmark_type** — Role: Type of data-centric task. How to set: Choose from selection, labeling, slice discovery. Default/range: Multiple types. Effect: Different benchmarks test different data skills.

## Validation checks
- Data strategies should measurably improve over baselines.
- Results should be reproducible.
- The benchmark should discriminate between strategies.

## Failure modes
- Benchmarks may not capture all dimensions of data quality.
- Fixed models may favor certain data strategies.
- Benchmark-specific tuning may not generalize.

## Adaptation notes for VLM training
- DataPerf provides a template for benchmarking VLM data curation.
- Apply data-centric benchmarking to multimodal data strategies.
- Use the benchmark methodology for internal data quality evaluation.

## Implementation notes
- Use DataPerf's provided infrastructure.
- Submit to leaderboards for comparison.
- Document strategies for reproducibility.

## Evidence from the paper
- DataPerf provides standardized benchmarks for data-centric AI tasks.
- The benchmarks cover data selection, labeling, and slice discovery.
- Fixed models ensure data quality is the variable under study.
- DataPerf has driven innovation in data-centric techniques.

## Source paper
- **Title**: DataPerf: Benchmarks for Data-Centric AI Development
- **Year**: 2023
- **Venue**: NeurIPS
- **Paper ID**: arxiv-2207.10062v2
- **URL**: http://arxiv.org/abs/2207.10062v2
- **arXiv ID**: 2207.10062v2
