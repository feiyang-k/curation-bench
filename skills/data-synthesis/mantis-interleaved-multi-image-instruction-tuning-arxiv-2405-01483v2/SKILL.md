# Mantis: Interleaved Multi-Image Instruction Tuning

## One-line decision
Use this skill when you want to create instruction data for multi-image understanding tasks like comparison, reasoning across images, and temporal understanding. Avoid it when you only need single-image instruction data.

## Skill metadata
- **Skill type**: multi-image-instruction-data
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Create multi-image instruction tuning data for training VLMs that can understand relationships, comparisons, and reasoning across multiple images in a single conversation.

## Problem signature
- Modality: multiple images with instruction data requiring cross-image understanding.
- Data state: instruction data generated for multi-image tasks (comparison, temporal, spatial reasoning).
- Scale regime: 721K multi-image instruction samples.
- Model requirement: VLM with multi-image input support.

## Use when
- You want a VLM that understands relationships between multiple images.
- You need training data for image comparison, temporal, or multi-view tasks.
- Your VLM supports multi-image input.

## Do not use when
- Single-image understanding is sufficient.
- Your VLM cannot handle multiple images.
- You do not need cross-image reasoning.

## Required inputs
- **multi_image_sources**: Sources of related image sets (temporal, comparison, multi-view).
- **instruction_generator**: Pipeline for generating multi-image instruction data.
- **vlm_architecture**: VLM supporting multiple image inputs.

## Optional inputs
- **image_relationship_labels**: Labels describing relationships between images.

## Outputs
- **mantis_instruct_data**: 721K multi-image instruction samples.
- **mantis_model**: VLM trained for multi-image understanding.

## Assumptions and prerequisites
- Multi-image understanding is a distinct capability from single-image.
- Specialized instruction data is needed for cross-image reasoning.
- 721K samples provide sufficient multi-image training signal.

## Procedure
1. **Curate multi-image sources**
   Action: Collect sets of related images from diverse sources.
   Why: Related images enable cross-image reasoning tasks.
   Note: See paper for details.
2. **Generate multi-image instructions**
   Action: Create instruction-response pairs requiring understanding across images.
   Why: Cross-image instructions teach multi-image reasoning.
   Note: See paper for details.
3. **Cover diverse task types**
   Action: Include comparison, temporal, spatial, and logical reasoning tasks.
   Why: Diverse tasks build comprehensive multi-image understanding.
   Note: See paper for details.
4. **Train multi-image VLM**
   Action: Fine-tune a VLM on the 721K multi-image instruction data.
   Why: Specialized training enables multi-image capabilities.
   Note: See paper for details.

## Parameters to set
- **image_pairs** — Role: Number and type of image relationships. How to set: Include comparison, temporal, and multi-view pairs. Default/range: Diverse. Effect: More relationship types improve flexibility.
- **instruction_types** — Role: Types of multi-image instructions. How to set: Cover comparison, change detection, temporal, and reasoning. Default/range: Multiple types. Effect: Diverse types build comprehensive capability.

## Validation checks
- The model should correctly reason across multiple images.
- Multi-image benchmarks should show improvement.
- Single-image performance should not degrade.

## Failure modes
- The model may not distinguish relevant from irrelevant images.
- Multi-image data generation is more complex than single-image.
- Interleaved image-text formatting may be inconsistent.

## Adaptation notes for VLM training
- Multi-image instruction data is essential for document comparison, temporal understanding, etc.
- Combine with single-image data for balanced training.
- The multi-image approach extends to video understanding.

## Implementation notes
- Use consistent image ordering conventions.
- Track per-task multi-image performance.
- Handle variable numbers of images per instruction.

## Evidence from the paper
- Mantis creates 721K multi-image instruction samples for cross-image understanding.
- The model handles comparison, temporal, and spatial reasoning across images.
- Multi-image instruction tuning is a distinct and important capability.
- Mantis achieves state-of-the-art on multi-image benchmarks.

## Source paper
- **Title**: Mantis: Interleaved Multi-Image Instruction Tuning
- **Year**: 2024
- **Venue**: arXiv
- **Paper ID**: arxiv-2405.01483v2
- **URL**: http://arxiv.org/abs/2405.01483v2
- **arXiv ID**: 2405.01483v2
