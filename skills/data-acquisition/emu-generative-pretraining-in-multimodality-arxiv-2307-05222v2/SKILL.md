# Emu: Generative Pretraining in Multimodality

## One-line decision
Use this skill when you want to curate diverse interleaved multimodal data combining web pages, image-text pairs, and video for generative pretraining. Avoid it when you only need paired image-text data without interleaved document structure.

## Skill metadata
- **Skill type**: interleaved-multimodal-pretraining-data
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Curate a diverse corpus of interleaved multimodal data (web documents, image-text pairs, videos with subtitles) for generative pretraining of a unified multimodal model.

## Problem signature
- Modality: interleaved image-text web documents, image-text pairs, and video-text pairs.
- Data state: multiple data sources curated into interleaved sequences: web docs, paired data, and video data.
- Scale regime: billions of multimodal tokens from diverse sources.
- Model requirement: Autoregressive multimodal model with visual encoder and causal transformer.

## Use when
- You want to train a generative multimodal model on diverse data types.
- You can collect web pages, image-text pairs, and video-text data.
- You need a model that can both understand and generate images.

## Do not use when
- You only need image understanding without generation.
- You cannot collect or process video data.
- You need a contrastive model rather than a generative one.

## Required inputs
- **web_interleaved_data**: Web pages with naturally interleaved images and text.
- **paired_image_text**: Standard image-caption pair datasets.
- **video_text_data**: Videos with subtitles or descriptions.

## Optional inputs
- **image_generation_data**: High-quality image-text pairs specifically for generation quality.

## Outputs
- **emu_pretraining_corpus**: Diverse interleaved multimodal corpus.
- **emu_model**: Generative multimodal model for both understanding and generation.

## Assumptions and prerequisites
- Diverse interleaved data produces more capable generative models.
- Video data adds temporal understanding capabilities.
- Unified autoregressive training over multiple data types is effective.

## Procedure
1. **Collect web interleaved documents**
   Action: Extract web pages with interleaved images and text, preserving document structure.
   Why: Interleaved documents teach multimodal reasoning.
   Note: See paper for details.
2. **Gather paired image-text data**
   Action: Include LAION and similar paired datasets.
   Why: Paired data provides clean alignment signal.
   Note: See paper for details.
3. **Process video-text data**
   Action: Extract keyframes from videos and pair with subtitles or descriptions.
   Why: Video data adds temporal and dynamic understanding.
   Note: See paper for details.
4. **Create unified interleaved sequences**
   Action: Format all data types as interleaved token sequences.
   Why: Enables unified autoregressive training.
   Note: See paper for details.
5. **Pretrain generative model**
   Action: Train the Emu model on the unified corpus.
   Why: Diverse pretraining produces a versatile multimodal model.
   Note: See paper for details.

## Parameters to set
- **data_type_weights** — Role: Sampling weights for web, paired, and video data. How to set: Balance based on target capabilities. Default/range: Task-dependent. Effect: Affects which capabilities the model develops.
- **video_frame_rate** — Role: Keyframe extraction rate from videos. How to set: 1-2 FPS for efficiency. Default/range: 1 FPS. Effect: Higher rates capture more temporal detail but increase data size.
- **interleave_format** — Role: How images and text are interleaved in sequences. How to set: Preserve natural document order. Default/range: Natural order. Effect: Proper formatting teaches correct image-text relationships.

## Validation checks
- The model should handle understanding and generation across modalities.
- Video understanding benchmarks should benefit from video pretraining data.
- Image generation quality should be reasonable for an autoregressive model.

## Failure modes
- Video processing at scale is computationally expensive.
- Quality variation across data types may cause training instability.
- The model may favor dominant data types over rare ones.

## Adaptation notes for VLM training
- The multi-source interleaved approach applies to any generative multimodal model.
- Add domain-specific data sources for specialized applications.
- The video-text processing pipeline is reusable for video-language models.

## Implementation notes
- Use efficient video decoding for keyframe extraction.
- Pre-tokenize all data types to avoid bottlenecks.
- Monitor per-data-type loss during training.

## Evidence from the paper
- Emu demonstrates that diverse interleaved pretraining produces a versatile multimodal model.
- The model achieves strong performance on both understanding and generation benchmarks.
- Including video data improves temporal reasoning capabilities.
- Emu's data recipe has influenced subsequent generative multimodal models.

## Source paper
- **Title**: Emu: Generative Pretraining in Multimodality
- **Year**: 2023
- **Venue**: ICLR
- **Paper ID**: arxiv-2307.05222v2
- **URL**: http://arxiv.org/abs/2307.05222v2
- **arXiv ID**: 2307.05222v2
