# ShareGPT4Video: Improving Video Understanding and Generation with Better Captions

## One-line decision
Use this skill when you want to generate high-quality video captions using GPT-4V and train an open-source video captioner for scaling. Avoid it when you do not work with video or have sufficient video captions.

## Skill metadata
- **Skill type**: video-recaptioning-pipeline
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Generate high-quality video captions using GPT-4V on a seed set, then train an open-source video captioner (ShareCaptioner-Video) to scale to 4.8M video clips, improving both video understanding and generation.

## Problem signature
- Modality: videos with detailed GPT-4V-quality synthetic captions.
- Data state: video clips recaptioned with GPT-4V-quality descriptions.
- Scale regime: 4.8M video clips with high-quality captions.
- Model requirement: GPT-4V for seed captions; open-source video captioner for scaling.

## Use when
- You need high-quality video captions at scale.
- You can generate seed captions with GPT-4V.
- You want to improve both video understanding and generation.

## Do not use when
- You do not work with video data.
- You have sufficient video captions.
- You cannot afford GPT-4V API calls for seed generation.

## Required inputs
- **video_clips**: Video clips to be captioned.
- **gpt4v_api**: GPT-4V for generating seed video captions.
- **base_video_captioner**: Open-source model to train as ShareCaptioner-Video.

## Optional inputs
- **quality_filter**: Filter for removing low-quality video captions.

## Outputs
- **sharegpt4video_data**: 4.8M video clips with high-quality captions.
- **share_captioner_video**: Open-source video captioning model.

## Assumptions and prerequisites
- GPT-4V generates better video captions than existing methods.
- A trained video captioner can scale GPT-4V-quality captions.
- Better video captions improve both understanding and generation.

## Procedure
1. **Generate seed video captions with GPT-4V**
   Action: Caption a seed set of videos with GPT-4V.
   Why: Creates high-quality seed data for training the video captioner.
   Note: See paper for details.
2. **Train ShareCaptioner-Video**
   Action: Fine-tune an open-source model on the seed captions.
   Why: Enables scaling without continued API costs.
   Note: See paper for details.
3. **Scale to 4.8M videos**
   Action: Caption 4.8M video clips with ShareCaptioner-Video.
   Why: Provides high-quality captions at scale.
   Note: See paper for details.
4. **Improve video models**
   Action: Use the captions for video understanding and generation training.
   Why: Better captions improve downstream models.
   Note: See paper for details.

## Parameters to set
- **seed_size** — Role: Number of GPT-4V seed captions. How to set: Enough for training the captioner. Default/range: Thousands. Effect: More seeds improve captioner quality.
- **target_scale** — Role: Total videos to caption. How to set: 4.8M for comprehensive coverage. Default/range: 4.8M. Effect: More captions improve downstream models.

## Validation checks
- ShareCaptioner-Video should match GPT-4V caption quality.
- Video models trained on the captions should improve.
- Captions should be temporally accurate and detailed.

## Failure modes
- GPT-4V may not handle all video types well.
- Video captioning is harder than image captioning.
- Temporal accuracy may be difficult to maintain at scale.

## Adaptation notes for VLM training
- Apply the ShareGPT4V recipe to video captioning.
- The seed-then-scale approach generalizes to video recaptioning.
- Combine video captions with image captions for unified training.

## Implementation notes
- Sample frames strategically for GPT-4V video captioning.
- Train the video captioner with temporal awareness.
- Validate caption temporal accuracy.

## Evidence from the paper
- ShareGPT4Video generates 4.8M high-quality video captions using a seed-then-scale approach.
- ShareCaptioner-Video replicates GPT-4V caption quality at scale.
- Better video captions improve both video understanding and generation models.
- The approach mirrors ShareGPT4V's success for video data.

## Source paper
- **Title**: ShareGPT4Video: Improving Video Understanding and Generation with Better Captions
- **Year**: 2024
- **Venue**: arXiv
- **Paper ID**: arxiv-2406.04325v2
- **URL**: http://arxiv.org/abs/2406.04325v2
- **arXiv ID**: 2406.04325v2
