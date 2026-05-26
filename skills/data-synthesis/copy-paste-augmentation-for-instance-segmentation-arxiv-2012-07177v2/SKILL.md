# Copy-Paste Augmentation for Instance Segmentation

## One-line decision
Use this skill when you want to augment instance segmentation data by copying object instances from one image and pasting them onto another. Avoid it when standard augmentation is sufficient or you do not need instance segmentation.

## Skill metadata
- **Skill type**: instance-paste-augmentation
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Augment instance segmentation training data by copying object instances from one image and pasting them onto another, creating new training examples with diverse object compositions.

## Problem signature
- Modality: images with pasted object instances and updated annotations.
- Data state: training images augmented with copied-and-pasted object instances.
- Scale regime: any instance segmentation dataset.
- Model requirement: Any instance segmentation model.

## Use when
- You need more diverse object compositions in training.
- You have instance segmentation masks for copy-paste.
- You want to improve rare object detection.

## Do not use when
- You do not have instance segmentation masks.
- Standard augmentation is sufficient.
- Your task is not instance segmentation.

## Required inputs
- **source_images**: Images with instance segmentation masks.
- **target_images**: Images to paste instances onto.
- **paste_strategy**: Strategy for selecting and placing pasted instances.

## Optional inputs
- **blending**: Blending method for natural-looking pastes.

## Outputs
- **augmented_images**: Images with copy-pasted instances.
- **updated_annotations**: Segmentation annotations including pasted instances.

## Assumptions and prerequisites
- Copy-paste creates useful training diversity.
- Pasted instances provide meaningful training signal.
- The augmentation improves rare object detection.

## Procedure
1. **Select source instances**
   Action: Choose instances to copy from source images.
   Why: Instance selection controls augmentation diversity.
   Note: See paper for details.
2. **Paste onto target images**
   Action: Place selected instances on target images.
   Why: Creates new training compositions.
   Note: See paper for details.
3. **Update annotations**
   Action: Add masks and labels for pasted instances.
   Why: Annotations must reflect the augmented content.
   Note: See paper for details.
4. **Train with augmented data**
   Action: Train the model with copy-paste augmented data.
   Why: Validates the augmentation benefit.
   Note: See paper for details.

## Parameters to set
- **paste_probability** — Role: Probability of applying copy-paste. How to set: 0.5-1.0. Default/range: 0.5. Effect: Higher probability increases augmentation frequency.
- **num_pasted** — Role: Number of instances pasted per image. How to set: 1-5 instances. Default/range: 3. Effect: More instances increase diversity but may clutter.

## Validation checks
- Copy-paste should improve instance segmentation metrics.
- Rare object detection should benefit most.
- The augmentation should not degrade common object detection.

## Failure modes
- Pasted instances may look unnatural.
- Too many pasted instances may create unrealistic scenes.
- Annotation updates must be accurate.

## Adaptation notes for VLM training
- Copy-paste augmentation can be used in VLM grounding data augmentation.
- Apply to increase diversity of grounded image-text training data.
- Combine with text augmentation for complete multimodal augmentation.

## Implementation notes
- Use simple alpha blending for paste quality.
- Apply random scaling and positioning for diversity.
- Monitor per-category AP to assess benefit.

## Evidence from the paper
- Copy-paste augmentation improves instance segmentation by 1-2 AP.
- The approach is especially effective for rare object categories.
- Simple pasting without blending is surprisingly effective.
- Copy-paste is widely adopted in detection and segmentation pipelines.

## Source paper
- **Title**: Copy-Paste Augmentation for Instance Segmentation
- **Year**: 2021
- **Venue**: CVPR
- **Paper ID**: arxiv-2012.07177v2
- **URL**: http://arxiv.org/abs/2012.07177v2
- **arXiv ID**: 2012.07177v2
