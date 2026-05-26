# LMMs-Eval: Reality Check on the Evaluation of Large Multimodal Models

## One-line decision
Use this skill when you need a unified evaluation framework for consistently evaluating VLMs across dozens of benchmarks. Avoid it when you only evaluate on 1-2 benchmarks.

## Skill metadata
- **Skill type**: unified-vlm-evaluation-framework
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Provide a unified evaluation framework for consistently evaluating VLMs across dozens of benchmarks, ensuring reproducible and fair comparison.

## Problem signature
- Modality: evaluation framework covering dozens of VLM benchmarks.
- Data state: unified benchmark collection with consistent evaluation code.
- Scale regime: 50+ benchmarks in a single framework.
- Model requirement: Any VLM for evaluation.

## Use when
- You need to evaluate VLMs across many benchmarks.
- You want reproducible, consistent evaluation.
- You want a unified evaluation framework.

## Do not use when
- You only evaluate on 1-2 specific benchmarks.
- You have your own evaluation pipeline.
- Custom evaluation is needed.

## Required inputs
- **vlm_to_evaluate**: VLM for evaluation.
- **benchmark_collection**: LMMs-Eval's collection of 50+ benchmarks.
- **evaluation_config**: Configuration for which benchmarks to run.

## Optional inputs
- **custom_benchmarks**: Additional benchmarks to add.

## Outputs
- **evaluation_results**: Scores across all selected benchmarks.
- **comparison_report**: Comparison with other evaluated VLMs.

## Assumptions and prerequisites
- Unified evaluation enables fair comparison.
- Consistent implementation reduces evaluation noise.
- Many benchmarks provide a comprehensive capability profile.

## Procedure
1. **Configure evaluation**
   Action: Select which benchmarks to run.
   Why: Not all benchmarks may be relevant.
   Note: See paper for details.
2. **Run evaluation**
   Action: Execute the VLM on selected benchmarks.
   Why: Produces evaluation scores.
   Note: See paper for details.
3. **Generate report**
   Action: Compile results into a comparison report.
   Why: Enables comparison with other VLMs.
   Note: See paper for details.
4. **Analyze strengths and weaknesses**
   Action: Identify per-benchmark performance patterns.
   Why: Reveals specific capabilities and gaps.
   Note: See paper for details.

## Parameters to set
- **benchmark_set** — Role: Which benchmarks to evaluate. How to set: Select relevant benchmarks. Default/range: 50+. Effect: More benchmarks provide broader evaluation.
- **evaluation_config** — Role: Configuration for each benchmark. How to set: Use default LMMs-Eval configs. Default/range: Default. Effect: Consistent configs ensure fair comparison.

## Validation checks
- Evaluation should be reproducible.
- Results should be consistent with official benchmark implementations.
- The framework should cover diverse capability dimensions.

## Failure modes
- Some benchmarks may have implementation differences.
- New benchmarks may not yet be included.
- Evaluation may be slow for many benchmarks.

## Adaptation notes for VLM training
- Use LMMs-Eval as the standard evaluation framework for VLM development.
- Track data curation impact across all benchmarks simultaneously.
- The framework enables rapid, comprehensive VLM evaluation.

## Implementation notes
- Use the LMMs-Eval framework for all VLM evaluation.
- Report results with the framework version for reproducibility.
- Add custom benchmarks as needed.

## Evidence from the paper
- LMMs-Eval provides a unified framework for 50+ VLM benchmarks.
- Consistent implementation ensures fair model comparison.
- The framework enables comprehensive capability profiling.
- LMMs-Eval is increasingly adopted as the standard VLM evaluation tool.

## Source paper
- **Title**: LMMs-Eval: Reality Check on the Evaluation of Large Multimodal Models
- **Year**: 2024
- **Venue**: arXiv
- **Paper ID**: arxiv-2407.12772v3
- **URL**: http://arxiv.org/abs/2407.12772v3
- **arXiv ID**: 2407.12772v3
