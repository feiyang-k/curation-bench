# Grounded SAM: Assembling Open-World Models for Diverse Visual Tasks

## One-line decision
Use this skill when you want to automatically generate grounded segmentation annotations by combining Grounding DINO for text-based detection with SAM for segmentation. Avoid it when you have manual grounding annotations or do not need automated annotation.

## Skill metadata
- **Skill type**: auto-grounding-annotation
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Automatically generate grounded segmentation annotations by chaining Grounding DINO (text-to-box detection) with SAM (box-to-mask segmentation), enabling text-prompted automatic annotation at scale.

## Problem signature
- Modality: images automatically annotated with grounded segmentation masks.
- Data state: images with text-prompted detection and segmentation annotations.
- Scale regime: unlimited automatic annotation from text descriptions.
- Model requirement: Grounding DINO + SAM chained pipeline.

## Use when
- You need automated grounding annotations at scale.
- You can describe target objects in text.
- You want both detection and segmentation annotations.

## Do not use when
- Manual annotations are available.
- You do not need grounded segmentation.
- Text descriptions cannot specify your targets.

## Required inputs
- **images**: Images to annotate.
- **text_descriptions**: Text descriptions of objects to annotate.
- **grounding_dino**: Grounding DINO for text-to-box detection.
- **sam**: SAM for box-to-mask segmentation.

## Optional inputs
- **confidence_threshold**: Threshold for detection confidence.

## Outputs
- **grounded_masks**: Segmentation masks linked to text descriptions.
- **detection_boxes**: Bounding boxes from text-based detection.

## Assumptions and prerequisites
- Text-based detection + SAM segmentation produces quality annotations.
- Chaining open-world models enables flexible annotation.
- Automated annotation scales better than manual.

## Procedure
1. **Detect with text prompts**
   Action: Use Grounding DINO to find objects matching text descriptions.
   Why: Text-based detection enables flexible targeting.
   Note: See paper for details.
2. **Segment with SAM**
   Action: Use detected boxes as SAM prompts for segmentation.
   Why: SAM produces high-quality masks from box prompts.
   Note: See paper for details.
3. **Quality filter**
   Action: Remove low-confidence detections and poor masks.
   Why: Quality filtering ensures annotation quality.
   Note: See paper for details.
4. **Use as training data**
   Action: Use grounded annotations for VLM training.
   Why: Automated annotations enable large-scale grounding data.
   Note: See paper for details.

## Parameters to set
- **detection_threshold** — Role: Minimum detection confidence. How to set: 0.3-0.5. Default/range: 0.3. Effect: Higher threshold reduces false positives.
- **text_prompt_design** — Role: How text descriptions are formatted. How to set: Simple object names or descriptions. Default/range: Object names. Effect: Prompt design affects detection quality.

## Validation checks
- Detections should match text descriptions.
- Segmentation masks should be accurate.
- The pipeline should scale to many images.

## Failure modes
- Text descriptions may be ambiguous.
- Grounding DINO may miss objects.
- SAM may produce imprecise masks.

## Adaptation notes for VLM training
- Grounded SAM is the standard auto-annotation tool for VLM data.
- Use for generating grounding training data at scale.
- Combine with VLM-generated descriptions for comprehensive annotation.

## Implementation notes
- Use the Grounded-SAM repository.
- Process images in batches.
- Validate annotations on random samples.

## Evidence from the paper
- Grounded SAM chains Grounding DINO + SAM for text-prompted annotation.
- The pipeline produces quality grounded segmentation at scale.
- Automated annotation enables large-scale grounding data creation.
- Grounded SAM is widely used for VLM data annotation.

## Source paper
- **Title**: Grounded SAM: Assembling Open-World Models for Diverse Visual Tasks
- **Year**: 2024
- **Venue**: GitHub
- **Paper ID**: github-grounded-sam-2024
- **URL**: https://github.com/IDEA-Research/Grounded-Segment-Anything
- **arXiv ID**: N/A
