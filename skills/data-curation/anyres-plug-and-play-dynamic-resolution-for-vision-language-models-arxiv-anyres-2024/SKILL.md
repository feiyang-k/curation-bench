# AnyRes: Plug-and-Play Dynamic Resolution for Vision-Language Models

## One-line decision
Use this skill when you want to process images at any resolution by tiling them into patches that fit the vision encoder's native resolution. Avoid it when fixed-resolution processing is sufficient.

## Skill metadata
- **Skill type**: dynamic-resolution-processing
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Process images at any resolution by dynamically tiling them into patches that fit the vision encoder's native resolution, preserving detail without architectural changes.

## Problem signature
- Modality: images at any resolution tiled for VLM processing.
- Data state: variable-resolution images processed through dynamic tiling.
- Scale regime: any image resolution.
- Model requirement: CLIP ViT with dynamic tiling support.

## Use when
- You need to process images at variable resolutions.
- Your CLIP encoder has a fixed native resolution.
- You want to preserve detail from high-resolution images.

## Do not use when
- Fixed-resolution processing is sufficient.
- Your encoder natively handles variable resolution.
- You cannot afford multi-tile processing.

## Required inputs
- **input_images**: Images at any resolution.
- **clip_encoder**: CLIP ViT with fixed native resolution (336x336).
- **tiling_strategy**: Strategy for dividing images into tiles.

## Optional inputs
- **max_tiles**: Maximum number of tiles per image.

## Outputs
- **tiled_features**: Visual features from all tiles.
- **anyres_vlm**: VLM with dynamic resolution support.

## Assumptions and prerequisites
- Tiling preserves detail from high-resolution images.
- Multiple tiles can be efficiently processed.
- Dynamic resolution improves detail-dependent tasks.

## Procedure
1. **Determine tiling layout**
   Action: Choose how many tiles to use based on image resolution.
   Why: Adaptive tiling matches image content.
   Note: See paper for details.
2. **Tile the image**
   Action: Divide the image into tiles matching encoder resolution.
   Why: Each tile is processed at native resolution.
   Note: See paper for details.
3. **Encode tiles**
   Action: Process each tile through the CLIP encoder.
   Why: Extracts features at native resolution.
   Note: See paper for details.
4. **Aggregate features**
   Action: Combine tile features for the language model.
   Why: Aggregated features represent the full image.
   Note: See paper for details.

## Parameters to set
- **native_resolution** — Role: Encoder's native resolution. How to set: 336x336 for CLIP. Default/range: 336. Effect: Defines tile size.
- **max_tiles** — Role: Maximum tiles per image. How to set: 4-12 for balance. Default/range: 6. Effect: More tiles capture more detail.

## Validation checks
- Detail-dependent tasks should improve with more tiles.
- Image-level understanding should not degrade.
- The approach should handle diverse aspect ratios.

## Failure modes
- Tiling may fragment objects across boundaries.
- More tiles increase compute linearly.
- Tile boundaries may introduce artifacts.

## Adaptation notes for VLM training
- AnyRes is the standard dynamic resolution approach for VLMs.
- Used in LLaVA-NeXT, InternVL2, Qwen2-VL, and many others.
- Dynamic resolution is essential for document and OCR tasks.

## Implementation notes
- Implement efficient tile layout selection.
- Process tiles in batch for efficiency.
- Handle edge tiles with padding.

## Evidence from the paper
- AnyRes enables processing images at any resolution through tiling.
- Dynamic resolution significantly improves detail-dependent tasks.
- The approach requires no architectural changes to the encoder.
- AnyRes is widely adopted across modern VLMs.

## Source paper
- **Title**: AnyRes: Plug-and-Play Dynamic Resolution for Vision-Language Models
- **Year**: 2024
- **Venue**: arXiv
- **Paper ID**: arxiv-anyres-2024
- **URL**: http://arxiv.org/abs/2401.06209
- **arXiv ID**: N/A
