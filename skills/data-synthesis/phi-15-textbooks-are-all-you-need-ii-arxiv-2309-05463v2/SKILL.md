# Phi-1.5: Textbooks Are All You Need II

## One-line decision
Use this skill when you want to generate synthetic textbook-quality training data to teach reasoning to small language models. Avoid it when you are training a large model where data quality filtering alone suffices.

## Skill metadata
- **Skill type**: synthetic-textbook-for-reasoning
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Generate synthetic textbook-quality training data using a strong LLM to teach common-sense reasoning to a 1.3B parameter model, demonstrating that data quality can substitute for scale.

## Problem signature
- Modality: synthetic textbook-quality text for reasoning training.
- Data state: LLM-generated educational content for reasoning training.
- Scale regime: 30B tokens of synthetic and filtered data.
- Model requirement: Phi-1.5 1.3B parameter model.

## Use when
- You want to teach reasoning to a small model.
- You can generate synthetic educational content.
- Data quality matters more than quantity.

## Do not use when
- You are training a very large model.
- You have sufficient high-quality reasoning data.
- Synthetic data generation is too expensive.

## Required inputs
- **synthetic_generator**: Strong LLM for generating textbook content.
- **quality_filters**: Filters for selecting educational-quality content.
- **base_model**: Small model (1.3B) for training.

## Optional inputs
- **web_filtered**: Heavily filtered web data supplement.

## Outputs
- **synthetic_textbooks**: Synthetic textbook-quality training data.
- **phi_1_5**: 1.3B model with strong reasoning.

## Assumptions and prerequisites
- Textbook-quality data teaches reasoning more effectively.
- Synthetic generation can produce educational content.
- Small models benefit most from high-quality data.

## Procedure
1. **Generate synthetic textbooks**
   Action: Use a strong LLM to generate educational text.
   Why: Creates textbook-quality training data.
   Note: See paper for details.
2. **Filter web data**
   Action: Select educational content from web data.
   Why: Supplements synthetic data with real content.
   Note: See paper for details.
3. **Combine data sources**
   Action: Mix synthetic and filtered data.
   Why: Both contribute complementary quality.
   Note: See paper for details.
4. **Train Phi-1.5**
   Action: Train the 1.3B model on curated data.
   Why: Validates quality-over-quantity approach.
   Note: See paper for details.

## Parameters to set
- **synthetic_fraction** — Role: Fraction of synthetic data. How to set: Significant fraction. Default/range: Large. Effect: More synthetic data improves reasoning.
- **total_tokens** — Role: Total training tokens. How to set: 30B. Default/range: 30B. Effect: Quality matters more than token count at small scale.

## Validation checks
- Phi-1.5 should outperform larger models on reasoning.
- Synthetic data should improve reasoning benchmarks.
- The approach should be cost-effective.

## Failure modes
- Synthetic data may lack diversity.
- Small models have inherent limitations.
- Quality filtering is expensive.

## Adaptation notes for VLM training
- Apply synthetic textbook generation to VLM visual reasoning training.
- Use quality-focused data curation for small VLMs.
- The approach validates data quality over quantity.

## Implementation notes
- Generate diverse educational content.
- Validate reasoning quality on benchmarks.
- Compare to web-only baselines.

## Evidence from the paper
- Phi-1.5 (1.3B) achieves reasoning comparable to much larger models through data quality.
- Synthetic textbook data is more effective than raw web data for reasoning.
- Data quality can substitute for model scale.
- 30B high-quality tokens outperform much larger low-quality corpora.

## Source paper
- **Title**: Phi-1.5: Textbooks Are All You Need II
- **Year**: 2023
- **Venue**: arXiv
- **Paper ID**: arxiv-2309.05463v2
- **URL**: http://arxiv.org/abs/2309.05463v2
- **arXiv ID**: 2309.05463v2
