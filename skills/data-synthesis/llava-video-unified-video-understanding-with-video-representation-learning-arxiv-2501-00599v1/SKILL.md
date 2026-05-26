# LLaVA-Video: Unified Video Understanding with Video Representation Learning

## One-line decision
Use this skill when you want to scale video instruction data for training a unified video understanding VLM with diverse temporal reasoning tasks. Avoid it when you only need image understanding or have limited video data.

## Skill metadata
- **Skill type**: video-instruction-scaling
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Scale video instruction data for training a unified video understanding VLM, covering diverse temporal reasoning tasks from short to long videos with comprehensive temporal annotations.

## Problem signature
- Modality: videos with scaled instruction-following data for diverse temporal tasks.
- Data state: curated video instruction data covering diverse temporal reasoning.
- Scale regime: millions of video instruction samples from diverse sources.
- Model requirement: LLaVA-style VLM adapted for video with temporal reasoning.

## Use when
- You want to train a comprehensive video understanding VLM.
- You need diverse temporal reasoning data.
- You can curate video data at scale.

## Do not use when
- Image understanding is sufficient.
- You have limited video data.
- You do not need temporal reasoning.

## Required inputs
- **video_sources**: Diverse video datasets for instruction generation.
- **temporal_annotations**: Temporal event and action annotations.
- **instruction_generator**: Pipeline for creating temporal instruction data.

## Optional inputs
- **long_video_data**: Long-form video data for extended temporal reasoning.

## Outputs
- **video_instruction_data**: Scaled video instruction dataset.
- **llava_video_model**: Unified video understanding VLM.

## Assumptions and prerequisites
- Diverse temporal reasoning data improves video understanding.
- Scaling video instruction data follows similar benefits as image instruction scaling.
- Short and long video understanding require different training data.

## Procedure
1. **Curate diverse video sources**
   Action: Collect videos from diverse sources covering different durations and content.
   Why: Source diversity ensures broad video understanding.
   Note: See paper for details.
2. **Generate temporal instructions**
   Action: Create instruction data requiring temporal reasoning.
   Why: Temporal reasoning is the key video-specific capability.
   Note: See paper for details.
3. **Scale instruction generation**
   Action: Generate millions of video instruction samples.
   Why: Scale improves coverage and diversity.
   Note: See paper for details.
4. **Train unified video VLM**
   Action: Train LLaVA-Video on the scaled instruction data.
   Why: Comprehensive data produces a versatile video VLM.
   Note: See paper for details.

## Parameters to set
- **video_duration_range** — Role: Range of video durations. How to set: Include short (seconds) to long (minutes) videos. Default/range: Varied. Effect: Duration diversity improves temporal flexibility.
- **temporal_task_types** — Role: Types of temporal reasoning tasks. How to set: Include ordering, causation, prediction, summarization. Default/range: Diverse. Effect: More types improve temporal understanding.

## Validation checks
- Video understanding should improve across multiple benchmarks.
- Temporal reasoning should be significantly better than image-only baselines.
- Long video understanding should be competitive.

## Failure modes
- Video processing at scale is computationally expensive.
- Temporal annotation quality may vary.
- Long videos may exceed model context capacity.

## Adaptation notes for VLM training
- LLaVA-Video's data recipe is a template for video VLM training.
- Combine video and image instruction data for unified training.
- The temporal instruction generation approach is reusable.

## Implementation notes
- Use efficient video encoding with frame sampling.
- Balance short and long video data.
- Monitor temporal reasoning metrics specifically.

## Evidence from the paper
- LLaVA-Video scales video instruction data for comprehensive temporal understanding.
- Diverse temporal reasoning data significantly improves video VLM performance.
- The model handles short to long videos with unified architecture.
- LLaVA-Video achieves state-of-the-art on multiple video understanding benchmarks.

## Source paper
- **Title**: LLaVA-Video: Unified Video Understanding with Video Representation Learning
- **Year**: 2025
- **Venue**: arXiv
- **Paper ID**: arxiv-2501.00599v1
- **URL**: http://arxiv.org/abs/2501.00599v1
- **arXiv ID**: 2501.00599v1
