# ConvNeXt V2: Co-designing and Scaling ConvNets with Masked Autoencoders

## One-line decision
Use this skill when you want to pre-train ConvNet vision encoders using masked autoencoder self-supervised learning for VLM pipelines. Avoid it when ViT-based encoders are preferred.

## Skill metadata
- **Skill type**: self-supervised-convnet-pretraining
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Pre-train ConvNet vision encoders using masked autoencoder (MAE) self-supervised learning, providing an alternative to ViT encoders for VLM vision backbones.

## Problem signature
- Modality: images for ConvNet self-supervised pretraining.
- Data state: large-scale images for self-supervised pretraining.
- Scale regime: ImageNet-22K or larger for pretraining.
- Model requirement: ConvNeXt V2 architecture with sparse convolutions for MAE.

## Use when
- You want ConvNet-based vision encoders for VLMs.
- You prefer ConvNets over ViTs.
- You want self-supervised pretraining for vision.

## Do not use when
- ViT-based encoders are preferred.
- CLIP pretraining is sufficient.
- You need the simplest encoder option.

## Required inputs
- **pretraining_images**: Large-scale images for self-supervised pretraining.
- **convnext_v2**: ConvNeXt V2 architecture with sparse convolutions.
- **mae_objective**: Masked autoencoder objective for pretraining.

## Optional inputs
- **downstream_data**: Data for fine-tuning on specific tasks.

## Outputs
- **convnext_v2_encoder**: Self-supervised ConvNet vision encoder.
- **vision_features**: Rich visual features for downstream use.

## Assumptions and prerequisites
- ConvNets can benefit from MAE-style pretraining.
- Sparse convolutions enable MAE with ConvNets.
- ConvNet features are complementary to ViT features.

## Procedure
1. **Design sparse convolutions**
   Action: Implement sparse convolutions for ConvNeXt MAE.
   Why: Standard convolutions cannot handle masked input.
   Note: See paper for details.
2. **Pre-train with MAE**
   Action: Train ConvNeXt V2 with masked autoencoder objective.
   Why: Self-supervised pretraining learns rich features.
   Note: See paper for details.
3. **Scale to large models**
   Action: Scale ConvNeXt V2 from Atto to Huge.
   Why: Larger models learn richer features.
   Note: See paper for details.
4. **Evaluate features**
   Action: Test features on downstream tasks.
   Why: Validates feature quality.
   Note: See paper for details.

## Parameters to set
- **model_scale** — Role: ConvNeXt V2 model size. How to set: Scale from Atto to Huge. Default/range: Variable. Effect: Larger models learn richer features.
- **masking_ratio** — Role: Fraction of input masked during MAE. How to set: 60% typical for images. Default/range: 60%. Effect: Higher ratio increases difficulty.

## Validation checks
- ConvNeXt V2 should produce strong visual features.
- MAE pretraining should improve over supervised pretraining.
- Features should be useful for VLM pipelines.

## Failure modes
- Sparse convolutions add implementation complexity.
- ConvNets may not scale as well as ViTs.
- MAE for ConvNets is less straightforward.

## Adaptation notes for VLM training
- ConvNeXt V2 provides an alternative vision encoder for VLMs.
- Use alongside ViT for multi-encoder VLMs (Cambrian-1).
- Self-supervised pretraining reduces data annotation needs.

## Implementation notes
- Implement sparse convolutions carefully.
- Use the ConvNeXt V2 codebase.
- Compare to ViT-based alternatives.

## Evidence from the paper
- ConvNeXt V2 enables MAE pretraining for ConvNets.
- Sparse convolutions solve the masking challenge for ConvNets.
- ConvNeXt V2 features are competitive with ViT features.
- The approach provides an alternative vision encoder for VLM pipelines.

## Source paper
- **Title**: ConvNeXt V2: Co-designing and Scaling ConvNets with Masked Autoencoders
- **Year**: 2023
- **Venue**: CVPR
- **Paper ID**: arxiv-2301.00808v2
- **URL**: http://arxiv.org/abs/2301.00808v2
- **arXiv ID**: 2301.00808v2
