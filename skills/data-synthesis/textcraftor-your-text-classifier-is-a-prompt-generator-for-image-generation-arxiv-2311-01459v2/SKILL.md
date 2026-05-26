# TextCraftor: Your Text Classifier is a Prompt Generator for Image Generation

## One-line decision
Use this skill when you want to refine text prompts for image generation to produce higher quality, more faithful synthetic training images. Avoid it when your prompts already produce satisfactory synthetic images.

## Skill metadata
- **Skill type**: prompt-refinement-for-generation
- **Paper kind**: operational-method
- **Actionability**: medium
- **Evidence quality**: full_paper

## Goal
Refine text prompts for image generation models to produce higher quality and more faithful synthetic images for training data augmentation.

## Problem signature
- Modality: refined text prompts for improved synthetic image generation.
- Data state: text prompts optimized for better synthetic image generation.
- Scale regime: any number of prompts to refine.
- Model requirement: Text-to-image model for generation; CLIP for quality assessment.

## Use when
- You want better synthetic images from text-to-image models.
- Your prompts produce suboptimal images.
- You use synthetic images for training data.

## Do not use when
- Your prompts already work well.
- You do not use synthetic images.
- Manual prompt engineering is sufficient.

## Required inputs
- **initial_prompts**: Text prompts for image generation.
- **generation_model**: Text-to-image model (Stable Diffusion, etc.).
- **quality_scorer**: CLIP or similar for assessing image-prompt alignment.

## Optional inputs
- **target_distribution**: Desired image distribution for training.

## Outputs
- **refined_prompts**: Optimized prompts for better image generation.
- **improved_images**: Higher quality synthetic images.

## Assumptions and prerequisites
- Prompt quality significantly affects generated image quality.
- Automated prompt refinement can outperform manual engineering.
- Better prompts lead to better training data.

## Procedure
1. **Generate initial images**
   Action: Generate images with initial prompts.
   Why: Establishes baseline generation quality.
   Note: See paper for details.
2. **Assess generation quality**
   Action: Score images for prompt faithfulness and quality.
   Why: Quality assessment guides refinement.
   Note: See paper for details.
3. **Refine prompts**
   Action: Optimize prompts based on quality feedback.
   Why: Refined prompts produce better images.
   Note: See paper for details.
4. **Regenerate with refined prompts**
   Action: Generate new images with refined prompts.
   Why: Validates prompt improvement.
   Note: See paper for details.

## Parameters to set
- **refinement_method** — Role: How prompts are refined. How to set: Use CLIP-guided optimization or LLM rewriting. Default/range: Task-dependent. Effect: Different methods produce different improvements.
- **quality_metric** — Role: Metric for assessing generation quality. How to set: CLIP score or aesthetic score. Default/range: CLIP score. Effect: Metric guides what aspects improve.

## Validation checks
- Refined prompts should produce higher quality images.
- Images should be more faithful to the intent.
- Refined synthetic data should improve downstream training.

## Failure modes
- Refinement may overfit to the quality metric.
- Some prompts may not be improvable.
- Refinement adds computational cost.

## Adaptation notes for VLM training
- Apply prompt refinement to VLM training data augmentation.
- Better prompts improve the quality of synthetic training data.
- Combine with CutMix/Mixup for comprehensive augmentation.

## Implementation notes
- Use CLIP scores for objective refinement.
- Compare refined vs original prompts.
- Validate downstream training improvement.

## Evidence from the paper
- TextCraftor shows that refined prompts significantly improve synthetic image quality.
- Automated prompt refinement outperforms manual engineering.
- Better prompts lead to more faithful and higher quality synthetic images.
- The approach improves downstream training when using synthetic data.

## Source paper
- **Title**: TextCraftor: Your Text Classifier is a Prompt Generator for Image Generation
- **Year**: 2023
- **Venue**: arXiv
- **Paper ID**: arxiv-2311.01459v2
- **URL**: http://arxiv.org/abs/2311.01459v2
- **arXiv ID**: 2311.01459v2
