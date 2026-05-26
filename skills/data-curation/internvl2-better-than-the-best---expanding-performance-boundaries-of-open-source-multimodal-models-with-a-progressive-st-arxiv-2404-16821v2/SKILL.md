# InternVL2: Better than the Best - Expanding Performance Boundaries of Open-Source Multimodal Models with a Progressive Strategy

## One-line decision
Use this skill when you want to progressively scale VLM data from alignment to multi-task to high-quality instruction data with dynamic resolution. Avoid it when you do not have multi-stage data or cannot afford progressive training.

## Skill metadata
- **Skill type**: progressive-training-data-scaling
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Scale VLM performance through progressive data strategies: starting with alignment data, adding multi-task data, and finishing with high-quality instruction data, using dynamic high-resolution input throughout.

## Problem signature
- Modality: images with progressive multi-stage instruction data.
- Data state: progressive data: alignment → multi-task → high-quality instruction.
- Scale regime: billions of alignment pairs; millions of instruction samples.
- Model requirement: InternViT-6B-448 + various LLM backends.

## Use when
- You want progressive VLM training with systematic data scaling.
- You have access to alignment, multi-task, and instruction data.
- You need a family of VLM models at different scales.

## Do not use when
- Single-stage training is sufficient.
- You cannot afford multi-stage training.
- You only need a single model size.

## Required inputs
- **alignment_data**: Large-scale image-text pairs for alignment.
- **multitask_data**: Diverse VL datasets formatted as instructions.
- **high_quality_data**: Curated high-quality instruction data.

## Optional inputs
- **model_family**: Multiple LLM backends for model family.

## Outputs
- **internvl2_family**: Family of VLM models at multiple scales.
- **progressive_recipe**: Progressive training recipe for VLM scaling.

## Assumptions and prerequisites
- Progressive data scaling builds capabilities systematically.
- High-quality instruction data at the final stage maximizes quality.
- A model family at multiple scales serves different deployment needs.

## Procedure
1. **Stage 1: Alignment pretraining**
   Action: Train on large-scale image-text pairs for alignment.
   Why: Establishes foundational visual-language connection.
   Note: See paper for details.
2. **Stage 2: Multi-task training**
   Action: Add diverse VL tasks for capability building.
   Why: Multi-task training develops broad capabilities.
   Note: See paper for details.
3. **Stage 3: High-quality instruction tuning**
   Action: Fine-tune on curated, high-quality instruction data.
   Why: Quality data at the final stage maximizes performance.
   Note: See paper for details.
4. **Scale across LLM backends**
   Action: Apply the recipe to different LLM sizes.
   Why: Creates a model family for diverse deployment needs.
   Note: See paper for details.

## Parameters to set
- **alignment_scale** — Role: Scale of alignment data. How to set: Billions of pairs. Default/range: Billions. Effect: Larger alignment improves foundation.
- **instruction_quality** — Role: Quality of final-stage instruction data. How to set: Heavily curated. Default/range: High quality. Effect: Quality at the final stage has the most impact.

## Validation checks
- Progressive training should show improvement at each stage.
- The model family should scale performance with model size.
- Comprehensive benchmarks should show state-of-the-art results.

## Failure modes
- Multi-stage training is expensive and complex.
- Stage transitions may cause instability.
- Data quality at each stage must be carefully managed.

## Adaptation notes for VLM training
- InternVL2's progressive recipe is a template for state-of-the-art VLM training.
- The model family approach serves diverse deployment scenarios.
- Progressive data scaling is increasingly recognized as the optimal approach.

## Implementation notes
- Use InternVL2's training codebase for reproducibility.
- Monitor per-stage metrics for quality control.
- Maintain data quality documentation for each stage.

## Evidence from the paper
- InternVL2 achieves state-of-the-art across comprehensive VLM benchmarks.
- Progressive data scaling systematically improves performance.
- High-quality instruction data at the final stage maximizes model quality.
- The model family serves diverse deployment needs from 1B to 76B parameters.

## Source paper
- **Title**: InternVL2: Better than the Best - Expanding Performance Boundaries of Open-Source Multimodal Models with a Progressive Strategy
- **Year**: 2024
- **Venue**: arXiv
- **Paper ID**: arxiv-2404.16821v2
- **URL**: http://arxiv.org/abs/2404.16821v2
- **arXiv ID**: 2404.16821v2
