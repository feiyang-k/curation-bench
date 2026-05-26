# Ferret: Refer and Ground Anything Anywhere at Any Granularity

## One-line decision
Use this skill when you want to create training data for a VLM that can both refer to and ground objects at point, box, and free-form region granularities. Avoid it when you only need image-level understanding without spatial referring.

## Skill metadata
- **Skill type**: spatial-referring-data
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Generate training data for a VLM that handles spatial referring and grounding at multiple granularities (points, bounding boxes, free-form regions), enabling both input and output spatial understanding.

## Problem signature
- Modality: images with spatial referring and grounding annotations at multiple granularities.
- Data state: instruction data with spatial annotations including points, boxes, and free-form regions.
- Scale regime: 1.1M instruction samples with spatial annotations.
- Model requirement: CLIP ViT + LLaMA with hybrid region representation.

## Use when
- You need a VLM that can understand and produce spatial references.
- You want multi-granularity spatial understanding (point, box, region).
- You need training data with diverse spatial annotation types.

## Do not use when
- Image-level understanding is sufficient.
- You do not need spatial input/output capabilities.
- You cannot generate spatial annotations for your data.

## Required inputs
- **spatially_annotated_images**: Images with bounding boxes, points, and region masks.
- **instruction_generator**: Pipeline for creating spatial referring and grounding instructions.
- **spatial_format**: Format for encoding spatial references in text.

## Optional inputs
- **free_form_regions**: Free-form region annotations beyond bounding boxes.

## Outputs
- **ferret_data**: 1.1M spatial instruction samples.
- **ferret_model**: VLM with multi-granularity spatial understanding.

## Assumptions and prerequisites
- Multi-granularity spatial annotations teach richer spatial understanding.
- Both referring (input spatial reference) and grounding (output spatial reference) are needed.
- Free-form regions provide finer spatial specification than boxes.

## Procedure
1. **Collect spatially annotated data**
   Action: Gather images with diverse spatial annotations from multiple sources.
   Why: Diverse spatial annotations enable multi-granularity training.
   Note: See paper for details.
2. **Generate referring instructions**
   Action: Create instructions that include spatial references as input.
   Why: Teaches the model to understand spatial references.
   Note: See paper for details.
3. **Generate grounding instructions**
   Action: Create instructions requiring the model to output spatial locations.
   Why: Teaches the model to produce spatial references.
   Note: See paper for details.
4. **Train with hybrid representation**
   Action: Train the model with a hybrid representation supporting points, boxes, and regions.
   Why: Multi-granularity representation enables flexible spatial understanding.
   Note: See paper for details.

## Parameters to set
- **spatial_granularities** — Role: Types of spatial references. How to set: Include points, boxes, and free-form regions. Default/range: 3 types. Effect: More granularities improve spatial flexibility.
- **referring_vs_grounding** — Role: Balance between referring and grounding data. How to set: Include both types. Default/range: Balanced. Effect: Both capabilities are needed for comprehensive spatial understanding.

## Validation checks
- The model should correctly interpret spatial references at all granularities.
- Grounding output should accurately localize referred objects.
- Multi-granularity should outperform box-only approaches.

## Failure modes
- Free-form regions are harder to annotate and evaluate.
- Spatial format encoding may limit precision.
- The model may default to box-level granularity.

## Adaptation notes for VLM training
- Ferret's spatial data generation approach applies to any VLM needing grounding.
- Multi-granularity data is reusable for other spatial VLMs.
- Combine with standard instruction data for balanced training.

## Implementation notes
- Use a continuous coordinate representation for spatial references.
- Implement efficient region encoding for free-form shapes.
- Track per-granularity performance.

## Evidence from the paper
- Ferret creates 1.1M instruction samples with multi-granularity spatial annotations.
- The model handles referring and grounding at point, box, and region granularities.
- Multi-granularity training improves both spatial understanding and general VLM performance.
- Ferret achieves strong results on referring expression and grounding benchmarks.

## Source paper
- **Title**: Ferret: Refer and Ground Anything Anywhere at Any Granularity
- **Year**: 2023
- **Venue**: ICLR
- **Paper ID**: arxiv-2310.07704v2
- **URL**: http://arxiv.org/abs/2310.07704v2
- **arXiv ID**: 2310.07704v2
