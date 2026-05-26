# InstructionGPT-4: A 200-Instruction Paradigm for Fine-Tuning MiniGPT-4

## One-line decision
Use this skill when you want to align a VLM with just 200 carefully curated high-quality instruction examples, pushing the LIMA principle to multimodal. Avoid it when you have more than 200 good instruction examples available.

## Skill metadata
- **Skill type**: minimal-instruction-curation
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Demonstrate that just 200 carefully curated high-quality visual instruction examples can effectively align a VLM, extending the LIMA principle to the multimodal setting.

## Problem signature
- Modality: 200 hand-curated visual instruction-response pairs.
- Data state: 200 maximally curated visual instruction examples.
- Scale regime: 200 examples — extremely minimal.
- Model requirement: MiniGPT-4 or similar VLM for alignment.

## Use when
- You want to test the minimum viable multimodal alignment dataset.
- Extreme quality is your priority.
- 200 examples is a meaningful starting point.

## Do not use when
- 200 examples cannot cover your task diversity.
- Larger datasets are available.
- Broad instruction diversity is critical.

## Required inputs
- **curated_examples**: 200 hand-selected high-quality visual instruction examples.
- **base_vlm**: Pre-trained VLM for alignment.

## Optional inputs
- **quality_criteria**: Criteria for selecting the 200 examples.

## Outputs
- **minimal_alignment_data**: 200 curated visual instruction examples.
- **aligned_vlm**: VLM aligned with minimal data.

## Assumptions and prerequisites
- 200 examples can provide meaningful alignment signal.
- Quality vastly outweighs quantity for alignment.
- The LIMA principle extends to multimodal.

## Procedure
1. **Curate 200 examples**
   Action: Hand-select 200 maximally high-quality visual instruction examples.
   Why: Maximum quality at minimum quantity.
   Note: See paper for details.
2. **Align VLM**
   Action: Fine-tune on the 200 examples.
   Why: Tests the minimal alignment hypothesis.
   Note: See paper for details.
3. **Evaluate**
   Action: Compare to larger-dataset alignment.
   Why: Validates the approach.
   Note: See paper for details.

## Parameters to set
- **sample_count** — Role: Number of alignment examples. How to set: 200 by design. Default/range: 200. Effect: Tests the minimum viable alignment.

## Validation checks
- Aligned VLM should show improved output quality.
- Quality should approach larger-dataset alignment.
- Each of 200 examples should be genuinely high quality.

## Failure modes
- 200 examples may not cover all task types.
- Some tasks may be impossible to cover.
- The approach may only work with specific base models.

## Adaptation notes for VLM training
- Extends LIMA's quality-over-quantity principle to VLMs.
- 200 examples is a useful minimum for testing alignment.
- Use as a starting point before scaling data.

## Implementation notes
- Invest heavily in curating each example.
- Focus on diverse, high-quality examples.
- Compare to larger alignment datasets.

## Evidence from the paper
- InstructionGPT-4 shows 200 examples can align a VLM.
- Quality over quantity applies to multimodal alignment.
- The approach extends LIMA to vision-language models.
- Minimal curated data can provide meaningful alignment.

## Source paper
- **Title**: InstructionGPT-4: A 200-Instruction Paradigm for Fine-Tuning MiniGPT-4
- **Year**: 2023
- **Venue**: arXiv
- **Paper ID**: arxiv-2308.12058v2
- **URL**: http://arxiv.org/abs/2308.12058v2
- **arXiv ID**: 2308.12058v2
