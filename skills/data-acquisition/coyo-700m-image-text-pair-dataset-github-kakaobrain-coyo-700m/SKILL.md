# COYO-700M: Image-Text Pair Dataset

## One-line decision
Use this skill when you need a large-scale open image-text dataset from Common Crawl as an alternative to LAION with transparent collection methodology. Avoid it when LAION-5B or other existing datasets are sufficient for your needs.

## Skill metadata
- **Skill type**: korean-web-image-text-collection
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Collect 700 million image-text pairs from Common Crawl with transparent methodology and comprehensive metadata, providing an open alternative to proprietary image-text datasets.

## Problem signature
- Modality: image-text pairs from Common Crawl with quality metadata.
- Data state: web-crawled image-text pairs with CLIP scores, language tags, and quality metadata.
- Scale regime: 700 million image-text pairs.
- Model requirement: No model required for collection; used for vision-language pretraining.

## Use when
- You need a large-scale open image-text dataset.
- You want an alternative to LAION with transparent methodology.
- You need comprehensive metadata for filtering.

## Do not use when
- LAION-5B or DataComp already meet your needs.
- You need a smaller, curated dataset.
- You need domain-specific image-text data.

## Required inputs
- **common_crawl**: Common Crawl web archive.
- **processing_pipeline**: Pipeline for extracting and filtering image-text pairs.
- **metadata_computation**: CLIP scores, aesthetic scores, safety scores.

## Optional inputs
- **additional_filters**: Domain-specific or quality filters.

## Outputs
- **coyo_700m**: 700M image-text pairs with metadata.
- **metadata_fields**: CLIP score, aesthetic score, safety score, language tag per pair.

## Assumptions and prerequisites
- Common Crawl contains sufficient image-text co-occurrences.
- Transparent methodology enables reproducible research.
- Metadata enables flexible downstream filtering.

## Procedure
1. **Extract image-text from Common Crawl**
   Action: Parse web pages to extract co-occurring images and alt-text.
   Why: Common Crawl is the primary source of web-scale image-text data.
   Note: See paper for details.
2. **Download and validate images**
   Action: Download images and verify validity.
   Why: Many URLs are broken or return invalid images.
   Note: See paper for details.
3. **Compute metadata**
   Action: Calculate CLIP scores, aesthetic scores, safety scores, and language tags.
   Why: Metadata enables flexible filtering by downstream users.
   Note: See paper for details.
4. **Release with documentation**
   Action: Package dataset with metadata and transparent methodology documentation.
   Why: Transparency enables reproducible and responsible use.
   Note: See paper for details.

## Parameters to set
- **clip_score_filter** — Role: Minimum CLIP score for initial filtering. How to set: Use a permissive threshold; let users filter further. Default/range: Permissive. Effect: Lower threshold keeps more data for user-side filtering.
- **metadata_fields** — Role: Metadata provided per pair. How to set: Include CLIP, aesthetic, safety, language. Default/range: 4+ fields. Effect: More metadata enables finer-grained filtering.

## Validation checks
- CLIP models trained on COYO should be competitive with LAION-trained models.
- Metadata should accurately reflect pair quality.
- The dataset should cover diverse visual content.

## Failure modes
- URL decay reduces dataset reproducibility over time.
- Quality may be lower than more aggressively filtered datasets.
- Non-English content may dominate certain segments.

## Adaptation notes for VLM training
- COYO-700M is used as pretraining data for CLIP and VLMs.
- Sub-filter using metadata for domain-specific applications.
- Combine with other datasets for broader coverage.

## Implementation notes
- Use img2dataset for efficient downloading.
- Store in parquet format for efficient querying.
- Provide metadata for all pairs to enable user-side filtering.

## Evidence from the paper
- COYO-700M provides 700 million image-text pairs from Common Crawl with transparent methodology.
- The dataset includes CLIP scores, aesthetic scores, safety scores, and language tags.
- COYO enables reproducible vision-language pretraining research.
- The dataset has been used to train competitive CLIP and VLM models.

## Source paper
- **Title**: COYO-700M: Image-Text Pair Dataset
- **Year**: 2022
- **Venue**: GitHub
- **Paper ID**: github-kakaobrain-coyo-700m
- **URL**: https://github.com/kakaobrain/coyo-dataset
- **arXiv ID**: N/A
