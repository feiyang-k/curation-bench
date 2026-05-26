# VILA: On Pre-training for Visual Language Models

## One-line decision
Use this skill when you want systematic ablation insights on VLM pretraining choices: frozen vs unfrozen LLM, interleaved vs paired data, text mixing. Avoid it when you have a well-established pretraining recipe.

## Skill metadata
- **Skill type**: vlm-pretraining-ablation
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Provide systematic ablation insights on VLM pretraining choices including whether to freeze the LLM, whether to use interleaved data, and how much text to mix in, guiding optimal VLM pretraining recipes.

## Problem signature
- Modality: ablation studies on VLM pretraining data choices.
- Data state: controlled pretraining experiments varying data and training choices.
- Scale regime: ablation at various scales.
- Model requirement: LLaVA-style VLM for ablation studies.

## Use when
- You are designing a VLM pretraining recipe.
- You want principled guidance on pretraining choices.
- You can run ablation experiments.

## Do not use when
- You have a proven pretraining recipe.
- You cannot run ablations.
- Single-stage fine-tuning is your approach.

## Required inputs
- **paired_data**: Image-text pairs for pretraining.
- **interleaved_data**: Interleaved image-text documents.
- **text_data**: Text-only data for mixing.
- **ablation_budget**: Compute for systematic ablations.

## Optional inputs
- **instruction_data**: Instruction data for fine-tuning stage.

## Outputs
- **pretraining_insights**: Systematic ablation results on pretraining choices.
- **vila_model**: VLM trained with optimal recipe.

## Assumptions and prerequisites
- Systematic ablation reveals optimal pretraining choices.
- Data type mixing significantly affects performance.
- Freezing vs unfreezing the LLM matters for pretraining.

## Procedure
1. **Ablate LLM freezing**
   Action: Compare frozen vs unfrozen LLM during pretraining.
   Why: Freezing affects both efficiency and capability.
   Note: See paper for details.
2. **Ablate data types**
   Action: Compare paired, interleaved, and mixed data.
   Why: Data type significantly affects capability.
   Note: See paper for details.
3. **Ablate text mixing**
   Action: Vary the ratio of text-only data in pretraining.
   Why: Text data helps preserve language capability.
   Note: See paper for details.
4. **Identify optimal recipe**
   Action: Combine best choices from ablations.
   Why: Optimal recipe maximizes VLM quality.
   Note: See paper for details.

## Parameters to set
- **llm_state** — Role: Whether LLM is frozen during pretraining. How to set: Unfreezing generally helps. Default/range: Unfrozen. Effect: Unfreezing improves visual understanding at risk of language degradation.
- **interleaved_fraction** — Role: Fraction of interleaved data. How to set: Include for few-shot capability. Default/range: 10-30%. Effect: Interleaved data enables in-context learning.
- **text_fraction** — Role: Fraction of text-only data. How to set: 10-20% preserves language. Default/range: 10-20%. Effect: Prevents language capability degradation.

## Validation checks
- Each ablation should show clear performance differences.
- The optimal recipe should outperform default choices.
- Insights should generalize across model sizes.

## Failure modes
- Ablation results may not transfer to all architectures.
- Small-scale ablations may not predict large-scale behavior perfectly.
- Interaction effects between choices may be complex.

## Adaptation notes for VLM training
- VILA's ablation insights guide VLM pretraining recipe design.
- The key findings: unfreeze LLM, include interleaved data, mix text data.
- Ablation methodology is reusable for any VLM pretraining.

## Implementation notes
- Run ablations at consistent smaller scales.
- Track multiple metrics for comprehensive comparison.
- Document all ablation configurations for reproducibility.

## Evidence from the paper
- VILA demonstrates that unfreezing the LLM during pretraining significantly helps.
- Interleaved data is important for in-context visual learning.
- Mixing text-only data prevents language capability degradation.
- Systematic ablation provides principled VLM recipe guidance.

## Source paper
- **Title**: VILA: On Pre-training for Visual Language Models
- **Year**: 2024
- **Venue**: CVPR
- **Paper ID**: arxiv-2312.07533v4
- **URL**: http://arxiv.org/abs/2312.07533v4
- **arXiv ID**: 2312.07533v4
