# Molmo and PixMo: Open Weights and Open Data for State-of-the-Art Multimodal Models

## One-line decision
Use this skill when you want fully open-source VLM training data (PixMo) that powers a state-of-the-art model without proprietary data dependencies. Avoid it when you are fine using proprietary data sources.

## Skill metadata
- **Skill type**: fully-open-vlm-data
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Create PixMo, a fully open-source dataset for VLM training that powers Molmo, a state-of-the-art VLM, demonstrating that open data can compete with proprietary training data.

## Problem signature
- Modality: fully open image-text instruction data.
- Data state: open-source instruction data without proprietary dependencies.
- Scale regime: curated open instruction data for SOTA VLM.
- Model requirement: OLMo + CLIP ViT with open training pipeline.

## Use when
- You want fully open-source VLM training data.
- You need reproducible VLM training.
- You want to avoid proprietary data dependencies.

## Do not use when
- Proprietary data sources are acceptable.
- You have your own data pipeline.
- Open data quality is insufficient.

## Required inputs
- **pixmo_data**: Open-source PixMo training data.
- **open_llm**: OLMo or similar open LLM.
- **open_encoder**: Open CLIP ViT encoder.

## Optional inputs
- **pointing_data**: PixMo pointing data for spatial grounding.

## Outputs
- **molmo_model**: State-of-the-art open-source VLM.
- **pixmo_dataset**: Fully open VLM training data.

## Assumptions and prerequisites
- Open data can match proprietary data quality.
- Full openness enables reproducible research.
- Careful curation compensates for data source restrictions.

## Procedure
1. **Curate PixMo dataset**
   Action: Create fully open instruction data without proprietary sources.
   Why: Full openness ensures reproducibility.
   Note: See paper for details.
2. **Include pointing data**
   Action: Add PixMo-Points for spatial grounding.
   Why: Pointing enables spatial interaction.
   Note: See paper for details.
3. **Train Molmo**
   Action: Train with fully open pipeline on PixMo.
   Why: End-to-end open training.
   Note: See paper for details.
4. **Validate SOTA performance**
   Action: Compare to proprietary-data VLMs.
   Why: Proves open data competitiveness.
   Note: See paper for details.

## Parameters to set
- **data_openness** — Role: Degree of data openness. How to set: Fully open source. Default/range: Fully open. Effect: Enables full reproducibility.
- **pointing_data** — Role: Spatial pointing annotation data. How to set: Include PixMo-Points. Default/range: Included. Effect: Enables spatial grounding.

## Validation checks
- Molmo should match proprietary-data VLMs.
- All data should be fully open and reproducible.
- The training pipeline should be fully transparent.

## Failure modes
- Open data may have coverage gaps.
- Some proprietary data may be hard to replace.
- Curation effort for open data is significant.

## Adaptation notes for VLM training
- PixMo provides a template for fully open VLM data.
- The pointing data is unique and valuable.
- Full openness enables community improvement.

## Implementation notes
- Use the PixMo data as provided.
- Leverage the open training pipeline.
- Compare to proprietary-data baselines.

## Evidence from the paper
- Molmo achieves state-of-the-art with fully open PixMo data.
- PixMo demonstrates that open data can compete with proprietary.
- The fully open pipeline enables reproducible VLM research.
- PixMo-Points provides unique spatial grounding data.

## Source paper
- **Title**: Molmo and PixMo: Open Weights and Open Data for State-of-the-Art Multimodal Models
- **Year**: 2024
- **Venue**: arXiv
- **Paper ID**: arxiv-2409.17146v1
- **URL**: http://arxiv.org/abs/2409.17146v1
- **arXiv ID**: 2409.17146v1
