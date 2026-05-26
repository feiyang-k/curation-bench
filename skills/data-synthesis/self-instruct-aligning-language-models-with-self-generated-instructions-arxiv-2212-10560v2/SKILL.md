# Self-Instruct: Aligning Language Models with Self-Generated Instructions

## One-line decision
Use this skill when you want to bootstrap instruction data from a seed set by having the model generate its own instructions iteratively. Avoid it when you have abundant human-written instructions or need domain expertise the model lacks.

## Skill metadata
- **Skill type**: self-instruction-generation
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Bootstrap instruction-following data by iteratively generating new instructions, inputs, and outputs from a seed set using the model itself, reducing reliance on human annotation.

## Problem signature
- Modality: text instructions with optional inputs and outputs.
- Data state: small seed set expanded through iterative self-generation.
- Scale regime: 175 seed → 52K generated instruction samples.
- Model requirement: Any capable LLM for self-instruction generation.

## Use when
- You need instruction data without large-scale human annotation.
- You have a small seed set of high-quality instructions.
- You want to diversify instruction coverage automatically.

## Do not use when
- You have abundant human-written instructions.
- You need domain-specific expertise the model lacks.
- Quality requirements exceed what self-generation can achieve.

## Required inputs
- **seed_instructions**: 175 hand-written seed instruction tasks.
- **generation_model**: LLM for generating new instructions and responses.
- **filtering_rules**: Rules for removing low-quality or duplicate generated instructions.

## Optional inputs
- **classification_filter**: Filter to remove classification-only tasks for diversity.

## Outputs
- **self_instruct_data**: 52K machine-generated instruction samples.
- **improved_model**: Model fine-tuned on self-generated instructions.

## Assumptions and prerequisites
- LLMs can generate diverse, valid instructions from a small seed set.
- Iterative generation expands coverage beyond the seed distribution.
- Quality filtering removes most low-quality generations.

## Procedure
1. **Start with seed instructions**
   Action: Begin with 175 hand-written instruction tasks.
   Why: Seeds provide initial diversity and quality.
   Note: See paper for details.
2. **Generate new instructions**
   Action: Prompt the model to generate new task instructions similar to but different from existing ones.
   Why: Iterative generation expands the instruction space.
   Note: See paper for details.
3. **Generate inputs and outputs**
   Action: For each new instruction, generate input-output pairs.
   Why: Complete task examples enable instruction tuning.
   Note: See paper for details.
4. **Filter generated data**
   Action: Remove duplicates, low-quality, and classification-only tasks.
   Why: Quality filtering ensures useful training data.
   Note: See paper for details.
5. **Fine-tune on generated data**
   Action: Fine-tune the base model on the 52K generated instructions.
   Why: Self-instruction tuning improves instruction following.
   Note: See paper for details.

## Parameters to set
- **seed_size** — Role: Number of seed instructions. How to set: 175 is sufficient for bootstrapping. Default/range: 175. Effect: More seeds increase initial diversity.
- **generation_rounds** — Role: Number of iterative generation rounds. How to set: Continue until desired size reached. Default/range: Until 52K. Effect: More rounds increase coverage.
- **rouge_filter** — Role: ROUGE threshold for deduplication. How to set: Filter instructions too similar to existing ones. Default/range: 0.7. Effect: Stricter filtering increases diversity.

## Validation checks
- Generated instructions should be diverse and non-trivial.
- The fine-tuned model should improve on instruction-following benchmarks.
- Quality should be reasonable compared to human-written data.

## Failure modes
- Generated instructions may lack diversity over many rounds.
- The model may generate tasks it cannot solve correctly.
- Self-reinforcing biases may compound over iterations.

## Adaptation notes for VLM training
- Self-Instruct has been adapted for visual instruction generation (LLaVA, etc.).
- Replace the LLM with Claude for potentially higher quality generation.
- The bootstrapping approach generalizes to any instruction data domain.

## Implementation notes
- Track instruction diversity metrics across generation rounds.
- Cache generated instructions for efficient deduplication.
- Monitor quality degradation over iterations.

## Evidence from the paper
- Self-Instruct generates 52K instruction samples from 175 seeds.
- GPT-3 fine-tuned on self-generated data nearly matches InstructGPT.
- The approach significantly reduces reliance on human annotation.
- Self-Instruct has become the foundation for many instruction data generation pipelines.

## Source paper
- **Title**: Self-Instruct: Aligning Language Models with Self-Generated Instructions
- **Year**: 2023
- **Venue**: ACL
- **Paper ID**: arxiv-2212.10560v2
- **URL**: http://arxiv.org/abs/2212.10560v2
- **arXiv ID**: 2212.10560v2
