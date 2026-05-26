# SVIT: Scaling up Visual Instruction Tuning

## One-line decision
Use this skill when you want to scale up visual instruction tuning data to 4.2M samples using GPT-4 with detailed image annotations. Avoid it when you already have sufficient instruction data or cannot afford GPT-4 generation at scale.

## Skill metadata
- **Skill type**: scaled-instruction-synthesis
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Scale visual instruction tuning data to 4.2 million samples by prompting GPT-4 with rich image annotations (captions, bounding boxes, region descriptions) from multiple sources.

## Problem signature
- Modality: images with GPT-4-generated instruction data using rich visual annotations as context.
- Data state: images with detailed annotations converted to text context for GPT-4 instruction generation.
- Scale regime: 4.2M instruction-following samples.
- Model requirement: GPT-4 for data generation; any VLM architecture for training.

## Use when
- You want to scale instruction tuning data beyond 150K-700K samples.
- You have rich image annotations (captions, boxes, region descriptions).
- You can afford GPT-4 generation at 4M+ scale.

## Do not use when
- Smaller instruction datasets are sufficient.
- You lack rich image annotations for GPT-4 context.
- GPT-4 costs at 4M scale are prohibitive.

## Required inputs
- **annotated_images**: Images with captions, bounding boxes, and region descriptions.
- **gpt4_api**: GPT-4 for generating instruction-response pairs.
- **annotation_sources**: Visual Genome, COCO, and other annotated datasets.

## Optional inputs
- **instruction_types**: Specific instruction types to emphasize.

## Outputs
- **svit_dataset**: 4.2M visual instruction samples.
- **improved_vlm**: VLM trained on scaled instruction data.

## Assumptions and prerequisites
- Rich image annotations provide sufficient context for GPT-4 to generate diverse instructions.
- Scaling instruction data beyond 700K provides meaningful improvements.
- Multiple annotation types (captions, boxes, descriptions) enable diverse instruction generation.

## Procedure
1. **Aggregate rich annotations**
   Action: Combine captions, bounding boxes, and region descriptions from multiple sources.
   Why: Rich context enables better GPT-4 instruction generation.
   Note: See paper for details.
2. **Design diverse instruction prompts**
   Action: Create prompts for conversation, detail, reasoning, and complex instructions.
   Why: Instruction diversity teaches broad capabilities.
   Note: See paper for details.
3. **Generate 4.2M instructions with GPT-4**
   Action: Run GPT-4 on all annotated images with diverse prompts.
   Why: Scales instruction data to 4.2M samples.
   Note: See paper for details.
4. **Train VLM on scaled data**
   Action: Fine-tune a VLM on the 4.2M instruction dataset.
   Why: Tests whether scaling instruction data improves performance.
   Note: See paper for details.

## Parameters to set
- **total_samples** — Role: Total instruction samples to generate. How to set: 4.2M for scaled training. Default/range: 4.2M. Effect: More data enables broader capability coverage.
- **annotation_richness** — Role: Level of annotation detail provided to GPT-4. How to set: Include captions, boxes, and region descriptions. Default/range: Multi-source annotations. Effect: Richer context produces better instructions.

## Validation checks
- 4.2M-trained model should outperform 150K-trained baseline.
- Instruction diversity should cover multiple visual reasoning types.
- Generated instructions should be grounded in the annotations.

## Failure modes
- GPT-4 may generate repetitive instructions at scale.
- Annotation errors propagate to generated instructions.
- Diminishing returns from scaling beyond a certain point.

## Adaptation notes for VLM training
- The scaling approach can be applied with Claude instead of GPT-4.
- Combine with data selection to keep only the best generated instructions.
- The multi-annotation context strategy is reusable for other VLM data generation.

## Implementation notes
- Parallelize GPT-4 API calls for scale.
- Monitor instruction diversity metrics during generation.
- Cache generated data for reproducibility.

## Evidence from the paper
- SVIT scales visual instruction tuning to 4.2M samples using GPT-4.
- Rich multi-source annotations enable diverse instruction generation.
- Scaling instruction data improves VLM performance across benchmarks.
- The dataset covers conversation, detail description, complex reasoning, and referring QA.

## Source paper
- **Title**: SVIT: Scaling up Visual Instruction Tuning
- **Year**: 2023
- **Venue**: arXiv
- **Paper ID**: arxiv-2307.04087v2
- **URL**: http://arxiv.org/abs/2307.04087v2
- **arXiv ID**: 2307.04087v2
