# OBELICS: An Open Web-Scale Filtered Dataset of Interleaved Image-Text Documents

## One-line decision
Use this skill when you want to build an open web-scale dataset of interleaved image-text documents for multimodal pretraining. Avoid it when you only need paired image-caption data without document context.

## Skill metadata
- **Skill type**: interleaved-dataset-construction
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Construct and release OBELICS, an open web-scale dataset of 141 million interleaved image-text web documents with 353 million images, providing an alternative to proprietary interleaved datasets like M3W.

## Problem signature
- Modality: interleaved image-text web documents preserving natural document structure.
- Data state: web pages from Common Crawl filtered and processed to preserve interleaved image-text structure.
- Scale regime: 141 million documents with 353 million images and 115 billion text tokens.
- Model requirement: No model required for dataset construction; used to train IDEFICS multimodal model.

## Use when
- You need an open, large-scale dataset of interleaved image-text documents.
- You want to train a Flamingo-style model with interleaved data.
- You need web documents with preserved image-text spatial relationships.

## Do not use when
- You only need image-caption pairs without document context.
- You cannot handle the scale of 141M documents.
- You need domain-specific documents rather than general web content.

## Required inputs
- **common_crawl**: Common Crawl web archive dumps.
- **html_parser**: Parser to extract text and image positions from HTML.
- **filtering_pipeline**: Multi-stage filtering for quality, safety, and deduplication.

## Optional inputs
- **nsfw_filter**: Classifier for removing NSFW images.
- **language_filter**: Language detection for multilingual splitting.

## Outputs
- **obelics_dataset**: 141M interleaved image-text web documents.
- **idefics_model**: IDEFICS model trained on OBELICS for validation.

## Assumptions and prerequisites
- Web documents with naturally interleaved images and text are valuable for multimodal pretraining.
- Open release enables reproducible multimodal research.
- Document-level context improves multimodal understanding.

## Procedure
1. **Parse Common Crawl HTML**
   Action: Extract text paragraphs and image URLs from web pages, preserving their relative positions.
   Why: Preserving document structure is key for interleaved learning.
   Note: See paper for details.
2. **Filter documents by quality**
   Action: Remove documents with too few images, too short text, or low-quality content.
   Why: Quality filtering reduces noise in the dataset.
   Note: See paper for details.
3. **Apply safety filters**
   Action: Remove NSFW images and toxic text.
   Why: Safety filtering is essential for responsible dataset release.
   Note: See paper for details.
4. **Deduplicate documents**
   Action: Remove near-duplicate documents based on text and URL similarity.
   Why: Deduplication prevents overfitting to repeated content.
   Note: See paper for details.
5. **Download and validate images**
   Action: Download images from URLs and verify they are valid and accessible.
   Why: Dead links and corrupted images must be removed.
   Note: See paper for details.
6. **Release and validate with IDEFICS**
   Action: Train IDEFICS on OBELICS to validate dataset quality.
   Why: End-to-end training validates the dataset's utility.
   Note: See paper for details.

## Parameters to set
- **min_images_per_doc** — Role: Minimum images for including a document. How to set: ≥1 image per document. Default/range: 1. Effect: Higher minimums keep only richly illustrated documents.
- **min_text_length** — Role: Minimum text content in a document. How to set: Remove very short documents. Default/range: Task-dependent. Effect: Removes trivially short documents.
- **dedup_threshold** — Role: Similarity threshold for document deduplication. How to set: Tune based on dataset analysis. Default/range: Not specified. Effect: Stricter deduplication reduces size but improves diversity.

## Validation checks
- IDEFICS trained on OBELICS should achieve competitive few-shot performance.
- Document structure (image positions) should be correctly preserved.
- Safety filtering should remove inappropriate content effectively.

## Failure modes
- Image URL decay over time reduces dataset reproducibility.
- Web documents may contain ads, navigation elements, and other irrelevant content.
- The scale of 141M documents requires significant storage and processing.

## Adaptation notes for VLM training
- OBELICS is the primary open alternative to Flamingo's proprietary M3W dataset.
- Use OBELICS as interleaved pretraining data for any Flamingo-style architecture.
- Combine with paired image-text data for balanced pretraining.

## Implementation notes
- Use distributed downloading for efficiency.
- Store documents in a structured format preserving image positions.
- Provide both raw HTML and processed versions for flexibility.

## Evidence from the paper
- OBELICS contains 141 million interleaved image-text web documents with 353 million images.
- IDEFICS trained on OBELICS achieves competitive performance with Flamingo models.
- The dataset is the largest open interleaved image-text dataset.
- OBELICS enables reproducible research on interleaved multimodal learning.

## Source paper
- **Title**: OBELICS: An Open Web-Scale Filtered Dataset of Interleaved Image-Text Documents
- **Year**: 2023
- **Venue**: NeurIPS
- **Paper ID**: arxiv-2306.16527v2
- **URL**: http://arxiv.org/abs/2306.16527v2
- **arXiv ID**: 2306.16527v2
