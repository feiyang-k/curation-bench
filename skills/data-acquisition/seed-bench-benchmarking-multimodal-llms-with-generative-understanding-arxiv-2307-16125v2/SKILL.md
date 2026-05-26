# SEED-Bench: Benchmarking Multimodal LLMs with Generative Understanding

## One-line decision
Use this skill when you need a large-scale benchmark testing VLM generative understanding across 12 evaluation dimensions. Avoid it when you only need perception evaluation or have simpler benchmarks.

## Skill metadata
- **Skill type**: multi-dimensional-generative-evaluation
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Create a large-scale benchmark for evaluating multimodal LLMs across 12 dimensions of generative understanding, with 19K multiple-choice questions and 27K human annotations.

## Problem signature
- Modality: images with multiple-choice questions across 12 evaluation dimensions.
- Data state: 19K evaluation questions with human annotations across 12 dimensions.
- Scale regime: 19K questions across 12 dimensions.
- Model requirement: Any VLM for evaluation.

## Use when
- You need comprehensive multi-dimensional VLM evaluation.
- You want to assess generative understanding capabilities.
- You need a large-scale benchmark with human annotations.

## Do not use when
- Simple perception evaluation is sufficient.
- You have domain-specific evaluation needs.
- You need very few evaluation dimensions.

## Required inputs
- **evaluation_images**: Images paired with evaluation questions.
- **dimension_taxonomy**: Taxonomy of 12 evaluation dimensions.
- **human_annotations**: 27K human annotations for quality assurance.

## Optional inputs
- **model_predictions**: VLM outputs for scoring.

## Outputs
- **seed_bench_scores**: Per-dimension and overall VLM scores.
- **dimension_profiles**: Capability profiles across 12 dimensions.

## Assumptions and prerequisites
- Generative understanding requires multi-dimensional evaluation.
- Multiple-choice format enables automatic evaluation.
- 12 dimensions cover the key generative understanding capabilities.

## Procedure
1. **Define evaluation dimensions**
   Action: Create 12 dimensions covering spatial, temporal, reasoning, and knowledge understanding.
   Why: Comprehensive dimensions enable thorough evaluation.
   Note: See paper for details.
2. **Generate evaluation questions**
   Action: Create 19K questions across the 12 dimensions.
   Why: Large scale ensures reliable evaluation.
   Note: See paper for details.
3. **Collect human annotations**
   Action: Have humans validate questions and answers.
   Why: Human validation ensures benchmark quality.
   Note: See paper for details.
4. **Evaluate VLMs**
   Action: Run VLMs on the benchmark and compute per-dimension scores.
   Why: Multi-dimensional scoring reveals specific capabilities.
   Note: See paper for details.

## Parameters to set
- **num_dimensions** — Role: Number of evaluation dimensions. How to set: 12 for comprehensive coverage. Default/range: 12. Effect: More dimensions provide finer-grained profiling.
- **questions_per_dimension** — Role: Questions per evaluation dimension. How to set: 1,000+ per dimension. Default/range: ~1,600. Effect: More questions improve reliability.

## Validation checks
- Per-dimension scores should reveal meaningful model differences.
- Human accuracy should serve as an upper bound.
- The benchmark should discriminate between model capabilities.

## Failure modes
- Multiple-choice format may not capture open-ended generation.
- Some dimensions may overlap.
- Human annotation quality may vary.

## Adaptation notes for VLM training
- SEED-Bench provides comprehensive VLM evaluation.
- Use for tracking VLM improvement during data curation.
- Combine with other benchmarks for complete evaluation.

## Implementation notes
- Use the SEED-Bench evaluation toolkit.
- Report per-dimension scores for detailed analysis.
- Track improvements across development iterations.

## Evidence from the paper
- SEED-Bench evaluates VLMs across 12 dimensions with 19K questions.
- The benchmark includes 27K human annotations for quality assurance.
- Multi-dimensional evaluation reveals specific capability strengths and weaknesses.
- SEED-Bench has become a standard comprehensive VLM benchmark.

## Source paper
- **Title**: SEED-Bench: Benchmarking Multimodal LLMs with Generative Understanding
- **Year**: 2023
- **Venue**: CVPR
- **Paper ID**: arxiv-2307.16125v2
- **URL**: http://arxiv.org/abs/2307.16125v2
- **arXiv ID**: 2307.16125v2
