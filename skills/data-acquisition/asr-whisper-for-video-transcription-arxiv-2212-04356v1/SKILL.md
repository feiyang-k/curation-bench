# ASR: Whisper for Video Transcription

## One-line decision
Use this skill when you want to use Whisper ASR to transcribe speech from videos for creating video-text training data. Avoid it when your videos do not have speech or you have existing transcripts.

## Skill metadata
- **Skill type**: video-speech-transcription
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Use Whisper, a robust automatic speech recognition model, to transcribe speech from videos at scale, creating text supervision for video-language model training.

## Problem signature
- Modality: video audio transcribed to text via ASR.
- Data state: videos with ASR-generated transcripts.
- Scale regime: unlimited video transcription at scale.
- Model requirement: Whisper ASR model for speech-to-text.

## Use when
- Your videos contain speech that needs transcription.
- You need text supervision from video audio.
- Manual transcription is infeasible at scale.

## Do not use when
- Videos do not contain speech.
- You have existing high-quality transcripts.
- ASR quality is insufficient for your needs.

## Required inputs
- **video_audio**: Audio tracks from videos.
- **whisper_model**: Whisper ASR model for transcription.
- **language_config**: Language for transcription.

## Optional inputs
- **timestamp_alignment**: Alignment of transcripts with video timestamps.

## Outputs
- **transcripts**: ASR-generated text transcripts for videos.
- **timestamped_text**: Transcripts with temporal alignment.

## Assumptions and prerequisites
- Whisper provides high-quality transcription.
- ASR transcripts provide useful text supervision.
- Scale compensates for occasional ASR errors.

## Procedure
1. **Extract audio from videos**
   Action: Separate audio tracks from videos.
   Why: Audio is the input for ASR.
   Note: See paper for details.
2. **Transcribe with Whisper**
   Action: Run Whisper on extracted audio.
   Why: Generates text transcripts.
   Note: See paper for details.
3. **Align with timestamps**
   Action: Align transcripts with video timestamps.
   Why: Enables temporal video-text alignment.
   Note: See paper for details.
4. **Use as training data**
   Action: Pair transcripts with video for training.
   Why: Text supervision for video-language learning.
   Note: See paper for details.

## Parameters to set
- **whisper_model_size** — Role: Whisper model variant. How to set: Large-v3 for best quality. Default/range: Large-v3. Effect: Larger models produce better transcription.
- **language** — Role: Target transcription language. How to set: Auto-detect or specify. Default/range: Auto. Effect: Language setting affects accuracy.

## Validation checks
- Transcription quality should be high on random samples.
- Timestamp alignment should be accurate.
- Multilingual videos should be handled correctly.

## Failure modes
- Noisy audio may produce poor transcripts.
- Multiple speakers may cause errors.
- Non-speech audio may be incorrectly transcribed.

## Adaptation notes for VLM training
- Whisper ASR is the standard tool for video text extraction.
- Use for creating text supervision for video-language models.
- Combine with visual captions for comprehensive video-text data.

## Implementation notes
- Use Whisper Large-v3 for best quality.
- Process audio in batches.
- Validate transcription quality on samples.

## Evidence from the paper
- Whisper provides robust speech-to-text transcription.
- ASR transcripts create valuable text supervision for video-language models.
- HowTo100M and similar datasets rely on ASR for text supervision.
- Whisper handles multiple languages and accents well.

## Source paper
- **Title**: ASR: Whisper for Video Transcription
- **Year**: 2023
- **Venue**: ICML
- **Paper ID**: arxiv-2212.04356v1
- **URL**: http://arxiv.org/abs/2212.04356v1
- **arXiv ID**: 2212.04356v1
