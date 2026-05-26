# Kinetics-400: A Large Video Understanding Dataset

## One-line decision
Use this skill when you need a large-scale action recognition dataset with 400 categories and 300K+ video clips for video encoder pretraining. Avoid it when temporal reasoning rather than action recognition is your focus.

## Skill metadata
- **Skill type**: large-scale-action-recognition-data
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Provide a large-scale human action recognition dataset with 400 action categories and 300K+ video clips from YouTube, enabling video encoder pretraining for video-language models.

## Problem signature
- Modality: video clips with human action category labels.
- Data state: 300K+ video clips with 400 action category labels.
- Scale regime: 300K+ clips, 400 categories.
- Model requirement: Any video understanding model for action recognition.

## Use when
- You need large-scale video action recognition data.
- You want to pretrain video encoders.
- You need diverse human action categories.

## Do not use when
- Temporal reasoning is your focus (use SSv2).
- Static image recognition is sufficient.
- You need longer-form video understanding.

## Required inputs
- **youtube_clips**: 300K+ 10-second video clips from YouTube.
- **action_labels**: 400 human action category labels.
- **temporal_trimming**: Clips trimmed to the relevant action segment.

## Optional inputs
- **audio**: Audio data from the clips.

## Outputs
- **kinetics_dataset**: 300K+ clips with 400 action labels.
- **action_benchmark**: Large-scale action recognition benchmark.

## Assumptions and prerequisites
- 400 action categories cover diverse human activities.
- YouTube provides sufficient video diversity.
- 10-second clips capture meaningful actions.

## Procedure
1. **Define action taxonomy**
   Action: Create 400 human action categories.
   Why: Broad taxonomy covers diverse actions.
   Note: See paper for details.
2. **Collect YouTube clips**
   Action: Gather 300K+ 10-second clips for each category.
   Why: Large scale enables effective pretraining.
   Note: See paper for details.
3. **Label actions**
   Action: Verify action labels through annotation.
   Why: Accurate labels provide training signal.
   Note: See paper for details.

## Parameters to set
- **num_categories** — Role: Number of action categories. How to set: 400 for broad coverage. Default/range: 400. Effect: More categories test broader recognition.
- **clips_per_category** — Role: Clips per action category. How to set: 400-1000 per category. Default/range: ~750. Effect: More clips improve per-category quality.

## Validation checks
- Action recognition accuracy should be measurable.
- The 400 categories should be distinguishable.
- The dataset should be large enough for pretraining.

## Failure modes
- YouTube videos may become unavailable.
- Some action categories may overlap.
- 10-second clips may miss longer actions.

## Adaptation notes for VLM training
- Kinetics is the standard pretraining dataset for video encoders.
- Video encoders pretrained on Kinetics are used in video VLMs.
- Combine with text-video data for video-language training.

## Implementation notes
- Use yt-dlp for video downloading.
- Handle missing videos gracefully.
- Evaluate on standard Kinetics benchmarks.

## Evidence from the paper
- Kinetics provides 300K+ video clips across 400 action categories.
- The dataset is the standard for video encoder pretraining.
- Large-scale action recognition enables strong video features.
- Kinetics-pretrained encoders are widely used in video VLMs.

## Source paper
- **Title**: Kinetics-400: A Large Video Understanding Dataset
- **Year**: 2017
- **Venue**: arXiv
- **Paper ID**: arxiv-1705.06950v1
- **URL**: http://arxiv.org/abs/1705.06950v1
- **arXiv ID**: 1705.06950v1
