# CutMix: Regularization Strategy to Train Strong Classifiers with Localizable Features

## One-line decision
Use this skill when you want to augment training images by cutting and pasting rectangular patches between images with mixed labels. Avoid it when your task does not benefit from spatial regularization.

## Skill metadata
- **Skill type**: region-mixing-augmentation
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Augment training data by cutting rectangular patches from one image and pasting them onto another, with labels mixed proportionally to the area of each image, producing a spatial regularization effect.

## Problem signature
- Modality: images with mixed labels from region swapping.
- Data state: training images augmented by cutting and pasting patches with proportional label mixing.
- Scale regime: any image classification or detection dataset.
- Model requirement: Any CNN or ViT; the augmentation is model-agnostic.

## Use when
- You want spatial regularization for image classification.
- You need data augmentation beyond simple transforms.
- You want to improve localization and feature learning.

## Do not use when
- Your task is not image classification or detection.
- Simple augmentation (flip, crop) is sufficient.
- You need clean, unmodified training images.

## Required inputs
- **training_images**: Image classification dataset.
- **cut_ratio**: Ratio controlling the size of cut patches.
- **label_mixing**: Strategy for mixing labels proportionally to patch area.

## Optional inputs
- **mask_strategy**: Strategy for selecting cut locations.

## Outputs
- **augmented_data**: Images with cut-and-pasted patches and mixed labels.
- **improved_model**: Model trained with CutMix regularization.

## Assumptions and prerequisites
- Mixing image regions with labels improves regularization.
- The model learns more localizable features from mixed training.
- CutMix is complementary to other augmentation methods.

## Procedure
1. **Select patch location and size**
   Action: Randomly select a rectangular patch location and size from the cut ratio distribution.
   Why: Random patches create diverse augmentation.
   Note: See paper for details.
2. **Cut and paste patches**
   Action: Replace the selected region in one image with the corresponding region from another image.
   Why: Creates mixed training samples.
   Note: See paper for details.
3. **Mix labels proportionally**
   Action: Mix the labels of the two images proportionally to the area ratio.
   Why: Proportional mixing provides correct supervision.
   Note: See paper for details.
4. **Train with CutMix**
   Action: Train the model with CutMix-augmented batches.
   Why: CutMix improves generalization and localization.
   Note: See paper for details.

## Parameters to set
- **alpha** — Role: Beta distribution parameter for cut ratio. How to set: alpha=1.0 for uniform distribution. Default/range: 1.0. Effect: Controls the size distribution of cut patches.
- **cutmix_prob** — Role: Probability of applying CutMix. How to set: 0.5-1.0. Default/range: 1.0. Effect: Higher probability means more augmented samples.

## Validation checks
- CutMix should improve classification accuracy over baseline augmentation.
- The model should learn more localizable features.
- Performance should improve on both classification and localization.

## Failure modes
- CutMix may create confusing samples if patches are too large.
- The augmentation may not help for tasks not requiring localization.
- Very high cut ratios may destroy important spatial structure.

## Adaptation notes for VLM training
- CutMix can be applied to VLM pretraining data augmentation.
- Extend to multimodal settings by adjusting text labels accordingly.
- Combine with Mixup for hybrid augmentation strategies.

## Implementation notes
- Implement CutMix in the data loader for efficiency.
- Apply CutMix after standard augmentations.
- Monitor the cut ratio distribution during training.

## Evidence from the paper
- CutMix improves ImageNet top-1 accuracy by ~1% over Mixup.
- The augmentation produces more localizable features.
- CutMix improves both classification and object detection.
- The method is simple, efficient, and widely adopted.

## Source paper
- **Title**: CutMix: Regularization Strategy to Train Strong Classifiers with Localizable Features
- **Year**: 2019
- **Venue**: ICCV
- **Paper ID**: arxiv-1905.04899v2
- **URL**: http://arxiv.org/abs/1905.04899v2
- **arXiv ID**: 1905.04899v2
