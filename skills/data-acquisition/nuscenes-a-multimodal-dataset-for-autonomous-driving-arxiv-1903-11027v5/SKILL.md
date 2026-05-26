# nuScenes: A Multimodal Dataset for Autonomous Driving

## One-line decision
Use this skill when you need a comprehensive multimodal autonomous driving dataset with cameras, LiDAR, radar, and 3D annotations for driving VLMs. Avoid it when driving data is not relevant to your work.

## Skill metadata
- **Skill type**: autonomous-driving-multimodal-data
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Provide a comprehensive multimodal autonomous driving dataset with 1,000 driving scenes, full sensor suite (cameras, LiDAR, radar), and 3D bounding box annotations.

## Problem signature
- Modality: multi-sensor driving data with 3D annotations.
- Data state: 1,000 driving scenes with multi-sensor and 3D annotation data.
- Scale regime: 1,000 scenes, 1.4M 3D bounding boxes.
- Model requirement: Any driving perception or VLM model.

## Use when
- You need autonomous driving multimodal data.
- You want 3D annotations for driving scenes.
- You need multi-sensor fusion data.

## Do not use when
- Driving is not your domain.
- You only need 2D data.
- Single-sensor data is sufficient.

## Required inputs
- **driving_scenes**: 1,000 diverse driving scenes.
- **sensor_data**: Camera, LiDAR, radar data per scene.
- **3d_annotations**: 3D bounding boxes for all objects.

## Optional inputs
- **map_data**: HD map annotations.

## Outputs
- **nuscenes_dataset**: 1,000 driving scenes with full annotation.
- **driving_benchmarks**: Benchmarks for driving perception.

## Assumptions and prerequisites
- Multi-sensor data enables comprehensive driving understanding.
- 3D annotations capture real-world spatial relationships.
- 1,000 diverse scenes provide sufficient coverage.

## Procedure
1. **Collect driving scenes**
   Action: Record 1,000 driving scenes with full sensor suite.
   Why: Diverse scenes ensure broad coverage.
   Note: See paper for details.
2. **Annotate in 3D**
   Action: Create 3D bounding boxes for all objects.
   Why: 3D annotations enable spatial understanding.
   Note: See paper for details.
3. **Provide multi-sensor data**
   Action: Include camera, LiDAR, and radar for each scene.
   Why: Multi-sensor enables sensor fusion research.
   Note: See paper for details.
4. **Create benchmarks**
   Action: Define detection, tracking, and prediction benchmarks.
   Why: Benchmarks enable standardized evaluation.
   Note: See paper for details.

## Parameters to set
- **num_scenes** — Role: Total driving scenes. How to set: 1,000 for diversity. Default/range: 1,000. Effect: More scenes improve coverage.
- **sensor_types** — Role: Types of sensors. How to set: Camera + LiDAR + radar. Default/range: Full suite. Effect: More sensors enable richer fusion.

## Validation checks
- 3D annotations should be accurate.
- Multi-sensor data should be temporally aligned.
- The dataset should cover diverse driving conditions.

## Failure modes
- Annotation errors in 3D.
- Limited geographic diversity.
- Complex data format may be challenging.

## Adaptation notes for VLM training
- nuScenes provides comprehensive data for driving VLMs.
- 3D annotations enable spatial reasoning evaluation.
- Combine with language annotations for driving VLM training.

## Implementation notes
- Use the nuScenes devkit for data access.
- Handle multi-sensor data alignment.
- Evaluate on nuScenes benchmarks.

## Evidence from the paper
- nuScenes provides 1,000 driving scenes with multi-sensor and 3D annotations.
- The dataset includes camera, LiDAR, and radar data.
- 1.4M 3D bounding boxes provide comprehensive annotation.
- nuScenes is the standard dataset for autonomous driving research.

## Source paper
- **Title**: nuScenes: A Multimodal Dataset for Autonomous Driving
- **Year**: 2020
- **Venue**: CVPR
- **Paper ID**: arxiv-1903.11027v5
- **URL**: http://arxiv.org/abs/1903.11027v5
- **arXiv ID**: 1903.11027v5
