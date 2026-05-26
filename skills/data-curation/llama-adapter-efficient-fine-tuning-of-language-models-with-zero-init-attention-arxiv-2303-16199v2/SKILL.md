# LLaMA-Adapter: Efficient Fine-tuning of Language Models with Zero-init Attention

## One-line decision
Use this skill when you want to efficiently add visual instruction-following to LLaMA using lightweight adapters with zero-initialized attention. Avoid it when full fine-tuning is feasible or you prefer other PEFT methods.

## Skill metadata
- **Skill type**: adapter-based-vlm-training
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Add visual instruction-following capability to LLaMA using lightweight zero-initialized attention adapters, enabling efficient multimodal fine-tuning with only 1.2M learnable parameters.

## Problem signature
- Modality: visual instruction data for adapter-based VLM training.
- Data state: standard visual instruction data used with lightweight adapters.
- Scale regime: 52K instruction samples.
- Model requirement: LLaMA with zero-initialized attention adapters.

## Use when
- You want extremely parameter-efficient VLM training.
- You prefer adapter-based approaches.
- You have limited compute for VLM training.

## Do not use when
- Full fine-tuning is feasible.
- You prefer LoRA or other PEFT methods.
- Maximum performance is needed regardless of efficiency.

## Required inputs
- **base_llama**: Pre-trained LLaMA model.
- **visual_encoder**: CLIP visual encoder for image features.
- **instruction_data**: Visual instruction-following data.

## Optional inputs
- **adapter_config**: Adapter architecture configuration.

## Outputs
- **llama_adapter**: LLaMA with visual adapters.
- **efficient_vlm**: VLM with only 1.2M trainable parameters.

## Assumptions and prerequisites
- Zero-initialized attention prevents harmful early-stage interference.
- 1.2M parameters are sufficient for adding visual capability.
- Adapters enable efficient multi-task switching.

## Procedure
1. **Add zero-init attention adapters**
   Action: Insert lightweight adapters with zero initialization.
   Why: Zero-init prevents harmful interference during early training.
   Note: See paper for details.
2. **Connect visual encoder**
   Action: Link CLIP encoder to the adapters.
   Why: Visual features flow through adapters to the LLM.
   Note: See paper for details.
3. **Fine-tune adapters only**
   Action: Train only the 1.2M adapter parameters.
   Why: Extremely parameter-efficient training.
   Note: See paper for details.
4. **Evaluate visual instruction following**
   Action: Test on visual conversation benchmarks.
   Why: Validates adapter-based VLM capability.
   Note: See paper for details.

## Parameters to set
- **adapter_params** — Role: Total adapter parameters. How to set: ~1.2M. Default/range: 1.2M. Effect: Minimal parameters for visual capability.
- **zero_init** — Role: Initialization strategy. How to set: Zero-initialize adapter attention. Default/range: Zero. Effect: Prevents early training interference.

## Validation checks
- The VLM should follow visual instructions with only 1.2M trainable parameters.
- Zero-init should improve training stability.
- Adapter-based VLM should approach full fine-tuning quality.

## Failure modes
- 1.2M parameters may limit complex reasoning.
- Adapters may not capture all visual information.
- Zero-init may slow convergence.

## Adaptation notes for VLM training
- Zero-init adapters provide an extremely efficient VLM training approach.
- The adapter pattern enables multi-task VLM without full retraining.
- Combine with LoRA for more capacity.

## Implementation notes
- Implement zero-initialized attention correctly.
- Use the LLaMA-Adapter codebase.
- Compare to LoRA and full fine-tuning baselines.

## Evidence from the paper
- LLaMA-Adapter adds visual capability with only 1.2M trainable parameters.
- Zero-initialized attention prevents harmful early training interference.
- The approach demonstrates extremely parameter-efficient VLM training.
- Adapter-based VLMs can be fine-tuned in minutes on a single GPU.

## Source paper
- **Title**: LLaMA-Adapter: Efficient Fine-tuning of Language Models with Zero-init Attention
- **Year**: 2023
- **Venue**: arXiv
- **Paper ID**: arxiv-2303.16199v2
- **URL**: http://arxiv.org/abs/2303.16199v2
- **arXiv ID**: 2303.16199v2
