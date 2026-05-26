# LIMA: Less Is More for Alignment

## One-line decision
Use this skill when you want to align an LLM with just 1,000 carefully curated instruction examples, demonstrating that quality trumps quantity. Avoid it when you have abundant alignment data or need maximum diversity.

## Skill metadata
- **Skill type**: minimal-alignment-data
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Demonstrate that a carefully curated set of just 1,000 high-quality instruction examples is sufficient for effective LLM alignment, validating the 'less is more' principle for alignment data.

## Problem signature
- Modality: 1,000 carefully curated instruction-response pairs.
- Data state: hand-curated 1,000 high-quality instruction samples.
- Scale regime: 1,000 samples — minimal by design.
- Model requirement: LLaMA 65B for fine-tuning.

## Use when
- You want to test the minimum viable alignment dataset.
- Quality is your primary concern, not quantity.
- You can hand-curate a small number of examples.

## Do not use when
- You need maximum instruction diversity.
- 1,000 examples cannot cover your target tasks.
- You prefer larger-scale instruction tuning.

## Required inputs
- **curated_examples**: 1,000 hand-selected high-quality instruction-response pairs.
- **base_model**: Strong base LLM (LLaMA 65B).

## Optional inputs
- **quality_criteria**: Criteria for selecting the 1,000 examples.

## Outputs
- **lima_data**: 1,000 curated alignment samples.
- **lima_model**: LLM aligned with minimal data.

## Assumptions and prerequisites
- Almost all knowledge is learned during pretraining.
- Alignment needs only a small amount of high-quality data.
- Quality is far more important than quantity for alignment.

## Procedure
1. **Curate 1,000 examples**
   Action: Hand-select 1,000 high-quality instruction-response pairs.
   Why: Maximum quality with minimal quantity.
   Note: See paper for details.
2. **Source from diverse origins**
   Action: Select from StackExchange, wikiHow, Reddit, and expert writers.
   Why: Source diversity ensures broad coverage.
   Note: See paper for details.
3. **Fine-tune with minimal data**
   Action: Fine-tune LLaMA 65B on just 1,000 examples.
   Why: Tests the minimal alignment hypothesis.
   Note: See paper for details.
4. **Evaluate alignment quality**
   Action: Compare LIMA outputs to models trained on much more data.
   Why: Validates the less-is-more hypothesis.
   Note: See paper for details.

## Parameters to set
- **sample_count** — Role: Total alignment samples. How to set: 1,000 by design. Default/range: 1000. Effect: Minimal quantity; maximum quality.
- **source_diversity** — Role: Diversity of example sources. How to set: Mix StackExchange, wikiHow, expert-written. Default/range: Diverse sources. Effect: Source diversity improves coverage.

## Validation checks
- LIMA should produce aligned outputs comparable to models trained on orders of magnitude more data.
- Output quality should be high despite minimal training data.
- The model should handle diverse instruction types.

## Failure modes
- 1,000 examples may not cover all instruction types.
- The result depends heavily on the base model quality.
- Very specific or rare instructions may not be handled.

## Adaptation notes for VLM training
- LIMA's insight applies to VLM alignment: quality over quantity.
- Curate a small set of high-quality visual instruction examples.
- The less-is-more principle guides efficient VLM alignment.

## Implementation notes
- Invest heavily in curating each of the 1,000 examples.
- Select diverse sources and topics.
- Compare to larger-scale alignment baselines.

## Evidence from the paper
- LIMA demonstrates that 1,000 curated examples can effectively align a 65B model.
- Quality matters far more than quantity for alignment data.
- Almost all knowledge comes from pretraining; alignment is about style.
- LIMA outputs are competitive with models trained on 52K+ instruction samples.

## Source paper
- **Title**: LIMA: Less Is More for Alignment
- **Year**: 2023
- **Venue**: NeurIPS
- **Paper ID**: arxiv-2305.11206v1
- **URL**: http://arxiv.org/abs/2305.11206v1
- **arXiv ID**: 2305.11206v1
