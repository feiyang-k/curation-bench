# GeoChat: Grounded Large Vision-Language Model for Remote Sensing

## One-line decision
Use this skill when you want to create instruction data for remote sensing VLMs covering satellite image understanding, change detection, and visual grounding. Avoid it when you do not work with remote sensing or satellite imagery.

## Skill metadata
- **Skill type**: remote-sensing-instruction-data
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Generate instruction-following data for remote sensing VLMs by combining satellite image annotations with LLM-generated instructions for scene classification, object detection, change detection, and visual grounding.

## Problem signature
- Modality: remote sensing images with grounded instruction-following data.
- Data state: satellite images annotated with grounded instructions covering diverse RS tasks.
- Scale regime: 318K remote sensing instruction samples.
- Model requirement: LLaVA-style VLM adapted for remote sensing.

## Use when
- You need instruction data for remote sensing VLMs.
- You want to add grounding capability to RS image understanding.
- You need RS-specific task coverage (change detection, scene classification).

## Do not use when
- You do not work with remote sensing.
- General image instruction data is sufficient.
- You lack satellite image datasets.

## Required inputs
- **rs_image_datasets**: Remote sensing image datasets with annotations.
- **instruction_generator**: Pipeline for generating RS-specific instruction data.
- **grounding_annotations**: Object locations in satellite images.

## Optional inputs
- **change_detection_pairs**: Pairs of before/after satellite images.

## Outputs
- **geochat_data**: 318K remote sensing instruction samples.
- **geochat_model**: RS-specific VLM with grounding capability.

## Assumptions and prerequisites
- Remote sensing requires domain-specific instruction data.
- Grounding is important for RS image understanding.
- Existing RS annotations can be converted to instruction format.

## Procedure
1. **Aggregate RS datasets**
   Action: Collect satellite image datasets with scene, detection, and segmentation annotations.
   Why: Diverse RS datasets provide training signal.
   Note: See paper for details.
2. **Generate RS instructions**
   Action: Convert annotations to instruction format using LLM-based generation.
   Why: Instruction format enables conversational RS understanding.
   Note: See paper for details.
3. **Add grounding annotations**
   Action: Include spatial coordinates in instructions for grounding.
   Why: Grounding enables spatial RS reasoning.
   Note: See paper for details.
4. **Train RS-VLM**
   Action: Fine-tune LLaVA on the 318K RS instruction samples.
   Why: Domain-specific tuning enables RS understanding.
   Note: See paper for details.

## Parameters to set
- **rs_task_types** — Role: Types of RS tasks covered. How to set: Include scene classification, detection, change detection, grounding. Default/range: 4+ types. Effect: More tasks improve RS versatility.
- **instruction_count** — Role: Total instruction samples. How to set: 318K for comprehensive RS coverage. Default/range: 318K. Effect: More data improves domain coverage.

## Validation checks
- The model should correctly classify RS scenes.
- Grounding should accurately localize objects in satellite images.
- RS-specific benchmarks should show improvement.

## Failure modes
- General VLM vision encoders may not handle RS imagery well.
- RS terminology may not be well represented in the LLM.
- Small objects in satellite images may be hard to ground.

## Adaptation notes for VLM training
- GeoChat's approach can be adapted for other specialized domains.
- The grounding-in-RS approach is valuable for GIS applications.
- Combine with general instruction data for balanced RS-VLM training.

## Implementation notes
- Use RS-specific vision preprocessing for satellite imagery.
- Adapt coordinate systems for RS spatial references.
- Evaluate on RS-specific benchmarks.

## Evidence from the paper
- GeoChat creates 318K remote sensing instruction samples with grounding.
- The model handles scene classification, detection, change detection, and grounding.
- Domain-specific instruction data significantly improves RS understanding.
- GeoChat demonstrates the value of specialized VLM training data.

## Source paper
- **Title**: GeoChat: Grounded Large Vision-Language Model for Remote Sensing
- **Year**: 2023
- **Venue**: CVPR
- **Paper ID**: arxiv-2311.15826v3
- **URL**: http://arxiv.org/abs/2311.15826v3
- **arXiv ID**: 2311.15826v3
