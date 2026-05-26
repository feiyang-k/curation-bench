# Pixtral 12B: A Frontier Multimodal Model

## One-line decision
Use this skill when you want to train a natively multimodal model that processes variable numbers of images at any resolution without fixed token budgets. Avoid it when fixed-resolution VLM approaches work for your needs.

## Skill metadata
- **Skill type**: natively-multimodal-architecture
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Train a natively multimodal 12B model that processes variable numbers of images at any resolution, demonstrating efficient multimodal architecture with flexible visual processing.

## Problem signature
- Modality: variable images at any resolution with text.
- Data state: multimodal pretraining and instruction data at flexible resolutions.
- Scale regime: large-scale multimodal pretraining.
- Model requirement: Pixtral architecture with native multimodal processing.

## Use when
- You want native multimodal processing without fixed tokens.
- You need variable image count support.
- You want efficient multi-image processing.

## Do not use when
- Fixed-resolution approaches are sufficient.
- You only process single images.
- Simpler architectures meet your needs.

## Required inputs
- **multimodal_data**: Images and text for multimodal pretraining.
- **variable_resolution**: Data at various resolutions and image counts.
- **pixtral_architecture**: Natively multimodal architecture.

## Optional inputs
- **instruction_data**: Task-specific instruction data.

## Outputs
- **pixtral_model**: 12B natively multimodal model.
- **flexible_pipeline**: Pipeline for flexible visual processing.

## Assumptions and prerequisites
- Native multimodal architecture is more efficient than add-on.
- Variable resolution eliminates information loss from resizing.
- 12B parameters provide strong capability.

## Procedure
1. **Design native multimodal architecture**
   Action: Build architecture processing images natively without fixed tokens.
   Why: Avoids information loss from fixed tokenization.
   Note: See paper for details.
2. **Train on multimodal data**
   Action: Pretrain on diverse multimodal data.
   Why: Builds broad multimodal understanding.
   Note: See paper for details.
3. **Support variable images**
   Action: Handle variable numbers of images per context.
   Why: Real-world use requires flexible image counts.
   Note: See paper for details.
4. **Evaluate comprehensively**
   Action: Test on diverse multimodal benchmarks.
   Why: Validates flexible multimodal capability.
   Note: See paper for details.

## Parameters to set
- **model_size** — Role: Total model parameters. How to set: 12B for strong capability. Default/range: 12B. Effect: Balanced size and capability.
- **resolution_handling** — Role: How different resolutions are processed. How to set: Native variable resolution. Default/range: Variable. Effect: No information loss from resizing.

## Validation checks
- Variable resolution should improve detail-dependent tasks.
- Multiple image support should work seamlessly.
- Performance should be competitive with larger models.

## Failure modes
- Native multimodal architecture is harder to implement.
- Variable resolution increases compute variability.
- 12B may be insufficient for some complex tasks.

## Adaptation notes for VLM training
- Pixtral demonstrates native multimodal architecture benefits.
- Variable resolution is increasingly adopted by modern VLMs.
- The 12B size provides a practical deployment point.

## Implementation notes
- Implement native multimodal token processing.
- Handle variable image counts efficiently.
- Benchmark against fixed-resolution alternatives.

## Evidence from the paper
- Pixtral 12B processes variable images at any resolution natively.
- Native multimodal architecture avoids information loss.
- The model achieves frontier performance at 12B parameters.
- Flexible visual processing is the direction for modern VLMs.

## Source paper
- **Title**: Pixtral 12B: A Frontier Multimodal Model
- **Year**: 2024
- **Venue**: Mistral
- **Paper ID**: arxiv-pixtral-2024
- **URL**: https://mistral.ai/news/pixtral-12b/
- **arXiv ID**: N/A
