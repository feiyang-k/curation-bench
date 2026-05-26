# TokenFlow: Unified Image Tokenizer for Multimodal Understanding and Generation

## One-line decision
Use this skill when you want a unified image tokenizer that supports both understanding and generation tasks in VLMs. Avoid it when separate tokenizers for understanding and generation work for you.

## Skill metadata
- **Skill type**: unified-image-tokenization
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Create a unified image tokenizer that works for both visual understanding and image generation, bridging the gap between discriminative and generative visual processing.

## Problem signature
- Modality: images tokenized for both understanding and generation.
- Data state: training data for unified tokenizer spanning both tasks.
- Scale regime: large-scale image data for tokenizer training.
- Model requirement: Unified tokenizer for understanding and generation VLMs.

## Use when
- You want one tokenizer for both understanding and generation.
- You build models that both understand and generate images.
- You want to unify visual processing.

## Do not use when
- Separate tokenizers work fine.
- You only do understanding or only generation.
- Custom tokenizers are needed.

## Required inputs
- **image_data**: Large-scale images for tokenizer training.
- **understanding_tasks**: Data for validating understanding quality.
- **generation_tasks**: Data for validating generation quality.

## Optional inputs
- **codebook_config**: VQVAE codebook configuration.

## Outputs
- **unified_tokenizer**: Tokenizer for both understanding and generation.
- **tokenized_data**: Images tokenized for unified VLM training.

## Assumptions and prerequisites
- A single tokenizer can serve both understanding and generation.
- Unified tokenization simplifies model architecture.
- The quality tradeoff is acceptable for both tasks.

## Procedure
1. **Design unified tokenizer**
   Action: Create a tokenizer balancing understanding and generation needs.
   Why: Unifies visual processing.
   Note: See paper for details.
2. **Train on diverse images**
   Action: Train on large-scale images.
   Why: Diverse training ensures quality.
   Note: See paper for details.
3. **Validate on both tasks**
   Action: Test on understanding and generation benchmarks.
   Why: Confirms dual capability.
   Note: See paper for details.

## Parameters to set
- **codebook_size** — Role: Size of discrete token vocabulary. How to set: 16K-64K for good quality. Default/range: 32K. Effect: Larger codebook improves quality.

## Validation checks
- Understanding quality should match CLIP-based tokenization.
- Generation quality should match VQGAN-based tokenization.
- Unified approach should simplify the pipeline.

## Failure modes
- Compromising between tasks may hurt both.
- Codebook size may be insufficient.
- Training is complex.

## Adaptation notes for VLM training
- Unified tokenization simplifies VLM architectures.
- Enables models like Chameleon that do both tasks.
- The approach is key for unified multimodal models.

## Implementation notes
- Balance understanding and generation objectives.
- Use large codebooks for quality.
- Compare to separate tokenizer baselines.

## Evidence from the paper
- TokenFlow unifies image tokenization for understanding and generation.
- A single tokenizer can serve both tasks effectively.
- Unified tokenization simplifies multimodal model architectures.
- The approach bridges discriminative and generative visual processing.

## Source paper
- **Title**: TokenFlow: Unified Image Tokenizer for Multimodal Understanding and Generation
- **Year**: 2024
- **Venue**: arXiv
- **Paper ID**: arxiv-2412.03069v2
- **URL**: http://arxiv.org/abs/2412.03069v2
- **arXiv ID**: 2412.03069v2
