# Visual Prompt Tuning

## One-line decision
Use this skill when you want to adapt a pre-trained vision model to a new task by prepending learnable visual prompt tokens, training only the prompts. Avoid it when full fine-tuning is affordable or LoRA is preferred.

## Skill metadata
- **Skill type**: parameter-efficient-visual-adaptation
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Adapt pre-trained vision models to new tasks by prepending a small number of learnable visual prompt tokens to the input, training only the prompt tokens while keeping the model frozen.

## Problem signature
- Modality: images with learnable visual prompt tokens.
- Data state: task-specific data used to train visual prompts only.
- Scale regime: any dataset; only prompt tokens are trained.
- Model requirement: Pre-trained ViT with frozen weights.

## Use when
- You want extremely parameter-efficient visual adaptation.
- You need to adapt to many tasks without full fine-tuning.
- You want to keep the vision model frozen.

## Do not use when
- Full fine-tuning is affordable.
- LoRA provides better results.
- You need to change the model architecture.

## Required inputs
- **pretrained_vit**: Frozen pre-trained ViT.
- **task_data**: Task-specific training data.
- **visual_prompts**: Learnable prompt tokens to prepend.

## Optional inputs
- **deep_prompting**: Prompts at multiple layers (VPT-Deep).

## Outputs
- **adapted_model**: Vision model adapted through visual prompts.
- **prompt_tokens**: Learned task-specific visual prompt tokens.

## Assumptions and prerequisites
- A small number of prompt tokens can adapt a frozen model.
- Visual prompting is analogous to language prompting.
- Frozen models preserve general representations.

## Procedure
1. **Initialize visual prompts**
   Action: Create learnable prompt tokens.
   Why: Prompts are the only trainable parameters.
   Note: See paper for details.
2. **Prepend to input**
   Action: Add prompts before image patch tokens.
   Why: Prompts influence model processing.
   Note: See paper for details.
3. **Train prompts only**
   Action: Train only the prompt tokens on task data.
   Why: Extremely parameter-efficient adaptation.
   Note: See paper for details.
4. **Evaluate adaptation**
   Action: Test on the target task.
   Why: Validates prompt-based adaptation.
   Note: See paper for details.

## Parameters to set
- **num_prompt_tokens** — Role: Number of visual prompt tokens. How to set: 10-100 tokens. Default/range: 50. Effect: More tokens provide more adaptation capacity.
- **prompt_depth** — Role: Where to add prompts. How to set: VPT-Shallow (input only) or VPT-Deep (all layers). Default/range: VPT-Deep. Effect: Deep prompting provides more capacity.

## Validation checks
- Prompt-tuned model should approach full fine-tuning quality.
- Only prompt tokens should be updated.
- The approach should work across diverse tasks.

## Failure modes
- Very few prompts may be insufficient.
- Some tasks may require more adaptation.
- Prompt-based adaptation may not match LoRA quality.

## Adaptation notes for VLM training
- Visual prompt tuning provides efficient VLM adaptation.
- Apply to domain-specific VLM adaptation with minimal data.
- Compare to LoRA for the best efficient adaptation method.

## Implementation notes
- Implement prompt tokens as learnable parameters.
- Use VPT-Deep for best results.
- Compare to full fine-tuning and LoRA.

## Evidence from the paper
- Visual Prompt Tuning adapts ViTs with only 0.1% trainable parameters.
- VPT matches full fine-tuning on most tasks.
- Visual prompts are analogous to language prompts for adaptation.
- The approach enables efficient multi-task VLM adaptation.

## Source paper
- **Title**: Visual Prompt Tuning
- **Year**: 2022
- **Venue**: ECCV
- **Paper ID**: arxiv-2203.12119v2
- **URL**: http://arxiv.org/abs/2203.12119v2
- **arXiv ID**: 2203.12119v2
