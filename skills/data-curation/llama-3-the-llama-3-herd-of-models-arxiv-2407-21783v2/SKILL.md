# Llama 3: The Llama 3 Herd of Models

## One-line decision
Use this skill when you want to understand Meta's comprehensive approach to pretraining data curation covering text, code, multimodal, and multilingual data at massive scale. Avoid it when you do not need insights into large-scale pretraining data recipes.

## Skill metadata
- **Skill type**: comprehensive-pretraining-recipe
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Document the comprehensive data curation approach for Llama 3, covering 15 trillion tokens of text and code plus multimodal data, with detailed filtering, deduplication, and quality scoring methodologies.

## Problem signature
- Modality: text, code, and multimodal data curated for large-scale pretraining.
- Data state: web text filtered, deduplicated, and quality-scored; multimodal data curated separately.
- Scale regime: 15 trillion tokens for text; multimodal data for vision capabilities.
- Model requirement: Llama 3 transformer architecture up to 405B parameters.

## Use when
- You want insights into industrial-scale pretraining data curation.
- You need guidance on data processing at trillion-token scale.
- You want to understand multimodal data integration in LLMs.

## Do not use when
- You are working at much smaller scale.
- You do not need comprehensive pretraining guidance.
- You have a well-established data pipeline.

## Required inputs
- **web_text**: Trillion-token scale web text from Common Crawl.
- **code_data**: Code from various sources.
- **multimodal_data**: Image-text and video-text data for multimodal capabilities.
- **quality_classifier**: Classifier for scoring text quality.

## Optional inputs
- **safety_filters**: Content safety and toxicity filtering.
- **language_filters**: Multilingual filtering and balancing.

## Outputs
- **llama3_data_pipeline**: Comprehensive data curation methodology.
- **llama3_models**: Pre-trained models up to 405B parameters.

## Assumptions and prerequisites
- Data quality is as important as quantity at trillion-token scale.
- Multi-stage filtering and quality scoring produce better training data.
- Multimodal data requires separate curation pipelines.

## Procedure
1. **Web text extraction**
   Action: Extract text from Common Crawl with quality filtering.
   Why: Web text is the primary source for pretraining.
   Note: See paper for details.
2. **Quality classification**
   Action: Train and apply quality classifiers to score text.
   Why: Quality scoring enables data-driven filtering.
   Note: See paper for details.
3. **Deduplication**
   Action: Apply aggressive deduplication at document and paragraph level.
   Why: Dedup removes redundancy and improves training efficiency.
   Note: See paper for details.
4. **Safety filtering**
   Action: Remove harmful, toxic, and PII-containing text.
   Why: Safety filtering is essential for responsible AI.
   Note: See paper for details.
5. **Multimodal data curation**
   Action: Curate image-text pairs for vision capabilities.
   Why: Multimodal data enables vision-language understanding.
   Note: See paper for details.
6. **Data mixing optimization**
   Action: Optimize mixing ratios across data sources.
   Why: The mix affects model capabilities.
   Note: See paper for details.

## Parameters to set
- **total_tokens** — Role: Total training tokens. How to set: 15T+ for frontier models. Default/range: 15T. Effect: More unique data improves model quality.
- **quality_threshold** — Role: Quality classifier threshold. How to set: Tune based on model performance. Default/range: Medium-high. Effect: Higher threshold keeps cleaner data.
- **safety_threshold** — Role: Safety filter aggressiveness. How to set: Strict filtering for responsible deployment. Default/range: Strict. Effect: Removes harmful content.

## Validation checks
- Llama 3 should achieve state-of-the-art performance.
- Data quality should be measurably improved by each filtering step.
- Safety filtering should remove harmful content effectively.

## Failure modes
- Quality classifiers may have biases.
- Aggressive filtering may remove valid content.
- The 15T token scale requires massive infrastructure.

## Adaptation notes for VLM training
- Llama 3's data curation insights apply to VLM pretraining pipelines.
- The quality classification approach generalizes to multimodal data.
- The multi-stage filtering pipeline is a best practice template.

## Implementation notes
- Use the paper's methodology as a reference for your own pipeline.
- Apply quality classification at the appropriate scale for your data.
- Monitor quality metrics throughout the pipeline.

## Evidence from the paper
- Llama 3 is trained on 15 trillion tokens of curated text and code data.
- Multi-stage quality filtering significantly improves pretraining data quality.
- Data mixing optimization across sources affects model capabilities.
- Llama 3 achieves state-of-the-art performance across many benchmarks.

## Source paper
- **Title**: Llama 3: The Llama 3 Herd of Models
- **Year**: 2024
- **Venue**: arXiv
- **Paper ID**: arxiv-2407.21783v2
- **URL**: http://arxiv.org/abs/2407.21783v2
- **arXiv ID**: 2407.21783v2
