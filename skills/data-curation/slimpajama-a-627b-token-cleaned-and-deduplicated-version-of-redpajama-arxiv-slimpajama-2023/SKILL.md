# SlimPajama: A 627B Token Cleaned and Deduplicated Version of RedPajama

## One-line decision
Use this skill when you want to build a cleaned and deduplicated open text corpus from RedPajama for LLM pretraining. Avoid it when you already have a sufficient clean text corpus.

## Skill metadata
- **Skill type**: dedup-and-clean-web-corpus
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Create SlimPajama, a 627B token cleaned and deduplicated version of the 1.2T token RedPajama dataset, through aggressive deduplication and quality filtering.

## Problem signature
- Modality: text from RedPajama after cleaning and deduplication.
- Data state: RedPajama text cleaned and deduplicated from 1.2T to 627B tokens.
- Scale regime: 627B tokens from original 1.2T.
- Model requirement: Any LLM for pretraining.

## Use when
- You want a clean, deduplicated open text corpus.
- You need an alternative to The Pile or C4.
- You want transparent data processing.

## Do not use when
- You already have a clean text corpus.
- You need more than 627B unique tokens.
- You need domain-specific text.

## Required inputs
- **redpajama**: 1.2T token RedPajama dataset.
- **dedup_pipeline**: Exact and near-duplicate removal pipeline.
- **quality_filters**: Text quality filtering pipeline.

## Optional inputs
- **additional_filters**: Domain or quality-specific filters.

## Outputs
- **slimpajama**: 627B token cleaned text corpus.
- **dedup_report**: Deduplication statistics and analysis.

## Assumptions and prerequisites
- ~48% of RedPajama is duplicated or low quality.
- Deduplication significantly improves training efficiency.
- 627B clean tokens are better than 1.2T noisy tokens.

## Procedure
1. **Exact deduplication**
   Action: Remove exact duplicate documents from RedPajama.
   Why: Exact duplicates waste training compute.
   Note: See paper for details.
2. **Near-deduplication with MinHash**
   Action: Apply MinHash for fuzzy duplicate removal.
   Why: Near-duplicates add little unique information.
   Note: See paper for details.
3. **Quality filtering**
   Action: Remove low-quality text using heuristic filters.
   Why: Quality filtering improves remaining text.
   Note: See paper for details.
4. **Validate with LLM training**
   Action: Train LLMs on SlimPajama and compare to RedPajama.
   Why: End-to-end validation proves cleaning value.
   Note: See paper for details.

## Parameters to set
- **dedup_method** — Role: Deduplication algorithm. How to set: MinHash + exact dedup. Default/range: Combined. Effect: Both methods are needed for thorough dedup.
- **removal_rate** — Role: Fraction of data removed. How to set: ~48% for RedPajama. Default/range: 48%. Effect: Significant removal indicates high original redundancy.

## Validation checks
- LLMs trained on SlimPajama should match or exceed RedPajama-trained ones.
- Dedup statistics should show significant redundancy removal.
- Text quality should measurably improve.

## Failure modes
- Aggressive dedup may remove valid content.
- 627B tokens may be insufficient for very large models.
- Some quality issues may survive filtering.

## Adaptation notes for VLM training
- SlimPajama provides a clean text component for VLM pretraining.
- The dedup pipeline is reusable for other corpora.
- Combine with image-text data for multimodal pretraining.

## Implementation notes
- Use the SlimPajama pipeline for reproducibility.
- Apply to your own text corpora.
- Compare training efficiency on clean vs original data.

## Evidence from the paper
- SlimPajama removes 48% of RedPajama through dedup and cleaning.
- LLMs trained on 627B clean tokens match those on 1.2T noisy tokens.
- Deduplication is the most impactful processing step.
- The cleaned corpus improves training efficiency significantly.

## Source paper
- **Title**: SlimPajama: A 627B Token Cleaned and Deduplicated Version of RedPajama
- **Year**: 2023
- **Venue**: CerebrasGPT
- **Paper ID**: arxiv-slimpajama-2023
- **URL**: https://www.cerebras.net/blog/slimpajama-a-627b-token-cleaned-and-deduplicated-version-of-redpajama
- **arXiv ID**: N/A
