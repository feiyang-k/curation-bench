# HowTo100M: Learning a Text-Video Embedding by Watching Hundred Million Narrated Video Clips

## One-line decision
Use this skill when you want to mine narrated instructional videos from YouTube as video-text training data at hundred-million scale. Avoid it when you need clean video captions rather than noisy ASR transcripts.

## Skill metadata
- **Skill type**: instructional-video-mining
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Mine narrated instructional videos from YouTube at hundred-million scale, using automatically transcribed narrations as text supervision for learning video-text embeddings.

## Problem signature
- Modality: video clips with ASR-transcribed narrations as text supervision.
- Data state: YouTube instructional videos with automatically generated speech transcripts.
- Scale regime: 136 million video clips from 1.22 million YouTube videos.
- Model requirement: No model required for collection; ASR transcription is automated; validated with video-text embedding training.

## Use when
- You need large-scale video-text data for pretraining.
- You can tolerate noisy ASR transcriptions as text supervision.
- You want instructional/how-to video content.

## Do not use when
- You need clean, accurate video captions.
- You need non-instructional video content.
- YouTube content is unavailable in your region.

## Required inputs
- **youtube_videos**: Instructional videos from YouTube.
- **asr_transcription**: Automatic speech recognition system for transcribing narrations.
- **clip_segmentation**: Method for segmenting videos into clips aligned with transcript segments.

## Optional inputs
- **topic_filter**: Filter for selecting specific instructional topics.

## Outputs
- **howto100m_dataset**: 136M video clips with ASR transcriptions from 1.22M YouTube videos.
- **video_text_embeddings**: Learned video-text embedding space.

## Assumptions and prerequisites
- ASR transcriptions, while noisy, provide useful text supervision for video understanding.
- Instructional videos contain natural narration aligned with visual content.
- Scale compensates for noise in ASR transcriptions.

## Procedure
1. **Identify instructional YouTube videos**
   Action: Search YouTube for instructional/how-to videos across diverse topics.
   Why: Instructional videos have narrations describing visual actions.
   Note: See paper for details.
2. **Download and transcribe**
   Action: Download videos and extract ASR transcriptions.
   Why: ASR provides text supervision without manual annotation.
   Note: See paper for details.
3. **Segment into clips**
   Action: Segment videos into clips aligned with transcript segments.
   Why: Clip-transcript pairs form the training data units.
   Note: See paper for details.
4. **Train video-text embeddings**
   Action: Train a dual-encoder model on clip-transcript pairs.
   Why: Learns aligned video and text representations.
   Note: See paper for details.
5. **Evaluate on downstream tasks**
   Action: Test on video retrieval and QA tasks.
   Why: Validates the learned representations.
   Note: See paper for details.

## Parameters to set
- **clip_duration** — Role: Duration of video clips. How to set: Align with transcript segments. Default/range: ~5-10 seconds. Effect: Shorter clips have tighter text alignment but less visual context.
- **asr_quality** — Role: Quality of automatic speech recognition. How to set: Use best available ASR. Default/range: YouTube ASR. Effect: Better ASR improves text supervision quality.
- **topic_diversity** — Role: Range of instructional topics covered. How to set: Include diverse how-to categories. Default/range: 23K+ activities. Effect: More topics improve generalization.

## Validation checks
- Video-text retrieval metrics should improve with more training data.
- The noisy ASR supervision should still enable meaningful video understanding.
- Topic coverage should be broad across instructional categories.

## Failure modes
- ASR errors introduce significant noise in text supervision.
- Narrations may describe off-screen content or future actions.
- YouTube video availability changes over time.

## Adaptation notes for VLM training
- HowTo100M is a foundational video-text dataset for video understanding research.
- Combine with cleaner caption datasets for balanced training.
- The mining approach can be applied to other video platforms.

## Implementation notes
- Use yt-dlp for efficient YouTube video downloading.
- Store video IDs rather than videos for space efficiency.
- Handle ASR errors through noise-robust training objectives.

## Evidence from the paper
- HowTo100M provides 136M video clips from 1.22M YouTube instructional videos.
- Despite noisy ASR transcriptions, the scale enables effective video-text embedding learning.
- The dataset covers 23K+ activities across diverse instructional topics.
- HowTo100M has become a foundational dataset for video-language research.

## Source paper
- **Title**: HowTo100M: Learning a Text-Video Embedding by Watching Hundred Million Narrated Video Clips
- **Year**: 2019
- **Venue**: ICCV
- **Paper ID**: arxiv-1906.02604v2
- **URL**: http://arxiv.org/abs/1906.02604v2
- **arXiv ID**: 1906.02604v2
