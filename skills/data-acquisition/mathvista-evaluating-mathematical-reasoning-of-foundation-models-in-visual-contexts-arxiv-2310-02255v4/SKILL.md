# MathVista: Evaluating Mathematical Reasoning of Foundation Models in Visual Contexts

## One-line decision
Use this skill when you need a benchmark testing mathematical reasoning in visual contexts including charts, plots, diagrams, and geometry. Avoid it when you do not need mathematical reasoning evaluation.

## Skill metadata
- **Skill type**: math-visual-reasoning-benchmark
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Create a comprehensive benchmark for evaluating mathematical reasoning in visual contexts, combining 28 existing datasets with 3 new datasets covering diverse math visual reasoning tasks.

## Problem signature
- Modality: images with mathematical reasoning questions (charts, plots, geometry, tables, etc.).
- Data state: 6,141 questions across 31 datasets testing diverse math visual reasoning.
- Scale regime: 6,141 questions from 31 datasets.
- Model requirement: Any VLM or foundation model to evaluate.

## Use when
- You need to evaluate mathematical reasoning in visual contexts.
- You want to benchmark VLMs on chart, plot, and geometry understanding.
- You need a comprehensive math visual reasoning evaluation.

## Do not use when
- Mathematical reasoning is not your focus.
- You need pure text-based math evaluation.
- You have domain-specific math evaluation needs.

## Required inputs
- **math_visual_questions**: Questions requiring math reasoning about visual inputs.
- **existing_datasets**: 28 existing math visual reasoning datasets.
- **new_datasets**: 3 new datasets for IQTest, FunctionQA, and PaperQA.

## Optional inputs
- **difficulty_labels**: Per-question difficulty and reasoning type.

## Outputs
- **mathvista_scores**: Per-task and overall math visual reasoning scores.
- **reasoning_analysis**: Analysis of reasoning types and difficulty levels.

## Assumptions and prerequisites
- Mathematical reasoning in visual contexts is a distinct and important capability.
- Combining multiple datasets provides comprehensive coverage.
- Different visual math tasks test different reasoning skills.

## Procedure
1. **Aggregate existing datasets**
   Action: Combine 28 existing math visual reasoning datasets.
   Why: Aggregation provides comprehensive coverage.
   Note: See paper for details.
2. **Create new datasets**
   Action: Create IQTest, FunctionQA, and PaperQA for uncovered reasoning types.
   Why: New datasets fill gaps in existing coverage.
   Note: See paper for details.
3. **Categorize reasoning types**
   Action: Label questions by math reasoning type and visual context.
   Why: Enables fine-grained analysis of model capabilities.
   Note: See paper for details.
4. **Evaluate foundation models**
   Action: Test VLMs, LLMs, and tool-augmented models on MathVista.
   Why: Comprehensive evaluation reveals math visual reasoning capabilities.
   Note: See paper for details.

## Parameters to set
- **num_datasets** — Role: Number of source datasets. How to set: 31 for comprehensive coverage. Default/range: 31. Effect: More datasets cover more reasoning types.
- **question_types** — Role: Types of math visual reasoning. How to set: Include geometry, algebra, statistics, calculus, etc. Default/range: Diverse. Effect: More types test broader math understanding.

## Validation checks
- Questions should require visual input to answer.
- Mathematical reasoning should be verifiable.
- The benchmark should discriminate between model capabilities.

## Failure modes
- Some questions may be answerable without the image.
- Mathematical reasoning evaluation may be sensitive to answer format.
- Aggregated datasets may have inconsistent difficulty.

## Adaptation notes for VLM training
- MathVista reveals whether VLM training data includes sufficient mathematical content.
- Include math-focused instruction data to improve MathVista performance.
- The benchmark covers chart, plot, geometry, and table reasoning.

## Implementation notes
- Use flexible answer matching for numerical answers.
- Report per-reasoning-type performance.
- Compare against tool-augmented baselines.

## Evidence from the paper
- MathVista combines 31 datasets with 6,141 questions testing math visual reasoning.
- The benchmark covers geometry, algebra, statistics, and more in visual contexts.
- Top VLMs achieve ~50-60%, well below human performance.
- MathVista has become a standard benchmark for VLM mathematical reasoning.

## Source paper
- **Title**: MathVista: Evaluating Mathematical Reasoning of Foundation Models in Visual Contexts
- **Year**: 2023
- **Venue**: ICLR
- **Paper ID**: arxiv-2310.02255v4
- **URL**: http://arxiv.org/abs/2310.02255v4
- **arXiv ID**: 2310.02255v4
