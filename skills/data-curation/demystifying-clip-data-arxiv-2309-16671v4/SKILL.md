# Demystifying CLIP Data

## One-line decision
Use this skill when you want to curate CLIP training data using metadata from an existing high-quality dataset rather than model-based filtering. Avoid it when you do not have a reference metadata set or prefer model-based scoring over metadata matching.

## Skill metadata
- **Skill type**: metadata-curated-data-filtering
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Curate CLIP training data by aligning a large candidate pool's metadata distribution with that of a high-quality reference dataset (CLIP's WIT), using substring matching on text rather than model-based scoring.

## Problem signature
- Modality: image-text pairs from web crawl, filtered via text metadata alignment.
- Data state: large raw web-crawled pool (CommonCrawl) that needs filtering to match a target data distribution.
- Scale regime: 400M curated pairs from billions of CommonCrawl candidates.
- Model requirement: No model needed for filtering; only metadata matching. CLIP ViT-B/32 or ViT-L/14 for training.

## Use when
- You have a large raw data pool and a reference high-quality dataset whose metadata distribution you want to match.
- You want to avoid using a pretrained CLIP model for scoring (avoiding circular dependency).
- You need a principled, reproducible data curation strategy.

## Do not use when
- You do not have access to metadata from a high-quality reference dataset.
- Your candidate pool's text format is very different from the reference set.
- You prefer model-based quality scoring over metadata distribution matching.

## Required inputs
- **candidate_pool**: Large web-crawled image-text pairs (e.g., CommonCrawl).
- **reference_metadata**: Metadata (text entries) from a high-quality dataset like CLIP's WIT.
- **substring_matching_rules**: Rules for matching candidate text against reference metadata entries.

## Optional inputs
- **balancing_strategy**: Strategy to balance selected data across concepts (e.g., cap per entry at 20K).
- **additional_filters**: Language detection, length filtering, or NSFW removal.

## Outputs
- **metaclip_dataset**: Curated dataset (400M pairs) matching the reference metadata distribution.
- **trained_clip**: CLIP model trained on MetaCLIP data achieving competitive or superior performance.

## Assumptions and prerequisites
- The metadata distribution of a high-quality dataset encodes useful curation decisions.
- Substring matching on text is a sufficient proxy for semantic alignment with the reference distribution.
- Matching distributions avoids the circular dependency of using a CLIP model to filter CLIP training data.

## Procedure
1. **Extract reference metadata**
   Action: Collect text entries from the reference dataset (e.g., CLIP's WIT 500K queries).
   Why: These entries define the target data distribution.
   Note: See paper for details.
2. **Substring match candidates**
   Action: For each candidate pair, check whether its text contains any reference metadata entry as a substring.
   Why: Selects candidates whose text aligns with the reference distribution.
   Note: See paper for details.
3. **Balance across entries**
   Action: Cap the number of matches per metadata entry (e.g., 20K) to prevent dominant entries from skewing the distribution.
   Why: Ensures concept diversity in the curated dataset.
   Note: See paper for details.
4. **Train CLIP on curated data**
   Action: Train a CLIP model on the curated MetaCLIP dataset.
   Why: Validates that the curation strategy produces high-quality training data.
   Note: See paper for details.
5. **Benchmark against baselines**
   Action: Compare to OpenAI CLIP and OpenCLIP trained on other datasets.
   Why: Demonstrates the effectiveness of metadata-curated data.
   Note: See paper for details.

## Parameters to set
- **entry_cap** — Role: Maximum pairs per metadata entry for balancing. How to set: 20K provides good balance at 400M scale. Default/range: 20K. Effect: Lower caps increase diversity but reduce total dataset size.
- **metadata_source** — Role: Reference dataset whose distribution to match. How to set: Use CLIP's WIT query set or equivalent. Default/range: 500K entries from WIT. Effect: The reference set defines what concepts are covered.
- **total_budget** — Role: Target number of curated pairs. How to set: 400M to match CLIP's WIT scale. Default/range: 400M. Effect: Larger budgets allow more pairs per entry.

## Validation checks
- The curated dataset's concept distribution should align with the reference metadata.
- CLIP trained on MetaCLIP should match or exceed CLIP trained on WIT.
- Zero-shot ImageNet accuracy should reach ~79-80% with ViT-L/14.

## Failure modes
- Substring matching may admit false positives with ambiguous text.
- The reference metadata may not cover domain-specific or emerging concepts.
- Aggressive balancing may discard high-quality pairs from popular entries.

## Adaptation notes for VLM training
- Apply metadata curation to any VLM pretraining pipeline as an alternative to CLIP score filtering.
- The metadata distribution matching principle can be extended to domain-specific reference sets.
- Combine with model-based filtering for a hybrid curation strategy.

## Implementation notes
- Implement substring matching efficiently with inverted indices or tries.
- Cache match results to avoid redundant processing on reruns.
- Monitor the distribution of selected pairs across metadata entries.

## Evidence from the paper
- MetaCLIP reveals that CLIP's curation can be approximated by metadata-driven substring matching and balancing.
- MetaCLIP ViT-L/14 achieves 79.2% zero-shot ImageNet accuracy, matching or exceeding OpenAI CLIP with fully transparent curation.
- The approach curates 400M high-quality image-text pairs from CommonCrawl without using a pretrained CLIP model for scoring.
- Curation is the key factor; algorithm + data distribution matters more than raw data size.

## Source paper
- **Title**: Demystifying CLIP Data
- **Year**: 2023
- **Venue**: ICLR
- **Paper ID**: arxiv-2309.16671v4
- **URL**: http://arxiv.org/abs/2309.16671v4
- **arXiv ID**: 2309.16671v4
