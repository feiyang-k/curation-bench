# MMMU: A Massive Multi-discipline Multimodal Understanding and Reasoning Benchmark

## One-line decision
Use this skill when you need a benchmark testing expert-level multimodal understanding across 30+ subjects using college exam questions. Avoid it when you need basic visual QA evaluation rather than expert-level assessment.

## Skill metadata
- **Skill type**: expert-level-multimodal-benchmark
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Create an expert-level multimodal benchmark using 11,500 college exam questions across 30+ subjects spanning art, science, engineering, medicine, and more, testing both visual understanding and domain knowledge.

## Problem signature
- Modality: images from academic subjects with expert-level multiple-choice questions.
- Data state: 11,500 questions from college exams and textbooks across 30+ disciplines.
- Scale regime: 11,500 questions across 6 core disciplines and 30+ subjects.
- Model requirement: Any VLM to evaluate at expert level.

## Use when
- You need expert-level multimodal evaluation.
- You want to test VLMs on college-level content.
- You need evaluation across diverse academic disciplines.

## Do not use when
- Basic visual QA evaluation is sufficient.
- You need domain-specific rather than multi-discipline evaluation.
- Your model targets non-academic applications.

## Required inputs
- **exam_questions**: College exam and textbook questions with images.
- **subject_taxonomy**: Taxonomy of 30+ academic subjects.
- **expert_validation**: Domain expert validation of question quality.

## Optional inputs
- **difficulty_labels**: Per-question difficulty ratings.

## Outputs
- **mmmu_scores**: Per-subject and overall expert-level VLM scores.
- **subject_profiles**: VLM performance across 30+ academic disciplines.

## Assumptions and prerequisites
- College exam questions test expert-level understanding.
- Multi-discipline coverage reveals cross-domain capabilities.
- Images from academic sources test diverse visual understanding.

## Procedure
1. **Collect exam questions**
   Action: Gather questions from college exams and textbooks across 30+ subjects.
   Why: Expert-level questions test deep understanding.
   Note: See paper for details.
2. **Curate image-question pairs**
   Action: Select questions requiring visual understanding of academic images.
   Why: Visual grounding ensures the benchmark tests multimodal capability.
   Note: See paper for details.
3. **Validate with domain experts**
   Action: Have experts review questions for correctness and difficulty.
   Why: Expert validation ensures benchmark quality.
   Note: See paper for details.
4. **Evaluate VLMs**
   Action: Test VLMs on the benchmark and analyze per-subject performance.
   Why: Reveals expert-level capabilities across disciplines.
   Note: See paper for details.

## Parameters to set
- **num_subjects** — Role: Number of academic subjects. How to set: 30+ for broad coverage. Default/range: 30+. Effect: More subjects test broader expertise.
- **question_difficulty** — Role: Difficulty level of questions. How to set: College exam level. Default/range: College-level. Effect: Expert-level questions discriminate better.

## Validation checks
- Questions should require both visual understanding and domain knowledge.
- Human expert accuracy should be high (>80%) as a quality check.
- The benchmark should discriminate between model capabilities.

## Failure modes
- Some subjects may be underrepresented.
- College-level questions may have cultural biases.
- Multiple choice format may miss deeper understanding.

## Adaptation notes for VLM training
- MMMU tests whether VLM data includes sufficient domain knowledge.
- Use MMMU to evaluate the impact of domain-specific training data.
- The multi-discipline approach reveals data coverage gaps.

## Implementation notes
- Use the MMMU evaluation server for standardized results.
- Report per-subject and per-discipline performance.
- Compare against human expert baselines.

## Evidence from the paper
- MMMU contains 11,500 college exam questions across 30+ subjects and 6 core disciplines.
- The benchmark tests expert-level multimodal understanding and reasoning.
- Top VLMs (GPT-4V) achieve ~56% on MMMU, well below human expert performance.
- MMMU has become a standard benchmark for testing VLM expertise.

## Source paper
- **Title**: MMMU: A Massive Multi-discipline Multimodal Understanding and Reasoning Benchmark
- **Year**: 2023
- **Venue**: CVPR
- **Paper ID**: arxiv-2311.16502v3
- **URL**: http://arxiv.org/abs/2311.16502v3
- **arXiv ID**: 2311.16502v3
