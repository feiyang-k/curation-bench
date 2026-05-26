# No Robots: A Dataset of Personally Written Instructions

## One-line decision
Use this skill when you want a dataset of 10K personally written instruction-response pairs created entirely by skilled humans, not AI. Avoid it when AI-generated instruction data is acceptable for your needs.

## Skill metadata
- **Skill type**: human-written-instruction-data
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Provide 10K high-quality instruction-response pairs written entirely by skilled human annotators, demonstrating the value of human-crafted training data over AI-generated alternatives.

## Problem signature
- Modality: text instruction-response pairs written by humans.
- Data state: 10K instruction samples personally written by skilled annotators.
- Scale regime: 10K human-written instruction samples.
- Model requirement: Any LLM for instruction tuning.

## Use when
- You want human-written instruction data.
- You value data quality and authenticity.
- You want to avoid AI-generated data artifacts.

## Do not use when
- AI-generated data is acceptable.
- You need more than 10K instruction samples.
- Human-written data is too expensive.

## Required inputs
- **skilled_annotators**: Trained writers for instruction creation.
- **writing_guidelines**: Guidelines for diverse, high-quality instructions.
- **quality_review**: Multi-stage review process.

## Optional inputs
- **category_targets**: Target categories for balanced coverage.

## Outputs
- **no_robots_data**: 10K human-written instruction samples.
- **quality_model**: Model trained on human-crafted instructions.

## Assumptions and prerequisites
- Human-written data has distinct quality advantages.
- Skilled annotators produce more natural instructions.
- 10K human samples provide meaningful training signal.

## Procedure
1. **Recruit skilled writers**
   Action: Hire trained annotators for instruction writing.
   Why: Skilled writers produce higher quality instructions.
   Note: See paper for details.
2. **Define writing guidelines**
   Action: Provide guidelines for diverse, high-quality instructions.
   Why: Guidelines ensure consistency and quality.
   Note: See paper for details.
3. **Write instructions**
   Action: Annotators personally write 10K instruction-response pairs.
   Why: Human authorship ensures authenticity.
   Note: See paper for details.
4. **Multi-stage review**
   Action: Review and refine all samples for quality.
   Why: Quality control maintains high standards.
   Note: See paper for details.

## Parameters to set
- **sample_count** — Role: Total human-written samples. How to set: 10K for meaningful coverage. Default/range: 10K. Effect: Quality matters more than quantity.
- **annotator_skill** — Role: Skill level of writers. How to set: Trained, experienced writers. Default/range: Skilled. Effect: Better writers produce better data.

## Validation checks
- Human-written data should feel more natural than AI-generated.
- Models should benefit from human-written quality.
- Coverage should span diverse instruction types.

## Failure modes
- 10K samples may not cover all instruction types.
- Human writing is expensive at scale.
- Writer biases may affect the dataset.

## Adaptation notes for VLM training
- Human-written instruction data serves as a gold standard for comparison.
- Use as a quality reference for evaluating AI-generated instruction data.
- Consider human-written visual instructions for VLM quality baseline.

## Implementation notes
- Invest in writer training and guidelines.
- Implement multi-stage quality review.
- Compare to AI-generated alternatives.

## Evidence from the paper
- No Robots provides 10K instruction samples personally written by skilled humans.
- Human-written data has distinct quality characteristics vs AI-generated.
- The dataset demonstrates the value of human craftsmanship in instruction data.
- Models trained on human data show natural instruction following.

## Source paper
- **Title**: No Robots: A Dataset of Personally Written Instructions
- **Year**: 2024
- **Venue**: arXiv
- **Paper ID**: arxiv-2312.15233v1
- **URL**: http://arxiv.org/abs/2312.15233v1
- **arXiv ID**: 2312.15233v1
