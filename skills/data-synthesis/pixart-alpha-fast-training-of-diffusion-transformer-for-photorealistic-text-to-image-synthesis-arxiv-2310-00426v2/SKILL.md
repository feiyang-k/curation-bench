# PixArt-alpha: Fast Training of Diffusion Transformer for Photorealistic Text-to-Image Synthesis

## One-line decision
Use this skill when you want to train a high-quality text-to-image model efficiently using carefully curated high-quality captions from an LLM. Avoid it when you already have a well-trained text-to-image model.

## Skill metadata
- **Skill type**: efficient-dit-training-data
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Train a high-quality text-to-image Diffusion Transformer (DiT) efficiently by using LLM-generated high-quality captions and progressive training from low to high resolution.

## Problem signature
- Modality: images with LLM-generated detailed captions for diffusion training.
- Data state: images recaptioned with LLM-generated detailed descriptions.
- Scale regime: internal dataset with recaptioned images.
- Model requirement: DiT architecture + T5 text encoder.

## Use when
- You want efficient text-to-image model training.
- You can recaption training images with an LLM.
- You want high-quality generation with less compute.

## Do not use when
- You already have a well-trained generation model.
- Recaptioning is infeasible for your data.
- Image generation is not your goal.

## Required inputs
- **training_images**: Images for generation training.
- **llm_captioner**: LLM for generating detailed captions.
- **dit_architecture**: Diffusion Transformer architecture.

## Optional inputs
- **progressive_schedule**: Schedule for increasing resolution during training.

## Outputs
- **pixart_model**: Efficient high-quality text-to-image model.
- **recaptioned_data**: Images with LLM-generated detailed captions.

## Assumptions and prerequisites
- LLM-generated captions improve generation quality.
- Progressive resolution training is more efficient.
- DiT architecture enables efficient scaling.

## Procedure
1. **Recaption training images**
   Action: Generate detailed captions for all images using an LLM.
   Why: Better captions improve prompt following.
   Note: See paper for details.
2. **Train at low resolution**
   Action: Start training DiT at 256x256.
   Why: Low resolution training is efficient for learning basics.
   Note: See paper for details.
3. **Progressive resolution increase**
   Action: Increase resolution to 512x512 and 1024x1024.
   Why: Progressive increase is more efficient than training at high resolution from scratch.
   Note: See paper for details.
4. **Evaluate generation quality**
   Action: Compare to Stable Diffusion and DALL-E baselines.
   Why: Validates training efficiency and quality.
   Note: See paper for details.

## Parameters to set
- **caption_quality** — Role: Quality of LLM-generated captions. How to set: Use strong LLM for detailed descriptions. Default/range: High quality. Effect: Better captions significantly improve generation.
- **progressive_stages** — Role: Number of resolution stages. How to set: 3 stages (256→512→1024). Default/range: 3. Effect: Progressive training is more efficient.

## Validation checks
- PixArt should match DALL-E/SD quality with less training compute.
- LLM captions should improve over original captions.
- Progressive training should be more efficient.

## Failure modes
- LLM captions may introduce hallucinated content.
- Progressive training requires careful stage transitions.
- DiT may require different tuning than U-Net diffusion.

## Adaptation notes for VLM training
- PixArt demonstrates that caption quality matters for generation.
- The recaptioning approach applies to any generation training.
- Efficient training recipes transfer to VLM data processing.

## Implementation notes
- Use a strong LLM for recaptioning.
- Implement progressive resolution training.
- Compare to baselines at equal compute.

## Evidence from the paper
- PixArt-alpha matches DALL-E 2 quality with 10% of the training cost.
- LLM-generated captions significantly improve generation quality.
- Progressive resolution training is more efficient than constant high resolution.
- The approach demonstrates that data quality reduces compute requirements.

## Source paper
- **Title**: PixArt-alpha: Fast Training of Diffusion Transformer for Photorealistic Text-to-Image Synthesis
- **Year**: 2024
- **Venue**: ICLR
- **Paper ID**: arxiv-2310.00426v2
- **URL**: http://arxiv.org/abs/2310.00426v2
- **arXiv ID**: 2310.00426v2
