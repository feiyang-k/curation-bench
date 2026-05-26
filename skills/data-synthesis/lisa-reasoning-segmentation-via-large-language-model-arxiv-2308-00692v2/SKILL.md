# LISA: Reasoning Segmentation via Large Language Model

## One-line decision
Use this skill when you want to create training data for a VLM that outputs segmentation masks through language-based reasoning. Avoid it when you do not need segmentation output or can use standard segmentation datasets.

## Skill metadata
- **Skill type**: reasoning-segmentation-data
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Create training data and a model (LISA) that combines large language model reasoning with segmentation mask output, enabling segmentation driven by complex natural language queries.

## Problem signature
- Modality: images with segmentation masks generated through language-based reasoning queries.
- Data state: reasoning segmentation data combining language instructions with segmentation targets.
- Scale regime: 239K instruction-segmentation samples.
- Model requirement: VLM (LLaVA) with SAM decoder for segmentation output.

## Use when
- You need a VLM that outputs segmentation masks.
- You want segmentation driven by complex language queries.
- You can combine VLM with a segmentation decoder.

## Do not use when
- Standard semantic segmentation meets your needs.
- You do not need language-driven segmentation.
- You cannot integrate a segmentation decoder.

## Required inputs
- **segmentation_datasets**: Existing segmentation datasets (COCO, ADE20K, etc.).
- **reasoning_instructions**: Language queries requiring reasoning to identify segmentation targets.
- **vlm_architecture**: VLM with segmentation decoder integration.

## Optional inputs
- **complex_reasoning_data**: Questions requiring multi-step reasoning for segmentation.

## Outputs
- **reasoning_seg_data**: 239K instruction-segmentation samples.
- **lisa_model**: VLM with segmentation mask output capability.

## Assumptions and prerequisites
- Complex language queries can drive more flexible segmentation.
- VLMs can learn to output segmentation masks with appropriate training data.
- Reasoning capability improves segmentation on complex queries.

## Procedure
1. **Prepare segmentation datasets**
   Action: Convert existing segmentation data into instruction format.
   Why: Reformatting enables VLM-based training.
   Note: See paper for details.
2. **Generate reasoning queries**
   Action: Create complex queries requiring reasoning to identify targets.
   Why: Reasoning queries teach beyond simple referring expressions.
   Note: See paper for details.
3. **Integrate segmentation decoder**
   Action: Add SAM decoder to VLM architecture with [SEG] token.
   Why: Enables the VLM to output segmentation masks.
   Note: See paper for details.
4. **Train on combined data**
   Action: Train on both standard and reasoning segmentation data.
   Why: Balanced training develops both direct and reasoning-based segmentation.
   Note: See paper for details.

## Parameters to set
- **seg_token** — Role: Special token triggering segmentation output. How to set: Add [SEG] token to vocabulary. Default/range: [SEG]. Effect: Bridges language generation and mask prediction.
- **seg_data_ratio** — Role: Ratio of segmentation to standard instruction data. How to set: Balance both types. Default/range: Mixed. Effect: Too much seg data may hurt general VLM capability.

## Validation checks
- Segmentation masks should accurately match the queried objects.
- Reasoning queries should produce correct segmentation.
- General VLM capabilities should be maintained.

## Failure modes
- Complex reasoning may lead to incorrect object identification.
- The segmentation decoder may produce imprecise masks.
- Integration may degrade general VLM performance.

## Adaptation notes for VLM training
- LISA's approach of adding segmentation output to VLMs is widely adopted.
- The [SEG] token pattern generalizes to other structured outputs.
- Combine reasoning segmentation with standard VLM instruction data.

## Implementation notes
- Use LoRA for efficient VLM fine-tuning with segmentation.
- Pre-train the segmentation decoder separately.
- Monitor both segmentation and VLM metrics during training.

## Evidence from the paper
- LISA enables segmentation through complex language-based reasoning.
- The model achieves strong results on reasoning segmentation benchmarks.
- The [SEG] token approach efficiently integrates segmentation into VLMs.
- 239K instruction-segmentation samples provide sufficient training signal.

## Source paper
- **Title**: LISA: Reasoning Segmentation via Large Language Model
- **Year**: 2023
- **Venue**: CVPR
- **Paper ID**: arxiv-2308.00692v2
- **URL**: http://arxiv.org/abs/2308.00692v2
- **arXiv ID**: 2308.00692v2
