# Deduplicating Training Data Makes Language Models Better

## One-line decision
Use this skill when you want to apply exact and near-duplicate removal to LLM training data using suffix arrays and MinHash. Avoid it when your dataset is already deduplicated or too small for dedup to matter.

## Skill metadata
- **Skill type**: exact-and-near-deduplication
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Demonstrate that both exact and near-duplicate removal from training data improves LLM quality, using suffix arrays for exact dedup and MinHash for near dedup.

## Problem signature
- Modality: text data for LLM training.
- Data state: training corpora with significant exact and near duplication.
- Scale regime: C4 (800GB) and other web-scale corpora.
- Model requirement: Any LLM; dedup is a preprocessing step.

## Use when
- You have web-scale text data with duplication.
- You want to improve LLM training efficiency.
- You can afford the compute for deduplication.

## Do not use when
- Your data is already deduplicated.
- Your dataset is small and curated.
- You need all data including duplicates.

## Required inputs
- **training_corpus**: Text corpus to deduplicate.
- **suffix_array**: Suffix array implementation for exact dedup.
- **minhash**: MinHash implementation for near dedup.

## Optional inputs
- **dedup_threshold**: Jaccard similarity threshold for near-dedup.

## Outputs
- **deduped_corpus**: Corpus with duplicates removed.
- **dedup_statistics**: Statistics on duplicates found and removed.

## Assumptions and prerequisites
- Web-scale corpora contain significant duplication.
- Removing duplicates improves training efficiency and model quality.
- Both exact and near dedup are important.

## Procedure
1. **Apply exact deduplication**
   Action: Use suffix arrays to find and remove exact duplicate substrings.
   Why: Exact duplicates waste training compute.
   Note: See paper for details.
2. **Apply near deduplication**
   Action: Use MinHash to find and remove near-duplicate documents.
   Why: Near-duplicates are also wasteful.
   Note: See paper for details.
3. **Measure dedup impact**
   Action: Train models on deduped vs. non-deduped data and compare.
   Why: Validates the benefit of deduplication.
   Note: See paper for details.
4. **Analyze memorization**
   Action: Measure whether dedup reduces memorization of training data.
   Why: Dedup should reduce verbatim memorization.
   Note: See paper for details.

## Parameters to set
- **exact_dedup_method** — Role: Algorithm for exact dedup. How to set: Suffix arrays for efficiency. Default/range: Suffix array. Effect: Finds all exact duplicate substrings.
- **near_dedup_threshold** — Role: Jaccard threshold for near-dedup. How to set: 0.8 for moderate dedup. Default/range: 0.8. Effect: Lower threshold removes more documents.
- **minhash_params** — Role: MinHash signature parameters. How to set: 128 permutations typical. Default/range: 128. Effect: More permutations improve accuracy.

## Validation checks
- Dedup should remove a significant fraction of data.
- Model quality should improve or maintain with dedup.
- Memorization should decrease after dedup.

## Failure modes
- Aggressive dedup may remove valid repeated content.
- Suffix array computation requires significant memory.
- Near-dedup thresholds need tuning per dataset.

## Adaptation notes for VLM training
- Apply both dedup methods to VLM text data.
- Extend to image-text pair dedup using image hashes.
- Combine with SemDeDup for multi-level deduplication.

## Implementation notes
- Use the paper's suffix array implementation for efficiency.
- Apply dedup before other filtering steps.
- Monitor dedup rate to calibrate threshold.

## Evidence from the paper
- Deduplication removes 1-19% of C4 data depending on method.
- LLMs trained on deduped data achieve better perplexity.
- Dedup significantly reduces verbatim memorization of training data.
- Both exact and near dedup contribute independently to improvement.

## Source paper
- **Title**: Deduplicating Training Data Makes Language Models Better
- **Year**: 2022
- **Venue**: ACL
- **Paper ID**: arxiv-2107.06499v2
- **URL**: http://arxiv.org/abs/2107.06499v2
- **arXiv ID**: 2107.06499v2
