# Wukong: A 100 Million Large-scale Chinese Cross-modal Pre-training Benchmark

## One-line decision
Use this skill when you need a large-scale Chinese image-text dataset for training multilingual or Chinese-specific VLMs. Avoid it when you only need English image-text data.

## Skill metadata
- **Skill type**: chinese-image-text-dataset
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Construct Wukong, a 100 million Chinese image-text pair dataset from the web, providing the largest Chinese cross-modal pretraining benchmark.

## Problem signature
- Modality: Chinese image-text pairs from the web.
- Data state: 100M Chinese image-text pairs collected and filtered.
- Scale regime: 100 million Chinese image-text pairs.
- Model requirement: Chinese CLIP or multilingual VLM.

## Use when
- You need Chinese image-text pretraining data.
- You want to build Chinese-specific VLMs.
- You need a multilingual image-text dataset.

## Do not use when
- You only need English data.
- Chinese is not a target language.
- You have sufficient Chinese image-text data.

## Required inputs
- **chinese_web**: Chinese web content with images.
- **collection_pipeline**: Pipeline for extracting Chinese image-text pairs.
- **quality_filters**: Chinese-specific quality filters.

## Optional inputs
- **clip_model**: Chinese CLIP for quality scoring.

## Outputs
- **wukong_dataset**: 100M Chinese image-text pairs.
- **chinese_clip**: Chinese CLIP model trained on Wukong.

## Assumptions and prerequisites
- Chinese web contains sufficient image-text pairs.
- Chinese-specific filtering improves quality.
- 100M pairs enable effective Chinese VLM pretraining.

## Procedure
1. **Crawl Chinese web**
   Action: Extract image-text pairs from Chinese websites.
   Why: Chinese web is the primary source.
   Note: See paper for details.
2. **Filter for quality**
   Action: Apply Chinese-specific text and image quality filters.
   Why: Quality filtering removes noise.
   Note: See paper for details.
3. **Train Chinese CLIP**
   Action: Train CLIP on the 100M Chinese pairs.
   Why: Validates the dataset quality.
   Note: See paper for details.
4. **Evaluate**
   Action: Test on Chinese VL benchmarks.
   Why: Validates Chinese visual-language understanding.
   Note: See paper for details.

## Parameters to set
- **dataset_size** — Role: Total Chinese image-text pairs. How to set: 100M for comprehensive coverage. Default/range: 100M. Effect: More data improves Chinese VLM quality.
- **chinese_filters** — Role: Chinese-specific quality filters. How to set: Language-specific text quality heuristics. Default/range: Chinese-specific. Effect: Language-specific filtering improves quality.

## Validation checks
- Chinese CLIP should perform well on Chinese VL benchmarks.
- The dataset should cover diverse Chinese visual content.
- Quality should be comparable to English datasets.

## Failure modes
- Chinese web content may have different noise characteristics.
- Some Chinese text may be difficult to filter.
- The dataset may have regional biases.

## Adaptation notes for VLM training
- Wukong provides Chinese data for multilingual VLMs.
- Combine with English datasets for balanced multilingual training.
- The Chinese web collection methodology applies to other languages.

## Implementation notes
- Use Chinese NLP tools for text processing.
- Handle Chinese character encoding correctly.
- Evaluate on Chinese-specific benchmarks.

## Evidence from the paper
- Wukong provides 100M Chinese image-text pairs from the web.
- The dataset is the largest Chinese cross-modal pretraining benchmark.
- Chinese CLIP trained on Wukong achieves strong Chinese VL performance.
- The dataset enables Chinese-specific vision-language research.

## Source paper
- **Title**: Wukong: A 100 Million Large-scale Chinese Cross-modal Pre-training Benchmark
- **Year**: 2022
- **Venue**: NeurIPS
- **Paper ID**: arxiv-2202.06767v2
- **URL**: http://arxiv.org/abs/2202.06767v2
- **arXiv ID**: 2202.06767v2
