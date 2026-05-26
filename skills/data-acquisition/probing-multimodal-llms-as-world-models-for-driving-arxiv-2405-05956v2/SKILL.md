# Probing Multimodal LLMs as World Models for Driving

## One-line decision
Use this skill when you need a benchmark testing VLMs as world models for autonomous driving understanding. Avoid it when driving is not your domain.

## Skill metadata
- **Skill type**: driving-world-model-benchmark
- **Paper kind**: operational-method
- **Actionability**: medium
- **Evidence quality**: full_paper

## Goal
Create a benchmark probing VLMs as world models for driving scenarios, testing understanding of physics, traffic rules, and spatial reasoning.

## Problem signature
- Modality: driving scenario images with world model reasoning questions.
- Data state: curated driving scenarios with physics and reasoning questions.
- Scale regime: evaluation benchmark for driving VLMs.
- Model requirement: Any VLM for evaluation.

## Use when
- You evaluate VLMs for driving understanding.
- You want to test world model capabilities.
- Driving reasoning evaluation is needed.

## Do not use when
- Driving is not your domain.
- General VLM evaluation is sufficient.
- You need general world model testing.

## Required inputs
- **driving_scenarios**: Driving scene images with scenarios.
- **reasoning_questions**: Questions about physics, rules, and spatial reasoning.
- **ground_truth**: Correct reasoning answers.

## Optional inputs
- **difficulty_levels**: Per-question difficulty.

## Outputs
- **driving_benchmark**: Driving world model evaluation results.
- **reasoning_analysis**: Analysis of VLM driving reasoning.

## Assumptions and prerequisites
- VLMs should understand driving physics and rules.
- World model capabilities are testable through reasoning questions.
- Driving understanding requires spatial and temporal reasoning.

## Procedure
1. **Design driving scenarios**
   Action: Create diverse driving scenarios.
   Why: Scenarios test different aspects of driving understanding.
   Note: See paper for details.
2. **Create reasoning questions**
   Action: Write questions testing physics, rules, and spatial understanding.
   Why: Questions probe world model capabilities.
   Note: See paper for details.
3. **Evaluate VLMs**
   Action: Test VLMs on the benchmark.
   Why: Measures driving world model capability.
   Note: See paper for details.
4. **Analyze reasoning**
   Action: Identify which reasoning types VLMs handle well.
   Why: Reveals specific strengths and weaknesses.
   Note: See paper for details.

## Parameters to set
- **scenario_types** — Role: Types of driving scenarios. How to set: Include various traffic situations. Default/range: Diverse. Effect: More types test broader understanding.

## Validation checks
- VLMs should demonstrate driving physics understanding.
- Questions should test genuine world model reasoning.
- Results should differentiate model capabilities.

## Failure modes
- Some scenarios may be ambiguous.
- VLMs may use shortcuts rather than reasoning.
- The benchmark may not cover all driving situations.

## Adaptation notes for VLM training
- Use for evaluating driving-specific VLM training data.
- Driving world model testing extends to other physical domains.
- The benchmark guides driving-specific data curation.

## Implementation notes
- Include diverse driving scenarios.
- Test on leading VLMs.
- Compare to human driver reasoning.

## Evidence from the paper
- The benchmark tests VLMs as world models for driving.
- Current VLMs show significant gaps in driving reasoning.
- Physics and spatial reasoning are challenging for VLMs.
- The evaluation guides driving-specific VLM improvement.

## Source paper
- **Title**: Probing Multimodal LLMs as World Models for Driving
- **Year**: 2024
- **Venue**: arXiv
- **Paper ID**: arxiv-2405.05956v2
- **URL**: http://arxiv.org/abs/2405.05956v2
- **arXiv ID**: 2405.05956v2
