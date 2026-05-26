# Conceptual Captions: A Cleaned, Hypernymed, Image Alt-text Dataset For Automatic Image Captioning

## One-line decision
Use this skill when you want to build an image captioning dataset from web alt-text using automated cleaning and hypernym replacement. Avoid it when you need fine-grained or domain-specific captions that web alt-text cannot provide.

## Skill metadata
- **Skill type**: alt-text-cleaning-pipeline
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Construct a large-scale image captioning dataset (Conceptual Captions, CC3M) from web alt-text using automated pipelines for text cleaning, hypernym replacement, and image-text relevance filtering.

## Problem signature
- Modality: image-text pairs derived from web page alt-text with automated cleaning.
- Data state: raw web alt-text cleaned through multi-stage filtering and text normalization.
- Scale regime: 3.3 million image-caption pairs from billions of web page candidates.
- Model requirement: No model training required for dataset construction; uses existing NLP and vision tools for filtering.

## Use when
- You want to build an image-caption dataset from web alt-text.
- You need automated caption cleaning without manual annotation.
- You want a general-purpose pretraining dataset at million-scale.

## Do not use when
- You need domain-specific or expert-level captions.
- You need fine-grained spatial or attribute descriptions.
- You require captions with precise named entities (hypernym replacement removes them).

## Required inputs
- **web_crawl**: Web pages with image alt-text attributes.
- **nlp_pipeline**: POS tagger, NER, hypernym database (WordNet) for text cleaning.
- **image_text_filter**: Classifier to measure image-text relevance.

## Optional inputs
- **profanity_filter**: Filter to remove offensive or inappropriate content.
- **deduplication**: Near-duplicate image detection for deduplication.

## Outputs
- **cc3m_dataset**: 3.3M cleaned image-caption pairs.
- **cleaning_pipeline**: Reusable multi-stage text cleaning pipeline.

## Assumptions and prerequisites
- Web alt-text, while noisy, contains useful image descriptions after cleaning.
- Hypernym replacement (e.g., 'Barack Obama' → 'a person') improves generalization.
- Multi-stage filtering produces captions suitable for pretraining.

## Procedure
1. **Extract alt-text from web pages**
   Action: Parse HTML to extract image-alt-text pairs from web crawl.
   Why: Alt-text is the primary source of image descriptions on the web.
   Note: See paper for details.
2. **Filter by text quality**
   Action: Remove alt-text that is too short, too long, contains HTML/boilerplate, or is not English.
   Why: Low-quality alt-text adds noise to the dataset.
   Note: See paper for details.
3. **Apply hypernym replacement**
   Action: Replace named entities (persons, locations, brands) with hypernyms using NER + WordNet.
   Why: Improves generalization by reducing memorization of specific entities.
   Note: See paper for details.
4. **Filter by image-text relevance**
   Action: Use a learned classifier to score image-text relevance and remove misaligned pairs.
   Why: Many alt-text strings describe the page context rather than the image.
   Note: See paper for details.
5. **Deduplicate and finalize**
   Action: Remove near-duplicate images and export the final dataset.
   Why: Deduplication prevents overfitting to repeated examples.
   Note: See paper for details.

## Parameters to set
- **min_caption_length** — Role: Minimum words in cleaned caption. How to set: 3-5 words minimum. Default/range: ~3. Effect: Removes trivially short captions.
- **hypernym_level** — Role: How far up the WordNet hierarchy to replace. How to set: One level up from the entity. Default/range: 1 level. Effect: More abstract hypernyms reduce specificity.
- **relevance_threshold** — Role: Minimum image-text relevance score. How to set: Tune on held-out samples. Default/range: Not specified. Effect: Stricter threshold reduces dataset size but improves quality.

## Validation checks
- Cleaned captions should be grammatically correct and image-relevant.
- The dataset should be large enough for effective pretraining (>1M pairs).
- Hypernym replacement should improve generalization on downstream tasks.

## Failure modes
- Hypernym replacement may remove useful specificity from captions.
- Text cleaning rules may be too aggressive and remove valid captions.
- Image-text relevance filtering depends on the quality of the classifier.

## Adaptation notes for VLM training
- The CC3M cleaning pipeline inspired subsequent datasets (CC12M, SBU, etc.).
- Adapt the hypernym replacement for domain-specific applications.
- Use CC3M as a pretraining alignment dataset for VLMs (as in LLaVA).

## Implementation notes
- Use spaCy or similar NLP toolkit for efficient NER and POS tagging.
- Batch image-text relevance scoring for efficiency.
- Store both original and cleaned captions for analysis.

## Evidence from the paper
- Conceptual Captions (CC3M) provides 3.3M automatically cleaned image-caption pairs from web alt-text.
- The hypernyming step replaces named entities with generic concepts, improving model generalization.
- Models trained on CC3M perform comparably to those trained on manually annotated COCO captions.
- The automated pipeline enables dataset construction at scale without manual annotation.

## Source paper
- **Title**: Conceptual Captions: A Cleaned, Hypernymed, Image Alt-text Dataset For Automatic Image Captioning
- **Year**: 2018
- **Venue**: ACL
- **Paper ID**: arxiv-1809.00470v1
- **URL**: http://arxiv.org/abs/1809.00470v1
- **arXiv ID**: 1809.00470v1
