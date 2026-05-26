# LLaVA-NeXT-Video: Scaling Video Understanding to Strong Image-Level Performance

## One-line decision
Use this skill when you want to transfer strong image understanding from LLaVA-NeXT to video through efficient frame sampling and video-specific data. Avoid it when you are building a video-from-scratch VLM.

## Skill metadata
- **Skill type**: image-to-video-transfer-data
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Transfer strong image understanding from LLaVA-NeXT to video through efficient frame sampling, dynamic resolution per frame, and video-specific instruction data, achieving video understanding without full video pretraining.

## Problem signature
- Modality: video frames processed as multiple images with video instruction data.
- Data state: video instruction data leveraging image-level VLM capability.
- Scale regime: video instruction data for transfer learning.
- Model requirement: LLaVA-NeXT architecture with video frame sampling.

## Use when
- You have a strong image VLM and want to add video.
- You prefer transfer learning over full video pretraining.
- Frame-based video processing is acceptable.

## Do not use when
- You need temporal modeling beyond frame sampling.
- Full video pretraining is preferred.
- Frame-based processing is too coarse.

## Required inputs
- **image_vlm**: Strong image VLM (LLaVA-NeXT) as base.
- **video_instruction_data**: Video-specific instruction data.
- **frame_sampling**: Strategy for sampling frames from videos.

## Optional inputs
- **temporal_data**: Data requiring temporal reasoning.

## Outputs
- **video_vlm**: Video-capable VLM transferred from image model.
- **transfer_recipe**: Recipe for image-to-video transfer.

## Assumptions and prerequisites
- Strong image understanding transfers to video.
- Frame sampling captures sufficient temporal information.
- Video-specific data adds temporal capability.

## Procedure
1. **Start with image VLM**
   Action: Use LLaVA-NeXT as the base model.
   Why: Leverages strong image understanding.
   Note: See paper for details.
2. **Add frame sampling**
   Action: Sample frames from videos for processing.
   Why: Converts video to multi-image input.
   Note: See paper for details.
3. **Train on video data**
   Action: Fine-tune on video instruction data.
   Why: Adds video-specific understanding.
   Note: See paper for details.
4. **Evaluate video performance**
   Action: Test on video understanding benchmarks.
   Why: Validates image-to-video transfer.
   Note: See paper for details.

## Parameters to set
- **frames_per_video** — Role: Number of frames sampled. How to set: 8-32 frames. Default/range: 16. Effect: More frames capture more temporal detail.
- **per_frame_resolution** — Role: Resolution per frame. How to set: Dynamic resolution (AnyRes). Default/range: AnyRes. Effect: Higher resolution improves per-frame detail.

## Validation checks
- Video performance should be strong from image transfer.
- Image capability should not degrade.
- Frame sampling should capture key temporal events.

## Failure modes
- Frame sampling may miss important temporal events.
- Transfer may not capture all video-specific reasoning.
- Many frames increase compute cost.

## Adaptation notes for VLM training
- Image-to-video transfer is an efficient approach for video VLMs.
- Frame sampling with strong per-frame understanding is competitive.
- Video-specific instruction data bridges the capability gap.

## Implementation notes
- Use uniform or key frame sampling.
- Apply AnyRes to each frame.
- Monitor both image and video metrics.

## Evidence from the paper
- LLaVA-NeXT-Video achieves strong video understanding from image transfer.
- Frame sampling with dynamic resolution captures sufficient temporal information.
- Video-specific instruction data adds temporal capability.
- Image-to-video transfer is more efficient than full video pretraining.

## Source paper
- **Title**: LLaVA-NeXT-Video: Scaling Video Understanding to Strong Image-Level Performance
- **Year**: 2024
- **Venue**: arXiv
- **Paper ID**: arxiv-2410.02713v1
- **URL**: http://arxiv.org/abs/2410.02713v1
- **arXiv ID**: 2410.02713v1
