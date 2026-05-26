# ScanNet: Richly-annotated 3D Reconstructions of Indoor Scenes

## One-line decision
Use this skill when you need a richly annotated 3D indoor scene dataset for 3D vision-language understanding research. Avoid it when you do not work with 3D scene understanding.

## Skill metadata
- **Skill type**: 3d-scene-understanding-data
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Create a richly annotated 3D indoor scene dataset with 1,513 scans, semantic segmentation, object instances, and camera poses for 3D vision-language research.

## Problem signature
- Modality: 3D reconstructions of indoor scenes with semantic annotations.
- Data state: 1,513 RGB-D scans with 3D semantic labels and object instances.
- Scale regime: 1,513 annotated 3D scenes.
- Model requirement: 3D understanding models; used for 3D VLM training.

## Use when
- You need 3D scene understanding data.
- You work with indoor 3D environments.
- You need 3D annotations for VLM training.

## Do not use when
- You only work with 2D images.
- 3D is not relevant to your task.
- You need outdoor 3D data.

## Required inputs
- **rgb_d_scanner**: RGB-D scanning equipment.
- **indoor_scenes**: Indoor environments to scan.
- **annotation_pipeline**: 3D semantic annotation pipeline.

## Optional inputs
- **language_annotations**: Natural language descriptions of 3D scenes.

## Outputs
- **scannet_dataset**: 1,513 annotated 3D indoor scenes.
- **3d_benchmarks**: Benchmarks for 3D scene understanding.

## Assumptions and prerequisites
- 3D annotations enable spatial VLM understanding.
- Indoor scenes provide diverse spatial layouts.
- RGB-D scanning captures sufficient 3D detail.

## Procedure
1. **Scan indoor scenes**
   Action: Use RGB-D scanners to capture indoor environments.
   Why: Creates 3D reconstructions of real spaces.
   Note: See paper for details.
2. **Annotate semantically**
   Action: Label objects and surfaces in 3D.
   Why: Semantic labels provide training signal.
   Note: See paper for details.
3. **Create benchmarks**
   Action: Define 3D understanding tasks and benchmarks.
   Why: Enables standardized evaluation.
   Note: See paper for details.

## Parameters to set
- **num_scenes** — Role: Total scanned scenes. How to set: 1,513 for diverse coverage. Default/range: 1,513. Effect: More scenes improve diversity.
- **annotation_types** — Role: Types of 3D annotations. How to set: Include semantic segmentation and instances. Default/range: Multiple types. Effect: Richer annotations enable more tasks.

## Validation checks
- 3D reconstructions should be accurate.
- Annotations should be consistent across scenes.
- The dataset should cover diverse indoor environments.

## Failure modes
- RGB-D scanning has resolution limitations.
- Indoor scenes may have similar layouts.
- 3D annotation is labor-intensive.

## Adaptation notes for VLM training
- ScanNet provides 3D data for spatial VLM understanding.
- Combine with language annotations for 3D VLMs.
- The dataset enables 3D question answering and grounding.

## Implementation notes
- Use the ScanNet API for data access.
- Handle 3D data formats appropriately.
- Evaluate on standard 3D benchmarks.

## Evidence from the paper
- ScanNet provides 1,513 richly annotated 3D indoor scenes.
- The dataset includes semantic segmentation and object instances.
- ScanNet is the standard dataset for 3D scene understanding.
- The dataset enables 3D vision-language research.

## Source paper
- **Title**: ScanNet: Richly-annotated 3D Reconstructions of Indoor Scenes
- **Year**: 2017
- **Venue**: CVPR
- **Paper ID**: arxiv-1702.04405v2
- **URL**: http://arxiv.org/abs/1702.04405v2
- **arXiv ID**: 1702.04405v2
