# WIT: Wikipedia-based Image Text Dataset for Multimodal Multilingual Machine Learning

## One-line decision
Use this skill when you need a multilingual image-text dataset mined from Wikipedia covering 108 languages with curated metadata. Avoid it when you only need English data or web-crawled alt-text.

## Skill metadata
- **Skill type**: wikipedia-image-text-mining
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Mine Wikipedia for image-text pairs across 108 languages, creating a multilingual, curated image-text dataset with rich metadata from Wikipedia's structured content.

## Problem signature
- Modality: Wikipedia images paired with multilingual text in 108 languages.
- Data state: 11.5M image-text sets from Wikipedia with structured metadata.
- Scale regime: 11.5 million image-text sets across 108 languages.
- Model requirement: Any multilingual VLM for training.

## Use when
- You need multilingual image-text data.
- You want curated text from Wikipedia rather than web alt-text.
- You need data across 108 languages.

## Do not use when
- You only need English.
- Web-crawled data is sufficient.
- You need very large scale (billions).

## Required inputs
- **wikipedia_dumps**: Wikipedia database dumps across languages.
- **extraction_pipeline**: Pipeline for extracting image-text pairs from Wikipedia.
- **language_metadata**: Language identification for each pair.

## Optional inputs
- **concept_alignment**: Cross-lingual concept alignment.

## Outputs
- **wit_dataset**: 11.5M multilingual image-text sets from Wikipedia.
- **multilingual_metadata**: Per-pair language and concept metadata.

## Assumptions and prerequisites
- Wikipedia provides curated, factual text.
- 108 languages enable broad multilingual coverage.
- Wikipedia's structured content provides rich metadata.

## Procedure
1. **Extract from Wikipedia**
   Action: Parse Wikipedia to extract image-text pairs.
   Why: Wikipedia provides curated, multilingual content.
   Note: See paper for details.
2. **Process across languages**
   Action: Extract pairs from Wikipedia in 108 languages.
   Why: Multilingual extraction enables broad coverage.
   Note: See paper for details.
3. **Add metadata**
   Action: Include Wikipedia concept, language, and context metadata.
   Why: Metadata enables flexible filtering and analysis.
   Note: See paper for details.
4. **Release dataset**
   Action: Package the multilingual image-text dataset.
   Why: Enables multilingual VLM research.
   Note: See paper for details.

## Parameters to set
- **num_languages** — Role: Number of languages included. How to set: All available Wikipedia languages. Default/range: 108. Effect: More languages improve multilingual coverage.
- **pairs_per_language** — Role: Image-text pairs per language. How to set: Extract all available. Default/range: Variable. Effect: Low-resource languages have fewer pairs.

## Validation checks
- Text should be factual and curated (from Wikipedia).
- Language identification should be accurate.
- Coverage should span diverse topics.

## Failure modes
- Low-resource languages may have few pairs.
- Wikipedia text style may differ from conversational.
- Images may not always match text context.

## Adaptation notes for VLM training
- WIT provides multilingual data for VLM pretraining.
- Combine with LAION for English-heavy + multilingual balance.
- Wikipedia metadata enables concept-aligned training.

## Implementation notes
- Use Wikipedia dumps for efficient extraction.
- Handle multilingual text encoding correctly.
- Track per-language statistics.

## Evidence from the paper
- WIT provides 11.5M image-text sets from Wikipedia in 108 languages.
- Wikipedia text is curated and factual.
- The dataset enables multilingual VLM research.
- Rich metadata supports flexible data usage.

## Source paper
- **Title**: WIT: Wikipedia-based Image Text Dataset for Multimodal Multilingual Machine Learning
- **Year**: 2021
- **Venue**: SIGIR
- **Paper ID**: arxiv-2103.01913v2
- **URL**: http://arxiv.org/abs/2103.01913v2
- **arXiv ID**: 2103.01913v2
