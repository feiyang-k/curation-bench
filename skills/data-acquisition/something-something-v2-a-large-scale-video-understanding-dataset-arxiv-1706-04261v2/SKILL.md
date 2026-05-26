# Something-Something V2: A Large-Scale Video Understanding Dataset

## One-line decision
Use this skill when you need a video dataset requiring temporal understanding of human actions for training video-language models. Avoid it when you do not need temporal action understanding.

## Skill metadata
- **Skill type**: temporal-action-video-data
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Provide a video dataset of 220K clips showing humans performing actions on objects, requiring temporal understanding rather than appearance-based recognition.

## Problem signature
- Modality: short video clips of human-object interactions with action labels.
- Data state: 220K video clips with temporal action labels.
- Scale regime: 220K labeled video clips.
- Model requirement: Any video understanding model.

## Use when
- You need temporal action understanding training data.
- You want to test video models beyond appearance recognition.
- You need human-object interaction videos.

## Do not use when
- Appearance-based recognition is sufficient.
- Temporal understanding is not needed.
- You need longer-form video.

## Required inputs
- **video_clips**: 220K clips of human-object interactions.
- **action_labels**: Labels describing the temporal action performed.
- **temporal_structure**: Temporal ordering of actions.

## Optional inputs
- **fine_grained_labels**: Sub-action labels.

## Outputs
- **ssv2_dataset**: 220K temporal action video clips.
- **temporal_benchmark**: Benchmark for temporal understanding.

## Assumptions and prerequisites
- Temporal understanding requires more than appearance recognition.
- Human-object interactions provide rich temporal training signal.
- Short clips can capture meaningful temporal patterns.

## Procedure
1. **Collect interaction videos**
   Action: Record human-object interactions in diverse settings.
   Why: Interactions require temporal understanding.
   Note: See paper for details.
2. **Label actions**
   Action: Annotate temporal actions in each clip.
   Why: Action labels provide training signal.
   Note: See paper for details.
3. **Design temporal benchmark**
   Action: Create benchmarks testing temporal understanding.
   Why: Evaluates beyond appearance recognition.
   Note: See paper for details.

## Parameters to set
- **num_clips** — Role: Total video clips. How to set: 220K for diversity. Default/range: 220K. Effect: More clips improve action coverage.
- **action_categories** — Role: Number of action types. How to set: 174 for diverse actions. Default/range: 174. Effect: More actions test broader understanding.

## Validation checks
- Models should require temporal reasoning, not just appearance.
- Action recognition should depend on temporal ordering.
- The benchmark should differentiate temporal from static models.

## Failure modes
- Some actions may be recognizable from single frames.
- Short clips may lack temporal context.
- Action labels may be ambiguous.

## Adaptation notes for VLM training
- Something-Something provides temporal understanding for video VLMs.
- Temporal action data complements appearance-based video datasets.
- Use for evaluating video VLM temporal reasoning.

## Implementation notes
- Use the SSv2 data loader.
- Evaluate temporal sensitivity.
- Compare frame-based vs temporal models.

## Evidence from the paper
- Something-Something V2 provides 220K clips requiring temporal understanding.
- Models must understand temporal ordering, not just appearance.
- The dataset tests genuine temporal reasoning capability.
- SSv2 is a standard benchmark for video temporal understanding.

## Source paper
- **Title**: Something-Something V2: A Large-Scale Video Understanding Dataset
- **Year**: 2017
- **Venue**: ICCV
- **Paper ID**: arxiv-1706.04261v2
- **URL**: http://arxiv.org/abs/1706.04261v2
- **arXiv ID**: 1706.04261v2
