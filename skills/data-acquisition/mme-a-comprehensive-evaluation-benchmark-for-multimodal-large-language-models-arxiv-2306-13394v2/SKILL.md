# MME: A Comprehensive Evaluation Benchmark for Multimodal Large Language Models

## One-line decision
Use this skill when you need a comprehensive VLM benchmark testing both perception and cognition abilities with yes/no questions. Avoid it when you need open-ended evaluation or have specific benchmark needs.

## Skill metadata
- **Skill type**: perception-cognition-evaluation
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Create a comprehensive VLM evaluation benchmark testing 14 subtasks across perception (existence, count, position, color, poster, celebrity, scene, landmark, artwork, OCR) and cognition (commonsense reasoning, numerical calculation, text translation, code reasoning).

## Problem signature
- Modality: images with yes/no perception and cognition questions.
- Data state: evaluation images with binary yes/no questions across 14 subtasks.
- Scale regime: evaluation dataset across 14 subtasks.
- Model requirement: Any VLM for evaluation.

## Use when
- You need comprehensive perception and cognition evaluation.
- You want a simple yes/no evaluation format.
- You need a broad-coverage VLM benchmark.

## Do not use when
- You need open-ended evaluation.
- Yes/no format is too restrictive.
- You have specific task evaluation needs.

## Required inputs
- **evaluation_images**: Images for perception and cognition evaluation.
- **binary_questions**: Yes/no questions across 14 subtasks.
- **subtask_taxonomy**: Taxonomy of perception and cognition subtasks.

## Optional inputs
- **difficulty_levels**: Per-question difficulty levels.

## Outputs
- **mme_scores**: Perception and cognition scores per subtask.
- **total_score**: Combined perception + cognition total.

## Assumptions and prerequisites
- Yes/no questions provide a simple, unambiguous evaluation format.
- 14 subtasks cover the major perception and cognition capabilities.
- Combining perception and cognition gives a holistic assessment.

## Procedure
1. **Define subtask taxonomy**
   Action: Create 14 subtasks spanning perception and cognition.
   Why: Comprehensive coverage enables thorough evaluation.
   Note: See paper for details.
2. **Create yes/no questions**
   Action: Design binary questions for each subtask.
   Why: Yes/no format enables automatic, unambiguous evaluation.
   Note: See paper for details.
3. **Evaluate VLMs**
   Action: Run VLMs on all subtasks and compute scores.
   Why: Per-subtask scoring reveals specific capabilities.
   Note: See paper for details.
4. **Compute aggregate scores**
   Action: Sum perception and cognition subtask scores.
   Why: Aggregate scores enable overall model comparison.
   Note: See paper for details.

## Parameters to set
- **num_subtasks** — Role: Number of evaluation subtasks. How to set: 14 covering both perception and cognition. Default/range: 14. Effect: More subtasks provide broader coverage.
- **evaluation_format** — Role: Question format. How to set: Binary yes/no questions. Default/range: Yes/no. Effect: Simple format reduces evaluation noise.

## Validation checks
- Scores should correlate with model capability.
- Perception and cognition should be separately meaningful.
- The benchmark should be easy to administer.

## Failure modes
- Yes/no format may not capture nuanced understanding.
- Random guessing has 50% baseline.
- Some subtasks may have too few questions.

## Adaptation notes for VLM training
- MME provides quick comprehensive VLM evaluation.
- Use for rapid comparison during data curation experiments.
- Combine with more detailed benchmarks for thorough evaluation.

## Implementation notes
- Use the MME evaluation toolkit.
- Report perception and cognition scores separately.
- Compare against the MME leaderboard.

## Evidence from the paper
- MME evaluates VLMs across 14 subtasks covering perception and cognition.
- The yes/no format provides simple, unambiguous evaluation.
- MME has become one of the most widely used VLM benchmarks.
- Combined perception and cognition scores provide holistic assessment.

## Source paper
- **Title**: MME: A Comprehensive Evaluation Benchmark for Multimodal Large Language Models
- **Year**: 2023
- **Venue**: arXiv
- **Paper ID**: arxiv-2306.13394v2
- **URL**: http://arxiv.org/abs/2306.13394v2
- **arXiv ID**: 2306.13394v2
