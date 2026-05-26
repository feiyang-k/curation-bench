# Unnatural Instructions: Tuning Language Models with (Almost) No Human Labor

## One-line decision
Use this skill when you want to generate diverse instruction data by prompting an LLM with creative seed constraints for novel instruction types. Avoid it when standard self-instruct provides sufficient diversity.

## Skill metadata
- **Skill type**: unnatural-instruction-generation
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Generate diverse instruction data by prompting an LLM with creative constraints that produce 'unnatural' but effective instruction-response pairs, expanding beyond the distribution of standard seed instructions.

## Problem signature
- Modality: text instruction-response pairs from creative LLM prompting.
- Data state: 64K instruction samples generated through creative prompting.
- Scale regime: 64K creative instruction samples.
- Model requirement: InstructGPT or similar for generation.

## Use when
- You want instruction data beyond standard templates.
- You need creative, diverse instruction types.
- Standard self-instruct lacks diversity.

## Do not use when
- Standard instruction generation is sufficient.
- You need domain-specific instructions.
- Creative instructions may confuse your model.

## Required inputs
- **generation_model**: LLM for creative instruction generation.
- **creative_prompts**: Prompts designed to elicit novel instruction types.
- **quality_filter**: Filter for removing incoherent generations.

## Optional inputs
- **expansion_templates**: Templates for expanding instructions.

## Outputs
- **unnatural_instructions**: 64K creative instruction samples.
- **diverse_model**: Model fine-tuned on diverse instructions.

## Assumptions and prerequisites
- Creative prompting produces more diverse instructions.
- Unusual instructions teach broader instruction-following.
- Diversity matters as much as quality for instruction data.

## Procedure
1. **Design creative prompts**
   Action: Create prompts that elicit unusual instruction types.
   Why: Creative constraints produce diverse instructions.
   Note: See paper for details.
2. **Generate instructions**
   Action: Run the LLM with creative prompts.
   Why: Generates novel instruction-response pairs.
   Note: See paper for details.
3. **Filter and expand**
   Action: Remove bad generations and expand good ones.
   Why: Quality control and augmentation.
   Note: See paper for details.
4. **Fine-tune on diverse data**
   Action: Train a model on the creative instruction data.
   Why: Validates diversity benefit.
   Note: See paper for details.

## Parameters to set
- **creative_constraints** — Role: Types of creative constraints. How to set: Include format, domain, reasoning constraints. Default/range: Diverse. Effect: More creative constraints produce more diverse data.
- **expansion_factor** — Role: How much to expand each instruction. How to set: 3-5 variants per instruction. Default/range: 3-5x. Effect: Expansion increases diversity further.

## Validation checks
- Generated instructions should be genuinely diverse.
- The model should handle unusual instruction types.
- Diversity should improve over standard approaches.

## Failure modes
- Creative constraints may produce incoherent instructions.
- Unusual instructions may not be useful for practical tasks.
- Quality may be lower than carefully curated data.

## Adaptation notes for VLM training
- Apply creative instruction generation to visual instruction data.
- Extend to multimodal creative instruction types.
- Combine with standard instructions for balanced training.

## Implementation notes
- Design creative prompts carefully for quality.
- Filter aggressively for coherence.
- Compare to standard self-instruct baselines.

## Evidence from the paper
- Unnatural Instructions generates 64K creative instruction samples.
- Diverse instructions teach broader instruction-following capability.
- The approach reduces reliance on human-written instruction templates.
- Creative generation produces instruction types not found in standard datasets.

## Source paper
- **Title**: Unnatural Instructions: Tuning Language Models with (Almost) No Human Labor
- **Year**: 2023
- **Venue**: ACL
- **Paper ID**: arxiv-2212.09689v2
- **URL**: http://arxiv.org/abs/2212.09689v2
- **arXiv ID**: 2212.09689v2
