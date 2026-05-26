# DCLM: DataComp for Language Models

## One-line decision
Use this skill when you want a benchmark-driven approach to evaluate text data filtering strategies for LLM training, analogous to DataComp for CLIP. Avoid it when you are not filtering text data for LLM/VLM training.

## Skill metadata
- **Skill type**: language-model-data-benchmark
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Extend the DataComp framework to language model training, providing a standardized benchmark for evaluating text data filtering and curation strategies on Common Crawl data.

## Problem signature
- Modality: text from Common Crawl with evaluable filtering strategies.
- Data state: large Common Crawl text pool requiring filtering for LLM training.
- Scale regime: 240 trillion token candidate pool filtered to various sizes.
- Model requirement: Standard transformer LLM for benchmarking filtering strategies.

## Use when
- You want to benchmark text data filtering strategies.
- You need principled guidance for LLM text data curation.
- You want to compare filtering approaches systematically.

## Do not use when
- You are not working with text data filtering.
- You have a well-established data pipeline.
- You need multimodal-specific filtering.

## Required inputs
- **common_crawl_pool**: 240T token Common Crawl candidate pool.
- **filtering_strategy**: Strategy for selecting a training subset.
- **evaluation_suite**: Downstream benchmarks for LLM evaluation.

## Optional inputs
- **model_based_filter**: Trained quality classifier for text filtering.

## Outputs
- **filtered_dataset**: Training data selected by the filtering strategy.
- **benchmark_results**: Downstream performance of LLM trained on filtered data.

## Assumptions and prerequisites
- Standardized benchmarking reveals best filtering practices.
- Filtering strategies have measurable impact on LLM quality.
- Results from smaller scales predict larger scale outcomes.

## Procedure
1. **Define candidate pool**
   Action: Establish the 240T token Common Crawl pool as the universe.
   Why: Common pool enables fair comparison.
   Note: See paper for details.
2. **Apply filtering strategy**
   Action: Run the candidate filtering strategy on the pool.
   Why: Filtering is the variable under study.
   Note: See paper for details.
3. **Train LLM on filtered data**
   Action: Train a standardized LLM on the filtered subset.
   Why: Fixed model ensures differences are data-driven.
   Note: See paper for details.
4. **Evaluate on benchmarks**
   Action: Run downstream evaluations.
   Why: Standardized evaluation enables comparison.
   Note: See paper for details.

## Parameters to set
- **pool_scale** — Role: Size of candidate pool. How to set: Use DCLM's provided pools. Default/range: 240T tokens. Effect: Larger pools allow more aggressive filtering.
- **filter_type** — Role: Type of filtering approach. How to set: Compare heuristic, classifier-based, and model-based. Default/range: Various. Effect: Different approaches have different strengths.

## Validation checks
- Filtered data should outperform random sampling baseline.
- Quality classifiers should beat heuristic filters.
- Results should be reproducible.

## Failure modes
- Optimal filters may not transfer to different pool compositions.
- Small-scale experiments may not predict large-scale outcomes perfectly.
- The benchmark may not capture all dimensions of data quality.

## Adaptation notes for VLM training
- DCLM filtering insights apply to the text component of VLM training.
- Use DCLM-validated quality classifiers for your own text data.
- The benchmark methodology extends to multimodal data filtering.

## Implementation notes
- Use the DCLM codebase and provided pools.
- Report results at standardized scales for comparison.
- Track per-benchmark improvements from filtering.

## Evidence from the paper
- DCLM extends DataComp to language model data filtering benchmarking.
- Quality classifier-based filtering achieves the best results.
- The 240T token pool enables systematic filtering experiments.
- DCLM-filtered data produces competitive LLM models.

## Source paper
- **Title**: DCLM: DataComp for Language Models
- **Year**: 2024
- **Venue**: NeurIPS
- **Paper ID**: arxiv-2406.11794v3
- **URL**: http://arxiv.org/abs/2406.11794v3
- **arXiv ID**: 2406.11794v3
