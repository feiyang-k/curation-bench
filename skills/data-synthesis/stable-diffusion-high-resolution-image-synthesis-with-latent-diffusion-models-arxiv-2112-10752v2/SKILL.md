# Stable Diffusion: High-Resolution Image Synthesis with Latent Diffusion Models

## One-line decision
Use this skill when you want to use text-to-image diffusion models to generate synthetic training images for augmenting VLM training data. Avoid it when you have sufficient real training images or synthetic images would not improve your task.

## Skill metadata
- **Skill type**: text-to-image-for-data-augmentation
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Use latent diffusion models (Stable Diffusion) for high-quality text-to-image generation, applicable to generating synthetic training images for augmenting VLM training datasets.

## Problem signature
- Modality: text prompts → synthetic images for training data augmentation.
- Data state: synthetic images generated from text prompts to augment training data.
- Scale regime: unlimited synthetic image generation.
- Model requirement: Latent Diffusion Model (Stable Diffusion) for image generation.

## Use when
- You need to augment training data with synthetic images.
- You have text descriptions for desired training images.
- You want to fill gaps in your training data distribution.

## Do not use when
- You have sufficient real training images.
- Synthetic images would not improve your task.
- Image quality is critical and diffusion quality is insufficient.

## Required inputs
- **text_prompts**: Text descriptions of desired images.
- **diffusion_model**: Stable Diffusion or similar text-to-image model.
- **generation_config**: Guidance scale, steps, and sampling parameters.

## Optional inputs
- **negative_prompts**: Descriptions of what to avoid in generated images.
- **control_signals**: ControlNet or similar for controlled generation.

## Outputs
- **synthetic_images**: Generated images matching text prompts.
- **augmented_dataset**: Training dataset augmented with synthetic images.

## Assumptions and prerequisites
- Diffusion models can generate sufficiently realistic training images.
- Synthetic images complement real images in training.
- Text prompts can specify desired image content accurately.

## Procedure
1. **Design text prompts**
   Action: Create text descriptions for desired synthetic images.
   Why: Prompts control the generated content.
   Note: See paper for details.
2. **Generate images**
   Action: Run Stable Diffusion with the prompts.
   Why: Generates synthetic training images.
   Note: See paper for details.
3. **Filter generated images**
   Action: Remove low-quality or unfaithful generations.
   Why: Quality control ensures useful training data.
   Note: See paper for details.
4. **Augment training data**
   Action: Mix synthetic images with real training data.
   Why: Augmentation fills gaps in the training distribution.
   Note: See paper for details.

## Parameters to set
- **guidance_scale** — Role: How closely to follow the text prompt. How to set: 7.5-15 for prompt faithfulness. Default/range: 7.5. Effect: Higher guidance improves prompt adherence but may reduce diversity.
- **num_inference_steps** — Role: Number of denoising steps. How to set: 20-50 for quality. Default/range: 50. Effect: More steps improve quality but increase compute.
- **synthetic_ratio** — Role: Ratio of synthetic to real images. How to set: Start with 10-30% synthetic. Default/range: 10-30%. Effect: Too much synthetic may shift distribution.

## Validation checks
- Generated images should match the text prompts.
- Augmented training should improve over real-only baselines.
- Synthetic images should be visually realistic.

## Failure modes
- Diffusion models may generate artifacts or unrealistic features.
- Generated images may not match the real data distribution.
- Over-reliance on synthetic data may cause distribution shift.

## Adaptation notes for VLM training
- Use Stable Diffusion to generate rare or underrepresented training examples for VLMs.
- Generate synthetic chart, diagram, or scene images for VLM data augmentation.
- Combine with text generation for complete synthetic image-text pair creation.

## Implementation notes
- Use batch generation for efficiency.
- Apply CLIP filtering to verify prompt-image alignment.
- Monitor the synthetic-to-real ratio during training.

## Evidence from the paper
- Latent Diffusion Models generate high-quality images from text prompts.
- Stable Diffusion enables unlimited synthetic image generation for data augmentation.
- Synthetic training images can complement real data for improved model training.
- Text-to-image generation is increasingly used for VLM training data augmentation.

## Source paper
- **Title**: Stable Diffusion: High-Resolution Image Synthesis with Latent Diffusion Models
- **Year**: 2022
- **Venue**: CVPR
- **Paper ID**: arxiv-2112.10752v2
- **URL**: http://arxiv.org/abs/2112.10752v2
- **arXiv ID**: 2112.10752v2
