# RandAugment: Practical Automated Data Augmentation with a Reduced Search Space

## One-line decision
Use this skill when you want simple automated data augmentation with only two hyperparameters (number and magnitude of transforms). Avoid it when you have a custom augmentation pipeline or do not need automated augmentation.

## Skill metadata
- **Skill type**: automated-augmentation
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Simplify automated data augmentation to just two hyperparameters: N (number of transforms) and M (magnitude of transforms), applied uniformly without per-transform search.

## Problem signature
- Modality: images for classification and detection training.
- Data state: training images augmented with random compositions of image transforms.
- Scale regime: any image dataset.
- Model requirement: Any image model; augmentation is model-agnostic.

## Use when
- You want automated augmentation without expensive policy search.
- You need a simple, tunable augmentation strategy.
- You want to augment image data for VLM training.

## Do not use when
- You have a custom augmentation pipeline.
- Your data is not images.
- Simple augmentations (flip, crop) are sufficient.

## Required inputs
- **training_images**: Image dataset to augment.
- **transform_set**: Set of image transforms (rotation, color, shear, etc.).
- **n_and_m**: Number of transforms N and magnitude M.

## Optional inputs
- **proxy_task**: Small-scale task for tuning N and M.

## Outputs
- **augmented_images**: Images with random compositions of transforms.
- **improved_model**: Model trained with RandAugment.

## Assumptions and prerequisites
- A fixed magnitude for all transforms is sufficient.
- Simple random composition matches complex policy search.
- Two hyperparameters are easy to tune.

## Procedure
1. **Define transform set**
   Action: Choose a set of standard image transforms.
   Why: The transform set defines the augmentation space.
   Note: See paper for details.
2. **Select N and M**
   Action: Choose N (number of transforms) and M (magnitude).
   Why: These two hyperparameters control the augmentation.
   Note: See paper for details.
3. **Apply random augmentation**
   Action: For each image, randomly apply N transforms at magnitude M.
   Why: Random composition creates diverse augmentations.
   Note: See paper for details.
4. **Train with augmentation**
   Action: Train the model on augmented data.
   Why: Augmentation improves generalization.
   Note: See paper for details.

## Parameters to set
- **n_transforms** — Role: Number of transforms applied per image. How to set: 2-3 for most tasks. Default/range: 2. Effect: More transforms create more diverse augmentations.
- **magnitude** — Role: Intensity of each transform. How to set: 9-15 on a 0-30 scale. Default/range: 9-15. Effect: Higher magnitude creates stronger augmentation.

## Validation checks
- RandAugment should match or exceed AutoAugment performance.
- The augmentation should improve over no augmentation.
- N and M should be easy to tune on a proxy task.

## Failure modes
- Very high magnitude may distort images beyond recognition.
- Some transforms may not be suitable for all image types.
- The uniform magnitude assumption may not hold for all transforms.

## Adaptation notes for VLM training
- RandAugment is commonly used in VLM pretraining image pipelines.
- Apply to CLIP and VLM training for improved image robustness.
- Combine with CutMix and Mixup for comprehensive augmentation.

## Implementation notes
- Use the timm or torchvision implementation.
- Tune N and M on a small proxy task.
- Apply augmentation in the data loader.

## Evidence from the paper
- RandAugment matches AutoAugment with just 2 hyperparameters (N, M).
- The method eliminates the need for expensive augmentation policy search.
- RandAugment is widely used in vision model training pipelines.
- Simple random composition of transforms is surprisingly effective.

## Source paper
- **Title**: RandAugment: Practical Automated Data Augmentation with a Reduced Search Space
- **Year**: 2020
- **Venue**: CVPR Workshops
- **Paper ID**: arxiv-1909.13719v2
- **URL**: http://arxiv.org/abs/1909.13719v2
- **arXiv ID**: 1909.13719v2
