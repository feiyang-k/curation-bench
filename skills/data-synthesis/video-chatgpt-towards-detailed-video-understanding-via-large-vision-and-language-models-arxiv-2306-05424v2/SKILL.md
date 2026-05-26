# Video-ChatGPT: Towards Detailed Video Understanding via Large Vision and Language Models

## One-line decision
Use this skill when you want to generate video instruction data by prompting GPT-3.5 with video descriptions and annotations for video understanding VLM training. Avoid it when you do not work with video or have sufficient video instruction data.

## Skill metadata
- **Skill type**: video-instruction-synthesis
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Generate 100K video instruction-following samples by prompting GPT-3.5 with video descriptions, using these for training a video-language model capable of detailed video understanding.

## Problem signature
- Modality: videos with GPT-3.5-generated instruction-response pairs.
- Data state: video descriptions and annotations used as context for LLM instruction generation.
- Scale regime: 100K video instruction samples.
- Model requirement: GPT-3.5 for data generation; LLaVA-like architecture adapted for video.

## Use when
- You need video instruction-following data.
- You can describe videos textually for LLM-based data generation.
- You want to adapt an image VLM for video understanding.

## Do not use when
- You have sufficient video instruction data.
- You do not work with video.
- You need image-only instruction data.

## Required inputs
- **video_descriptions**: Textual descriptions of video content.
- **gpt35_api**: GPT-3.5 for generating instruction-response pairs.
- **video_encoder**: Temporal video encoding for the VLM.

## Optional inputs
- **video_annotations**: Additional annotations (actions, objects, temporal events).

## Outputs
- **video_instruction_data**: 100K video instruction-following samples.
- **video_chatgpt_model**: Video-language model for detailed video understanding.

## Assumptions and prerequisites
- Textual video descriptions provide sufficient context for LLM instruction generation.
- GPT-3.5 can generate meaningful video-related instructions from descriptions.
- Temporal video encoding enables video understanding from an image VLM base.

## Procedure
1. **Describe videos textually**
   Action: Create detailed textual descriptions of video content including temporal events.
   Why: Text descriptions serve as context for LLM instruction generation.
   Note: See paper for details.
2. **Generate instructions with GPT-3.5**
   Action: Prompt GPT-3.5 to create QA pairs about the video content.
   Why: LLM generates diverse instruction-following data.
   Note: See paper for details.
3. **Adapt VLM for video**
   Action: Add temporal pooling to the image VLM to handle video frames.
   Why: Temporal processing enables video understanding.
   Note: See paper for details.
4. **Train on video instruction data**
   Action: Fine-tune the video VLM on the 100K generated samples.
   Why: Instruction tuning teaches video conversation ability.
   Note: See paper for details.

## Parameters to set
- **video_samples** — Role: Number of videos for instruction generation. How to set: Cover diverse video types. Default/range: 100K instructions from diverse videos. Effect: More samples improve video understanding breadth.
- **temporal_encoding** — Role: How temporal information is encoded. How to set: Use temporal pooling of frame features. Default/range: Spatial + temporal pooling. Effect: Temporal encoding enables video-specific understanding.

## Validation checks
- Generated instructions should be temporally grounded in video content.
- The model should answer questions about temporal events correctly.
- Video understanding should improve over image-only baselines.

## Failure modes
- Text descriptions may miss important visual details.
- GPT-3.5 may generate instructions not answerable from the video.
- Simple temporal pooling may lose fine-grained temporal information.

## Adaptation notes for VLM training
- The video instruction synthesis approach is reusable for other video VLMs.
- Replace GPT-3.5 with Claude for potentially better instruction quality.
- Extend the temporal encoding for longer videos.

## Implementation notes
- Sample frames uniformly for temporal representation.
- Generate diverse instruction types (temporal, spatial, action-based).
- Evaluate on video QA and captioning benchmarks.

## Evidence from the paper
- Video-ChatGPT generates 100K video instruction samples using GPT-3.5.
- The model handles diverse video understanding tasks including temporal reasoning.
- Adapting an image VLM with temporal pooling enables video understanding.
- The approach provides a practical recipe for building video-language models.

## Source paper
- **Title**: Video-ChatGPT: Towards Detailed Video Understanding via Large Vision and Language Models
- **Year**: 2023
- **Venue**: ACL
- **Paper ID**: arxiv-2306.05424v2
- **URL**: http://arxiv.org/abs/2306.05424v2
- **arXiv ID**: 2306.05424v2
