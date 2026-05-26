# RefinedWeb: A Falcon's Recipe for High-Quality Web Data

## One-line decision
Use this skill when you want to build a high-quality web text corpus through aggressive deduplication and filtering of Common Crawl. Avoid it when you have a curated text corpus or do not need web-scale text data.

## Skill metadata
- **Skill type**: web-data-refinement
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Demonstrate that properly cleaned and deduplicated web-only data (from Common Crawl) can match or exceed curated multi-source corpora like The Pile for LLM training.

## Problem signature
- Modality: text from Common Crawl after extensive cleaning and deduplication.
- Data state: Common Crawl text processed with aggressive deduplication and quality filtering.
- Scale regime: 5 trillion tokens of refined web text.
- Model requirement: Any LLM; validated with Falcon models.

## Use when
- You want high-quality web text without curating multiple sources.
- You can invest in aggressive deduplication and filtering.
- You need trillions of clean text tokens.

## Do not use when
- You need domain-specific text not well represented on the web.
- You already have a sufficient curated text corpus.
- You cannot afford the compute for aggressive deduplication at scale.

## Required inputs
- **common_crawl**: Common Crawl web archive dumps.
- **dedup_pipeline**: Aggressive deduplication pipeline (exact + fuzzy).
- **quality_filters**: Text quality filters (perplexity, language, etc.).

## Optional inputs
- **safety_filters**: Content safety and toxicity filters.

## Outputs
- **refinedweb_corpus**: 5 trillion tokens of high-quality web text.
- **falcon_models**: LLMs trained on RefinedWeb demonstrating its quality.

## Assumptions and prerequisites
- Aggressive filtering and deduplication can make web-only data competitive with curated corpora.
- The web contains sufficient diversity for general LLM training.
- Deduplication is more important than source curation.

## Procedure
1. **Extract text from Common Crawl**
   Action: Parse Common Crawl HTML to extract clean text.
   Why: Common Crawl is the largest available web archive.
   Note: See paper for details.
2. **Apply quality filters**
   Action: Filter by language, text quality, perplexity, and content safety.
   Why: Removes noise, non-English content, and harmful text.
   Note: See paper for details.
3. **Aggressive deduplication**
   Action: Apply both exact and fuzzy deduplication (MinHash) at web scale.
   Why: Web data contains massive duplication; removing it dramatically improves quality.
   Note: See paper for details.
4. **Validate with LLM training**
   Action: Train Falcon models on RefinedWeb and compare to multi-source baselines.
   Why: End-to-end validation proves the web-only approach works.
   Note: See paper for details.

## Parameters to set
- **dedup_aggressiveness** — Role: How aggressively to deduplicate. How to set: Use both exact and MinHash fuzzy dedup. Default/range: Aggressive. Effect: More dedup improves quality but reduces size.
- **quality_threshold** — Role: Minimum text quality score. How to set: Tune perplexity and quality filters. Default/range: Medium-high. Effect: Stricter thresholds keep cleaner text.
- **target_size** — Role: Final corpus size. How to set: 5T tokens for comprehensive coverage. Default/range: 5T tokens. Effect: Larger corpora provide more diversity.

## Validation checks
- Falcon models trained on RefinedWeb should match or exceed The Pile-trained baselines.
- Deduplication rate should show significant redundancy removal.
- Text quality metrics should confirm improvement over raw Common Crawl.

## Failure modes
- Aggressive deduplication may remove valid repeated content (quotes, etc.).
- Web-only data may lack specialized domain coverage.
- Quality filters may have biases against certain text styles.

## Adaptation notes for VLM training
- RefinedWeb's filtering pipeline applies to the text component of VLM training.
- Combine with image-text data for complete VLM pretraining.
- The web-only approach challenges the need for multi-source curation.

## Implementation notes
- Use MinHash with appropriate signature sizes for scalable fuzzy dedup.
- Process Common Crawl in parallel across multiple nodes.
- Cache dedup signatures for incremental processing.

## Evidence from the paper
- RefinedWeb shows that properly filtered web-only data matches curated multi-source corpora.
- Aggressive deduplication is the single most impactful processing step.
- Falcon models trained on RefinedWeb achieve competitive LLM performance.
- 5 trillion tokens of refined web text provide comprehensive language coverage.

## Source paper
- **Title**: RefinedWeb: A Falcon's Recipe for High-Quality Web Data
- **Year**: 2023
- **Venue**: NeurIPS
- **Paper ID**: arxiv-2306.01116v1
- **URL**: http://arxiv.org/abs/2306.01116v1
- **arXiv ID**: 2306.01116v1
