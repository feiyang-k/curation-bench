# Scaling Vision Transformers to 22 Billion Parameters

## One-line decision
Use this skill when you want to scale vision transformers to 22B parameters using JFT data with efficient training techniques. Avoid it when you do not need a very large vision encoder.

## Skill metadata
- **Skill type**: scaled-vision-encoder-pretraining
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Scale Vision Transformers to 22 billion parameters using JFT-4B data with efficient training techniques, producing ViT-22B as a strong vision backbone for VLM pipelines.

## Problem signature
- Modality: images for vision transformer pretraining at extreme scale.
- Data state: JFT-4B dataset of 4 billion labeled images.
- Scale regime: 4 billion images, 22 billion parameters.
- Model requirement: ViT-22B with parallel attention, QK normalization, and other scaling modifications.

## Use when
- You need the largest possible vision encoder.
- You can afford training at 22B parameter scale.
- You need maximum visual representation quality.

## Do not use when
- Smaller ViT models are sufficient.
- You cannot afford extreme-scale training.
- Deployment constraints require smaller models.

## Required inputs
- **jft_4b**: 4 billion labeled images from JFT.
- **scaled_architecture**: ViT with scaling modifications for stability.
- **training_infrastructure**: Large-scale TPU/GPU infrastructure.

## Optional inputs
- **distillation**: Distillation to smaller models.

## Outputs
- **vit_22b**: 22B parameter vision transformer.
- **scaled_features**: Extremely rich visual representations.

## Assumptions and prerequisites
- Scaling vision transformers improves representation quality.
- JFT-4B provides sufficient data for 22B training.
- Architecture modifications enable stable training at extreme scale.

## Procedure
1. **Scale ViT architecture**
   Action: Add parallel attention, QK normalization for stable 22B training.
   Why: Standard ViT becomes unstable at extreme scale.
   Note: See paper for details.
2. **Train on JFT-4B**
   Action: Train ViT-22B on 4 billion labeled images.
   Why: Massive data is needed for massive models.
   Note: See paper for details.
3. **Evaluate representations**
   Action: Test frozen features on downstream tasks.
   Why: Validates representation quality.
   Note: See paper for details.
4. **Distill to smaller models**
   Action: Optionally distill to smaller deployable models.
   Why: Transfers knowledge to practical sizes.
   Note: See paper for details.

## Parameters to set
- **model_params** — Role: Total model parameters. How to set: 22B for maximum capability. Default/range: 22B. Effect: Larger models capture more visual information.
- **training_data** — Role: Training data for pretraining. How to set: JFT-4B for sufficient scale. Default/range: 4B images. Effect: More data enables larger models.

## Validation checks
- ViT-22B should outperform smaller ViTs on representation quality.
- Training should be stable with the scaling modifications.
- Features should transfer effectively to downstream tasks.

## Failure modes
- 22B parameters require massive compute.
- Training instability is a major risk at this scale.
- Diminishing returns from further scaling.

## Adaptation notes for VLM training
- ViT-22B features provide the richest visual representations for VLMs.
- Distillation enables practical deployment of large-scale knowledge.
- The scaling techniques are reusable for other architectures.

## Implementation notes
- Use the paper's architectural modifications for stability.
- Implement efficient distributed training.
- Monitor training loss carefully for instability signs.

## Evidence from the paper
- ViT-22B is the largest dense vision transformer at publication time.
- The model achieves state-of-the-art representation quality.
- JFT-4B provides sufficient data for training at this scale.
- Architectural modifications enable stable training at extreme scale.

## Source paper
- **Title**: Scaling Vision Transformers to 22 Billion Parameters
- **Year**: 2023
- **Venue**: ICML
- **Paper ID**: arxiv-2302.05442v1
- **URL**: http://arxiv.org/abs/2302.05442v1
- **arXiv ID**: 2302.05442v1
