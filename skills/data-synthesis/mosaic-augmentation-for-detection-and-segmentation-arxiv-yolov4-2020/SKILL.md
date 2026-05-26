# Mosaic Augmentation for Detection and Segmentation

## One-line decision
Use this skill when you want to create training images by combining four cropped images into a mosaic grid for object detection training. Avoid it when standard single-image augmentation is sufficient.

## Skill metadata
- **Skill type**: mosaic-image-augmentation
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Create training images by combining four cropped images into a 2x2 mosaic grid, providing diverse spatial compositions and scale variations for improved object detection training.

## Problem signature
- Modality: mosaic images combining 4 training images for detection.
- Data state: training images augmented with mosaic combinations.
- Scale regime: any object detection dataset.
- Model requirement: Any object detection model; commonly used with YOLO.

## Use when
- You want diverse spatial compositions for detection training.
- You need multi-scale object training from mosaics.
- You want to improve small object detection.

## Do not use when
- Single-image augmentation is sufficient.
- Your task does not involve detection.
- Mosaic artifacts would harm your task.

## Required inputs
- **training_images**: Detection dataset with bounding box annotations.
- **mosaic_config**: Configuration for 2x2 mosaic creation.

## Optional inputs
- **scale_range**: Scale range for cropping within mosaic.

## Outputs
- **mosaic_images**: 4-image mosaic augmented training samples.
- **updated_boxes**: Bounding boxes adjusted for mosaic positions.

## Assumptions and prerequisites
- Mosaic provides rich spatial diversity.
- Multi-image mosaics improve scale robustness.
- The augmentation benefits detection training.

## Procedure
1. **Select 4 images**
   Action: Randomly select 4 training images.
   Why: 4 images provide diverse mosaic content.
   Note: See paper for details.
2. **Crop and arrange**
   Action: Crop regions and arrange in a 2x2 grid.
   Why: Creates diverse spatial compositions.
   Note: See paper for details.
3. **Adjust annotations**
   Action: Transform bounding boxes to mosaic coordinates.
   Why: Annotations must match the mosaic layout.
   Note: See paper for details.
4. **Train with mosaics**
   Action: Include mosaic images in training batches.
   Why: Validates the augmentation benefit.
   Note: See paper for details.

## Parameters to set
- **mosaic_probability** — Role: Probability of creating a mosaic. How to set: 0.5-1.0. Default/range: 1.0. Effect: Higher probability increases diversity.
- **crop_range** — Role: Range of crop regions within mosaic. How to set: Random crops within each quadrant. Default/range: Random. Effect: More variation improves robustness.

## Validation checks
- Detection AP should improve with mosaic augmentation.
- Small object detection should benefit particularly.
- The augmentation should not create too many artifacts.

## Failure modes
- Mosaic boundaries may create artifacts.
- Very small objects may be lost in cropping.
- 4 images per sample increases preprocessing time.

## Adaptation notes for VLM training
- Mosaic augmentation is used in VLM grounding data preprocessing.
- Apply to detection-focused VLM training for grounding capability.
- Combine with CutMix and Mixup for comprehensive augmentation.

## Implementation notes
- Implement efficient mosaic creation in the data loader.
- Handle bounding box clipping at mosaic boundaries.
- Monitor detection metrics with and without mosaics.

## Evidence from the paper
- Mosaic augmentation improves YOLO detection by combining 4 images per sample.
- The approach provides rich spatial diversity and multi-scale training.
- Mosaic is especially effective for small object detection.
- The augmentation is widely adopted in modern detection pipelines.

## Source paper
- **Title**: Mosaic Augmentation for Detection and Segmentation
- **Year**: 2020
- **Venue**: arXiv
- **Paper ID**: arxiv-yolov4-2020
- **URL**: https://arxiv.org/abs/2004.10934
- **arXiv ID**: N/A
