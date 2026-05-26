# DINOv2: Learning Robust Visual Features without Supervision

## One-line decision
Use this skill when you want to curate and deduplicate large-scale image data for self-supervised vision pretraining using retrieval-based curation. Avoid it when you are not doing self-supervised pretraining or have curated image data.

## Skill metadata
- **Skill type**: self-supervised-vision-data-pipeline
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Curate LVD-142M, a curated dataset of 142 million images for self-supervised vision pretraining, using retrieval-based deduplication and diversity sampling from uncurated web images.

## Problem signature
- Modality: images curated for self-supervised pretraining.
- Data state: web-crawled images curated through retrieval-based deduplication and diversity sampling.
- Scale regime: 142 million curated images from web sources.
- Model requirement: ViT models trained with self-supervised objectives (iBOT + DINO).

## Use when
- You want a curated image dataset for self-supervised pretraining.
- You need a strong vision backbone for VLM pipelines.
- You want to apply retrieval-based data curation.

## Do not use when
- You already have a curated image dataset.
- You are not doing self-supervised pretraining.
- CLIP-style training is your target.

## Required inputs
- **uncurated_images**: Large pool of web-crawled images.
- **reference_dataset**: Curated reference dataset (ImageNet-22K) for guiding curation.
- **retrieval_pipeline**: Pipeline for retrieving similar images from the uncurated pool.

## Optional inputs
- **dedup_filter**: Deduplication filter for the curated set.

## Outputs
- **lvd_142m**: 142M curated images for self-supervised pretraining.
- **dinov2_model**: Strong vision backbone trained on curated data.

## Assumptions and prerequisites
- Retrieval-based curation produces better training data than random web images.
- Self-supervised pretraining benefits from curated, diverse data.
- A curated reference dataset guides the selection process.

## Procedure
1. **Build retrieval index**
   Action: Build a nearest-neighbor index of the uncurated web image pool.
   Why: Enables efficient retrieval-based curation.
   Note: See paper for details.
2. **Retrieve similar images**
   Action: For each reference image, retrieve similar images from the pool.
   Why: Reference-guided retrieval selects relevant images.
   Note: See paper for details.
3. **Deduplicate**
   Action: Remove near-duplicate images from the retrieved set.
   Why: Deduplication prevents overfitting.
   Note: See paper for details.
4. **Diversity sampling**
   Action: Sample for maximum diversity in the curated set.
   Why: Diversity improves pretraining quality.
   Note: See paper for details.
5. **Train DINOv2**
   Action: Train ViT models with self-supervised objectives on LVD-142M.
   Why: Validates the curation approach.
   Note: See paper for details.

## Parameters to set
- **curated_size** — Role: Total images in curated dataset. How to set: 142M for comprehensive coverage. Default/range: 142M. Effect: More images improve pretraining quality.
- **reference_dataset** — Role: Reference dataset guiding curation. How to set: ImageNet-22K or similar. Default/range: ImageNet-22K. Effect: Reference quality affects curation quality.
- **retrieval_k** — Role: Number of retrieved images per reference. How to set: Tune for desired dataset size. Default/range: Variable. Effect: More retrieved images increase dataset size.

## Validation checks
- DINOv2 should produce strong linear probing features.
- The curated dataset should be more diverse than random web images.
- Self-supervised features should transfer to diverse downstream tasks.

## Failure modes
- Reference dataset biases may propagate to curation.
- Retrieval may miss important image types not in the reference.
- Deduplication may be overly aggressive.

## Adaptation notes for VLM training
- DINOv2 encoders are used alongside CLIP in VLMs (Cambrian-1, etc.).
- The retrieval-based curation approach applies to any image dataset.
- LVD-142M provides a template for curated vision pretraining data.

## Implementation notes
- Use FAISS for efficient retrieval indexing.
- Pre-compute embeddings for the full web image pool.
- Monitor diversity metrics during curation.

## Evidence from the paper
- DINOv2 trains on LVD-142M, a retrieval-curated dataset of 142M images.
- The curated data produces vision features that rival or exceed supervised pretraining.
- Retrieval-based curation with deduplication and diversity sampling is effective.
- DINOv2 features are widely used as complementary vision encoders in VLMs.

## Source paper
- **Title**: DINOv2: Learning Robust Visual Features without Supervision
- **Year**: 2023
- **Venue**: TMLR
- **Paper ID**: arxiv-2304.07193v2
- **URL**: http://arxiv.org/abs/2304.07193v2
- **arXiv ID**: 2304.07193v2
