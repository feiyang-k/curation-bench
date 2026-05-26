# Multimodal C4: An Open, Billion-scale Corpus of Images Interleaved with Text

## One-line decision
Use this skill when you want to augment C4 text corpus with interleaved images placed at relevant positions for multimodal pretraining. Avoid it when you only need paired image-text data or cannot process the billion-scale corpus.

## Skill metadata
- **Skill type**: interleaved-corpus-construction
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Augment the C4 text corpus with images placed at relevant positions within documents, creating Multimodal C4 (MMC4) — a billion-scale corpus of interleaved image-text documents for multimodal pretraining.

## Problem signature
- Modality: text documents from C4 augmented with images placed at relevant positions.
- Data state: C4 text documents with images retrieved and placed using CLIP-based relevance scoring.
- Scale regime: 101.2 million documents with 571 million images.
- Model requirement: CLIP model for computing image-text relevance to place images; any multimodal model for training.

## Use when
- You want interleaved image-text data derived from an existing text corpus.
- You need a large-scale open dataset for Flamingo-style training.
- You want images placed at contextually relevant positions within documents.

## Do not use when
- You need naturally interleaved documents (MMC4 places images algorithmically).
- You cannot handle the scale of 571M images.
- You need perfectly aligned image-text data.

## Required inputs
- **c4_corpus**: The C4 text corpus (cleaned Common Crawl text).
- **image_sources**: Images from the original web pages that contained the C4 text.
- **clip_model**: CLIP model for computing image-text relevance scores.

## Optional inputs
- **face_filter**: Filter to remove images with detected faces for privacy.
- **dedup_filter**: Near-duplicate image removal.

## Outputs
- **mmc4_dataset**: 101.2M documents with 571M images interleaved at relevant positions.
- **image_placement_scores**: CLIP relevance scores for each image-sentence assignment.

## Assumptions and prerequisites
- CLIP relevance scores can effectively determine where to place images in text.
- C4 text quality carries over when augmented with images.
- Algorithmic placement is a reasonable proxy for natural interleaving.

## Procedure
1. **Retrieve original web page images**
   Action: For each C4 document, retrieve images from the original web page URL.
   Why: Original page images are most likely to be relevant to the text.
   Note: See paper for details.
2. **Compute CLIP relevance scores**
   Action: Score each image against each sentence in the document using CLIP.
   Why: CLIP scores determine optimal image placement.
   Note: See paper for details.
3. **Place images at relevant positions**
   Action: Assign each image to the sentence with the highest CLIP relevance score.
   Why: Contextual placement creates meaningful interleaved sequences.
   Note: See paper for details.
4. **Filter and deduplicate**
   Action: Remove low-relevance images, face images, and near-duplicates.
   Why: Quality and safety filtering improves dataset utility.
   Note: See paper for details.
5. **Validate with multimodal training**
   Action: Train a multimodal model on MMC4 to validate the dataset.
   Why: End-to-end training confirms the dataset is useful for learning.
   Note: See paper for details.

## Parameters to set
- **clip_relevance_threshold** — Role: Minimum CLIP score for including an image. How to set: Filter out images below a relevance threshold. Default/range: Task-dependent. Effect: Higher threshold keeps fewer but more relevant images.
- **max_images_per_doc** — Role: Maximum images per document. How to set: Cap to prevent over-illustrated documents. Default/range: Not specified. Effect: Too many images may overwhelm the text signal.
- **placement_strategy** — Role: How images are assigned to positions in text. How to set: Assign to highest-scoring sentence. Default/range: Greedy assignment. Effect: Greedy is simple; optimal assignment may be better.

## Validation checks
- Image placements should be contextually relevant to surrounding text.
- Models trained on MMC4 should develop in-context multimodal learning.
- The dataset should complement paired image-text datasets.

## Failure modes
- Algorithmic placement may put images in wrong positions.
- Retrieved images may no longer be available due to URL decay.
- Face filtering may be overly aggressive on valid content.

## Adaptation notes for VLM training
- MMC4 is useful as interleaved pretraining data for Flamingo-style models.
- Combine with OBELICS for broader interleaved data coverage.
- The CLIP-based placement strategy can be applied to any text corpus.

## Implementation notes
- Cache CLIP embeddings for efficient relevance computation.
- Use distributed processing for the 100M+ document corpus.
- Store placement scores for analysis and threshold tuning.

## Evidence from the paper
- Multimodal C4 provides 101.2M documents with 571M images placed at contextually relevant positions.
- The CLIP-based placement strategy effectively positions images near relevant text.
- MMC4 enables training of multimodal models with in-context learning capability.
- The dataset is fully open and provides both core and full versions.

## Source paper
- **Title**: Multimodal C4: An Open, Billion-scale Corpus of Images Interleaved with Text
- **Year**: 2023
- **Venue**: NeurIPS
- **Paper ID**: arxiv-2304.06939v2
- **URL**: http://arxiv.org/abs/2304.06939v2
- **arXiv ID**: 2304.06939v2
