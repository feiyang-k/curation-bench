# Chameleon: Mixed-Modal Early-Fusion Foundation Models

## One-line decision
Use this skill when you want to train a mixed-modal model using early fusion of image and text tokens for both understanding and generation. Avoid it when you only need understanding (not generation) or cannot tokenize images.

## Skill metadata
- **Skill type**: mixed-modal-pretraining-data
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Train a mixed-modal foundation model using early fusion of interleaved image and text tokens, enabling both understanding and generation of images and text in a single architecture.

## Problem signature
- Modality: interleaved image and text tokens for early fusion training.
- Data state: mixed-modal data: text-only, image-text pairs, and interleaved image-text sequences.
- Scale regime: trillions of mixed-modal tokens.
- Model requirement: Autoregressive transformer with image tokenizer for early fusion.

## Use when
- You want a model that both understands and generates images and text.
- You can tokenize images for early fusion.
- You need a unified architecture for all modalities.

## Do not use when
- Understanding-only is sufficient.
- You cannot implement image tokenization.
- Late fusion approaches work well for your needs.

## Required inputs
- **text_data**: Text-only data for language modeling.
- **image_text_pairs**: Paired image-text data.
- **interleaved_data**: Interleaved image-text web documents.
- **image_tokenizer**: VQGAN or similar for tokenizing images.

## Optional inputs
- **safety_data**: Safety alignment data.

## Outputs
- **chameleon_model**: Mixed-modal model for understanding and generation.
- **mixed_modal_pipeline**: Data pipeline for early fusion training.

## Assumptions and prerequisites
- Early fusion of image and text tokens enables better cross-modal reasoning.
- A single model can handle both understanding and generation.
- Mixed-modal training at scale produces versatile capabilities.

## Procedure
1. **Tokenize images**
   Action: Convert images to discrete tokens using VQGAN.
   Why: Token-based representation enables unified processing.
   Note: See paper for details.
2. **Prepare mixed-modal data**
   Action: Combine text-only, image-text, and interleaved data streams.
   Why: Mixed data develops both understanding and generation.
   Note: See paper for details.
3. **Train with early fusion**
   Action: Train a single transformer on interleaved image-text token sequences.
   Why: Early fusion enables deep cross-modal interaction.
   Note: See paper for details.
4. **Evaluate both understanding and generation**
   Action: Test on VL understanding and image generation benchmarks.
   Why: Validates both capabilities.
   Note: See paper for details.

## Parameters to set
- **modal_mix** — Role: Ratio of text, image-text, and interleaved data. How to set: Balance for desired capabilities. Default/range: Balanced. Effect: Mix determines relative capability strength.
- **image_tokenizer_quality** — Role: Quality of image tokenization. How to set: High-quality VQGAN with large codebook. Default/range: High quality. Effect: Better tokenization improves generation quality.

## Validation checks
- Understanding benchmarks should be competitive with late-fusion models.
- Image generation quality should be reasonable.
- The model should seamlessly switch between understanding and generation.

## Failure modes
- Image tokenization introduces a quality bottleneck.
- Generation and understanding may compete for model capacity.
- Early fusion increases training complexity.

## Adaptation notes for VLM training
- Chameleon's early fusion approach is an alternative to late fusion VLMs.
- The mixed-modal training strategy applies to other early fusion architectures.
- Image tokenization quality is critical for generation capability.

## Implementation notes
- Use a high-quality VQGAN tokenizer.
- Implement careful data mixing for stable training.
- Monitor both understanding and generation metrics.

## Evidence from the paper
- Chameleon achieves competitive understanding and generation with early fusion.
- Mixed-modal training on trillions of tokens produces versatile capabilities.
- Early fusion enables deep cross-modal reasoning.
- The model handles interleaved image-text input and output.

## Source paper
- **Title**: Chameleon: Mixed-Modal Early-Fusion Foundation Models
- **Year**: 2024
- **Venue**: arXiv
- **Paper ID**: arxiv-2405.09818v1
- **URL**: http://arxiv.org/abs/2405.09818v1
- **arXiv ID**: 2405.09818v1
