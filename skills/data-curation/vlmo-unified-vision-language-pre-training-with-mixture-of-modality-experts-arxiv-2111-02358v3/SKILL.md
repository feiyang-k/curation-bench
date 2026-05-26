# VLMo: Unified Vision-Language Pre-Training with Mixture-of-Modality-Experts

## One-line decision
Use this skill when you want to train a unified VLM using mixture-of-modality-experts that can serve as both dual-encoder and fusion-encoder. Avoid it when you prefer simpler single-mode architectures.

## Skill metadata
- **Skill type**: mixture-of-experts-vlm-data
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Train a unified VLM using Mixture-of-Modality-Experts (MoME) that can flexibly operate as a dual-encoder for retrieval or a fusion-encoder for understanding, trained on both image-text pair and image-text-pair-plus-document data.

## Problem signature
- Modality: image-text pairs for contrastive and fusion-based training.
- Data state: image-text pairs with both contrastive and fusion objectives.
- Scale regime: standard VL pretraining datasets.
- Model requirement: Transformer with MoME layers supporting dual and fusion modes.

## Use when
- You want a single model for both retrieval and understanding.
- You can train with both contrastive and fusion objectives.
- You want flexible model deployment.

## Do not use when
- Single-mode architecture is sufficient.
- You only need retrieval or only understanding.
- MoME complexity is unnecessary.

## Required inputs
- **image_text_pairs**: Paired data for contrastive training.
- **fusion_data**: Data for fusion-based understanding training.
- **mome_architecture**: Transformer with MoME layers.

## Optional inputs
- **text_only_data**: Text data for language expert training.

## Outputs
- **vlmo_model**: Unified VLM with dual-encoder and fusion-encoder modes.
- **flexible_vlm**: Model deployable in multiple modes.

## Assumptions and prerequisites
- MoME enables flexible multi-mode operation.
- Both contrastive and fusion training are beneficial.
- A single model can excel in both modes.

## Procedure
1. **Design MoME architecture**
   Action: Create transformer with modality-specific expert layers.
   Why: MoME enables flexible mode switching.
   Note: See paper for details.
2. **Train with dual objectives**
   Action: Train with both contrastive and fusion objectives.
   Why: Both objectives develop complementary capabilities.
   Note: See paper for details.
3. **Deploy in appropriate mode**
   Action: Use dual-encoder for retrieval, fusion-encoder for understanding.
   Why: Flexible deployment serves different tasks.
   Note: See paper for details.

## Parameters to set
- **expert_types** — Role: Types of modality experts. How to set: Vision, language, and fusion experts. Default/range: 3 types. Effect: Different experts handle different modalities.
- **training_objectives** — Role: Objectives for training. How to set: Contrastive + ITM + MLM. Default/range: Multiple. Effect: Multiple objectives develop complementary capabilities.

## Validation checks
- Dual-encoder mode should excel at retrieval.
- Fusion-encoder mode should excel at understanding.
- Both modes should benefit from unified training.

## Failure modes
- MoME adds architectural complexity.
- Expert routing may not be optimal.
- Training multiple objectives requires careful balancing.

## Adaptation notes for VLM training
- MoME provides flexible VLM deployment for different tasks.
- The dual-mode approach serves both retrieval and understanding needs.
- Expert-based architectures are used in many subsequent VLMs.

## Implementation notes
- Implement MoME layers with clean expert routing.
- Train with balanced multiple objectives.
- Evaluate in both dual-encoder and fusion-encoder modes.

## Evidence from the paper
- VLMo uses MoME for flexible dual-encoder and fusion-encoder operation.
- Unified training develops both retrieval and understanding capabilities.
- The model achieves state-of-the-art on both retrieval and understanding tasks.
- MoME enables flexible deployment for different downstream tasks.

## Source paper
- **Title**: VLMo: Unified Vision-Language Pre-Training with Mixture-of-Modality-Experts
- **Year**: 2022
- **Venue**: NeurIPS
- **Paper ID**: arxiv-2111.02358v3
- **URL**: http://arxiv.org/abs/2111.02358v3
- **arXiv ID**: 2111.02358v3
