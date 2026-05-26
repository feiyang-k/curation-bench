# LAION-5B: An Open Large-Scale Dataset for Training Next Generation Image-Text Models

## One-line decision
Use this skill when you need to build a multi-billion scale open image-text dataset from Common Crawl using CLIP score filtering. Avoid it when you need a small curated dataset or cannot handle the infrastructure for billions of image downloads.

## Skill metadata
- **Skill type**: web-scale-dataset-construction
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Construct an open, publicly available dataset of 5.85 billion image-text pairs from Common Crawl using CLIP-based filtering, enabling reproducible research on large-scale vision-language model training.

## Problem signature
- Modality: image-text pairs extracted from Common Crawl HTML with CLIP-score-based quality filtering.
- Data state: raw Common Crawl web pages processed to extract and filter image-text pairs.
- Scale regime: 5.85 billion image-text pairs across multiple languages.
- Model requirement: Pre-trained CLIP model for computing image-text alignment scores during filtering.

## Use when
- You need an open, large-scale image-text dataset for CLIP or VLM pretraining.
- You want to replicate or improve upon CLIP/DALL-E training at scale.
- You need multilingual image-text data (LAION-5B covers 100+ languages).

## Do not use when
- You need highly curated, domain-specific data rather than broad web-scraped data.
- You cannot handle the storage and bandwidth for billions of images.
- Legal or ethical constraints prevent using web-scraped image-text data.

## Required inputs
- **common_crawl_dumps**: Raw Common Crawl web archive dumps (HTML).
- **clip_model**: Pre-trained CLIP model for computing image-text alignment scores.
- **processing_pipeline**: Pipeline for HTML parsing, image URL extraction, downloading, and CLIP scoring.

## Optional inputs
- **safety_filters**: NSFW classifiers and content safety models to filter inappropriate content.
- **language_detector**: Language identification model for splitting by language.
- **watermark_detector**: Model to detect and flag watermarked images.

## Outputs
- **laion_5b_dataset**: 5.85 billion image-text pairs: 2.32B English (LAION-2B), 2.26B multilingual (LAION-Multi), 1.27B unverified (LAION-NOLANG).
- **metadata**: CLIP scores, language tags, NSFW probabilities, watermark probabilities, image dimensions for every pair.
- **knn_indices**: Pre-computed k-NN indices for efficient retrieval and deduplication.

## Assumptions and prerequisites
- Common Crawl contains sufficient image-text co-occurrences for billion-scale datasets.
- CLIP score filtering (cosine similarity ≥ 0.28) effectively removes misaligned pairs.
- Open release of large-scale datasets accelerates vision-language research.

## Procedure
1. **Parse Common Crawl HTML**
   Action: Extract image URLs and alt-text from Common Crawl web archive dumps.
   Why: Common Crawl provides petabytes of web content with image-text co-occurrences.
   Note: See paper for details.
2. **Download images**
   Action: Download images from extracted URLs using distributed downloaders (img2dataset).
   Why: Images must be downloaded to compute CLIP embeddings.
   Note: Many URLs will be broken or return errors; expect ~50% download success.
3. **Compute CLIP embeddings and scores**
   Action: Embed images and text with CLIP and compute cosine similarity scores.
   Why: CLIP scores measure image-text alignment quality.
   Note: See paper for details.
4. **Filter by CLIP score threshold**
   Action: Keep only pairs with CLIP cosine similarity ≥ 0.28.
   Why: Removes misaligned, noisy, or unrelated image-text pairs.
   Note: See paper for details.
5. **Apply safety filters**
   Action: Run NSFW classifier and watermark detector, storing probabilities as metadata.
   Why: Enables downstream users to apply their own safety thresholds.
   Note: See paper for details.
6. **Compute language tags and k-NN indices**
   Action: Detect language for each caption and build k-NN indices on CLIP embeddings.
   Why: Enables multilingual splits and efficient retrieval.
   Note: See paper for details.

## Parameters to set
- **clip_score_threshold** — Role: Minimum CLIP cosine similarity for keeping a pair. How to set: 0.28 balances quality and quantity. Default/range: 0.28. Effect: Higher threshold reduces dataset size but improves average quality.
- **min_image_size** — Role: Minimum image dimension in pixels. How to set: Vary by use case (64 for thumbnails, 256+ for training). Default/range: 64. Effect: Larger minimums exclude low-resolution images.
- **nsfw_threshold** — Role: Maximum NSFW probability for including a pair. How to set: Set by user preference. Default/range: Metadata provided; user filters. Effect: Lower threshold removes more potentially explicit content.

## Validation checks
- CLIP models trained on LAION-2B should match or exceed those trained on proprietary datasets.
- CLIP score distribution should show the filter effectively removes low-quality pairs.
- Language distribution should cover 100+ languages with English as the largest subset.

## Failure modes
- CLIP score filtering inherits biases from the CLIP model used for scoring.
- URLs decay over time (link rot) reducing the dataset's reproducibility.
- Web-crawled data may contain copyrighted, toxic, or private content.

## Adaptation notes for VLM training
- LAION-5B has become the de facto open dataset for CLIP and Stable Diffusion training.
- Sub-filter the dataset for domain-specific VLM applications using metadata fields.
- Combine LAION-5B with recaptioning (ShareGPT4V, CapsFusion) for higher quality captions.

## Implementation notes
- Use img2dataset for efficient distributed image downloading.
- Store metadata in parquet format for efficient querying.
- Pre-computed CLIP embeddings and k-NN indices are available for download.

## Evidence from the paper
- LAION-5B contains 5.85 billion CLIP-filtered image-text pairs from Common Crawl.
- OpenCLIP models trained on LAION-2B match or exceed OpenAI CLIP performance.
- The dataset enables open reproduction of large-scale vision-language pretraining previously limited to industry labs.
- LAION-5B includes pre-computed CLIP embeddings, safety scores, and k-NN indices.

## Source paper
- **Title**: LAION-5B: An Open Large-Scale Dataset for Training Next Generation Image-Text Models
- **Year**: 2022
- **Venue**: NeurIPS
- **Paper ID**: arxiv-2210.08402v1
- **URL**: http://arxiv.org/abs/2210.08402v1
- **arXiv ID**: 2210.08402v1
