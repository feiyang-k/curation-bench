# mPLUG-Owl: Modularization Empowers Large Language Models with Multimodality

## One-line decision
Use this skill when you want a modular VLM training approach using visual abstractor and two-stage training on alignment then instruction data. Avoid it when you prefer simpler projection approaches.

## Skill metadata
- **Skill type**: modular-vlm-data-pipeline
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Train a modular VLM using a visual abstractor module with two-stage training: first on image-text alignment data, then on instruction data with both visual and text-only instructions.

## Problem signature
- Modality: image-text alignment data + visual and text instruction data.
- Data state: two-stage data: image-text pairs → visual + text instructions.
- Scale regime: stage 1: image-text alignment; stage 2: instruction tuning.
- Model requirement: CLIP ViT + visual abstractor + LLaMA.

## Use when
- You want modular VLM architecture with visual abstractor.
- You follow a two-stage training approach.
- You mix visual and text-only instruction data.

## Do not use when
- Simple projection is sufficient.
- You prefer single-stage training.
- You do not need the visual abstractor module.

## Required inputs
- **alignment_data**: Image-text pairs for stage 1 alignment.
- **visual_instructions**: Visual instruction-following data.
- **text_instructions**: Text-only instruction data for LLM preservation.

## Optional inputs
- **visual_abstractor_config**: Configuration for the visual abstractor.

## Outputs
- **mplug_owl**: Modular VLM with visual abstractor.
- **training_pipeline**: Two-stage training pipeline.

## Assumptions and prerequisites
- A visual abstractor provides better visual compression than linear projection.
- Two-stage training builds capabilities progressively.
- Mixing visual and text instructions preserves LLM quality.

## Procedure
1. **Stage 1: Visual alignment**
   Action: Train visual abstractor on image-text alignment data.
   Why: Aligns visual features with the LLM's space.
   Note: See paper for details.
2. **Stage 2: Instruction tuning**
   Action: Fine-tune on both visual and text-only instructions.
   Why: Builds instruction-following while preserving language.
   Note: See paper for details.
3. **Evaluate comprehensively**
   Action: Test on both visual and language benchmarks.
   Why: Validates dual capability.
   Note: See paper for details.

## Parameters to set
- **abstractor_tokens** — Role: Number of visual tokens from abstractor. How to set: 65 for good compression. Default/range: 65. Effect: Fewer tokens compress vision; more tokens preserve detail.
- **text_instruction_ratio** — Role: Fraction of text-only instructions. How to set: Mix visual and text instructions. Default/range: Balanced. Effect: Text instructions preserve LLM capability.

## Validation checks
- Visual understanding should be strong after two-stage training.
- Language capability should be preserved.
- The visual abstractor should outperform linear projection.

## Failure modes
- The visual abstractor adds architectural complexity.
- Two-stage training requires more compute.
- Balancing visual and text data needs tuning.

## Adaptation notes for VLM training
- The modular approach enables flexible VLM customization.
- Visual abstractors are used in many subsequent VLMs.
- Two-stage training is a standard VLM recipe.

## Implementation notes
- Implement the visual abstractor with cross-attention.
- Balance visual and text instruction ratios.
- Monitor both visual and language metrics.

## Evidence from the paper
- mPLUG-Owl demonstrates effective modular VLM training.
- The visual abstractor compresses visual information effectively.
- Two-stage training builds capabilities progressively.
- Mixing visual and text instructions preserves LLM quality.

## Source paper
- **Title**: mPLUG-Owl: Modularization Empowers Large Language Models with Multimodality
- **Year**: 2023
- **Venue**: arXiv
- **Paper ID**: arxiv-2304.14178v2
- **URL**: http://arxiv.org/abs/2304.14178v2
- **arXiv ID**: 2304.14178v2
