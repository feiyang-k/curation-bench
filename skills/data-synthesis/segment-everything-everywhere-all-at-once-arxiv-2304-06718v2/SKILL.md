# Segment Everything Everywhere All at Once

## One-line decision
Use this skill when you want a unified segmentation model trained on diverse segmentation data types (semantic, instance, panoptic, interactive) for VLM grounding. Avoid it when you only need one segmentation type.

## Skill metadata
- **Skill type**: unified-segmentation-data
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Train a unified segmentation model on diverse segmentation data types (semantic, instance, panoptic, interactive) using a single architecture, providing comprehensive grounding capability for VLMs.

## Problem signature
- Modality: images with diverse segmentation annotation types.
- Data state: combined semantic, instance, panoptic, and interactive segmentation data.
- Scale regime: combined data from multiple segmentation datasets.
- Model requirement: SEEM architecture for unified segmentation.

## Use when
- You need unified segmentation across multiple types.
- You want a single model for all segmentation tasks.
- You need comprehensive VLM grounding data.

## Do not use when
- One segmentation type is sufficient.
- Specialized models are preferred.
- You do not need segmentation.

## Required inputs
- **semantic_seg_data**: Semantic segmentation datasets.
- **instance_seg_data**: Instance segmentation datasets.
- **panoptic_seg_data**: Panoptic segmentation datasets.
- **interactive_data**: Interactive segmentation data (click, box, text prompts).

## Optional inputs
- **referring_data**: Referring expression segmentation data.

## Outputs
- **seem_model**: Unified segmentation model.
- **unified_seg_data**: Combined segmentation data for training.

## Assumptions and prerequisites
- Diverse segmentation types can be unified.
- A single model handles all segmentation tasks.
- Unified training improves each task.

## Procedure
1. **Combine segmentation data**
   Action: Merge semantic, instance, panoptic, and interactive segmentation datasets.
   Why: Unified data enables unified training.
   Note: See paper for details.
2. **Design unified architecture**
   Action: Create SEEM architecture handling all segmentation types.
   Why: One architecture for all types.
   Note: See paper for details.
3. **Train unified model**
   Action: Train on combined segmentation data.
   Why: Unified training develops comprehensive capability.
   Note: See paper for details.
4. **Evaluate all types**
   Action: Test on benchmarks for each segmentation type.
   Why: Validates comprehensive capability.
   Note: See paper for details.

## Parameters to set
- **seg_types** — Role: Types of segmentation included. How to set: Include semantic, instance, panoptic, interactive. Default/range: All types. Effect: More types enable more comprehensive segmentation.
- **prompt_types** — Role: Types of prompts supported. How to set: Click, box, text, mask. Default/range: Multiple. Effect: More prompts enable flexible interaction.

## Validation checks
- Unified model should be competitive on each segmentation type.
- All prompt types should work correctly.
- No segmentation type should degrade significantly.

## Failure modes
- Unified training may compromise specialized performance.
- Some segmentation types may dominate.
- Architecture complexity increases.

## Adaptation notes for VLM training
- SEEM provides comprehensive segmentation for VLM grounding.
- Unified segmentation data supports versatile VLM spatial understanding.
- Combine with VLM instruction data for grounding capability.

## Implementation notes
- Use the SEEM codebase for unified segmentation.
- Balance training across segmentation types.
- Evaluate on per-type benchmarks.

## Evidence from the paper
- SEEM unifies semantic, instance, panoptic, and interactive segmentation.
- A single model handles all segmentation types and prompts.
- Unified training is competitive with specialized models.
- SEEM provides comprehensive grounding for VLM pipelines.

## Source paper
- **Title**: Segment Everything Everywhere All at Once
- **Year**: 2023
- **Venue**: NeurIPS
- **Paper ID**: arxiv-2304.06718v2
- **URL**: http://arxiv.org/abs/2304.06718v2
- **arXiv ID**: 2304.06718v2
