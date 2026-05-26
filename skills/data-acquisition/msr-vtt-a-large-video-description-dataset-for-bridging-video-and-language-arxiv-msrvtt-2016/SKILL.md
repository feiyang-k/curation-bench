# MSR-VTT: A Large Video Description Dataset for Bridging Video and Language

## One-line decision
Use this skill when you need a video description dataset with 10K web clips and 200K sentences for training and evaluating video-language models. Avoid it when you have sufficient video captioning data.

## Skill metadata
- **Skill type**: video-description-benchmark
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Provide a large video description dataset with 10K web video clips and 200K human-written sentences for training and evaluating video captioning and video-text retrieval.

## Problem signature
- Modality: video clips with human-written descriptions.
- Data state: 10K clips with 200K captioning sentences.
- Scale regime: 10K clips, 200K descriptions.
- Model requirement: Any video-language model.

## Use when
- You need video captioning training or evaluation data.
- You want video-text retrieval evaluation.
- You need diverse video descriptions.

## Do not use when
- You have sufficient video captioning data.
- You need very large-scale video data.
- You need specialized domain videos.

## Required inputs
- **video_clips**: 10K diverse web video clips.
- **human_descriptions**: 200K human-written descriptions.
- **evaluation_metrics**: Captioning and retrieval metrics.

## Optional inputs
- **category_labels**: Video category annotations.

## Outputs
- **msrvtt_dataset**: 10K clips with 200K descriptions.
- **video_language_benchmark**: Standard video-language evaluation.

## Assumptions and prerequisites
- 10K diverse clips cover broad video content.
- 200K descriptions provide rich text supervision.
- Human-written descriptions are high quality.

## Procedure
1. **Collect web video clips**
   Action: Gather 10K diverse clips from the web.
   Why: Diverse clips ensure broad coverage.
   Note: See paper for details.
2. **Collect descriptions**
   Action: Have annotators write 20 descriptions per clip.
   Why: Multiple descriptions capture diversity.
   Note: See paper for details.
3. **Create benchmarks**
   Action: Define captioning and retrieval benchmarks.
   Why: Enables standardized evaluation.
   Note: See paper for details.

## Parameters to set
- **num_clips** — Role: Total video clips. How to set: 10K for diversity. Default/range: 10K. Effect: More clips improve coverage.
- **descriptions_per_clip** — Role: Descriptions per video. How to set: 20 for diversity. Default/range: 20. Effect: More descriptions capture varied perspectives.

## Validation checks
- Descriptions should accurately describe video content.
- The benchmark should test both captioning and retrieval.
- The dataset should cover diverse video types.

## Failure modes
- 10K clips may not cover all video domains.
- Some descriptions may be generic.
- Video availability may change.

## Adaptation notes for VLM training
- MSR-VTT is a standard evaluation dataset for video-language models.
- Use for evaluating video VLM captioning and retrieval.
- Combine with larger datasets for video-language training.

## Implementation notes
- Use standard evaluation metrics (CIDEr, R@K).
- Handle the multi-description format.
- Report on standard evaluation splits.

## Evidence from the paper
- MSR-VTT provides 10K clips with 200K human descriptions.
- The dataset is a standard benchmark for video captioning and retrieval.
- 20 descriptions per clip provide rich evaluation diversity.
- MSR-VTT is widely used for video-language model evaluation.

## Source paper
- **Title**: MSR-VTT: A Large Video Description Dataset for Bridging Video and Language
- **Year**: 2016
- **Venue**: CVPR
- **Paper ID**: arxiv-msrvtt-2016
- **URL**: https://www.microsoft.com/en-us/research/publication/msr-vtt-a-large-video-description-dataset-for-bridging-video-and-language/
- **arXiv ID**: N/A
