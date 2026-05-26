# ALLaVA: Harnessing GPT4V-synthesized Data for A Lite Vision-Language Model

## One-line decision
Use this skill when you want to synthesize high-quality instruction data using GPT-4V on diverse image sources for training small VLMs. Avoid it when you cannot afford GPT-4V API calls or are training a large-scale model.

## Skill metadata
- **Skill type**: gpt4v-data-synthesis
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Synthesize high-quality instruction-following data using GPT-4V on images from diverse sources (LAION, VFlan, etc.) for training a lightweight VLM that punches above its weight.

## Problem signature
- Modality: images with GPT-4V-synthesized instruction data.
- Data state: diverse images annotated with GPT-4V-generated captions and instruction-response pairs.
- Scale regime: ~700K GPT-4V-synthesized samples.
- Model requirement: GPT-4V for data generation; lightweight VLM (Phi-2) for training.

## Use when
- You want high-quality instruction data for a small VLM.
- You can invest in GPT-4V API calls for data synthesis.
- You need data from diverse visual sources.

## Do not use when
- You cannot afford GPT-4V API calls.
- You are training a very large model where data quantity matters more.
- You have sufficient human-annotated instruction data.

## Required inputs
- **diverse_images**: Images from multiple sources (LAION, VFlan, etc.).
- **gpt4v_api**: GPT-4V for generating captions and instruction data.
- **prompt_templates**: Templates for caption generation and instruction synthesis.

## Optional inputs
- **quality_filter**: Filter for removing low-quality GPT-4V outputs.

## Outputs
- **allava_data**: ~700K high-quality instruction samples.
- **allava_model**: Lightweight VLM trained on the synthesized data.

## Assumptions and prerequisites
- GPT-4V generates higher quality instruction data than existing methods.
- Quality matters more than quantity for small model training.
- Diverse image sources improve data coverage.

## Procedure
1. **Collect diverse images**
   Action: Gather images from LAION, VFlan, and other diverse sources.
   Why: Source diversity ensures broad visual coverage.
   Note: See paper for details.
2. **Generate captions with GPT-4V**
   Action: Use GPT-4V to generate detailed captions for all images.
   Why: GPT-4V produces high-quality, detailed descriptions.
   Note: See paper for details.
3. **Synthesize instruction data**
   Action: Prompt GPT-4V to generate instruction-response pairs from the images.
   Why: Instruction data teaches the model to follow user queries.
   Note: See paper for details.
4. **Train lightweight VLM**
   Action: Train a small VLM (Phi-2 based) on the synthesized data.
   Why: High-quality data enables strong performance from a small model.
   Note: See paper for details.

## Parameters to set
- **data_size** — Role: Number of synthesized samples. How to set: ~700K for a lightweight model. Default/range: 700K. Effect: Quality matters more than quantity for small models.
- **image_sources** — Role: Diversity of image sources. How to set: Include multiple datasets for coverage. Default/range: LAION + VFlan + others. Effect: More sources improve visual diversity.

## Validation checks
- The small VLM should outperform larger models trained on lower-quality data.
- GPT-4V captions should be more detailed than existing captions.
- Instruction data should be diverse and visually grounded.

## Failure modes
- GPT-4V may hallucinate details not in the image.
- API costs may be prohibitive at larger scales.
- The model may overfit to GPT-4V's style.

## Adaptation notes for VLM training
- Replace GPT-4V with Claude for data synthesis.
- Scale the approach for larger models with more data.
- The quality-over-quantity insight applies broadly to VLM training.

## Implementation notes
- Batch GPT-4V API calls for cost efficiency.
- Store raw GPT-4V outputs for quality analysis.
- Track per-source data quality metrics.

## Evidence from the paper
- ALLaVA synthesizes ~700K high-quality instruction samples using GPT-4V.
- A lightweight VLM trained on this data outperforms larger models.
- Data quality matters more than quantity for small model training.
- Diverse image sources improve data coverage and model generalization.

## Source paper
- **Title**: ALLaVA: Harnessing GPT4V-synthesized Data for A Lite Vision-Language Model
- **Year**: 2024
- **Venue**: arXiv
- **Paper ID**: arxiv-2402.11684v3
- **URL**: http://arxiv.org/abs/2402.11684v3
- **arXiv ID**: 2402.11684v3
