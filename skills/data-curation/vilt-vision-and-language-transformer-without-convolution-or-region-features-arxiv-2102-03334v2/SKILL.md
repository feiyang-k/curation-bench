# ViLT: Vision-and-Language Transformer Without Convolution or Region Features

## One-line decision
Use this skill when you want to train a VLM that processes raw image patches without heavy vision preprocessing, using a single transformer for both modalities. Avoid it when you need strong visual features from a dedicated vision encoder.

## Skill metadata
- **Skill type**: minimal-vision-processing-vlm
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Train a vision-language model that processes raw image patches with minimal vision preprocessing, using a single transformer for both vision and language without convolutions or region features.

## Problem signature
- Modality: raw image patches + text tokens processed by a single transformer.
- Data state: standard image-text datasets processed with minimal vision preprocessing.
- Scale regime: standard VL datasets (CC3M, SBU, VG, COCO).
- Model requirement: Single transformer processing both image patches and text.

## Use when
- You want minimal vision preprocessing complexity.
- You prefer a single transformer for both modalities.
- You want fast inference without heavy vision encoders.

## Do not use when
- You need strong visual features from dedicated encoders.
- Maximum visual understanding is required.
- Region-level features are needed.

## Required inputs
- **image_text_data**: Standard image-text datasets.
- **patch_embedding**: Linear projection for image patches.
- **single_transformer**: Transformer processing both modalities.

## Optional inputs
- **pretraining_objectives**: ITM, MLM for pretraining.

## Outputs
- **vilt_model**: Minimal VLM without vision encoder.
- **fast_vlm**: Fast inference VLM.

## Assumptions and prerequisites
- Raw image patches contain sufficient visual information.
- A single transformer can process both modalities.
- Removing vision preprocessing dramatically improves efficiency.

## Procedure
1. **Embed image patches**
   Action: Linearly project image patches as input tokens.
   Why: Minimal vision preprocessing.
   Note: See paper for details.
2. **Combine with text tokens**
   Action: Process image and text tokens jointly.
   Why: Single transformer for both modalities.
   Note: See paper for details.
3. **Pretrain with VL objectives**
   Action: Train with ITM and MLM on standard VL data.
   Why: Standard VL pretraining objectives.
   Note: See paper for details.
4. **Fine-tune on downstream tasks**
   Action: Fine-tune for VQA, retrieval, etc.
   Why: Validates downstream capability.
   Note: See paper for details.

## Parameters to set
- **patch_size** — Role: Size of image patches. How to set: 32x32 or 16x16. Default/range: 32x32. Effect: Smaller patches capture more detail.
- **model_size** — Role: Transformer size. How to set: ViT-B/32 equivalent. Default/range: Base. Effect: Larger models improve but add compute.

## Validation checks
- ViLT should be significantly faster than region-based VLMs.
- Performance should be reasonable despite minimal vision processing.
- The efficiency-performance tradeoff should be favorable.

## Failure modes
- Raw patches may miss important visual details.
- No dedicated vision encoder limits visual understanding.
- Performance may lag behind encoder-based approaches.

## Adaptation notes for VLM training
- ViLT demonstrates the efficiency potential of minimal vision processing.
- The patch embedding approach influenced modern VLM designs.
- Trade-off between vision processing depth and inference speed.

## Implementation notes
- Use linear projection for patch embedding.
- Process both modalities in the same transformer.
- Compare inference speed to encoder-based VLMs.

## Evidence from the paper
- ViLT processes raw image patches without convolutions or region features.
- The approach is 10-100x faster than region-based VLMs.
- Minimal vision processing achieves reasonable VL performance.
- ViLT demonstrates the efficiency-performance tradeoff in VLM design.

## Source paper
- **Title**: ViLT: Vision-and-Language Transformer Without Convolution or Region Features
- **Year**: 2021
- **Venue**: ICML
- **Paper ID**: arxiv-2102.03334v2
- **URL**: http://arxiv.org/abs/2102.03334v2
- **arXiv ID**: 2102.03334v2
