# Ego4D: Around the World in 3,000 Hours of Egocentric Video

## One-line decision
Use this skill when you need a massive egocentric video dataset with diverse annotations for training video-language models. Avoid it when you do not work with egocentric/first-person video or need third-person video data.

## Skill metadata
- **Skill type**: egocentric-video-dataset
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Collect and annotate 3,670 hours of egocentric video from 931 participants across 74 locations and 9 countries, providing the largest egocentric video dataset with diverse temporal, spatial, and social annotations.

## Problem signature
- Modality: egocentric video with temporal, spatial, object, and social annotations.
- Data state: 3,670 hours of egocentric video with multiple annotation types.
- Scale regime: 3,670 hours, 931 participants, 9 countries.
- Model requirement: No model required for collection; used for video-language model training and benchmarking.

## Use when
- You need egocentric video data for first-person understanding.
- You want diverse temporal and spatial annotations.
- You need video-language training data from the first-person perspective.

## Do not use when
- You need third-person video data.
- Egocentric perspective is not relevant to your task.
- You need a smaller, more focused dataset.

## Required inputs
- **participants**: 931 participants wearing cameras in daily activities.
- **annotation_pipeline**: Multi-type annotation pipeline for temporal, spatial, and social annotations.
- **recording_infrastructure**: Egocentric camera recording setup across 9 countries.

## Optional inputs
- **privacy_filters**: Face blurring and privacy protection.

## Outputs
- **ego4d_dataset**: 3,670 hours of egocentric video with diverse annotations.
- **benchmark_suite**: Benchmark tasks for egocentric video understanding.

## Assumptions and prerequisites
- Egocentric video captures unique perspectives not available in third-person data.
- Diverse participants and locations provide broad coverage.
- Multiple annotation types enable varied research tasks.

## Procedure
1. **Recruit diverse participants**
   Action: Recruit 931 participants across 74 locations in 9 countries.
   Why: Diversity ensures broad coverage of activities and environments.
   Note: See paper for details.
2. **Record egocentric video**
   Action: Participants wear cameras during daily activities.
   Why: Egocentric recording captures first-person perspectives naturally.
   Note: See paper for details.
3. **Apply privacy protection**
   Action: Blur faces and remove sensitive content.
   Why: Privacy protection is essential for responsible data use.
   Note: See paper for details.
4. **Annotate with multiple types**
   Action: Annotate temporal boundaries, spatial relationships, objects, and social interactions.
   Why: Multiple annotation types enable diverse research tasks.
   Note: See paper for details.
5. **Define benchmark tasks**
   Action: Create benchmark tasks for episodic memory, hands-objects, forecasting, etc.
   Why: Benchmarks enable standardized evaluation.
   Note: See paper for details.

## Parameters to set
- **total_hours** — Role: Total video hours collected. How to set: 3,670 hours for comprehensive coverage. Default/range: 3,670. Effect: More hours increase activity and scenario diversity.
- **num_participants** — Role: Number of unique participants. How to set: 931 for diverse perspectives. Default/range: 931. Effect: More participants reduce individual bias.

## Validation checks
- The dataset should cover diverse daily activities.
- Annotations should be accurate and consistent.
- Benchmark tasks should be well-defined and reproducible.

## Failure modes
- Recording quality may vary across participants.
- Privacy concerns may limit data usability.
- Egocentric perspective may have limited visual context.

## Adaptation notes for VLM training
- Ego4D provides egocentric video for training video-language models.
- The dataset enables research on episodic memory and activity understanding.
- Combine with third-person video data for comprehensive video understanding.

## Implementation notes
- Use the Ego4D API for efficient data access.
- Handle the large scale (3,670 hours) with distributed processing.
- Track per-task performance across benchmark suites.

## Evidence from the paper
- Ego4D provides 3,670 hours of egocentric video from 931 participants across 9 countries.
- The dataset includes temporal, spatial, object, and social annotations.
- Ego4D defines 5 benchmark tasks for egocentric video understanding.
- The dataset is the largest egocentric video collection with diverse annotations.

## Source paper
- **Title**: Ego4D: Around the World in 3,000 Hours of Egocentric Video
- **Year**: 2022
- **Venue**: CVPR
- **Paper ID**: arxiv-2110.07058v2
- **URL**: http://arxiv.org/abs/2110.07058v2
- **arXiv ID**: 2110.07058v2
