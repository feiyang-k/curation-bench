# GLaMM: Pixel Grounding Large Multimodal Model

## One-line decision
Use this skill when you want to create training data for a VLM that generates text grounded at the pixel level with segmentation masks. Avoid it when you do not need pixel-level grounding in VLM outputs.

## Skill metadata
- **Skill type**: grounded-conversation-data
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Create GranD, a large-scale grounded conversation dataset with 7.5M unique image concepts, 810M regions, and dense grounding annotations linking text to pixel-level segmentation masks.

## Problem signature
- Modality: images with text grounded to pixel-level segmentation masks.
- Data state: grounded conversation data with pixel-level segmentation annotations.
- Scale regime: 7.5M image concepts, 810M regions, 11M images.
- Model requirement: VLM with pixel grounding decoder (SAM-based).

## Use when
- You need pixel-level grounding in VLM outputs.
- You want grounded conversation data at scale.
- You need dense region annotations with descriptions.

## Do not use when
- Bounding box grounding is sufficient.
- You do not need pixel-level grounding.
- You cannot process segmentation data.

## Required inputs
- **images**: 11M images for annotation.
- **automated_annotation**: Pipeline for generating region descriptions and masks.
- **grounding_decoder**: SAM-based decoder for pixel grounding.

## Optional inputs
- **human_validation**: Spot-check of automated annotations.

## Outputs
- **grand_dataset**: GranD dataset with 810M regions and pixel grounding.
- **glamm_model**: VLM with pixel-level grounded conversation.

## Assumptions and prerequisites
- Pixel-level grounding provides finer spatial understanding than boxes.
- Automated annotation can produce quality grounding at scale.
- Dense grounding improves VLM spatial reasoning.

## Procedure
1. **Generate region proposals and masks**
   Action: Use SAM to generate region masks for images.
   Why: SAM provides high-quality segmentation at scale.
   Note: See paper for details.
2. **Generate region descriptions**
   Action: Create text descriptions for each region.
   Why: Descriptions link text to visual regions.
   Note: See paper for details.
3. **Create grounded conversations**
   Action: Generate conversation data with inline pixel grounding.
   Why: Grounded conversations teach pixel-level understanding.
   Note: See paper for details.
4. **Train GLaMM**
   Action: Train a VLM with pixel grounding decoder on GranD.
   Why: Validates the dataset for pixel-level grounding.
   Note: See paper for details.

## Parameters to set
- **num_regions** — Role: Total region annotations. How to set: 810M for comprehensive coverage. Default/range: 810M. Effect: More regions improve grounding.
- **grounding_granularity** — Role: Level of spatial grounding. How to set: Pixel-level segmentation masks. Default/range: Pixel-level. Effect: Pixel grounding is finer than box grounding.

## Validation checks
- Pixel grounding should be accurate.
- Grounded conversations should be coherent and informative.
- The model should correctly link text to visual regions.

## Failure modes
- SAM masks may be over-segmented.
- Region descriptions may not match mask content.
- Pixel grounding adds computational cost.

## Adaptation notes for VLM training
- GranD provides the largest grounded VLM training dataset.
- Pixel grounding extends box grounding for finer spatial understanding.
- Combine with standard instruction data for balanced training.

## Implementation notes
- Use SAM for efficient mask generation.
- Cache region masks and descriptions.
- Monitor grounding accuracy on samples.

## Evidence from the paper
- GLaMM creates GranD with 810M regions and pixel-level grounding on 11M images.
- Pixel-level grounding enables finer spatial understanding than bounding boxes.
- The automated annotation pipeline produces quality grounding at scale.
- GLaMM achieves state-of-the-art on grounded conversation benchmarks.

## Source paper
- **Title**: GLaMM: Pixel Grounding Large Multimodal Model
- **Year**: 2023
- **Venue**: CVPR
- **Paper ID**: arxiv-2311.03356v2
- **URL**: http://arxiv.org/abs/2311.03356v2
- **arXiv ID**: 2311.03356v2
