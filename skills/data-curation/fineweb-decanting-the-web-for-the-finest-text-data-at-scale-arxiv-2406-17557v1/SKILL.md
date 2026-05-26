# FineWeb: Decanting the Web for the Finest Text Data at Scale

## One-line decision
Use this skill when you want to understand and apply state-of-the-art web text filtering techniques including quality classifiers trained on curated data. Avoid it when you are not processing web text or have sufficient text data already.

## Skill metadata
- **Skill type**: web-text-quality-filtering
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Apply state-of-the-art web text filtering techniques at scale to produce FineWeb, a 15-trillion-token high-quality web text dataset with detailed analysis of each filtering step's contribution.

## Problem signature
- Modality: text from Common Crawl with multi-stage quality filtering.
- Data state: Common Crawl processed through multiple filtering stages with ablation analysis.
- Scale regime: 15 trillion tokens of high-quality web text.
- Model requirement: Quality classifier trained on curated data; any LLM for validation.

## Use when
- You want the highest quality web text corpus.
- You want to understand which filtering steps matter most.
- You need trillions of tokens for LLM/VLM pretraining.

## Do not use when
- You already have sufficient text data.
- You need domain-specific rather than web text.
- You cannot process at Common Crawl scale.

## Required inputs
- **common_crawl**: Common Crawl web archive.
- **quality_classifier**: Classifier trained on curated vs. web text to score quality.
- **filtering_pipeline**: Multi-stage pipeline: URL filtering, text extraction, dedup, quality scoring.

## Optional inputs
- **ablation_budget**: Compute for ablating individual filtering steps.

## Outputs
- **fineweb_dataset**: 15T tokens of high-quality web text.
- **filtering_analysis**: Detailed analysis of each filtering step's impact.

## Assumptions and prerequisites
- Multi-stage filtering produces better text than single-step approaches.
- Quality classifiers capture aspects of text quality that heuristics miss.
- Ablation analysis reveals which steps matter most.

## Procedure
1. **URL-level filtering**
   Action: Remove URLs from known low-quality domains.
   Why: URL-level filtering is the cheapest quality signal.
   Note: See paper for details.
2. **Text extraction and cleaning**
   Action: Extract clean text from HTML with trafilatura.
   Why: Better text extraction improves downstream quality.
   Note: See paper for details.
3. **Deduplication**
   Action: Apply MinHash deduplication at scale.
   Why: Removes massive web redundancy.
   Note: See paper for details.
4. **Quality classification**
   Action: Score text with a quality classifier trained on curated data.
   Why: Learned quality scores capture nuanced text quality.
   Note: See paper for details.
5. **Ablate and validate**
   Action: Measure the impact of each step through ablation on LLM training.
   Why: Identifies which filtering steps are most valuable.
   Note: See paper for details.

## Parameters to set
- **quality_classifier_threshold** — Role: Minimum quality score for keeping text. How to set: Sweep thresholds and evaluate downstream. Default/range: Dataset-dependent. Effect: Higher thresholds reduce size but improve quality.
- **dedup_method** — Role: Deduplication algorithm. How to set: MinHash for scalability. Default/range: MinHash. Effect: Fuzzy dedup catches more duplicates than exact.
- **text_extractor** — Role: HTML-to-text extraction tool. How to set: Use trafilatura for best quality. Default/range: trafilatura. Effect: Better extraction reduces noise.

## Validation checks
- FineWeb-trained models should outperform RefinedWeb and C4 baselines.
- Each filtering step should show measurable improvement in ablations.
- The quality classifier should correlate with human quality judgments.

## Failure modes
- Quality classifiers may have biases from the training data.
- Over-filtering may remove valid niche content.
- Scale of processing requires significant infrastructure.

## Adaptation notes for VLM training
- FineWeb filtering techniques apply to the text component of VLM pretraining.
- The quality classifier approach generalizes to multimodal data scoring.
- Ablation methodology is reusable for any data processing pipeline.

## Implementation notes
- Use the HuggingFace datatrove library for processing.
- Run ablations at small scale before committing to full processing.
- Cache intermediate results for efficient iteration.

## Evidence from the paper
- FineWeb provides 15 trillion tokens of high-quality web text.
- Quality classifiers trained on curated data are the most impactful filtering step.
- Detailed ablation analysis reveals the contribution of each processing step.
- FineWeb-trained models outperform those trained on other web text corpora.

## Source paper
- **Title**: FineWeb: Decanting the Web for the Finest Text Data at Scale
- **Year**: 2024
- **Venue**: arXiv
- **Paper ID**: arxiv-2406.17557v1
- **URL**: http://arxiv.org/abs/2406.17557v1
- **arXiv ID**: 2406.17557v1
