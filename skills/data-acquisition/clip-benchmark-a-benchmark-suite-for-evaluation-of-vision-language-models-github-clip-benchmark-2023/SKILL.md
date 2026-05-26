# CLIP-Benchmark: A Benchmark Suite for Evaluation of Vision-Language Models

## One-line decision
Use this skill when you need a standardized benchmark suite for evaluating CLIP-style vision-language encoders across dozens of datasets. Avoid it when you only evaluate on ImageNet zero-shot.

## Skill metadata
- **Skill type**: clip-evaluation-suite
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Provide a standardized benchmark suite for evaluating CLIP-style vision-language encoders across dozens of zero-shot classification and retrieval datasets.

## Problem signature
- Modality: evaluation suite for CLIP-style encoders.
- Data state: dozens of evaluation datasets for zero-shot and retrieval.
- Scale regime: comprehensive evaluation benchmark.
- Model requirement: Any CLIP-style dual encoder.

## Use when
- You train CLIP-style encoders and need comprehensive evaluation.
- You want standardized comparison across models.
- You need more than ImageNet zero-shot evaluation.

## Do not use when
- ImageNet-only evaluation is sufficient.
- You are not training CLIP-style models.
- You have custom evaluation needs.

## Required inputs
- **clip_model**: CLIP-style encoder to evaluate.
- **benchmark_suite**: CLIP-Benchmark evaluation datasets.
- **evaluation_code**: Standardized evaluation code.

## Optional inputs
- **custom_datasets**: Additional evaluation datasets.

## Outputs
- **benchmark_results**: Comprehensive evaluation across dozens of datasets.
- **model_comparison**: Comparison with other CLIP models.

## Assumptions and prerequisites
- Comprehensive evaluation reveals more than single-dataset testing.
- Standardized evaluation enables fair model comparison.
- Multiple datasets test different capabilities.

## Procedure
1. **Configure evaluation**
   Action: Select evaluation datasets and metrics.
   Why: Flexible configuration for different needs.
   Note: See paper for details.
2. **Run zero-shot classification**
   Action: Evaluate zero-shot accuracy on classification datasets.
   Why: Standard CLIP evaluation.
   Note: See paper for details.
3. **Run retrieval evaluation**
   Action: Evaluate image-text and text-image retrieval.
   Why: Tests alignment quality.
   Note: See paper for details.
4. **Generate comparison report**
   Action: Compare results to other CLIP models.
   Why: Enables standardized comparison.
   Note: See paper for details.

## Parameters to set
- **num_datasets** — Role: Number of evaluation datasets. How to set: Include all available. Default/range: 40+. Effect: More datasets provide comprehensive evaluation.
- **evaluation_metrics** — Role: Metrics for evaluation. How to set: Accuracy for classification, R@K for retrieval. Default/range: Standard. Effect: Standard metrics enable comparison.

## Validation checks
- Results should be reproducible.
- Comparison should be fair across models.
- Evaluation should cover diverse visual domains.

## Failure modes
- Some datasets may not be available.
- Evaluation may be slow for many datasets.
- Not all capabilities are tested.

## Adaptation notes for VLM training
- CLIP-Benchmark is the standard evaluation for VLM vision encoders.
- Use to evaluate the impact of data curation on encoder quality.
- Comprehensive evaluation reveals training data effects.

## Implementation notes
- Use the CLIP-Benchmark codebase.
- Report all dataset results.
- Track improvements across training iterations.

## Evidence from the paper
- CLIP-Benchmark provides standardized evaluation across 40+ datasets.
- Comprehensive evaluation reveals model capabilities beyond ImageNet.
- Standardized comparison enables fair model ranking.
- The benchmark is widely used for CLIP model development.

## Source paper
- **Title**: CLIP-Benchmark: A Benchmark Suite for Evaluation of Vision-Language Models
- **Year**: 2023
- **Venue**: GitHub
- **Paper ID**: github-clip-benchmark-2023
- **URL**: https://github.com/LAION-AI/CLIP_benchmark
- **arXiv ID**: N/A
