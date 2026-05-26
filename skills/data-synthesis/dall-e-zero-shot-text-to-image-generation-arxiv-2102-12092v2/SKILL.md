# DALL-E: Zero-Shot Text-to-Image Generation

## One-line decision
Use this skill when you want to generate images autoregressively from text for dataset augmentation using a discrete VAE tokenizer. Avoid it when diffusion models provide better generation quality for your needs.

## Skill metadata
- **Skill type**: autoregressive-image-generation
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Generate images autoregressively from text descriptions using a discrete VAE tokenizer, enabling zero-shot text-to-image generation for dataset augmentation.

## Problem signature
- Modality: text-to-image generation via autoregressive modeling.
- Data state: 250M text-image pairs for training autoregressive generation.
- Scale regime: 250 million image-text pairs.
- Model requirement: dVAE tokenizer + autoregressive transformer.

## Use when
- You want autoregressive image generation from text.
- You need discrete image tokenization.
- You want large-scale text-to-image generation.

## Do not use when
- Diffusion models provide better quality.
- You do not need image generation.
- Real images are sufficient.

## Required inputs
- **image_text_pairs**: 250M image-text pairs for training.
- **dvae**: Discrete VAE for image tokenization.
- **autoregressive_model**: Transformer for autoregressive generation.

## Optional inputs
- **clip_reranking**: CLIP for reranking generated candidates.

## Outputs
- **dalle_model**: Autoregressive text-to-image generator.
- **generated_images**: Images generated from text descriptions.

## Assumptions and prerequisites
- Discrete VAE provides effective image tokenization.
- Autoregressive generation can produce diverse images.
- 250M pairs provide sufficient training data.

## Procedure
1. **Train discrete VAE**
   Action: Train dVAE to tokenize images into discrete tokens.
   Why: Discrete tokens enable autoregressive modeling.
   Note: See paper for details.
2. **Train autoregressive model**
   Action: Train transformer on text-image token sequences.
   Why: Autoregressive training learns text-conditioned generation.
   Note: See paper for details.
3. **Generate and rerank**
   Action: Generate multiple images per prompt and rerank with CLIP.
   Why: CLIP reranking selects the best generation.
   Note: See paper for details.

## Parameters to set
- **vocab_size** — Role: dVAE vocabulary size. How to set: 8192 for good quality. Default/range: 8192. Effect: Larger vocabulary captures more detail.
- **model_params** — Role: Size of autoregressive model. How to set: 12B for best quality. Default/range: 12B. Effect: Larger models generate better images.

## Validation checks
- Generated images should match text prompts.
- CLIP reranking should improve generation quality.
- Images should be diverse and realistic.

## Failure modes
- dVAE tokenization introduces quality loss.
- Autoregressive generation may produce artifacts.
- Very long prompts may not be well handled.

## Adaptation notes for VLM training
- DALL-E pioneered text-to-image generation for data augmentation.
- The dVAE approach influences image tokenization in VLMs.
- Use for generating synthetic training data.

## Implementation notes
- Use CLIP reranking for best results.
- Generate multiple candidates per prompt.
- Compare to diffusion-based alternatives.

## Evidence from the paper
- DALL-E generates diverse images from text descriptions.
- 250M image-text pairs enable effective autoregressive generation.
- CLIP reranking significantly improves generation quality.
- The approach pioneered large-scale text-to-image generation.

## Source paper
- **Title**: DALL-E: Zero-Shot Text-to-Image Generation
- **Year**: 2021
- **Venue**: ICML
- **Paper ID**: arxiv-2102.12092v2
- **URL**: http://arxiv.org/abs/2102.12092v2
- **arXiv ID**: 2102.12092v2
