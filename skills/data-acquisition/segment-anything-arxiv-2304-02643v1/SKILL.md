# Segment Anything

## One-line decision
Use this skill when you need to build a billion-scale segmentation mask dataset using a model-in-the-loop interactive annotation approach. Avoid it when you need text-grounded segmentation rather than prompt-based mask generation.

## Skill metadata
- **Skill type**: interactive-annotation-at-scale
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Build SA-1B, a dataset of 1.1 billion segmentation masks on 11 million images, using a model-in-the-loop data annotation engine where the SAM model assists human annotators and eventually generates masks automatically.

## Problem signature
- Modality: images with segmentation masks generated through model-assisted annotation.
- Data state: progressively annotated: manual → model-assisted → fully automatic mask generation.
- Scale regime: 1.1 billion masks on 11 million images.
- Model requirement: SAM (ViT-H) promptable segmentation model.

## Use when
- You need a large-scale segmentation dataset for pretraining.
- You want to use model-in-the-loop annotation to scale data collection.
- You need masks for diverse objects beyond standard detection categories.

## Do not use when
- You need text-grounded or semantic segmentation with class labels.
- You only need a few thousand annotated images.
- You need 3D or temporal segmentation.

## Required inputs
- **licensed_images**: 11M diverse, high-resolution images.
- **annotation_tool**: Interactive annotation tool with SAM model assistance.
- **sam_model**: Progressively trained SAM model for mask generation.

## Optional inputs
- **quality_review**: Human review of automatically generated masks.

## Outputs
- **sa_1b_dataset**: 1.1 billion segmentation masks on 11M images.
- **sam_model**: Trained promptable segmentation model.

## Assumptions and prerequisites
- Model-in-the-loop annotation can scale to billions of masks.
- Progressive automation (manual → assisted → automatic) maintains quality while increasing speed.
- Diverse prompts (points, boxes, masks) enable comprehensive segmentation.

## Procedure
1. **Phase 1: Manual annotation with SAM**
   Action: Human annotators create masks with SAM's interactive segmentation.
   Why: Bootstraps initial training data and validates the tool.
   Note: See paper for details.
2. **Phase 2: Model-assisted annotation**
   Action: SAM proposes masks that annotators refine.
   Why: Increases annotation speed 6x while maintaining quality.
   Note: See paper for details.
3. **Phase 3: Fully automatic annotation**
   Action: SAM generates masks automatically with a grid of point prompts.
   Why: Scales to billions of masks without human involvement.
   Note: See paper for details.
4. **Train SAM iteratively**
   Action: Retrain SAM on accumulated annotations between phases.
   Why: Progressive training improves mask quality.
   Note: See paper for details.
5. **Release SA-1B dataset**
   Action: Package and release the 1.1B mask dataset.
   Why: Enables downstream research and applications.
   Note: See paper for details.

## Parameters to set
- **prompt_grid_density** — Role: Density of automatic point prompts. How to set: 32x32 grid per image for comprehensive coverage. Default/range: 32x32. Effect: Denser grids find more objects but increase compute.
- **mask_quality_threshold** — Role: Minimum predicted IoU for keeping a mask. How to set: Filter low-confidence masks. Default/range: Model-dependent. Effect: Higher threshold keeps fewer but better masks.
- **nms_threshold** — Role: Non-maximum suppression overlap threshold. How to set: Standard NMS settings. Default/range: 0.7. Effect: Controls overlap between final masks.

## Validation checks
- Mask quality should be comparable to manually annotated datasets.
- Coverage should include diverse object types beyond standard categories.
- The dataset should enable strong zero-shot segmentation.

## Failure modes
- Automatic masks may miss small or occluded objects.
- Over-segmentation may produce too many fragmented masks.
- Class-agnostic masks lack semantic labels.

## Adaptation notes for VLM training
- SA-1B masks are widely used for VLM training data augmentation.
- Combine SAM masks with VLM-generated captions for grounded data.
- Use SAM as an annotation tool for constructing region-level VLM data.

## Implementation notes
- Use the SAM model in ONNX format for efficient inference.
- Process images in batches for the automatic phase.
- Store masks in the efficient RLE format.

## Evidence from the paper
- SA-1B contains 1.1 billion masks on 11M images, 400x larger than any existing segmentation dataset.
- Model-in-the-loop annotation achieves 6x speedup in the assisted phase.
- SAM achieves strong zero-shot segmentation across diverse image types.
- The dataset and model have become foundational tools for computer vision.

## Source paper
- **Title**: Segment Anything
- **Year**: 2023
- **Venue**: ICCV
- **Paper ID**: arxiv-2304.02643v1
- **URL**: http://arxiv.org/abs/2304.02643v1
- **arXiv ID**: 2304.02643v1
