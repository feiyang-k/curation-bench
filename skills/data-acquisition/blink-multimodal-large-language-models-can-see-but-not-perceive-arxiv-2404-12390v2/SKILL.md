# BLINK: Multimodal Large Language Models Can See but Not Perceive

## One-line decision
Use this skill when you need a benchmark revealing perception gaps in VLMs — tasks that are trivially easy for humans but hard for models. Avoid it when standard VLM benchmarks show sufficient performance.

## Skill metadata
- **Skill type**: visual-perception-gap-benchmark
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Create a benchmark that reveals visual perception gaps in VLMs — tasks that are trivially easy for humans (one blink) but surprisingly challenging for state-of-the-art VLMs.

## Problem signature
- Modality: images with perception tasks easy for humans but hard for VLMs.
- Data state: 3,807 carefully curated perception challenge examples.
- Scale regime: 3,807 diagnostic examples.
- Model requirement: Any VLM for evaluation.

## Use when
- You want to find perception gaps in VLMs.
- You need tasks where VLMs fail despite human ease.
- You want diagnostic rather than performance evaluation.

## Do not use when
- Standard performance benchmarks are sufficient.
- You do not need to identify perception gaps.
- Your VLM already handles basic perception well.

## Required inputs
- **perception_challenges**: 3,807 curated visual perception examples.
- **human_baselines**: Human performance on the examples.
- **vlm_to_evaluate**: VLM for evaluation.

## Optional inputs
- **difficulty_analysis**: Per-task difficulty analysis.

## Outputs
- **blink_scores**: VLM performance on perception challenges.
- **gap_analysis**: Analysis of human-VLM perception gaps.

## Assumptions and prerequisites
- VLMs have significant perception gaps despite high benchmark scores.
- Human-easy tasks reveal fundamental model limitations.
- Understanding gaps guides training data improvement.

## Procedure
1. **Curate perception challenges**
   Action: Create 3,807 examples easy for humans but challenging for VLMs.
   Why: Reveals perception gaps.
   Note: See paper for details.
2. **Establish human baselines**
   Action: Measure human performance on the challenges.
   Why: Human comparison contextualizes VLM gaps.
   Note: See paper for details.
3. **Evaluate VLMs**
   Action: Test state-of-the-art VLMs on BLINK.
   Why: Identifies specific perception failures.
   Note: See paper for details.
4. **Analyze gaps**
   Action: Determine which perception types VLMs fail on.
   Why: Guides targeted improvement.
   Note: See paper for details.

## Parameters to set
- **challenge_types** — Role: Types of perception challenges. How to set: Include spatial, temporal, counting, depth, etc. Default/range: 14 task types. Effect: More types reveal more gaps.
- **difficulty_calibration** — Role: How difficulty is calibrated. How to set: Easy for humans, variable for VLMs. Default/range: Human-easy. Effect: Ensures gaps are meaningful.

## Validation checks
- Human performance should be very high (near-ceiling).
- VLM performance should be significantly lower.
- The gap should indicate genuine perception limitations.

## Failure modes
- Some challenges may be ambiguous even for humans.
- The gap may narrow as VLMs improve.
- 3,807 examples may not cover all perception types.

## Adaptation notes for VLM training
- BLINK reveals which training data types are missing for VLM perception.
- Perception gaps guide data curation for visual understanding.
- Addressing BLINK failures requires targeted training data.

## Implementation notes
- Use the BLINK evaluation framework.
- Report human-VLM gap per task type.
- Prioritize addressing the largest gaps.

## Evidence from the paper
- BLINK reveals that VLMs can see but not perceive many visual properties.
- Tasks trivially easy for humans are challenging for state-of-the-art VLMs.
- The benchmark identifies 14 types of perception gaps.
- Understanding gaps guides targeted VLM improvement.

## Source paper
- **Title**: BLINK: Multimodal Large Language Models Can See but Not Perceive
- **Year**: 2024
- **Venue**: ECCV
- **Paper ID**: arxiv-2404.12390v2
- **URL**: http://arxiv.org/abs/2404.12390v2
- **arXiv ID**: 2404.12390v2
