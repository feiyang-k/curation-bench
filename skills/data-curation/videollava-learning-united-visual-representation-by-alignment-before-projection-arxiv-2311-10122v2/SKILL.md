# VideoLLaVA: Learning United Visual Representation by Alignment Before Projection

## One-line decision
Use this skill when you want to train a unified image-video VLM by aligning visual representations before projecting to the language model. Avoid it when you only need image understanding or cannot curate both image and video data.

## Skill metadata
- **Skill type**: unified-image-video-data
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Train a unified VLM handling both images and videos by aligning visual representations from both modalities before projecting to the language model, using curated image-text and video-text data.

## Problem signature
- Modality: images and videos with unified instruction-following data.
- Data state: combined image-text and video-text instruction data for unified training.
- Scale regime: 665K image + 100K video instruction samples.
- Model requirement: LanguageBind encoder for unified image-video representation + LLM.

## Use when
- You want a single model handling both image and video understanding.
- You can curate both image and video instruction data.
- You want unified visual representation for both modalities.

## Do not use when
- You only need image understanding.
- You cannot curate video instruction data.
- Separate image and video models are acceptable.

## Required inputs
- **image_instruction_data**: Image instruction-following data (e.g., LLaVA-1.5 data).
- **video_instruction_data**: Video instruction-following data (e.g., Video-ChatGPT data).
- **unified_encoder**: LanguageBind encoder for both image and video.

## Optional inputs
- **alignment_data**: Data for aligning image and video representations.

## Outputs
- **video_llava_model**: Unified image-video VLM.
- **unified_data_pipeline**: Pipeline for combined image-video training.

## Assumptions and prerequisites
- Aligning image and video representations enables unified training.
- Both modalities benefit from shared understanding.
- LanguageBind provides a unified encoding space.

## Procedure
1. **Align image and video representations**
   Action: Use LanguageBind to create aligned representations for both modalities.
   Why: Aligned representations enable unified processing.
   Note: See paper for details.
2. **Combine instruction data**
   Action: Mix image instruction data (665K) with video instruction data (100K).
   Why: Combined data trains both capabilities.
   Note: See paper for details.
3. **Train unified model**
   Action: Train the VLM on combined image-video instruction data.
   Why: Unified training enables a single model for both modalities.
   Note: See paper for details.
4. **Evaluate on both modalities**
   Action: Test on both image and video benchmarks.
   Why: Validates that both capabilities are maintained.
   Note: See paper for details.

## Parameters to set
- **image_video_ratio** — Role: Ratio of image to video instruction data. How to set: ~665K:100K. Default/range: ~6:1 image:video. Effect: Balance determines relative capability strength.
- **encoder_type** — Role: Unified visual encoder. How to set: LanguageBind for aligned representations. Default/range: LanguageBind. Effect: Better alignment improves unified understanding.

## Validation checks
- Image benchmarks should not degrade with video data addition.
- Video understanding should be competitive with video-only models.
- The model should seamlessly handle both modalities.

## Failure modes
- Image and video data may have different quality distributions.
- Unified training may compromise single-modality performance.
- LanguageBind alignment may not be perfect.

## Adaptation notes for VLM training
- The alignment-before-projection approach is reusable for other multi-modality VLMs.
- Extend to audio, 3D, or other modalities.
- The unified data pipeline supports incremental modality addition.

## Implementation notes
- Balance image and video batches during training.
- Monitor per-modality performance to detect degradation.
- Use the LanguageBind implementation for visual encoding.

## Evidence from the paper
- Video-LLaVA trains a unified image-video VLM through alignment before projection.
- The model handles both image and video understanding without modality-specific heads.
- Combining 665K image and 100K video instruction data enables unified training.
- Video-LLaVA achieves competitive results on both image and video benchmarks.

## Source paper
- **Title**: VideoLLaVA: Learning United Visual Representation by Alignment Before Projection
- **Year**: 2023
- **Venue**: EMNLP
- **Paper ID**: arxiv-2311.10122v2
- **URL**: http://arxiv.org/abs/2311.10122v2
- **arXiv ID**: 2311.10122v2
