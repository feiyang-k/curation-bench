# LLaVA-OneVision: Easy Visual Task Transfer

## One-line decision
Use this skill when you want a unified training recipe for single-image, multi-image, and video understanding with curated data at each stage. Avoid it when you only need single-image understanding.

## Skill metadata
- **Skill type**: unified-visual-task-data
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Design a unified training recipe covering single-image, multi-image, and video understanding with carefully curated data at each training stage, enabling easy transfer across visual tasks.

## Problem signature
- Modality: images and videos with unified instruction data across task types.
- Data state: curated data spanning single-image, multi-image, and video instruction tasks.
- Scale regime: millions of curated instruction samples across modalities.
- Model requirement: SigLIP-SO400M ViT + Qwen-2 LLM with AnyRes.

## Use when
- You want a unified model for image and video understanding.
- You need curated data across multiple visual modalities.
- You want to enable easy transfer across visual tasks.

## Do not use when
- Single-image understanding is sufficient.
- You cannot curate multi-modality data.
- You need specialized task-specific models.

## Required inputs
- **single_image_data**: Instruction data for single-image understanding.
- **multi_image_data**: Instruction data for multi-image understanding.
- **video_data**: Instruction data for video understanding.

## Optional inputs
- **cross_modal_data**: Data requiring understanding across modalities.

## Outputs
- **onevision_model**: Unified VLM for single-image, multi-image, and video.
- **unified_data_recipe**: Data curation recipe for cross-modal training.

## Assumptions and prerequisites
- Unified training benefits all visual modalities.
- Careful data curation at each stage prevents interference.
- AnyRes handles diverse input formats efficiently.

## Procedure
1. **Stage 1: Single-image pre-training**
   Action: Train on curated single-image instruction data.
   Why: Foundation of visual understanding.
   Note: See paper for details.
2. **Stage 2: Multi-modality training**
   Action: Add multi-image and video data to training.
   Why: Extends capability to multi-modal understanding.
   Note: See paper for details.
3. **Data balance optimization**
   Action: Optimize data mixing ratios across modalities.
   Why: Prevents any modality from dominating training.
   Note: See paper for details.
4. **Evaluate across modalities**
   Action: Test on single-image, multi-image, and video benchmarks.
   Why: Validates unified capability.
   Note: See paper for details.

## Parameters to set
- **stage_data** — Role: Data used at each training stage. How to set: Curate progressively from single to multi-modal. Default/range: Stage-specific. Effect: Progressive training builds capabilities sequentially.
- **modality_balance** — Role: Balance between image and video data. How to set: Tune to prevent modality interference. Default/range: Task-dependent. Effect: Balance affects per-modality performance.

## Validation checks
- Single-image performance should not degrade with multi-modal training.
- Video understanding should benefit from unified training.
- Transfer between visual tasks should be demonstrable.

## Failure modes
- Multi-modal training may cause interference.
- Data imbalance may favor one modality.
- Unified models may not match specialized models on specific tasks.

## Adaptation notes for VLM training
- The unified training recipe is a template for cross-modal VLMs.
- Data curation insights transfer to other multi-modal settings.
- Progressive training prevents catastrophic forgetting.

## Implementation notes
- Use stage-wise training with careful data transitions.
- Monitor per-modality metrics throughout training.
- Leverage AnyRes for handling diverse input sizes.

## Evidence from the paper
- LLaVA-OneVision achieves strong performance across single-image, multi-image, and video.
- Unified training with curated data enables easy task transfer.
- Progressive training prevents interference between modalities.
- The model achieves state-of-the-art on multiple benchmarks simultaneously.

## Source paper
- **Title**: LLaVA-OneVision: Easy Visual Task Transfer
- **Year**: 2024
- **Venue**: arXiv
- **Paper ID**: arxiv-2408.03326v2
- **URL**: http://arxiv.org/abs/2408.03326v2
- **arXiv ID**: 2408.03326v2
