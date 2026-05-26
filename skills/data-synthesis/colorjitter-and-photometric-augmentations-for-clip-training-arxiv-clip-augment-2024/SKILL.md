# ColorJitter and Photometric Augmentations for CLIP Training

## One-line decision
Use this skill when you want to apply photometric augmentations (color jitter, brightness, contrast) to CLIP training images for improved robustness. Avoid it when standard random crop and flip are sufficient.

## Skill metadata
- **Skill type**: photometric-augmentation-for-clip
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Apply photometric augmentations like color jittering, brightness, contrast, and saturation changes to CLIP training images for improved robustness to visual variations.

## Problem signature
- Modality: images with photometric augmentations for contrastive training.
- Data state: CLIP training images augmented with photometric transforms.
- Scale regime: any CLIP training scale.
- Model requirement: CLIP or similar contrastive model.

## Use when
- You want CLIP models robust to lighting and color changes.
- Standard crop/flip augmentation is insufficient.
- You need robustness to photometric variations.

## Do not use when
- Standard augmentation is sufficient.
- Photometric variations are not a concern.
- The augmentation is too aggressive for your task.

## Required inputs
- **training_images**: CLIP training images.
- **photometric_transforms**: Color jitter, brightness, contrast, saturation.
- **augmentation_config**: Configuration for transform intensities.

## Optional inputs
- **augmentation_probability**: Probability of applying each transform.

## Outputs
- **augmented_images**: Photometrically augmented training images.
- **robust_clip**: CLIP model robust to photometric variations.

## Assumptions and prerequisites
- Photometric augmentation improves robustness.
- Color jitter does not degrade semantic content.
- Augmentation improves zero-shot transfer.

## Procedure
1. **Configure photometric transforms**
   Action: Set color jitter parameters.
   Why: Controls augmentation intensity.
   Note: See paper for details.
2. **Apply during training**
   Action: Apply transforms randomly during CLIP training.
   Why: Creates diverse visual views.
   Note: See paper for details.
3. **Evaluate robustness**
   Action: Test on corrupted and shifted benchmarks.
   Why: Validates robustness improvement.
   Note: See paper for details.

## Parameters to set
- **jitter_strength** — Role: Intensity of color jittering. How to set: 0.2-0.4 for moderate jitter. Default/range: 0.3. Effect: Stronger jitter increases robustness.
- **brightness_range** — Role: Range of brightness variation. How to set: 0.8-1.2. Default/range: ±0.2. Effect: Covers common brightness variations.

## Validation checks
- Augmented CLIP should be more robust to visual variations.
- Clean accuracy should not significantly degrade.
- Robustness benchmarks should improve.

## Failure modes
- Too aggressive augmentation may hurt accuracy.
- Some domains may not benefit from color jitter.
- Augmentation adds minor compute overhead.

## Adaptation notes for VLM training
- Apply photometric augmentation to VLM training data preprocessing.
- Combine with geometric augmentations for comprehensive robustness.
- Standard practice for robust CLIP training.

## Implementation notes
- Use torchvision transforms for implementation.
- Apply probabilistically during training.
- Monitor both clean and robust accuracy.

## Evidence from the paper
- Photometric augmentation improves CLIP robustness to visual variations.
- Color jitter, brightness, and contrast augmentation are standard practice.
- The augmentation does not significantly hurt clean accuracy.
- Robust CLIP models transfer better to real-world conditions.

## Source paper
- **Title**: ColorJitter and Photometric Augmentations for CLIP Training
- **Year**: 2024
- **Venue**: Various
- **Paper ID**: arxiv-clip-augment-2024
- **URL**: http://arxiv.org/abs/2103.00020
- **arXiv ID**: N/A
