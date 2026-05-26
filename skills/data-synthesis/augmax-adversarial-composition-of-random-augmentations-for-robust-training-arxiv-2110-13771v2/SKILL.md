# AugMax: Adversarial Composition of Random Augmentations for Robust Training

## One-line decision
Use this skill when you want to combine random augmentations with adversarial training for improved robustness to distribution shifts. Avoid it when standard augmentation provides sufficient robustness.

## Skill metadata
- **Skill type**: adversarial-augmentation
- **Paper kind**: operational-method
- **Actionability**: medium
- **Evidence quality**: full_paper

## Goal
Combine random data augmentation with adversarial training by finding the worst-case mixture of augmented views for each training example, improving robustness to both synthetic corruptions and natural distribution shifts.

## Problem signature
- Modality: images with adversarially composed augmentations.
- Data state: training images augmented with adversarially selected compositions of transforms.
- Scale regime: any image classification dataset.
- Model requirement: Any differentiable image model.

## Use when
- You need robustness to distribution shifts.
- Standard augmentation does not provide sufficient robustness.
- You can afford the computational cost of adversarial augmentation.

## Do not use when
- Standard augmentation is sufficient.
- You cannot afford adversarial training cost.
- Robustness is not a priority.

## Required inputs
- **training_images**: Image dataset for training.
- **augmentation_set**: Set of random augmentations.
- **adversarial_objective**: Objective for finding worst-case augmentation mixtures.

## Optional inputs
- **dirichlet_prior**: Prior for augmentation mixing weights.

## Outputs
- **robust_model**: Model trained with adversarial augmentation composition.
- **augmented_data**: Adversarially composed augmented training images.

## Assumptions and prerequisites
- Worst-case augmentation mixtures improve robustness.
- Adversarial composition is more effective than random composition.
- The additional compute cost is justified by improved robustness.

## Procedure
1. **Generate augmented views**
   Action: Create multiple augmented views of each training image.
   Why: Multiple views provide candidates for adversarial selection.
   Note: See paper for details.
2. **Find worst-case mixture**
   Action: Optimize the mixture weights to find the worst-case combination.
   Why: Worst-case training improves robustness.
   Note: See paper for details.
3. **Train with adversarial augmentation**
   Action: Train the model on the adversarially composed augmentations.
   Why: Adversarial training improves robustness to distribution shifts.
   Note: See paper for details.
4. **Evaluate robustness**
   Action: Test on corrupted and shifted test sets.
   Why: Validates robustness improvements.
   Note: See paper for details.

## Parameters to set
- **num_augmented_views** — Role: Number of augmented views per image. How to set: 3-5 views. Default/range: 3. Effect: More views enable better adversarial selection.
- **adversarial_steps** — Role: Steps for finding worst-case mixture. How to set: 1-5 optimization steps. Default/range: 1. Effect: More steps find harder mixtures.

## Validation checks
- Robustness should improve on corrupted and shifted test sets.
- Clean accuracy should not degrade significantly.
- The adversarial augmentation should find meaningfully harder examples.

## Failure modes
- Adversarial training increases compute cost significantly.
- Optimizing mixture weights adds complexity.
- May overfit to specific corruption types.

## Adaptation notes for VLM training
- AugMax can be applied to VLM image encoder pretraining for robustness.
- The adversarial composition idea extends to multimodal augmentation.
- Combine with standard augmentation for comprehensive robustness.

## Implementation notes
- Implement adversarial optimization efficiently.
- Monitor robustness metrics during training.
- Compare against RandAugment and AugMax baselines.

## Evidence from the paper
- AugMax combines random augmentation with adversarial training for robustness.
- The adversarial composition finds harder training examples than random.
- AugMax improves robustness to both synthetic corruptions and natural shifts.
- The approach is complementary to standard augmentation methods.

## Source paper
- **Title**: AugMax: Adversarial Composition of Random Augmentations for Robust Training
- **Year**: 2021
- **Venue**: NeurIPS
- **Paper ID**: arxiv-2110.13771v2
- **URL**: http://arxiv.org/abs/2110.13771v2
- **arXiv ID**: 2110.13771v2
