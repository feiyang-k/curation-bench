# T5: Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer

## One-line decision
Use this skill when you want to understand the C4 text cleaning methodology and its impact on LLM pretraining quality. Avoid it when you are not cleaning web text or have a different cleaning pipeline.

## Skill metadata
- **Skill type**: c4-web-text-curation
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Curate C4 (Colossal Clean Crawled Corpus) from Common Crawl through aggressive text cleaning, and systematically study the impact of data cleaning on LLM pretraining quality.

## Problem signature
- Modality: text from Common Crawl cleaned through multiple filtering steps.
- Data state: Common Crawl text cleaned through language detection, quality filtering, and deduplication.
- Scale regime: 750GB of cleaned text (C4).
- Model requirement: T5 encoder-decoder transformer.

## Use when
- You want to understand web text cleaning best practices.
- You need a baseline cleaning methodology for Common Crawl.
- You want to study the impact of each cleaning step.

## Do not use when
- You have a more modern cleaning pipeline (FineWeb, RefinedWeb).
- You are not cleaning web text.
- C4 is insufficient for your needs.

## Required inputs
- **common_crawl**: Common Crawl web text.
- **cleaning_pipeline**: Multi-step text cleaning pipeline.
- **evaluation_model**: T5 for evaluating cleaning impact.

## Optional inputs
- **ablation_budget**: Compute for cleaning step ablations.

## Outputs
- **c4_corpus**: 750GB of cleaned Common Crawl text.
- **cleaning_analysis**: Impact analysis of each cleaning step.

## Assumptions and prerequisites
- Aggressive cleaning improves web text quality.
- Each cleaning step contributes measurably.
- Cleaned web text is suitable for LLM pretraining.

## Procedure
1. **Extract text from Common Crawl**
   Action: Parse web pages to extract text.
   Why: Text extraction is the first cleaning step.
   Note: See paper for details.
2. **Apply language filtering**
   Action: Keep only English text.
   Why: Removes non-English content.
   Note: See paper for details.
3. **Apply quality heuristics**
   Action: Remove low-quality text based on length, vocabulary, etc.
   Why: Heuristics catch common quality issues.
   Note: See paper for details.
4. **Deduplicate**
   Action: Remove exact duplicate text.
   Why: Dedup reduces redundancy.
   Note: See paper for details.
5. **Study cleaning impact**
   Action: Ablate each step and measure T5 performance.
   Why: Identifies which steps matter most.
   Note: See paper for details.

## Parameters to set
- **cleaning_steps** — Role: Which cleaning steps to apply. How to set: Apply all for maximum quality. Default/range: All steps. Effect: Each step improves quality incrementally.
- **min_text_length** — Role: Minimum text length for keeping a document. How to set: Remove very short documents. Default/range: Task-dependent. Effect: Removes trivially short content.

## Validation checks
- T5 should perform better with each cleaning step.
- C4 should be cleaner than raw Common Crawl.
- The cleaning pipeline should be reproducible.

## Failure modes
- Some cleaning heuristics may be too aggressive.
- English-only filtering limits multilingual use.
- C4 cleaning is now considered basic compared to modern methods.

## Adaptation notes for VLM training
- C4 methodology is the baseline for modern web text cleaning.
- RefinedWeb and FineWeb improve upon C4 cleaning.
- Apply C4-style cleaning to the text component of VLM data.

## Implementation notes
- Use the T5 data processing code for C4 reproduction.
- Compare C4 to more modern cleaned corpora.
- Apply incrementally for analysis.

## Evidence from the paper
- C4 provides 750GB of cleaned Common Crawl text.
- Each cleaning step measurably improves T5 pretraining quality.
- The C4 methodology established baseline web text cleaning practices.
- Subsequent work (RefinedWeb, FineWeb) has improved upon C4 cleaning.

## Source paper
- **Title**: T5: Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer
- **Year**: 2020
- **Venue**: JMLR
- **Paper ID**: arxiv-1910.10683v4
- **URL**: http://arxiv.org/abs/1910.10683v4
- **arXiv ID**: 1910.10683v4
