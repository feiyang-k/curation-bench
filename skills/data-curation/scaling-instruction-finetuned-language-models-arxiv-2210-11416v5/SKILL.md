# Scaling Instruction-Finetuned Language Models

## One-line decision
Use this skill when you want to understand how to scale instruction fine-tuning across number of tasks, model size, and chain-of-thought data for maximum benefit. Avoid it when you are doing single-task fine-tuning.

## Skill metadata
- **Skill type**: instruction-finetuning-at-scale
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Study the scaling behavior of instruction fine-tuning (Flan) across three dimensions: number of tasks, model size, and inclusion of chain-of-thought data, providing guidance for optimal instruction tuning at scale.

## Problem signature
- Modality: text instruction data across 1,836 tasks.
- Data state: 1,836 tasks formatted as instructions with optional chain-of-thought.
- Scale regime: 1,836 tasks scaling up to 540B parameters.
- Model requirement: PaLM models at various scales for scaling studies.

## Use when
- You want to understand instruction tuning scaling laws.
- You are designing a multi-task instruction tuning recipe.
- You want to add chain-of-thought data to instruction tuning.

## Do not use when
- You are doing single-task fine-tuning.
- You have a fixed, small instruction dataset.
- You cannot run scaling experiments.

## Required inputs
- **task_collection**: 1,836 tasks formatted as instructions.
- **scaling_models**: Models at multiple scales for ablation.
- **cot_data**: Chain-of-thought data for selected tasks.

## Optional inputs
- **task_mixing**: Mixing ratios across task categories.

## Outputs
- **scaling_insights**: Insights on instruction tuning scaling behavior.
- **flan_palm**: Instruction-tuned PaLM models.

## Assumptions and prerequisites
- More tasks improve instruction-following generalization.
- Larger models benefit more from instruction tuning.
- Chain-of-thought data improves reasoning capabilities.

## Procedure
1. **Aggregate 1,836 tasks**
   Action: Collect and format 1,836 tasks as instruction-response pairs.
   Why: Massive task diversity improves generalization.
   Note: See paper for details.
2. **Add chain-of-thought data**
   Action: Include step-by-step reasoning for 9 tasks.
   Why: CoT data teaches reasoning process.
   Note: See paper for details.
3. **Scale across dimensions**
   Action: Vary number of tasks, model size, and CoT inclusion.
   Why: Systematic scaling reveals optimal configurations.
   Note: See paper for details.
4. **Evaluate generalization**
   Action: Test on held-out tasks and benchmarks.
   Why: Measures instruction-following generalization.
   Note: See paper for details.

## Parameters to set
- **num_tasks** — Role: Number of instruction tasks. How to set: As many as available. Default/range: 1836. Effect: More tasks improve generalization.
- **model_scale** — Role: Model parameter count. How to set: Larger models benefit more. Default/range: 8B-540B. Effect: Larger models show bigger gains from instruction tuning.
- **cot_inclusion** — Role: Whether to include chain-of-thought data. How to set: Include CoT for reasoning tasks. Default/range: 9 CoT tasks. Effect: CoT significantly improves reasoning.

## Validation checks
- More tasks should improve held-out task performance.
- Larger models should show bigger gains from instruction tuning.
- CoT data should improve reasoning benchmarks.

## Failure modes
- Too many low-quality tasks may dilute training signal.
- Task mixing ratios need careful tuning.
- CoT benefits may be limited to reasoning-specific tasks.

## Adaptation notes for VLM training
- Flan's scaling insights apply to VLM instruction tuning.
- Include CoT data for VLM reasoning improvement.
- The task diversity principle applies to multimodal instruction data.

## Implementation notes
- Use Flan templates for instruction formatting.
- Balance task sampling during training.
- Track per-task performance for analysis.

## Evidence from the paper
- Scaling instruction tuning to 1,836 tasks significantly improves generalization.
- Larger models benefit more from instruction tuning.
- Chain-of-thought data substantially improves reasoning capabilities.
- Flan-PaLM 540B achieves state-of-the-art on multiple benchmarks.

## Source paper
- **Title**: Scaling Instruction-Finetuned Language Models
- **Year**: 2022
- **Venue**: JMLR
- **Paper ID**: arxiv-2210.11416v5
- **URL**: http://arxiv.org/abs/2210.11416v5
- **arXiv ID**: 2210.11416v5
