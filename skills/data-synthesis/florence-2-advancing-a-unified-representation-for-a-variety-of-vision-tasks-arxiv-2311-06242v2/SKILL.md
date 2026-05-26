# Florence-2: Advancing a Unified Representation for a Variety of Vision Tasks

## One-line decision
Use this skill when you need to build a large-scale multi-task dataset with diverse vision annotations (caption, detection, segmentation, grounding) using automated annotation engines. Avoid it when you only need a single task type or already have comprehensive multi-task annotations.

## Skill metadata
- **Skill type**: unified-annotation-engine
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Build FLD-5B, a 5.4 billion annotation dataset covering captions, region proposals, object detection, grounding, and segmentation using automated annotation engines, then train a unified sequence-to-sequence model on it.

## Problem signature
- Modality: images with diverse annotations: captions, bounding boxes, segmentation masks, region descriptions.
- Data state: 126M images annotated with 5.4B annotations from multiple automated engines.
- Scale regime: 5.4 billion annotations across multiple vision tasks.
- Model requirement: DaViT vision encoder + sequence-to-sequence transformer trained on multi-task data.

## Use when
- You need a comprehensive multi-task vision dataset at scale.
- You want to build annotation engines for automated dataset construction.
- You need a unified model handling captioning, detection, grounding, and segmentation.

## Do not use when
- You need only a single task type.
- You cannot build or run automated annotation engines.
- Manual annotation quality is critical for your application.

## Required inputs
- **source_images**: 126M images from web crawl and existing datasets.
- **annotation_engines**: Automated pipelines for caption, detection, grounding, and segmentation annotation.
- **multi_task_format**: Sequence-to-sequence format for unifying all task types.

## Optional inputs
- **human_verification**: Spot-check annotations for quality.

## Outputs
- **fld_5b_dataset**: 5.4B multi-task annotations across 126M images.
- **florence2_model**: Unified vision model handling diverse tasks via sequence-to-sequence.

## Assumptions and prerequisites
- Automated annotation engines can produce sufficient quality at scale.
- A unified sequence-to-sequence format can handle diverse vision tasks.
- Scale of annotations compensates for individual annotation noise.

## Procedure
1. **Build annotation engines**
   Action: Create automated pipelines for captioning, detection, grounding, and segmentation.
   Why: Manual annotation at 5B scale is infeasible.
   Note: See paper for details.
2. **Annotate 126M images**
   Action: Run all engines on the image collection to produce 5.4B annotations.
   Why: Comprehensive multi-task coverage enables unified training.
   Note: See paper for details.
3. **Format as sequence-to-sequence**
   Action: Convert all annotation types into text sequences for unified training.
   Why: Sequence format enables a single model to handle all tasks.
   Note: See paper for details.
4. **Train Florence-2**
   Action: Train the unified model on the full FLD-5B dataset.
   Why: Multi-task training produces a versatile vision foundation model.
   Note: See paper for details.

## Parameters to set
- **num_annotation_types** — Role: Number of distinct annotation tasks. How to set: Include caption, detection, grounding, segmentation, OCR. Default/range: 5+. Effect: More types produce a more versatile model.
- **annotations_per_image** — Role: Average annotations per image. How to set: ~43 annotations per image across tasks. Default/range: 43. Effect: Dense annotation improves multi-task learning.

## Validation checks
- Florence-2 should achieve competitive performance on each individual task.
- The unified model should not sacrifice per-task performance for generality.
- Annotation quality should be verified on random samples.

## Failure modes
- Automated annotations may be noisy for complex tasks like segmentation.
- The sequence format may be suboptimal for some task types.
- Training on 5.4B annotations requires significant compute.

## Adaptation notes for VLM training
- The annotation engine approach is reusable for domain-specific datasets.
- FLD-5B provides a comprehensive pretraining dataset for VLMs.
- The unified format enables easy extension to new task types.

## Implementation notes
- Run annotation engines in parallel across multiple GPUs.
- Use incremental annotation to handle the 126M image scale.
- Store annotations in a structured format for efficient loading.

## Evidence from the paper
- Florence-2 uses FLD-5B containing 5.4 billion annotations across 126M images.
- The model handles captioning, detection, grounding, and segmentation in a unified architecture.
- Automated annotation engines enable dataset construction at unprecedented scale.
- Florence-2 achieves competitive or state-of-the-art results across multiple vision benchmarks.

## Source paper
- **Title**: Florence-2: Advancing a Unified Representation for a Variety of Vision Tasks
- **Year**: 2023
- **Venue**: CVPR
- **Paper ID**: arxiv-2311.06242v2
- **URL**: http://arxiv.org/abs/2311.06242v2
- **arXiv ID**: 2311.06242v2
