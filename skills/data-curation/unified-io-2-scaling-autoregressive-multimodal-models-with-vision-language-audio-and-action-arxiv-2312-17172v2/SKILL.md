# Unified-IO 2: Scaling Autoregressive Multimodal Models with Vision, Language, Audio, and Action

## One-line decision
Use this skill when you want to unify training data across vision, language, audio, and action modalities for a single autoregressive model. Avoid it when you only need vision-language capability without audio or action.

## Skill metadata
- **Skill type**: multi-modal-data-unification
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Unify training data across vision, language, audio, and action modalities into a single autoregressive model, demonstrating multi-modal data unification at scale.

## Problem signature
- Modality: vision, language, audio, and action data unified in autoregressive sequences.
- Data state: multi-modal data from diverse sources unified into token sequences.
- Scale regime: 1 billion parameters trained on unified multi-modal data.
- Model requirement: Autoregressive transformer processing all modalities as tokens.

## Use when
- You want a single model for multiple modalities.
- You can unify data across vision, language, audio, and action.
- You want maximum modality coverage.

## Do not use when
- You only need vision-language capability.
- You cannot collect multi-modal data.
- Specialized models are preferred.

## Required inputs
- **vision_data**: Image and video data for visual understanding.
- **language_data**: Text data for language modeling.
- **audio_data**: Audio and speech data.
- **action_data**: Robot action and embodied data.

## Optional inputs
- **cross_modal_data**: Data requiring understanding across modalities.

## Outputs
- **unified_io2_model**: Single model handling vision, language, audio, and action.
- **unified_data_format**: Format for unifying diverse modalities.

## Assumptions and prerequisites
- All modalities can be tokenized into a common format.
- A single model can handle diverse modalities.
- Multi-modal training provides cross-modal benefits.

## Procedure
1. **Tokenize all modalities**
   Action: Convert vision, language, audio, and action data to tokens.
   Why: Common token format enables unified processing.
   Note: See paper for details.
2. **Unify data streams**
   Action: Interleave data from all modalities during training.
   Why: Unified training enables cross-modal understanding.
   Note: See paper for details.
3. **Train autoregressive model**
   Action: Train a single model on the unified multi-modal data.
   Why: Autoregressive training handles all modalities uniformly.
   Note: See paper for details.
4. **Evaluate across modalities**
   Action: Test on benchmarks from each modality.
   Why: Validates multi-modal capability.
   Note: See paper for details.

## Parameters to set
- **modality_mix** — Role: Mixing ratios across modalities. How to set: Balance based on data availability and target capabilities. Default/range: Task-dependent. Effect: Mix affects per-modality performance.
- **tokenizer_design** — Role: How each modality is tokenized. How to set: Use modality-specific tokenizers. Default/range: VQVAE for images, BPE for text, etc. Effect: Tokenizer quality affects model quality.

## Validation checks
- The model should perform well across all modalities.
- Cross-modal benefits should be measurable.
- No modality should degrade significantly.

## Failure modes
- Token space may be too large for efficient learning.
- Some modalities may dominate training.
- Cross-modal interference may occur.

## Adaptation notes for VLM training
- Unified-IO 2's data unification approach extends VLM to more modalities.
- The tokenization framework is reusable for custom multi-modal models.
- Multi-modal unification is a direction for future VLM development.

## Implementation notes
- Use modality-specific tokenizers for best quality.
- Balance modality sampling during training.
- Monitor per-modality metrics.

## Evidence from the paper
- Unified-IO 2 handles vision, language, audio, and action in a single model.
- Multi-modal training provides cross-modal benefits.
- Token-based unification enables processing of diverse modalities.
- The model achieves competitive results across multiple modality benchmarks.

## Source paper
- **Title**: Unified-IO 2: Scaling Autoregressive Multimodal Models with Vision, Language, Audio, and Action
- **Year**: 2024
- **Venue**: CVPR
- **Paper ID**: arxiv-2312.17172v2
- **URL**: http://arxiv.org/abs/2312.17172v2
- **arXiv ID**: 2312.17172v2
