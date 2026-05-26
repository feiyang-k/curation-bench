# Osprey: Pixel Understanding with Visual Instruction Tuning

## One-line decision
Use this skill when you want to create pixel-level instruction tuning data where the VLM can understand and describe individual pixel regions in images. Avoid it when bounding box-level understanding is sufficient.

## Skill metadata
- **Skill type**: pixel-level-instruction-data
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Create pixel-level instruction tuning data where the VLM can understand, describe, and reason about individual pixel regions specified by segmentation masks.

## Problem signature
- Modality: images with pixel-level mask-based instruction data.
- Data state: instruction data with pixel-level region specifications using masks.
- Scale regime: 724K pixel-level instruction samples.
- Model requirement: VLM with mask-based region input capability.

## Use when
- You need pixel-level visual understanding in VLMs.
- You can provide segmentation masks as input.
- You need region-level instruction data.

## Do not use when
- Bounding box regions are sufficient.
- You cannot generate segmentation masks.
- Image-level understanding is adequate.

## Required inputs
- **images_with_masks**: Images with segmentation masks for regions.
- **pixel_instruction_generator**: Pipeline for generating pixel-level instructions.
- **mask_encoder**: Encoder for processing pixel-level masks.

## Optional inputs
- **sam_masks**: SAM-generated masks for automatic segmentation.

## Outputs
- **pixel_instruction_data**: 724K pixel-level instruction samples.
- **osprey_model**: VLM with pixel-level understanding.

## Assumptions and prerequisites
- Pixel-level regions provide finer granularity than bounding boxes.
- Mask-based input enables precise region specification.
- Pixel-level instructions teach fine-grained understanding.

## Procedure
1. **Generate region masks**
   Action: Create segmentation masks for image regions using SAM or annotations.
   Why: Masks define pixel-level regions.
   Note: See paper for details.
2. **Generate pixel-level instructions**
   Action: Create instructions about specific masked regions.
   Why: Exercises pixel-level understanding.
   Note: See paper for details.
3. **Train with mask input**
   Action: Train the VLM to accept masks as input and understand regions.
   Why: Enables pixel-level visual understanding.
   Note: See paper for details.
4. **Evaluate pixel-level understanding**
   Action: Test on region-level QA and description tasks.
   Why: Validates pixel-level capability.
   Note: See paper for details.

## Parameters to set
- **instruction_count** — Role: Total pixel-level instructions. How to set: 724K for comprehensive coverage. Default/range: 724K. Effect: More data improves pixel-level understanding.
- **mask_source** — Role: Source of segmentation masks. How to set: SAM for automatic; annotations for quality. Default/range: Mixed. Effect: Mask quality affects training.

## Validation checks
- The model should accurately describe masked regions.
- Pixel-level should outperform box-level on fine-grained tasks.
- Masks should correctly specify intended regions.

## Failure modes
- Mask quality varies with segmentation method.
- Pixel-level processing increases compute.
- Some regions may be too small for meaningful description.

## Adaptation notes for VLM training
- Pixel-level instruction data extends VLM granularity beyond boxes.
- Combine with box-level and image-level data for comprehensive training.
- SAM provides efficient mask generation for data creation.

## Implementation notes
- Use SAM for efficient mask generation.
- Implement mask-to-token encoding.
- Track per-granularity performance.

## Evidence from the paper
- Osprey creates 724K pixel-level instruction samples with mask-based input.
- Pixel-level understanding enables finer granularity than bounding boxes.
- The model describes, reasons about, and classifies individual pixel regions.
- Pixel-level VLMs are valuable for detailed visual understanding.

## Source paper
- **Title**: Osprey: Pixel Understanding with Visual Instruction Tuning
- **Year**: 2024
- **Venue**: CVPR
- **Paper ID**: arxiv-2312.10032v2
- **URL**: http://arxiv.org/abs/2312.10032v2
- **arXiv ID**: 2312.10032v2
