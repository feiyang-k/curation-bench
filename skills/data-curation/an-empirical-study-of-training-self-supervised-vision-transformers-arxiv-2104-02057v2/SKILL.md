# An Empirical Study of Training Self-Supervised Vision Transformers

## One-line decision
Use this skill when you want to understand empirical best practices for training self-supervised ViTs (MoCo v3) including data, augmentation, and training stability. Avoid it when you are not training self-supervised vision models.

## Skill metadata
- **Skill type**: self-supervised-vit-training-recipe
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Provide empirical best practices for training self-supervised Vision Transformers, covering data augmentation, batch size, training stability, and optimization for MoCo v3.

## Problem signature
- Modality: images for self-supervised ViT pretraining.
- Data state: ImageNet images with self-supervised training recipes.
- Scale regime: ImageNet-1K scale.
- Model requirement: ViT with MoCo v3 self-supervised training.

## Use when
- You are training self-supervised ViTs.
- You need training stability guidance.
- You want empirical recipe recommendations.

## Do not use when
- You are not using self-supervised pretraining.
- CLIP-supervised training is your approach.
- You have stable training recipes.

## Required inputs
- **imagenet**: ImageNet-1K for self-supervised training.
- **moco_v3**: MoCo v3 implementation.
- **training_config**: Training hyperparameters for ablation.

## Optional inputs
- **augmentation_config**: Augmentation choices for ablation.

## Outputs
- **training_recipe**: Empirical best practices for self-supervised ViTs.
- **moco_v3_vit**: Self-supervised ViT with best recipe.

## Assumptions and prerequisites
- Self-supervised ViT training has specific best practices.
- Training stability is a key challenge.
- Empirical ablation reveals optimal recipes.

## Procedure
1. **Ablate training settings**
   Action: Vary batch size, learning rate, augmentation for self-supervised ViT.
   Why: Identifies optimal training configuration.
   Note: See paper for details.
2. **Address training instability**
   Action: Study and fix training instability issues.
   Why: Stability is critical for self-supervised ViTs.
   Note: See paper for details.
3. **Recommend best practices**
   Action: Compile empirical best practices from ablations.
   Why: Provides actionable training guidance.
   Note: See paper for details.

## Parameters to set
- **batch_size** — Role: Training batch size. How to set: 4096 for ViT-B. Default/range: 4096. Effect: Batch size affects self-supervised learning quality.
- **learning_rate** — Role: Base learning rate. How to set: Scale with batch size. Default/range: 1.5e-4 * batch/256. Effect: LR scaling is critical for stability.

## Validation checks
- Self-supervised ViT should achieve strong linear probe accuracy.
- Training should be stable without instability tricks.
- Recipes should generalize across ViT scales.

## Failure modes
- Training instability can cause divergence.
- Some settings may not transfer across datasets.
- Self-supervised features may not match supervised on some tasks.

## Adaptation notes for VLM training
- MoCo v3 recipes inform self-supervised vision encoder training for VLMs.
- Training stability insights apply to any ViT training.
- Self-supervised ViTs complement CLIP encoders in VLM pipelines.

## Implementation notes
- Use the MoCo v3 codebase.
- Monitor training loss for instability.
- Apply recommended hyperparameters.

## Evidence from the paper
- MoCo v3 provides empirical best practices for self-supervised ViT training.
- Training stability requires specific techniques.
- The recipe produces competitive self-supervised ViT features.
- Empirical ablation reveals optimal training configurations.

## Source paper
- **Title**: An Empirical Study of Training Self-Supervised Vision Transformers
- **Year**: 2021
- **Venue**: ICCV
- **Paper ID**: arxiv-2104.02057v2
- **URL**: http://arxiv.org/abs/2104.02057v2
- **arXiv ID**: 2104.02057v2
