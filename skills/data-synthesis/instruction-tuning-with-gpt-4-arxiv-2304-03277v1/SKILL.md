# Instruction Tuning with GPT-4

## One-line decision
Use this skill when you want to generate high-quality instruction data using GPT-4 for fine-tuning smaller models. Avoid it when you cannot afford GPT-4 API calls or have sufficient human-written data.

## Skill metadata
- **Skill type**: gpt4-instruction-distillation
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Generate high-quality instruction-following data using GPT-4, producing both English and Chinese instruction datasets for training smaller models.

## Problem signature
- Modality: text instruction-response pairs from GPT-4.
- Data state: 52K GPT-4-generated instruction-response pairs.
- Scale regime: 52K instruction samples.
- Model requirement: GPT-4 for generation; any LLM for fine-tuning.

## Use when
- You want high-quality instruction data from GPT-4.
- You need instruction data in English and Chinese.
- You are fine-tuning a smaller model.

## Do not use when
- You cannot afford GPT-4 API calls.
- You have sufficient human-written instruction data.
- You need domain-specific instructions GPT-4 cannot generate.

## Required inputs
- **gpt4_api**: GPT-4 for generating instruction-response pairs.
- **seed_instructions**: Seed instructions for prompting GPT-4.
- **language_config**: Configuration for English and/or Chinese generation.

## Optional inputs
- **quality_filter**: Filter for removing low-quality generations.

## Outputs
- **gpt4_instructions**: 52K GPT-4-generated instruction samples.
- **fine_tuned_model**: Model trained on GPT-4 instruction data.

## Assumptions and prerequisites
- GPT-4 generates higher quality instruction data than GPT-3.5.
- Quality instruction data from GPT-4 enables effective distillation.
- Both English and Chinese benefit from GPT-4 instruction generation.

## Procedure
1. **Design instruction prompts**
   Action: Create prompts for diverse instruction generation.
   Why: Prompt design controls instruction diversity and quality.
   Note: See paper for details.
2. **Generate with GPT-4**
   Action: Use GPT-4 to generate instruction-response pairs.
   Why: GPT-4 produces higher quality than weaker models.
   Note: See paper for details.
3. **Quality filter**
   Action: Remove low-quality or harmful generations.
   Why: Basic filtering ensures data quality.
   Note: See paper for details.
4. **Fine-tune smaller model**
   Action: Train a smaller model on GPT-4 instruction data.
   Why: Distills GPT-4's instruction-following to a smaller model.
   Note: See paper for details.

## Parameters to set
- **generation_model** — Role: LLM for instruction generation. How to set: Use GPT-4 for highest quality. Default/range: GPT-4. Effect: Better teacher produces better instruction data.
- **sample_count** — Role: Number of instruction samples. How to set: 52K for diverse coverage. Default/range: 52K. Effect: More samples improve instruction diversity.

## Validation checks
- GPT-4-generated data should produce better students than GPT-3.5 data.
- Instruction quality should be higher than Self-Instruct.
- The fine-tuned model should follow diverse instructions.

## Failure modes
- GPT-4 API costs are significant.
- Generated data inherits GPT-4's biases.
- Some instruction types may be poorly generated.

## Adaptation notes for VLM training
- Extend to visual instruction generation for VLMs.
- Replace GPT-4 with Claude for alternative instruction generation.
- Combine with Evol-Instruct for complexity scaling.

## Implementation notes
- Batch API calls for cost efficiency.
- Generate in both English and Chinese for multilingual coverage.
- Compare GPT-4 vs GPT-3.5 instruction quality.

## Evidence from the paper
- GPT-4 instruction data produces significantly better student models than GPT-3.5 data.
- 52K GPT-4-generated instructions cover diverse task types.
- The quality gap between GPT-4 and GPT-3.5 instruction data is significant.
- Instruction tuning with GPT-4 data is a standard practice.

## Source paper
- **Title**: Instruction Tuning with GPT-4
- **Year**: 2023
- **Venue**: arXiv
- **Paper ID**: arxiv-2304.03277v1
- **URL**: http://arxiv.org/abs/2304.03277v1
- **arXiv ID**: 2304.03277v1
