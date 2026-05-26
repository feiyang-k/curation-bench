# Visual Genome: Connecting Language and Vision Using Crowdsourced Dense Image Annotations

## One-line decision
Use this skill when you need a densely annotated dataset with region descriptions, objects, attributes, relationships, and QA pairs for training grounding-capable VLMs. Avoid it when you only need image-level captions or cannot use crowdsourced annotations.

## Skill metadata
- **Skill type**: dense-annotation-collection
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Create a densely annotated visual dataset with region descriptions, objects, attributes, relationships, and question-answer pairs, connecting language and vision at the region level.

## Problem signature
- Modality: images with dense annotations: region descriptions, objects, attributes, relationships, and QA pairs.
- Data state: 108K images with 5.4M region descriptions, 1.7M QA pairs, 3.8M object instances, 2.8M attributes, 2.3M relationships.
- Scale regime: 108K images with millions of dense annotations.
- Model requirement: No model required for dataset construction; used to train various VLMs.

## Use when
- You need region-level language-vision annotations.
- You want to train models for visual relationship understanding.
- You need diverse annotation types (descriptions, QA, relationships, attributes).

## Do not use when
- You only need image-level captions.
- The 108K image scale is too small for your pretraining needs.
- You need pixel-level segmentation rather than bounding box annotations.

## Required inputs
- **source_images**: 108K images from COCO and other sources.
- **crowdsourcing_platform**: Platform for collecting diverse annotations from crowd workers.
- **annotation_schema**: Schema defining region descriptions, objects, attributes, relationships, and QA.

## Optional inputs
- **quality_control**: Multiple annotators per image for quality verification.

## Outputs
- **visual_genome_dataset**: Densely annotated dataset with 5.4M region descriptions and millions of other annotations.
- **scene_graphs**: Structured scene graph representations of images.

## Assumptions and prerequisites
- Crowdsourced workers can provide meaningful region-level annotations.
- Dense annotations enable fine-grained vision-language understanding.
- Multiple annotation types provide complementary learning signals.

## Procedure
1. **Collect region descriptions**
   Action: Have crowd workers draw bounding boxes and write descriptions for image regions.
   Why: Region-level descriptions connect language to spatial image content.
   Note: See paper for details.
2. **Annotate objects and attributes**
   Action: Collect object labels and their attributes within regions.
   Why: Structured annotations enable object-centric understanding.
   Note: See paper for details.
3. **Annotate relationships**
   Action: Collect relationships between object pairs.
   Why: Relationships capture scene structure.
   Note: See paper for details.
4. **Collect question-answer pairs**
   Action: Have workers generate QA pairs about image content.
   Why: QA annotations enable VQA training.
   Note: See paper for details.
5. **Construct scene graphs**
   Action: Build structured scene graphs from object, attribute, and relationship annotations.
   Why: Scene graphs provide a structured representation of image content.
   Note: See paper for details.

## Parameters to set
- **regions_per_image** — Role: Number of annotated regions per image. How to set: 50+ for dense coverage. Default/range: ~50. Effect: More regions capture more image content.
- **annotation_types** — Role: Types of annotations collected. How to set: Include descriptions, objects, attributes, relationships, QA. Default/range: 5 types. Effect: More types provide richer training signal.

## Validation checks
- Region descriptions should accurately describe the bounded content.
- Object labels and attributes should be consistent.
- Scene graphs should accurately represent image structure.

## Failure modes
- Crowdsourced annotations may contain errors or inconsistencies.
- Region boundaries may be imprecise.
- Annotation vocabulary may be biased toward common objects.

## Adaptation notes for VLM training
- Visual Genome is widely used for VLM training (region QA, grounding, scene understanding).
- Reformatted as instruction data for LLaVA-1.5 and similar VLMs.
- Scene graphs enable structured visual reasoning training.

## Implementation notes
- Use the Visual Genome API for efficient data loading.
- Handle the varied annotation formats with a unified loader.
- Monitor annotation quality statistics.

## Evidence from the paper
- Visual Genome provides 5.4M region descriptions, 1.7M QA pairs, 3.8M objects, 2.8M attributes, and 2.3M relationships across 108K images.
- The dataset connects language and vision at the region level through dense annotations.
- Visual Genome scene graphs have become a standard for visual relationship understanding.
- The dataset is used in VLM instruction tuning (LLaVA-1.5, InstructBLIP, etc.).

## Source paper
- **Title**: Visual Genome: Connecting Language and Vision Using Crowdsourced Dense Image Annotations
- **Year**: 2017
- **Venue**: IJCV
- **Paper ID**: arxiv-1602.07332v1
- **URL**: http://arxiv.org/abs/1602.07332v1
- **arXiv ID**: 1602.07332v1
