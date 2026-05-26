# Magpie: Alignment Data Synthesis from Scratch by Prompting Aligned LLMs with Nothing

## One-line decision
Use this skill when you want to generate instruction data by prompting an aligned LLM with just the system prompt to elicit user-like instructions from the model itself. Avoid it when you have instruction data or prefer structured generation approaches.

## Skill metadata
- **Skill type**: template-free-instruction-generation
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Generate instruction-following data by prompting an aligned LLM with just the system prompt and empty user turn, causing the model to generate realistic user instructions from its alignment training, bypassing the need for seed instructions.

## Problem signature
- Modality: text instruction-response pairs generated from model's alignment.
- Data state: instructions generated from the model's inherent alignment training.
- Scale regime: millions of instruction samples generated cheaply.
- Model requirement: Aligned LLM (Llama-3-Instruct or similar) for instruction generation.

## Use when
- You want to generate instruction data without seed instructions.
- You have access to an aligned LLM.
- You want a simple, scalable instruction generation method.

## Do not use when
- You have high-quality seed instructions.
- You need domain-specific instructions the model hasn't seen.
- The aligned LLM lacks the capabilities you need.

## Required inputs
- **aligned_llm**: Instruction-tuned LLM (Llama-3-Instruct, etc.).
- **system_prompt**: System prompt that triggers instruction generation.
- **generation_config**: Temperature, sampling parameters for diverse generation.

## Optional inputs
- **quality_filter**: Filter for removing low-quality generations.
- **topic_guidance**: Optional topic steering for targeted generation.

## Outputs
- **magpie_data**: Large-scale instruction-response pairs.
- **instruction_analysis**: Analysis of generated instruction distribution.

## Assumptions and prerequisites
- Aligned LLMs have learned the distribution of user instructions.
- Prompting with just the system prompt elicits this distribution.
- Generated instructions are realistic and diverse.

## Procedure
1. **Prepare system prompt**
   Action: Use the standard system prompt for the aligned LLM.
   Why: The system prompt primes the model for instruction generation.
   Note: See paper for details.
2. **Generate user instructions**
   Action: Prompt with system message only, letting the model generate user instructions.
   Why: The model's alignment training causes it to generate realistic instructions.
   Note: See paper for details.
3. **Generate responses**
   Action: Feed generated instructions back to the model for response generation.
   Why: Complete instruction-response pairs are needed for training.
   Note: See paper for details.
4. **Filter and curate**
   Action: Remove duplicates, low-quality, and harmful instruction-response pairs.
   Why: Quality filtering ensures useful training data.
   Note: See paper for details.

## Parameters to set
- **temperature** — Role: Sampling temperature for generation. How to set: 0.7-1.0 for diverse instructions. Default/range: 1.0. Effect: Higher temperature increases diversity.
- **generation_scale** — Role: Number of instructions to generate. How to set: Generate millions; filter for quality. Default/range: Millions. Effect: More generation allows more aggressive filtering.
- **filter_criteria** — Role: Quality criteria for keeping instructions. How to set: Remove too-short, repetitive, or harmful. Default/range: Multi-criteria. Effect: Stricter filtering improves quality at the cost of quantity.

## Validation checks
- Generated instructions should be diverse and realistic.
- Models trained on Magpie data should match or exceed seed-instruction-based methods.
- The instruction distribution should cover diverse topics and styles.

## Failure modes
- The model may generate repetitive instruction patterns.
- Some generated instructions may be trivial or low-quality.
- The distribution may be biased toward the model's alignment data.

## Adaptation notes for VLM training
- Extend Magpie to visual instruction generation for VLMs.
- Use with multimodal aligned models for generating visual instructions.
- Combine with quality filtering for high-quality instruction data.

## Implementation notes
- Use vLLM for efficient batch generation.
- Generate more than needed and filter aggressively.
- Analyze instruction topic distribution for balance.

## Evidence from the paper
- Magpie generates instruction data by prompting aligned LLMs with just the system prompt.
- The approach bypasses the need for seed instructions entirely.
- Models trained on Magpie data match or exceed those trained on standard instruction data.
- The method is simple, scalable, and surprisingly effective.

## Source paper
- **Title**: Magpie: Alignment Data Synthesis from Scratch by Prompting Aligned LLMs with Nothing
- **Year**: 2024
- **Venue**: arXiv
- **Paper ID**: arxiv-2406.08464v3
- **URL**: http://arxiv.org/abs/2406.08464v3
- **arXiv ID**: 2406.08464v3
