# Masked Autoencoders Are Scalable Vision Learners

## One-line decision
Use this skill when you want to pre-train a ViT by masking 75% of image patches and reconstructing them, learning rich visual features. Avoid it when contrastive pretraining (CLIP, DINO) is sufficient.

## Skill metadata
- **Skill type**: masked-image-modeling-pretraining
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Pre-train Vision Transformers by masking 75% of image patches and training the model to reconstruct them, learning rich visual features through an efficient self-supervised approach.

## Problem signature
- Modality: images with masked patch reconstruction pretraining.
- Data state: ImageNet images for masked autoencoder pretraining.
- Scale regime: ImageNet scale with efficient training.
- Model requirement: ViT encoder + lightweight decoder for masked image modeling.

## Use when
- You want efficient self-supervised ViT pretraining.
- You need features from masked image modeling.
- You want to pretrain vision encoders cheaply.

## Do not use when
- Contrastive pretraining is preferred.
- You already have pretrained vision encoders.
- The downstream task favors contrastive features.

## Required inputs
- **pretraining_images**: ImageNet for MAE pretraining.
- **mae_architecture**: ViT encoder + lightweight decoder.
- **masking_strategy**: Random masking of 75% of patches.

## Optional inputs
- **downstream_data**: Data for fine-tuning evaluation.

## Outputs
- **mae_encoder**: Pre-trained ViT encoder from MAE.
- **visual_features**: Rich visual features from reconstruction.

## Assumptions and prerequisites
- Masking 75% of patches forces meaningful feature learning.
- Reconstruction teaches visual representation.
- MAE is more computationally efficient than contrastive methods.

## Procedure
1. **Mask image patches**
   Action: Randomly mask 75% of image patches.
   Why: High masking ratio forces learning.
   Note: See paper for details.
2. **Encode visible patches**
   Action: Process only visible patches with the encoder.
   Why: Efficient: only 25% of patches processed.
   Note: See paper for details.
3. **Reconstruct masked patches**
   Action: Decode to reconstruct the original image.
   Why: Reconstruction teaches visual features.
   Note: See paper for details.
4. **Use encoder for downstream**
   Action: Discard decoder; use encoder features.
   Why: Encoder features are the goal.
   Note: See paper for details.

## Parameters to set
- **mask_ratio** — Role: Fraction of patches masked. How to set: 75% for optimal learning. Default/range: 75%. Effect: Higher ratio forces more difficult reconstruction.
- **decoder_depth** — Role: Depth of the reconstruction decoder. How to set: Lightweight (2-4 layers). Default/range: 4 layers. Effect: Lightweight decoder makes training efficient.

## Validation checks
- Fine-tuned MAE should achieve strong ImageNet accuracy.
- 75% masking should outperform lower ratios.
- MAE should be more efficient than contrastive pretraining.

## Failure modes
- MAE features may differ from contrastive features.
- Fine-tuning is typically needed (unlike CLIP zero-shot).
- Reconstruction quality may not directly predict downstream quality.

## Adaptation notes for VLM training
- MAE provides EVA-style initialization for VLM vision encoders.
- MAE + CLIP combined provides complementary features.
- The efficient pretraining approach scales well.

## Implementation notes
- Use the MAE codebase for pretraining.
- Process only visible patches for efficiency.
- Compare to DINO and CLIP pretraining.

## Evidence from the paper
- MAE pre-trains ViTs by reconstructing 75% masked patches.
- The approach is significantly more efficient than contrastive methods.
- MAE features are strong after fine-tuning.
- High masking ratio (75%) is surprisingly effective.

## Source paper
- **Title**: Masked Autoencoders Are Scalable Vision Learners
- **Year**: 2022
- **Venue**: CVPR
- **Paper ID**: arxiv-2111.06377v2
- **URL**: http://arxiv.org/abs/2111.06377v2
- **arXiv ID**: 2111.06377v2
