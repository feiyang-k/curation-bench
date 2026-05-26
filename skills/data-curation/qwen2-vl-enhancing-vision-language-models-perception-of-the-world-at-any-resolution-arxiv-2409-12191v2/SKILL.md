# Qwen2-VL: Enhancing Vision-Language Model's Perception of the World at Any Resolution

## One-line decision
Use this skill when you want to train a VLM with native dynamic resolution support and multi-stage data covering images, videos, and documents. Avoid it when you use fixed-resolution input and do not need dynamic resolution.

## Skill metadata
- **Skill type**: dynamic-resolution-data-pipeline
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Build a multi-stage data pipeline for training a VLM with native dynamic resolution, supporting images at any aspect ratio and resolution, plus video and document understanding.

## Problem signature
- Modality: images, videos, and documents at any resolution.
- Data state: multi-stage data: web pairs, multi-task, instruction tuning with dynamic resolution.
- Scale regime: billions of web pairs; millions of instruction samples.
- Model requirement: ViT with Naive Dynamic Resolution + Qwen-2 LLM.

## Use when
- You want native dynamic resolution VLM training.
- You need multi-modal coverage (image, video, document).
- You want state-of-the-art VLM performance.

## Do not use when
- Fixed resolution is sufficient.
- You only need image understanding.
- You cannot implement native dynamic resolution.

## Required inputs
- **web_pairs**: Billions of image-text pairs for pretraining.
- **multitask_data**: Diverse VL datasets for multi-task training.
- **instruction_data**: High-quality instruction data for fine-tuning.

## Optional inputs
- **video_data**: Video instruction data for temporal understanding.

## Outputs
- **qwen2_vl_model**: State-of-the-art VLM with dynamic resolution.
- **data_pipeline**: Multi-stage data pipeline for dynamic resolution VLM.

## Assumptions and prerequisites
- Native dynamic resolution captures more visual detail.
- Multi-stage training progressively builds capabilities.
- Multi-modal data coverage enables versatile understanding.

## Procedure
1. **Stage 1: Pretraining on web pairs**
   Action: Train on billions of web image-text pairs with dynamic resolution.
   Why: Establishes foundational vision-language alignment.
   Note: See paper for details.
2. **Stage 2: Multi-task training**
   Action: Add VQA, grounding, OCR, and detection data.
   Why: Builds specific capabilities.
   Note: See paper for details.
3. **Stage 3: Instruction tuning**
   Action: Fine-tune on high-quality instruction data.
   Why: Enables interactive use.
   Note: See paper for details.
4. **Evaluate comprehensively**
   Action: Test across image, video, and document benchmarks.
   Why: Validates multi-modal capability.
   Note: See paper for details.

## Parameters to set
- **min_pixels** — Role: Minimum image pixels processed. How to set: 256 for thumbnails. Default/range: 256. Effect: Smaller minimums handle tiny images.
- **max_pixels** — Role: Maximum image pixels processed. How to set: Based on compute budget. Default/range: 1280*28*28. Effect: Larger maximums enable higher resolution.

## Validation checks
- Dynamic resolution should improve over fixed resolution on detail-heavy tasks.
- Multi-modal performance should be competitive across all modalities.
- The model should handle diverse aspect ratios correctly.

## Failure modes
- Dynamic resolution increases compute variability.
- Very high resolution images may exceed memory.
- Multi-stage training is complex and expensive.

## Adaptation notes for VLM training
- Qwen2-VL's data pipeline is a state-of-the-art template for VLM training.
- Native dynamic resolution is increasingly adopted by modern VLMs.
- The multi-stage approach balances data quantity and quality.

## Implementation notes
- Implement efficient dynamic resolution batching.
- Monitor per-resolution performance.
- Use mixed-resolution training for robustness.

## Evidence from the paper
- Qwen2-VL achieves state-of-the-art across image, video, and document benchmarks.
- Native dynamic resolution significantly improves detail-dependent tasks.
- Multi-stage data pipeline with dynamic resolution is highly effective.
- The model handles images at any resolution and aspect ratio.

## Source paper
- **Title**: Qwen2-VL: Enhancing Vision-Language Model's Perception of the World at Any Resolution
- **Year**: 2024
- **Venue**: arXiv
- **Paper ID**: arxiv-2409.12191v2
- **URL**: http://arxiv.org/abs/2409.12191v2
- **arXiv ID**: 2409.12191v2
