# COCO: Microsoft COCO: Common Objects in Context

## One-line decision
Use this skill when you need a foundational multi-purpose vision dataset with captions, detections, segmentation, and keypoints for VLM development. Avoid it when you need web-scale data rather than a carefully annotated 330K image dataset.

## Skill metadata
- **Skill type**: multi-purpose-vision-dataset
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Create a large-scale dataset for object detection, segmentation, captioning, and keypoint estimation with detailed annotations of common objects in their natural context.

## Problem signature
- Modality: images with dense annotations: captions, bounding boxes, segmentation masks, and keypoints.
- Data state: 330K images with multi-type human annotations on 80 object categories.
- Scale regime: 330K images, 2.5M labeled instances, 5 captions per image.
- Model requirement: No model required for dataset construction; foundational for VLM training and evaluation.

## Use when
- You need high-quality multi-type annotations for VLM development.
- You want a standard evaluation benchmark for vision-language tasks.
- You need clean caption data for VLM pretraining or alignment.

## Do not use when
- You need web-scale data (COCO is 330K images).
- You need specialized domain annotations.
- You need more than 80 object categories.

## Required inputs
- **flickr_images**: Images from Flickr depicting common objects in context.
- **annotation_platform**: AMT or similar for multi-type annotation.
- **annotation_schema**: Schema for captions, bounding boxes, masks, and keypoints.

## Optional inputs
- **stuff_annotations**: Pixel-level stuff annotations for scene understanding.

## Outputs
- **coco_dataset**: 330K images with captions, detections, segmentation, and keypoints.
- **evaluation_benchmarks**: Standard benchmarks for detection, segmentation, and captioning.

## Assumptions and prerequisites
- Common objects in natural contexts provide useful training signal.
- Multiple annotation types on the same images enable multi-task learning.
- Five captions per image provide sufficient text diversity.

## Procedure
1. **Collect images from Flickr**
   Action: Gather images containing common objects in natural scenes.
   Why: Flickr provides diverse, natural images.
   Note: See paper for details.
2. **Annotate bounding boxes**
   Action: Have annotators draw bounding boxes around all objects.
   Why: Detection annotations enable object localization.
   Note: See paper for details.
3. **Annotate segmentation masks**
   Action: Collect pixel-level segmentation for each object instance.
   Why: Segmentation enables fine-grained understanding.
   Note: See paper for details.
4. **Collect captions**
   Action: Have 5 annotators write independent captions for each image.
   Why: Multiple captions capture diverse descriptions.
   Note: See paper for details.
5. **Annotate keypoints**
   Action: Annotate body keypoints for person instances.
   Why: Keypoints enable pose estimation.
   Note: See paper for details.

## Parameters to set
- **num_categories** — Role: Number of object categories. How to set: 80 categories covering common objects. Default/range: 80. Effect: More categories increase coverage.
- **captions_per_image** — Role: Number of caption annotations per image. How to set: 5 independent captions. Default/range: 5. Effect: More captions increase text diversity.

## Validation checks
- Annotations should be accurate and consistent across annotators.
- Captions should describe the main content of images.
- Object categories should cover common everyday objects.

## Failure modes
- 80 categories may not cover all objects of interest.
- Annotation quality varies across workers.
- The dataset may have geographic and demographic biases.

## Adaptation notes for VLM training
- COCO captions are used for VLM pretraining alignment (LLaVA, MiniGPT-4).
- COCO detections are used for grounding evaluation.
- The dataset is foundational for nearly all VLM development.

## Implementation notes
- Use the COCO API for efficient data loading.
- Leverage the 5-caption diversity for training.
- Use COCO evaluation servers for standardized benchmarking.

## Evidence from the paper
- COCO provides 330K images with multi-type annotations: captions, detections, segmentation, and keypoints.
- Five captions per image provide diverse text supervision.
- COCO is the most widely used dataset for vision-language model development and evaluation.
- The dataset covers 80 common object categories in natural contexts.

## Source paper
- **Title**: COCO: Microsoft COCO: Common Objects in Context
- **Year**: 2014
- **Venue**: ECCV
- **Paper ID**: arxiv-1405.0312v3
- **URL**: http://arxiv.org/abs/1405.0312v3
- **arXiv ID**: 1405.0312v3
