# Grit: General Robust Image Task Benchmark

## One-line decision
Use this skill when you need a benchmark testing VLM robustness across multiple visual tasks with distribution shifts. Avoid it when standard in-distribution benchmarks are sufficient.

## Skill metadata
- **Skill type**: robust-multi-task-benchmark
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Create a benchmark testing VLM robustness across multiple visual tasks (classification, detection, grounding, captioning) with controlled distribution shifts.

## Problem signature
- Modality: images with multi-task evaluation under distribution shifts.
- Data state: evaluation data with controlled distribution shifts across tasks.
- Scale regime: multi-task evaluation benchmark.
- Model requirement: Any VLM for multi-task robustness evaluation.

## Use when
- You need robustness evaluation across tasks.
- You want to test VLM under distribution shifts.
- Multi-task evaluation is needed.

## Do not use when
- Standard in-distribution evaluation is sufficient.
- Single-task robustness testing works.
- You do not need distribution shift evaluation.

## Required inputs
- **multi_task_data**: Evaluation data across multiple visual tasks.
- **distribution_shifts**: Controlled shifts for robustness testing.
- **evaluation_framework**: Framework for consistent multi-task evaluation.

## Optional inputs
- **shift_severity**: Levels of distribution shift severity.

## Outputs
- **robustness_scores**: Per-task robustness evaluation results.
- **shift_analysis**: Analysis of performance under distribution shifts.

## Assumptions and prerequisites
- Robustness across tasks is important for practical VLMs.
- Distribution shifts reveal model fragility.
- Multi-task evaluation provides comprehensive assessment.

## Procedure
1. **Define task suite**
   Action: Select multiple visual tasks for evaluation.
   Why: Multi-task coverage ensures comprehensive testing.
   Note: See paper for details.
2. **Apply distribution shifts**
   Action: Create controlled distribution shifts for each task.
   Why: Shifts test robustness beyond in-distribution.
   Note: See paper for details.
3. **Evaluate VLMs**
   Action: Test VLMs across tasks and shift levels.
   Why: Measures robustness comprehensively.
   Note: See paper for details.
4. **Analyze fragility patterns**
   Action: Identify which shifts cause the most degradation.
   Why: Reveals specific robustness weaknesses.
   Note: See paper for details.

## Parameters to set
- **task_count** — Role: Number of visual tasks. How to set: Include classification, detection, grounding, captioning. Default/range: 4+. Effect: More tasks test broader robustness.
- **shift_types** — Role: Types of distribution shifts. How to set: Include natural, synthetic, and domain shifts. Default/range: Multiple. Effect: Diverse shifts test different robustness aspects.

## Validation checks
- Performance should degrade gracefully under shifts.
- Some tasks should be more robust than others.
- The benchmark should differentiate model robustness.

## Failure modes
- Some shifts may be too easy or too hard.
- Multi-task evaluation is compute-intensive.
- Not all shift types may be relevant.

## Adaptation notes for VLM training
- Robustness benchmarks guide VLM data curation for robustness.
- Data augmentation should target identified fragile areas.
- Multi-task robustness is important for practical deployment.

## Implementation notes
- Use the GRIT benchmark framework.
- Report per-task and per-shift results.
- Compare robustness across model families.

## Evidence from the paper
- GRIT tests VLM robustness across multiple tasks with distribution shifts.
- Different tasks show different robustness patterns.
- Distribution shifts reveal model fragility not seen in standard evaluation.
- Robustness evaluation is essential for practical VLM deployment.

## Source paper
- **Title**: Grit: General Robust Image Task Benchmark
- **Year**: 2023
- **Venue**: arXiv
- **Paper ID**: arxiv-2306.14818v2
- **URL**: http://arxiv.org/abs/2306.14818v2
- **arXiv ID**: 2306.14818v2
