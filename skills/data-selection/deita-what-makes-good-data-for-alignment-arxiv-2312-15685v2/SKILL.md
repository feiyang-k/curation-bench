# Deita: What Makes Good Data for Alignment

## One-line decision
Use this skill when you want to select the best alignment data from a large pool using complexity and quality scoring. Avoid it when you do not have a large pool of alignment data to select from.

## Skill metadata
- **Skill type**: alignment-data-selection
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Select the most effective alignment data from a large pool by scoring each example on complexity and quality, then selecting a diverse, high-scoring subset for efficient alignment.

## Problem signature
- Modality: text instruction-response pairs scored for quality and complexity.
- Data state: large pool of alignment data scored and filtered for selection.
- Scale regime: 6K-10K selected from 300K+ candidates.
- Model requirement: Any LLM for alignment; scorers for quality and complexity.

## Use when
- You have a large pool of alignment data.
- You want to select the most effective subset.
- You can score data on quality and complexity.

## Do not use when
- Your alignment data pool is small.
- Random selection is sufficient.
- You cannot compute quality/complexity scores.

## Required inputs
- **alignment_pool**: Large pool of instruction-response pairs.
- **quality_scorer**: Model for scoring response quality.
- **complexity_scorer**: Model for scoring instruction complexity.

## Optional inputs
- **diversity_filter**: Filter for ensuring selected data diversity.

## Outputs
- **selected_data**: 6K-10K high-quality, complex alignment samples.
- **aligned_model**: Model aligned on the selected data.

## Assumptions and prerequisites
- Quality and complexity are key dimensions for alignment data value.
- A small, well-selected subset can match larger datasets.
- Scoring enables principled data selection.

## Procedure
1. **Score quality and complexity**
   Action: Score each example for response quality and instruction complexity.
   Why: Quality and complexity predict alignment value.
   Note: See paper for details.
2. **Select top examples**
   Action: Select examples with highest combined quality-complexity scores.
   Why: High-scoring examples provide the best alignment signal.
   Note: See paper for details.
3. **Ensure diversity**
   Action: Apply diversity filtering to the selected set.
   Why: Diversity prevents overfitting to specific patterns.
   Note: See paper for details.
4. **Align model**
   Action: Fine-tune the model on the selected 6K-10K examples.
   Why: Validates that selection improves alignment efficiency.
   Note: See paper for details.

## Parameters to set
- **selection_size** — Role: Number of examples to select. How to set: 6K-10K for efficient alignment. Default/range: 6K-10K. Effect: Smaller, better-selected data can match larger datasets.
- **quality_weight** — Role: Weight of quality in scoring. How to set: Balance with complexity. Default/range: Balanced. Effect: Affects which examples are selected.
- **complexity_weight** — Role: Weight of complexity in scoring. How to set: Balance with quality. Default/range: Balanced. Effect: Higher weight selects harder examples.

## Validation checks
- Selected data should outperform random selection.
- 6K-10K selected examples should match larger dataset performance.
- Quality and complexity scores should correlate with alignment value.

## Failure modes
- Scoring models may not perfectly predict alignment value.
- Small selected sets may miss important instruction types.
- Over-emphasis on complexity may select confusing examples.

## Adaptation notes for VLM training
- Apply Deita scoring to VLM instruction tuning data selection.
- Use complexity and quality scoring for any alignment data.
- The scoring approach generalizes to multimodal data.

## Implementation notes
- Train quality and complexity scorers on rated data.
- Use the Deita pipeline for reproducibility.
- Compare selected data to full data and random baselines.

## Evidence from the paper
- Deita selects 6K-10K examples that match 300K+ dataset performance.
- Quality and complexity scoring effectively identifies valuable alignment data.
- Data selection for alignment significantly improves efficiency.
- Small, well-selected datasets can match or exceed much larger ones.

## Source paper
- **Title**: Deita: What Makes Good Data for Alignment
- **Year**: 2024
- **Venue**: ICLR
- **Paper ID**: arxiv-2312.15685v2
- **URL**: http://arxiv.org/abs/2312.15685v2
- **arXiv ID**: 2312.15685v2
