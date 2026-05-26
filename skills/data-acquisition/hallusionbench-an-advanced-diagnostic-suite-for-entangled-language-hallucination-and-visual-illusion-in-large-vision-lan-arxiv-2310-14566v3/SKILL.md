# HallusionBench: An Advanced Diagnostic Suite for Entangled Language Hallucination and Visual Illusion in Large Vision-Language Models

## One-line decision
Use this skill when you need a diagnostic benchmark testing VLM vulnerability to both language hallucination and visual illusion. Avoid it when you only need standard hallucination evaluation (use POPE instead).

## Skill metadata
- **Skill type**: hallucination-illusion-benchmark
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Create a diagnostic benchmark that specifically tests VLM vulnerability to entangled language hallucination and visual illusion, providing targeted evaluation beyond standard hallucination benchmarks.

## Problem signature
- Modality: images designed to trigger hallucination and visual illusion in VLMs.
- Data state: 346 carefully designed image-question pairs targeting hallucination and illusion.
- Scale regime: 346 diagnostic evaluation pairs.
- Model requirement: Any VLM for diagnostic evaluation.

## Use when
- You need diagnostic hallucination evaluation.
- You want to test VLM vulnerability to visual illusions.
- You need targeted evaluation beyond POPE-style benchmarks.

## Do not use when
- Standard hallucination benchmarks are sufficient.
- You need a large-scale benchmark.
- Visual illusion testing is not relevant.

## Required inputs
- **diagnostic_images**: Images designed to trigger specific hallucination types.
- **targeted_questions**: Questions probing hallucination and illusion.
- **evaluation_criteria**: Criteria for assessing hallucination types.

## Optional inputs
- **illusion_types**: Categories of visual illusions tested.

## Outputs
- **hallusionbench_results**: Per-category hallucination and illusion scores.
- **diagnostic_analysis**: Analysis of VLM vulnerability patterns.

## Assumptions and prerequisites
- Targeted diagnostic evaluation reveals more than standard benchmarks.
- Language hallucination and visual illusion are distinct but entangled.
- Understanding vulnerability patterns guides improvement.

## Procedure
1. **Design diagnostic images**
   Action: Create images targeting specific hallucination and illusion types.
   Why: Targeted images expose specific vulnerabilities.
   Note: See paper for details.
2. **Create probing questions**
   Action: Write questions that test for specific hallucination patterns.
   Why: Targeted questions reveal specific failure modes.
   Note: See paper for details.
3. **Evaluate VLMs**
   Action: Test VLMs on the diagnostic benchmark.
   Why: Reveals vulnerability patterns.
   Note: See paper for details.
4. **Analyze failure patterns**
   Action: Categorize and analyze hallucination and illusion failures.
   Why: Understanding patterns guides improvement.
   Note: See paper for details.

## Parameters to set
- **num_examples** — Role: Total diagnostic examples. How to set: 346 for targeted evaluation. Default/range: 346. Effect: Quality matters more than quantity for diagnostics.
- **hallucination_categories** — Role: Types of hallucination tested. How to set: Include language hallucination and visual illusion. Default/range: Multiple categories. Effect: More categories reveal more vulnerability types.

## Validation checks
- The benchmark should expose known VLM failure modes.
- Diagnostic results should be actionable.
- Different VLMs should show different vulnerability patterns.

## Failure modes
- 346 examples may not cover all hallucination types.
- Diagnostic images may not generalize to real-world scenarios.
- The benchmark may become saturated as models improve.

## Adaptation notes for VLM training
- Use HallusionBench to evaluate the impact of data curation on hallucination.
- Targeted diagnostics complement broad evaluation benchmarks.
- Understanding vulnerability patterns guides targeted data improvements.

## Implementation notes
- Use the HallusionBench evaluation toolkit.
- Report per-category scores for detailed analysis.
- Compare vulnerability patterns across model families.

## Evidence from the paper
- HallusionBench provides targeted diagnostic evaluation for VLM hallucination and illusion.
- The benchmark reveals entangled language hallucination and visual illusion patterns.
- Different VLMs show distinct vulnerability profiles.
- Diagnostic evaluation provides more actionable insights than broad benchmarks.

## Source paper
- **Title**: HallusionBench: An Advanced Diagnostic Suite for Entangled Language Hallucination and Visual Illusion in Large Vision-Language Models
- **Year**: 2023
- **Venue**: CVPR
- **Paper ID**: arxiv-2310.14566v3
- **URL**: http://arxiv.org/abs/2310.14566v3
- **arXiv ID**: 2310.14566v3
