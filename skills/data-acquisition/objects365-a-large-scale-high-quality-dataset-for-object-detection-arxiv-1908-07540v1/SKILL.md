# Objects365: A Large-Scale, High-Quality Dataset for Object Detection

## One-line decision
Use this skill when you need a large-scale detection dataset with 365 categories for training open-vocabulary detection models used in VLM pipelines. Avoid it when you only need the 80 COCO categories or a smaller detection dataset.

## Skill metadata
- **Skill type**: large-vocabulary-detection-dataset
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Create a large-scale object detection dataset with 365 categories and over 2 million images, enabling training of detectors with broader vocabulary for VLM grounding pipelines.

## Problem signature
- Modality: images with bounding box annotations for 365 object categories.
- Data state: 2M+ images annotated with bounding boxes across 365 categories.
- Scale regime: 2 million images, 30 million bounding boxes, 365 categories.
- Model requirement: No model required for dataset construction; used to train detection models.

## Use when
- You need a large-vocabulary detection dataset for VLM grounding.
- You want to train detectors covering more categories than COCO.
- You need large-scale detection pretraining data.

## Do not use when
- COCO's 80 categories are sufficient.
- You do not need detection data.
- You need pixel-level segmentation rather than bounding boxes.

## Required inputs
- **source_images**: 2M+ images from web sources.
- **annotation_platform**: Large-scale annotation platform.
- **category_hierarchy**: 365-category hierarchy covering diverse objects.

## Optional inputs
- **quality_review**: Multi-round annotation review.

## Outputs
- **objects365_dataset**: 2M+ images with 30M bounding boxes across 365 categories.

## Assumptions and prerequisites
- 365 categories cover a broader range of objects than COCO's 80.
- Large-scale detection data improves downstream model quality.
- High annotation quality is maintained through multi-round review.

## Procedure
1. **Define category hierarchy**
   Action: Design 365 object categories covering diverse everyday objects.
   Why: Broad categories enable wide vocabulary detection.
   Note: See paper for details.
2. **Collect images**
   Action: Gather 2M+ images containing objects from the 365 categories.
   Why: Large image pool ensures diverse training data.
   Note: See paper for details.
3. **Annotate bounding boxes**
   Action: Annotate all instances of target categories with bounding boxes.
   Why: Detection training requires accurate bounding box labels.
   Note: See paper for details.
4. **Quality review**
   Action: Multi-round review to ensure annotation quality.
   Why: High quality labels are essential for training.
   Note: See paper for details.

## Parameters to set
- **num_categories** — Role: Number of detection categories. How to set: 365 for broad coverage. Default/range: 365. Effect: More categories enable wider vocabulary detection.
- **annotations_per_image** — Role: Average bounding boxes per image. How to set: Annotate all visible instances. Default/range: ~15 per image. Effect: Dense annotation improves detection training.

## Validation checks
- Detection models trained on Objects365 should generalize better than COCO-trained models.
- Annotation quality should be high across all 365 categories.
- The category set should cover diverse object types.

## Failure modes
- Some categories may have insufficient examples.
- Annotation quality may vary across categories.
- Very large scale makes quality control challenging.

## Adaptation notes for VLM training
- Objects365 is used for detection pretraining in VLM grounding pipelines.
- Combine with COCO and LVIS for comprehensive detection coverage.
- Use Objects365-trained detectors as annotation tools for VLM data.

## Implementation notes
- Use the Objects365 evaluation server for benchmarking.
- Pre-train detectors on Objects365 before fine-tuning on COCO.
- Track per-category AP for analysis.

## Evidence from the paper
- Objects365 provides 2M+ images with 30M bounding boxes across 365 categories.
- Detectors pre-trained on Objects365 achieve significant improvements on COCO.
- The 365-category vocabulary covers 4.5x more object types than COCO.
- Objects365 is widely used for detection pretraining in VLM pipelines.

## Source paper
- **Title**: Objects365: A Large-Scale, High-Quality Dataset for Object Detection
- **Year**: 2019
- **Venue**: ICCV
- **Paper ID**: arxiv-1908.07540v1
- **URL**: http://arxiv.org/abs/1908.07540v1
- **arXiv ID**: 1908.07540v1
