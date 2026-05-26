# ActivityNet: A Large-Scale Video Benchmark for Human Activity Understanding

## One-line decision
Use this skill when you need a large-scale video activity understanding dataset with temporal annotations for training video-language models. Avoid it when short-clip action recognition is sufficient.

## Skill metadata
- **Skill type**: activity-understanding-video-data
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Provide a large-scale benchmark for human activity understanding with 20K untrimmed videos and 200 activity categories with temporal boundaries.

## Problem signature
- Modality: untrimmed videos with temporal activity annotations.
- Data state: 20K untrimmed videos with temporal activity boundaries.
- Scale regime: 20K videos, 200 activity categories.
- Model requirement: Any video understanding model.

## Use when
- You need long-form activity understanding data.
- You want temporal localization training data.
- You need activity classification and detection.

## Do not use when
- Short clip recognition is sufficient.
- You do not need temporal localization.
- You need a different activity taxonomy.

## Required inputs
- **untrimmed_videos**: 20K untrimmed YouTube videos.
- **activity_labels**: 200 activity category labels.
- **temporal_annotations**: Start/end times for activities in videos.

## Optional inputs
- **dense_captions**: Dense captioning annotations.

## Outputs
- **activitynet_dataset**: 20K untrimmed videos with activity annotations.
- **activity_benchmarks**: Benchmarks for activity detection and captioning.

## Assumptions and prerequisites
- Untrimmed videos test temporal localization.
- 200 activities cover diverse human activities.
- Temporal annotations enable detection training.

## Procedure
1. **Collect untrimmed videos**
   Action: Gather 20K untrimmed YouTube videos of activities.
   Why: Untrimmed videos test temporal localization.
   Note: See paper for details.
2. **Annotate temporal boundaries**
   Action: Mark start/end times for activities.
   Why: Enables temporal activity detection.
   Note: See paper for details.
3. **Create activity taxonomy**
   Action: Define 200 activity categories.
   Why: Taxonomy provides classification structure.
   Note: See paper for details.

## Parameters to set
- **num_videos** — Role: Total untrimmed videos. How to set: 20K for diversity. Default/range: 20K. Effect: More videos improve coverage.
- **num_categories** — Role: Activity categories. How to set: 200 for broad coverage. Default/range: 200. Effect: More categories cover more activities.

## Validation checks
- Temporal annotations should be accurate.
- Activity categories should be distinguishable.
- The benchmark should test temporal understanding.

## Failure modes
- Untrimmed videos may have long inactive segments.
- Activity boundaries may be ambiguous.
- YouTube availability may change.

## Adaptation notes for VLM training
- ActivityNet provides long-form video understanding for video VLMs.
- Temporal activity detection is important for video comprehension.
- Dense captioning annotations add language supervision.

## Implementation notes
- Use the ActivityNet API for data access.
- Handle untrimmed video processing efficiently.
- Evaluate on temporal detection metrics.

## Evidence from the paper
- ActivityNet provides 20K untrimmed videos with 200 activity categories.
- Temporal annotations enable activity detection training.
- The dataset tests long-form temporal understanding.
- ActivityNet is a standard benchmark for video activity understanding.

## Source paper
- **Title**: ActivityNet: A Large-Scale Video Benchmark for Human Activity Understanding
- **Year**: 2015
- **Venue**: CVPR
- **Paper ID**: arxiv-1503.02001v3
- **URL**: http://arxiv.org/abs/1503.02001v3
- **arXiv ID**: 1503.02001v3
