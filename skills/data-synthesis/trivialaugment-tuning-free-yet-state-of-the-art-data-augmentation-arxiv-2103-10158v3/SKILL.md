# TrivialAugment: Tuning-free Yet State-of-the-Art Data Augmentation

## One-line decision
Use this skill when you want the simplest possible automated augmentation: randomly select one transform and one magnitude per image, no tuning needed. Avoid it when you prefer tuned augmentation policies.

## Skill metadata
- **Skill type**: tuning-free-augmentation
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Provide the simplest possible automated augmentation by randomly selecting one transform and one magnitude per image, requiring zero hyperparameter tuning while matching or exceeding more complex methods.

## Problem signature
- Modality: images with single random transform augmentation.
- Data state: training images augmented with a single random transform each.
- Scale regime: any image dataset.
- Model requirement: Any image model.

## Use when
- You want the simplest augmentation approach.
- You do not want to tune augmentation hyperparameters.
- Simple baselines are surprisingly effective for your task.

## Do not use when
- Tuned policies perform significantly better.
- You have compute for augmentation search.
- Domain-specific augmentation is needed.

## Required inputs
- **training_images**: Images to augment.
- **transform_set**: Set of possible transforms.

## Optional inputs


## Outputs
- **augmented_images**: Images with single random transforms.
- **simple_model**: Model trained with trivial augmentation.

## Assumptions and prerequisites
- One random transform per image is surprisingly effective.
- Complex augmentation policies may be unnecessary.
- Zero-tuning approaches reduce development effort.

## Procedure
1. **Define transform set**
   Action: Use standard image transforms.
   Why: Standard transforms provide sufficient diversity.
   Note: See paper for details.
2. **Apply one random transform**
   Action: For each image, randomly select one transform and one magnitude.
   Why: Simplest possible augmentation.
   Note: See paper for details.
3. **Train with augmentation**
   Action: Train the model with trivially augmented data.
   Why: Validates the simple approach.
   Note: See paper for details.

## Parameters to set
- **transform_count** — Role: Number of transforms applied per image. How to set: Exactly 1. Default/range: 1. Effect: Single transform is surprisingly effective.
- **magnitude_sampling** — Role: How magnitude is sampled. How to set: Uniform over the full range. Default/range: Uniform. Effect: Random sampling requires no tuning.

## Validation checks
- Should match RandAugment and AutoAugment accuracy.
- Zero hyperparameters should be a significant simplification.
- The method should generalize across datasets.

## Failure modes
- Some datasets may need stronger augmentation.
- Single transform may be insufficient for hard tasks.
- Random selection may occasionally produce harmful augmentations.

## Adaptation notes for VLM training
- Use TrivialAugment as the default augmentation for VLM image data.
- The simplest approach often works surprisingly well.
- Compare against TrivialAugment before investing in complex augmentation.

## Implementation notes
- Implement in a single line of code.
- Use uniform magnitude sampling.
- Compare to more complex alternatives.

## Evidence from the paper
- TrivialAugment matches AutoAugment and RandAugment with zero tuning.
- One random transform per image is surprisingly effective.
- The approach is the simplest possible automated augmentation.
- TrivialAugment validates that simple baselines should always be tried.

## Source paper
- **Title**: TrivialAugment: Tuning-free Yet State-of-the-Art Data Augmentation
- **Year**: 2021
- **Venue**: ICCV
- **Paper ID**: arxiv-2103.10158v3
- **URL**: http://arxiv.org/abs/2103.10158v3
- **arXiv ID**: 2103.10158v3
