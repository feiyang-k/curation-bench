# Cambrian: A Data-Centric Benchmark for Multimodal AI

## One-line decision
Use this skill when you need a vision-centric evaluation benchmark that tests visual perception rather than language ability in VLMs. Avoid it when standard VLM benchmarks are sufficient.

## Skill metadata
- **Skill type**: vision-centric-benchmark
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Create a vision-centric evaluation benchmark (CV-Bench) that specifically tests visual perception capabilities rather than language understanding in VLMs, addressing the gap in existing evaluations.

## Problem signature
- Modality: images with vision-centric evaluation questions.
- Data state: evaluation data targeting visual perception specifically.
- Scale regime: vision-centric evaluation benchmark.
- Model requirement: Any VLM for evaluation.

## Use when
- You need to evaluate VLM visual perception specifically.
- Standard benchmarks may conflate language and vision ability.
- You want to assess the visual component of your VLM.

## Do not use when
- Standard VLM benchmarks are sufficient.
- You only care about overall performance.
- Visual perception is not your focus.

## Required inputs
- **perception_images**: Images testing specific visual perception capabilities.
- **perception_questions**: Questions isolating visual perception.
- **evaluation_framework**: Framework for vision-centric evaluation.

## Optional inputs
- **perception_categories**: Categories of visual perception tested.

## Outputs
- **cv_bench_scores**: Vision-centric perception evaluation results.
- **perception_analysis**: Analysis of VLM visual perception quality.

## Assumptions and prerequisites
- VLM benchmarks should separately test vision and language.
- Visual perception can be isolated from language ability.
- Vision-centric evaluation reveals different model qualities.

## Procedure
1. **Design perception-focused tests**
   Action: Create tests that isolate visual perception.
   Why: Isolating perception reveals true visual capability.
   Note: See paper for details.
2. **Minimize language complexity**
   Action: Use simple language to minimize language confounds.
   Why: Ensures tests measure vision, not language.
   Note: See paper for details.
3. **Evaluate VLMs**
   Action: Test VLMs on vision-centric benchmarks.
   Why: Reveals visual perception quality.
   Note: See paper for details.
4. **Compare to standard benchmarks**
   Action: Compare vision-centric to standard evaluation.
   Why: Shows what standard benchmarks miss.
   Note: See paper for details.

## Parameters to set
- **perception_types** — Role: Types of visual perception tested. How to set: Include depth, spatial, counting, attributes. Default/range: Diverse. Effect: More types test broader perception.

## Validation checks
- Tests should isolate visual perception from language.
- Results should differ from language-heavy benchmarks.
- The benchmark should be informative for model development.

## Failure modes
- Perfectly isolating vision from language is difficult.
- Some perception may inherently require language.
- The benchmark may not cover all perception types.

## Adaptation notes for VLM training
- CV-Bench reveals which VLM data improves visual perception.
- Vision-centric evaluation guides visual data curation.
- Combine with standard benchmarks for complete evaluation.

## Implementation notes
- Use simple question formats.
- Focus on visual perception aspects.
- Compare VLM rankings across vision-centric and standard benchmarks.

## Evidence from the paper
- CV-Bench specifically tests VLM visual perception.
- Standard benchmarks may overweight language ability.
- Vision-centric evaluation reveals different model rankings.
- Separate evaluation of vision and language guides targeted improvement.

## Source paper
- **Title**: Cambrian: A Data-Centric Benchmark for Multimodal AI
- **Year**: 2024
- **Venue**: arXiv
- **Paper ID**: arxiv-cambrian-bench-2024
- **URL**: http://arxiv.org/abs/2406.16860v1
- **arXiv ID**: N/A
