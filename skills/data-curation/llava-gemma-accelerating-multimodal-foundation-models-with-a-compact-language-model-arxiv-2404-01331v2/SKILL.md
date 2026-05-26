# Llava-Gemma: Accelerating Multimodal Foundation Models with a Compact Language Model

## One-line decision
Use this skill when you want to adapt the LLaVA data recipe for compact language models like Gemma-2B for efficient VLM deployment. Avoid it when you are using a larger LLM and do not need compact VLMs.

## Skill metadata
- **Skill type**: compact-vlm-data-recipe
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Adapt the standard LLaVA instruction tuning data recipe for compact language models (Gemma-2B), demonstrating that the data recipe transfers effectively to smaller, more deployable models.

## Problem signature
- Modality: standard LLaVA instruction data applied to compact LLMs.
- Data state: LLaVA instruction data used with compact language models.
- Scale regime: standard LLaVA-1.5 data recipe (665K).
- Model requirement: Gemma-2B as compact language model + CLIP ViT.

## Use when
- You want a compact VLM for efficient deployment.
- You can adapt existing data recipes to smaller models.
- You need fast inference VLMs.

## Do not use when
- You need maximum capability regardless of size.
- Compact models are too limited for your task.
- You have a custom data recipe.

## Required inputs
- **llava_data**: Standard LLaVA-1.5 instruction data (665K).
- **compact_llm**: Gemma-2B or similar compact language model.
- **clip_encoder**: CLIP ViT for visual encoding.

## Optional inputs
- **adapted_hyperparams**: Hyperparameters adapted for compact models.

## Outputs
- **llava_gemma**: Compact VLM based on Gemma-2B.
- **transfer_analysis**: Analysis of data recipe transfer to compact models.

## Assumptions and prerequisites
- Standard data recipes transfer to compact models.
- Compact models can achieve reasonable VLM capability.
- Data quality is even more important for compact models.

## Procedure
1. **Apply LLaVA data recipe**
   Action: Use the standard LLaVA-1.5 665K instruction data.
   Why: Tests recipe transferability to compact models.
   Note: See paper for details.
2. **Adapt training for compact model**
   Action: Adjust hyperparameters for Gemma-2B.
   Why: Compact models may need different training dynamics.
   Note: See paper for details.
3. **Train LLaVA-Gemma**
   Action: Train the compact VLM on the adapted recipe.
   Why: Validates data recipe transfer.
   Note: See paper for details.
4. **Evaluate efficiency**
   Action: Compare performance and efficiency to larger VLMs.
   Why: Compact models should offer efficiency advantages.
   Note: See paper for details.

## Parameters to set
- **data_recipe** — Role: Instruction data recipe. How to set: Use standard LLaVA-1.5 recipe. Default/range: LLaVA-1.5 665K. Effect: Standard recipe provides validated baseline.
- **model_size** — Role: Compact model size. How to set: Gemma-2B. Default/range: 2B. Effect: Smaller models trade capability for efficiency.

## Validation checks
- Compact VLM should achieve reasonable performance.
- Efficiency should be significantly better than large VLMs.
- Data recipe should transfer without major modifications.

## Failure modes
- 2B models have inherent capability limitations.
- Some tasks may be too hard for compact models.
- Training dynamics may differ from larger models.

## Adaptation notes for VLM training
- Standard data recipes transfer well to compact VLMs.
- Compact VLMs are practical for edge deployment.
- Data quality becomes even more critical for small models.

## Implementation notes
- Use the LLaVA codebase with Gemma backbone.
- Adjust learning rates for compact model stability.
- Compare to Phi-3V and similar compact VLMs.

## Evidence from the paper
- LLaVA-Gemma demonstrates data recipe transfer to compact models.
- Gemma-2B achieves reasonable VLM capability with standard data.
- Compact VLMs offer significant inference efficiency advantages.
- Standard instruction data recipes are broadly transferable.

## Source paper
- **Title**: Llava-Gemma: Accelerating Multimodal Foundation Models with a Compact Language Model
- **Year**: 2024
- **Venue**: arXiv
- **Paper ID**: arxiv-2404.01331v2
- **URL**: http://arxiv.org/abs/2404.01331v2
- **arXiv ID**: 2404.01331v2
