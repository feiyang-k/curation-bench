# CogVLM: Visual Expert for Pretrained Language Models

## One-line decision
Use this skill when you want to add visual expert modules to an LLM with a two-stage data pipeline covering alignment and multi-task training. Avoid it when you are using a simpler linear projection approach.

## Skill metadata
- **Skill type**: visual-expert-data-pipeline
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Add visual expert modules to a pre-trained LLM and train them with a two-stage data pipeline: first alignment on 1.5B image-text pairs, then multi-task fine-tuning on diverse VL datasets.

## Problem signature
- Modality: image-text pairs for alignment; multi-task VL data for fine-tuning.
- Data state: two-stage data: 1.5B web pairs → multi-task VL datasets.
- Scale regime: 1.5B alignment pairs; diverse multi-task data.
- Model requirement: EVA2-CLIP-E ViT + Vicuna-v1.5 LLM with visual expert adapter.

## Use when
- You want to add deep visual understanding to an existing LLM.
- You can train visual expert modules without modifying the base LLM.
- You have access to both alignment and multi-task data.

## Do not use when
- A simple linear projection is sufficient.
- You cannot afford the compute for 1.5B pair alignment.
- You need a simpler architecture.

## Required inputs
- **alignment_data**: 1.5B image-text pairs for visual alignment.
- **multitask_data**: Diverse VL datasets for multi-task training.
- **base_llm**: Pre-trained LLM (Vicuna) to add visual capability to.

## Optional inputs
- **grounding_data**: Data with bounding box annotations for grounding.

## Outputs
- **cogvlm_model**: LLM with visual expert modules.
- **visual_expert_pipeline**: Two-stage data pipeline for adding vision to LLMs.

## Assumptions and prerequisites
- Visual expert modules can add vision without modifying the LLM.
- Two-stage training (alignment → multi-task) is effective.
- 1.5B alignment pairs provide sufficient visual grounding.

## Procedure
1. **Stage 1: Visual alignment**
   Action: Train visual expert modules on 1.5B image-text pairs.
   Why: Aligns visual features with the LLM's representation space.
   Note: See paper for details.
2. **Stage 2: Multi-task fine-tuning**
   Action: Fine-tune on diverse VL tasks (VQA, captioning, grounding, etc.).
   Why: Multi-task training develops diverse capabilities.
   Note: See paper for details.
3. **Evaluate comprehensively**
   Action: Test on VQA, captioning, grounding, and visual benchmarks.
   Why: Validates multi-task capability.
   Note: See paper for details.

## Parameters to set
- **alignment_scale** — Role: Number of image-text pairs for alignment. How to set: 1.5B for comprehensive alignment. Default/range: 1.5B. Effect: More alignment data improves visual grounding.
- **expert_architecture** — Role: Visual expert module design. How to set: Add visual expert layers in parallel to LLM layers. Default/range: Parallel expert layers. Effect: Parallel structure preserves LLM capability.

## Validation checks
- CogVLM should outperform simpler projection approaches.
- LLM capabilities should be preserved after visual expert addition.
- Multi-task performance should be strong across all tasks.

## Failure modes
- Visual expert modules add significant parameters.
- Two-stage training is computationally expensive.
- The architecture may not generalize to all LLMs.

## Adaptation notes for VLM training
- The visual expert pattern can be applied to any LLM.
- The two-stage pipeline is reusable for other VLM architectures.
- Extend with grounding data for spatial understanding.

## Implementation notes
- Freeze the base LLM during visual expert training.
- Use gradient checkpointing for memory efficiency.
- Track per-task metrics during multi-task training.

## Evidence from the paper
- CogVLM adds visual expert modules to an LLM without modifying the base model.
- Two-stage training (1.5B alignment + multi-task) produces strong VLM capabilities.
- CogVLM achieves state-of-the-art on 10+ VL benchmarks.
- The visual expert approach preserves LLM language capabilities.

## Source paper
- **Title**: CogVLM: Visual Expert for Pretrained Language Models
- **Year**: 2023
- **Venue**: arXiv
- **Paper ID**: arxiv-2311.03079v2
- **URL**: http://arxiv.org/abs/2311.03079v2
- **arXiv ID**: 2311.03079v2
