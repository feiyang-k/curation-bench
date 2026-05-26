# DALL-E 2: Hierarchical Text-Conditional Image Generation with CLIP Latents

## One-line decision
Use this skill when you want to generate images conditioned on CLIP embeddings for training data augmentation or dataset expansion. Avoid it when you do not need image generation or CLIP-guided generation.

## Skill metadata
- **Skill type**: clip-guided-image-generation
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Generate images by first producing CLIP image embeddings from text (via a prior), then decoding those embeddings into images using a diffusion decoder, enabling CLIP-guided image generation.

## Problem signature
- Modality: text prompts → CLIP embeddings → generated images.
- Data state: images generated through CLIP embedding space.
- Scale regime: unlimited generation from text prompts.
- Model requirement: CLIP prior + diffusion decoder (unCLIP architecture).

## Use when
- You want CLIP-guided image generation for data augmentation.
- You need to generate images that align with specific CLIP embeddings.
- You want to edit or vary existing images.

## Do not use when
- You do not need image generation.
- Latent diffusion (Stable Diffusion) is preferred.
- CLIP guidance is not needed.

## Required inputs
- **text_prompts**: Text descriptions for image generation.
- **clip_model**: CLIP model for computing text embeddings.
- **prior_model**: Model for generating CLIP image embeddings from text.
- **diffusion_decoder**: Decoder for generating images from CLIP embeddings.

## Optional inputs
- **image_embeddings**: CLIP embeddings of existing images for variation.

## Outputs
- **generated_images**: Images generated from text via CLIP embeddings.
- **clip_aligned_data**: Synthetic images with known CLIP embeddings.

## Assumptions and prerequisites
- CLIP embeddings capture meaningful visual semantics.
- A prior can learn to generate image embeddings from text.
- CLIP-guided generation produces useful training images.

## Procedure
1. **Encode text with CLIP**
   Action: Compute CLIP text embedding for the prompt.
   Why: CLIP text embedding defines the target semantics.
   Note: See paper for details.
2. **Generate image embedding with prior**
   Action: Use the prior to generate a CLIP image embedding from the text embedding.
   Why: The prior maps text to image embedding space.
   Note: See paper for details.
3. **Decode to image**
   Action: Use the diffusion decoder to generate an image from the CLIP embedding.
   Why: The decoder produces the final image.
   Note: See paper for details.
4. **Use for training data**
   Action: Apply generated images as training data augmentation.
   Why: CLIP-guided images have known semantic properties.
   Note: See paper for details.

## Parameters to set
- **prior_type** — Role: Type of prior model. How to set: Diffusion prior or autoregressive. Default/range: Diffusion prior. Effect: Prior type affects generation diversity.
- **decoder_steps** — Role: Diffusion steps for image generation. How to set: 20-100. Default/range: 64. Effect: More steps improve image quality.

## Validation checks
- Generated images should match text prompts semantically.
- CLIP embeddings of generated images should be close to target embeddings.
- Generated images should be useful for training data augmentation.

## Failure modes
- CLIP embedding space may not capture all visual details.
- The prior may generate out-of-distribution embeddings.
- Generated image quality may not match real images.

## Adaptation notes for VLM training
- CLIP-guided generation can augment VLM training data.
- Generate images with controlled CLIP embeddings for targeted augmentation.
- The unCLIP approach provides interpretable generation through CLIP space.

## Implementation notes
- Use the prior model for text-to-CLIP-embedding mapping.
- Apply CLIP filtering to verify generation quality.
- Compare generated images to real image distributions.

## Evidence from the paper
- DALL-E 2 generates images through CLIP embedding space.
- The prior-decoder architecture enables controlled generation.
- CLIP-guided generation produces semantically meaningful images.
- The approach enables image variation and editing through embedding manipulation.

## Source paper
- **Title**: DALL-E 2: Hierarchical Text-Conditional Image Generation with CLIP Latents
- **Year**: 2022
- **Venue**: arXiv
- **Paper ID**: arxiv-2204.06125v1
- **URL**: http://arxiv.org/abs/2204.06125v1
- **arXiv ID**: 2204.06125v1
