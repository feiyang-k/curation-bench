# LoRA: Low-Rank Adaptation of Large Language Models

## One-line decision
Use this skill when you want to efficiently fine-tune LLMs/VLMs on domain-specific data using low-rank adapter matrices instead of full fine-tuning. Avoid it when you can afford full fine-tuning or need maximum model capacity.

## Skill metadata
- **Skill type**: parameter-efficient-fine-tuning
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Enable efficient fine-tuning of large language models by adding low-rank adapter matrices to frozen pre-trained weights, dramatically reducing the number of trainable parameters while maintaining performance.

## Problem signature
- Modality: any modality; widely used for VLM fine-tuning.
- Data state: domain-specific or task-specific data for efficient fine-tuning.
- Scale regime: any fine-tuning dataset size.
- Model requirement: Any transformer-based model (LLM, VLM).

## Use when
- You want to fine-tune on domain-specific data with limited compute.
- You need parameter-efficient adaptation.
- You want to maintain multiple task-specific adapters.

## Do not use when
- Full fine-tuning is feasible and preferred.
- You need maximum model capacity for your task.
- Your model is already small enough for full fine-tuning.

## Required inputs
- **pretrained_model**: Pre-trained model to adapt.
- **fine_tuning_data**: Task-specific or domain-specific data.
- **lora_config**: Rank, target modules, and alpha configuration.

## Optional inputs
- **merge_weights**: Option to merge LoRA weights into the base model.

## Outputs
- **lora_adapters**: Small adapter weight files for each task.
- **adapted_model**: Model adapted for the specific task.

## Assumptions and prerequisites
- Weight updates during fine-tuning have low intrinsic rank.
- Low-rank adapters capture sufficient task-specific information.
- LoRA matches full fine-tuning on most tasks.

## Procedure
1. **Configure LoRA parameters**
   Action: Set rank, target modules (attention layers), and alpha.
   Why: Configuration determines adaptation capacity and efficiency.
   Note: See paper for details.
2. **Freeze base model**
   Action: Freeze all pre-trained parameters.
   Why: Only adapter parameters are trained.
   Note: See paper for details.
3. **Train LoRA adapters**
   Action: Fine-tune only the low-rank adapter matrices on task data.
   Why: Parameter-efficient training on limited data.
   Note: See paper for details.
4. **Merge or switch adapters**
   Action: Optionally merge adapters into base weights or switch between task adapters.
   Why: Merged weights have zero inference overhead.
   Note: See paper for details.

## Parameters to set
- **rank** — Role: Rank of the low-rank adaptation. How to set: 8-64 for most tasks. Default/range: 16. Effect: Higher rank increases capacity but also parameters.
- **alpha** — Role: Scaling factor for LoRA updates. How to set: Often set equal to rank or 2x rank. Default/range: 16-32. Effect: Higher alpha increases the magnitude of adaptation.
- **target_modules** — Role: Which layers get LoRA adapters. How to set: Attention layers (Q, K, V, O projections). Default/range: Attention layers. Effect: More modules increase capacity.

## Validation checks
- LoRA should match or approach full fine-tuning performance.
- Training should be significantly faster than full fine-tuning.
- Adapter sizes should be small (MBs, not GBs).

## Failure modes
- Very low rank may be insufficient for complex tasks.
- Some tasks may genuinely require full fine-tuning.
- LoRA may not work well for architectural modifications.

## Adaptation notes for VLM training
- LoRA is the standard method for VLM fine-tuning on domain-specific data.
- Use LoRA for efficient VLM adaptation to medical, scientific, or other domains.
- Combine with curated domain-specific data for targeted VLM improvement.

## Implementation notes
- Use the PEFT library for LoRA implementation.
- Start with rank 16 and adjust based on performance.
- Merge weights for deployment to avoid inference overhead.

## Evidence from the paper
- LoRA matches full fine-tuning on most NLP tasks with <0.1% of trainable parameters.
- Low-rank adapters effectively capture task-specific knowledge.
- LoRA has become the standard for parameter-efficient VLM fine-tuning.
- The approach enables maintaining multiple task-specific adapters efficiently.

## Source paper
- **Title**: LoRA: Low-Rank Adaptation of Large Language Models
- **Year**: 2022
- **Venue**: ICLR
- **Paper ID**: arxiv-2106.09685v2
- **URL**: http://arxiv.org/abs/2106.09685v2
- **arXiv ID**: 2106.09685v2
