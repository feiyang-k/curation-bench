# InternVid: A Large-scale Video-Text Dataset for Multimodal Understanding and Generation

## One-line decision
Use this skill when you need a 234M video-text dataset constructed with multi-scale captioning from ASR, metadata, and generated descriptions. Avoid it when you only need image-text data or a small video dataset.

## Skill metadata
- **Skill type**: large-scale-video-caption-pipeline
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Construct InternVid, a large-scale video-text dataset with 234 million video clips and captions generated through multi-scale captioning combining ASR transcripts, video metadata, and model-generated descriptions.

## Problem signature
- Modality: video clips with multi-scale generated captions.
- Data state: YouTube videos processed with multi-scale captioning pipeline.
- Scale regime: 234 million video clips from 7 million YouTube videos.
- Model requirement: Multi-scale captioning pipeline using ASR, metadata, and captioning models.

## Use when
- You need a very large-scale video-text dataset for pretraining.
- You want multi-scale captions combining multiple information sources.
- You need data for training video-language models.

## Do not use when
- Image-text data is sufficient for your needs.
- You cannot handle the scale of 234M clips.
- You need manually verified video captions.

## Required inputs
- **youtube_videos**: 7M YouTube videos across diverse topics.
- **captioning_pipeline**: Multi-scale pipeline combining ASR, metadata, and generated captions.
- **video_segmenter**: Tool for segmenting videos into coherent clips.

## Optional inputs
- **viclip_model**: ViCLIP model for video-text alignment scoring.

## Outputs
- **internvid_dataset**: 234M video clips with multi-scale captions.
- **viclip_model**: Video-text contrastive model trained on InternVid.

## Assumptions and prerequisites
- Multi-scale captioning produces richer descriptions than any single source.
- 234M clips provide sufficient scale for strong video-text pretraining.
- YouTube content is diverse enough for general video understanding.

## Procedure
1. **Collect YouTube videos**
   Action: Download 7M YouTube videos across diverse categories.
   Why: Diverse videos ensure broad content coverage.
   Note: See paper for details.
2. **Segment into clips**
   Action: Split videos into semantically coherent clips.
   Why: Clips are the natural unit for video-text learning.
   Note: See paper for details.
3. **Generate multi-scale captions**
   Action: Combine ASR transcripts, video metadata, and model-generated descriptions.
   Why: Multiple sources provide complementary information.
   Note: See paper for details.
4. **Filter and clean**
   Action: Remove low-quality clips and captions.
   Why: Quality filtering improves dataset utility.
   Note: See paper for details.
5. **Train ViCLIP**
   Action: Train a video-text contrastive model on InternVid.
   Why: Validates dataset quality through downstream performance.
   Note: See paper for details.

## Parameters to set
- **num_clips** — Role: Total video clips in the dataset. How to set: Extract from all collected videos. Default/range: 234M. Effect: Larger datasets improve pretraining quality.
- **captioning_sources** — Role: Sources for multi-scale captioning. How to set: Combine ASR, metadata, and generated descriptions. Default/range: 3 sources. Effect: More sources provide richer captions.
- **clip_duration** — Role: Duration of video clips. How to set: 5-30 seconds for coherence. Default/range: Variable. Effect: Clip length affects caption granularity.

## Validation checks
- ViCLIP trained on InternVid should achieve strong video-text retrieval.
- Captions should be informative and aligned with video content.
- The dataset should cover diverse visual and topical content.

## Failure modes
- YouTube video availability changes over time.
- Multi-scale captioning may produce contradictory information.
- Very large datasets require significant storage and processing.

## Adaptation notes for VLM training
- InternVid provides the largest open video-text dataset for pretraining.
- Use ViCLIP embeddings for video understanding downstream tasks.
- Combine with image-text data for unified multimodal training.

## Implementation notes
- Use distributed video processing for 234M clips.
- Cache intermediate captioning results.
- Store video IDs for reproducibility.

## Evidence from the paper
- InternVid contains 234M video clips with multi-scale captions from 7M YouTube videos.
- ViCLIP trained on InternVid achieves state-of-the-art video-text retrieval.
- Multi-scale captioning produces richer descriptions than single-source approaches.
- InternVid is the largest open video-text dataset.

## Source paper
- **Title**: InternVid: A Large-scale Video-Text Dataset for Multimodal Understanding and Generation
- **Year**: 2024
- **Venue**: ICLR
- **Paper ID**: arxiv-2307.06942v3
- **URL**: http://arxiv.org/abs/2307.06942v3
- **arXiv ID**: 2307.06942v3
