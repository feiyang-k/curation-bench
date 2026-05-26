# SBU Captions Dataset

## One-line decision
Use this skill when you want to mine naturally occurring image-caption pairs from Flickr for vision-language pretraining. Avoid it when you need larger scale data or more descriptive captions than Flickr provides.

## Skill metadata
- **Skill type**: flickr-caption-mining
- **Paper kind**: operational-method
- **Actionability**: medium
- **Evidence quality**: full_paper

## Goal
Construct a million-scale image-caption dataset by mining Flickr for images with naturally descriptive user-written captions, filtering for caption quality.

## Problem signature
- Modality: image-text pairs from Flickr with user-written captions.
- Data state: Flickr images filtered for caption quality and descriptiveness.
- Scale regime: 1 million image-caption pairs from Flickr.
- Model requirement: No model required for collection; quality filtering uses simple heuristics.

## Use when
- You need a million-scale image-caption dataset from social media.
- You want user-written captions rather than alt-text.
- You need a medium-scale dataset for VLM alignment.

## Do not use when
- You need billion-scale data.
- Flickr content coverage is insufficient for your domain.
- You need highly detailed or structured captions.

## Required inputs
- **flickr_api**: Flickr API for image and metadata retrieval.
- **caption_quality_filters**: Heuristics for selecting descriptive captions.
- **download_pipeline**: Image downloading infrastructure.

## Optional inputs
- **additional_filters**: Content safety and deduplication filters.

## Outputs
- **sbu_dataset**: 1M image-caption pairs from Flickr.

## Assumptions and prerequisites
- Flickr users sometimes write descriptive captions for their photos.
- Simple heuristics can identify descriptive vs. non-descriptive captions.
- Million-scale data is useful for pretraining and alignment.

## Procedure
1. **Query Flickr for images**
   Action: Search Flickr for images with user-written descriptions.
   Why: Flickr is a rich source of user-annotated photographs.
   Note: See paper for details.
2. **Filter for descriptive captions**
   Action: Apply heuristics to select captions that describe image content.
   Why: Many Flickr captions are non-descriptive (dates, names, etc.).
   Note: See paper for details.
3. **Download and validate**
   Action: Download images and validate caption-image pairs.
   Why: Ensures data quality and availability.
   Note: See paper for details.
4. **Release dataset**
   Action: Package the filtered image-caption pairs.
   Why: Enables research use.
   Note: See paper for details.

## Parameters to set
- **caption_filters** — Role: Rules for selecting descriptive captions. How to set: Filter by length, content words, and structure. Default/range: Task-specific heuristics. Effect: Stricter filters reduce size but improve quality.

## Validation checks
- Captions should describe image content.
- The dataset should cover diverse visual content.
- Models trained on SBU should learn meaningful image-text associations.

## Failure modes
- Many Flickr captions are non-descriptive.
- The dataset is relatively small by modern standards.
- Flickr content has specific photographic biases.

## Adaptation notes for VLM training
- SBU is commonly used as part of VLM pretraining data mixes (e.g., in BLIP, LLaVA).
- Combine with CC3M, CC12M, and LAION for broader coverage.
- The Flickr mining approach can be applied to other photo-sharing platforms.

## Implementation notes
- Respect Flickr API rate limits.
- Store image URLs and metadata for reproducibility.
- Monitor caption quality statistics.

## Evidence from the paper
- SBU Captions provides 1M image-caption pairs mined from Flickr.
- User-written Flickr captions are more natural than web alt-text.
- The dataset has been widely used in VLM pretraining data mixes.
- Simple caption quality filtering is effective for selecting descriptive pairs.

## Source paper
- **Title**: SBU Captions Dataset
- **Year**: 2011
- **Venue**: NeurIPS
- **Paper ID**: crossref-nips-2011-sbu
- **URL**: https://proceedings.neurips.cc/paper/2011
- **arXiv ID**: N/A
