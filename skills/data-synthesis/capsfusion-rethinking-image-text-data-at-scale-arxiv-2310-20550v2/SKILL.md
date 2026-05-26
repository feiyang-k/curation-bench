# CapsFusion: Rethinking Image-Text Data at Scale

## One-line decision
Use this skill when you want to fuse noisy web captions with synthetic model-generated captions using an LLM to get the best of both. Avoid it when you have only one caption source or cannot afford LLM-based fusion.

## Skill metadata
- **Skill type**: caption-fusion
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Fuse raw web captions (which contain world knowledge and named entities) with synthetic model-generated captions (which are more visually descriptive) using an LLM, producing hybrid captions that combine the strengths of both.

## Problem signature
- Modality: images with dual captions (web alt-text and synthetic) fused into a single improved caption.
- Data state: images with both original web captions and synthetic captions from a captioning model.
- Scale regime: 120M fused captions at scale.
- Model requirement: An LLM (e.g., ChatGPT) for fusing pairs of captions; a captioning model for generating synthetic captions.

## Use when
- You have both noisy web captions and synthetic model-generated captions for the same images.
- You want to preserve world knowledge from web text while gaining visual accuracy from synthetic captions.
- You can use an LLM to merge caption pairs at scale.

## Do not use when
- You have only one caption source.
- You cannot afford LLM inference for caption fusion.
- Web captions are entirely uninformative and contribute nothing.

## Required inputs
- **web_captions**: Original noisy web alt-text for each image.
- **synthetic_captions**: Model-generated captions from a captioning model (e.g., BLIP2).
- **fusion_llm**: LLM used to fuse the two caption types into one.

## Optional inputs
- **fusion_prompt**: Prompt template guiding the LLM to merge captions.
- **quality_filter**: Post-fusion filter to remove bad fusions.

## Outputs
- **fused_captions**: Hybrid captions combining web knowledge and synthetic visual descriptions.
- **fusion_log**: Record of original captions and fused output for auditing.

## Assumptions and prerequisites
- Web captions contain world knowledge (names, events, context) that synthetic captions lack.
- Synthetic captions provide better visual descriptions than noisy web text.
- An LLM can effectively merge complementary information from two caption types.

## Procedure
1. **Generate synthetic captions**
   Action: Run a captioning model on all images to produce visually descriptive captions.
   Why: Creates the synthetic component for fusion.
   Note: See paper for details.
2. **Design fusion prompt**
   Action: Create an LLM prompt that instructs the model to merge web and synthetic captions, keeping the best of both.
   Why: The prompt controls fusion quality and what information is preserved.
   Note: See paper for details.
3. **Fuse captions with LLM**
   Action: Feed pairs of (web caption, synthetic caption) to the LLM with the fusion prompt.
   Why: LLM reasoning combines complementary information from both sources.
   Note: See paper for details.
4. **Filter fused captions**
   Action: Remove fused captions that are too generic, contradictory, or poorly formed.
   Why: Quality control ensures the fusion actually improved captions.
   Note: See paper for details.
5. **Train VLM on fused data**
   Action: Pre-train a VLM on the CapsFusion dataset and compare to web-only and synthetic-only baselines.
   Why: Validates that fusion outperforms using either caption type alone.
   Note: See paper for details.

## Parameters to set
- **fusion_prompt_template** — Role: Instructions for the LLM to merge captions. How to set: Instruct to keep named entities from web, visual details from synthetic, and resolve conflicts. Default/range: See paper. Effect: Prompt quality directly affects fusion quality.
- **synthetic_captioner** — Role: Model generating the synthetic captions. How to set: Use BLIP2 or similar strong captioner. Default/range: BLIP2. Effect: Better captioner produces better fusion input.
- **fusion_batch_size** — Role: Number of caption pairs fused per LLM call. How to set: 1 pair per call for quality. Default/range: 1. Effect: Batching multiple pairs may degrade quality.

## Validation checks
- Fused captions should contain world knowledge from web captions and visual details from synthetic ones.
- VLM trained on fused data should outperform both web-only and synthetic-only baselines.
- Caption length and informativeness should increase after fusion.

## Failure modes
- The LLM may incorrectly resolve conflicts between web and synthetic captions.
- Fusion at scale is expensive due to LLM inference costs.
- The LLM may introduce hallucinations not present in either source caption.

## Adaptation notes for VLM training
- The fusion approach can be applied to any pair of caption sources.
- Replace the LLM with Claude for potentially higher quality fusion.
- Extend to fuse more than two caption types (e.g., web + synthetic + OCR-derived).

## Implementation notes
- Batch LLM calls efficiently to manage cost.
- Cache fusion results for reproducibility.
- Compare random samples of fused vs original captions to verify quality.

## Evidence from the paper
- CapsFusion combines web captions (with world knowledge) and synthetic captions (with visual accuracy) using LLM-based fusion.
- Models trained on CapsFusion data outperform those trained on web-only or synthetic-only captions on 12 downstream tasks.
- CapsFusion produces 120M fused captions that preserve named entities and add visual descriptions.
- The fusion approach is complementary to other data curation methods.

## Source paper
- **Title**: CapsFusion: Rethinking Image-Text Data at Scale
- **Year**: 2023
- **Venue**: CVPR
- **Paper ID**: arxiv-2310.20550v2
- **URL**: http://arxiv.org/abs/2310.20550v2
- **arXiv ID**: 2310.20550v2
