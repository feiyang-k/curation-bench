# MMBench: Is Your Multi-modal Model an All-around Player?

## One-line decision
Use this skill when you need a multi-dimensional benchmark evaluating VLMs across 20+ ability dimensions with robust circular evaluation. Avoid it when you only need a single-dimension evaluation or have simpler benchmarks.

## Skill metadata
- **Skill type**: multi-dimensional-vlm-benchmark
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Create a multi-dimensional VLM evaluation benchmark with 20+ ability dimensions and circular evaluation strategy to robustly assess VLM capabilities.

## Problem signature
- Modality: images with multiple-choice questions across 20+ ability dimensions.
- Data state: curated evaluation data spanning 20+ visual understanding ability dimensions.
- Scale regime: ~3,000 evaluation questions across 20+ dimensions.
- Model requirement: Any VLM to evaluate.

## Use when
- You need comprehensive multi-dimensional VLM evaluation.
- You want to identify specific capability strengths and weaknesses.
- You need robust evaluation beyond simple accuracy.

## Do not use when
- Simple benchmarks are sufficient.
- You need domain-specific evaluation.
- You only care about a single capability.

## Required inputs
- **evaluation_images**: Images paired with multi-choice questions.
- **ability_taxonomy**: Taxonomy of 20+ visual understanding abilities.
- **circular_evaluation**: Circular permutation of answer choices for robustness.

## Optional inputs
- **llm_judge**: LLM for extracting answers from free-form VLM outputs.

## Outputs
- **mmbench_scores**: Per-dimension and overall VLM evaluation scores.
- **ability_profile**: Radar chart of VLM capabilities across dimensions.

## Assumptions and prerequisites
- Multi-dimensional evaluation reveals more than single-score benchmarks.
- Circular evaluation reduces position bias in multiple choice.
- 20+ dimensions cover the key VLM capabilities.

## Procedure
1. **Define ability taxonomy**
   Action: Create a taxonomy of 20+ visual understanding abilities (object recognition, spatial reasoning, OCR, etc.).
   Why: Structured dimensions enable targeted evaluation.
   Note: See paper for details.
2. **Curate evaluation questions**
   Action: Create or collect evaluation questions for each ability dimension.
   Why: Per-dimension questions enable capability profiling.
   Note: See paper for details.
3. **Implement circular evaluation**
   Action: Permute answer choices and take the most consistent answer.
   Why: Reduces position bias in multiple choice evaluation.
   Note: See paper for details.
4. **Evaluate and profile VLMs**
   Action: Run VLMs through the benchmark and generate ability profiles.
   Why: Profiles reveal specific strengths and weaknesses.
   Note: See paper for details.

## Parameters to set
- **num_dimensions** — Role: Number of ability dimensions evaluated. How to set: 20+ for comprehensive coverage. Default/range: 20+. Effect: More dimensions provide finer-grained profiles.
- **circular_permutations** — Role: Number of answer permutations per question. How to set: Use all permutations (typically 4 for 4-choice). Default/range: All. Effect: More permutations improve robustness.

## Validation checks
- Evaluation should be consistent across answer permutations.
- Per-dimension scores should reveal meaningful differences between models.
- The benchmark should discriminate between model capabilities.

## Failure modes
- Multiple choice format may not capture open-ended capabilities.
- Some ability dimensions may have too few questions.
- LLM answer extraction may introduce errors.

## Adaptation notes for VLM training
- Use MMBench for evaluating VLM data curation impact across dimensions.
- The multi-dimensional evaluation reveals which data types improve which capabilities.
- Combine with other benchmarks for comprehensive evaluation.

## Implementation notes
- Use the MMBench evaluation server for standardized results.
- Generate radar charts for visual capability comparison.
- Track per-dimension improvement during VLM development.

## Evidence from the paper
- MMBench evaluates VLMs across 20+ ability dimensions with ~3,000 questions.
- Circular evaluation reduces position bias in multiple choice evaluation.
- Multi-dimensional profiling reveals specific capability strengths and weaknesses.
- MMBench has become a standard comprehensive VLM benchmark.

## Source paper
- **Title**: MMBench: Is Your Multi-modal Model an All-around Player?
- **Year**: 2023
- **Venue**: ECCV
- **Paper ID**: arxiv-2307.06281v4
- **URL**: http://arxiv.org/abs/2307.06281v4
- **arXiv ID**: 2307.06281v4
