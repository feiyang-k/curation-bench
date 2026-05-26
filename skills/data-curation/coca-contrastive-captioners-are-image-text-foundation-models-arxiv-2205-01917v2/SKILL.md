# CoCa: Contrastive Captioners are Image-Text Foundation Models

## One-line decision
Use this skill when you want to combine contrastive and captioning objectives on the same image-text data for a unified vision-language foundation model. Avoid it when you only need one objective (contrastive or captioning) and not both.

## Skill metadata
- **Skill type**: contrastive-captioning-data
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Train a unified vision-language foundation model using both contrastive and captioning objectives on the same image-text data, combining the strengths of CLIP-style and generative approaches.

## Problem signature
- Modality: image-text pairs trained with both contrastive and captioning losses.
- Data state: image-text pairs used for dual-objective training (contrastive + captioning).
- Scale regime: web-scale image-text pairs (JFT, ALIGN data).
- Model requirement: CoCa architecture with attentional pooler for contrastive + multimodal decoder for captioning.

## Use when
- You want a unified model for both retrieval and generation.
- You can train with dual objectives on image-text data.
- You want one model serving multiple downstream tasks.

## Do not use when
- You only need contrastive (CLIP-style) training.
- You only need generative (captioning) training.
- You cannot afford dual-objective training.

## Required inputs
- **image_text_pairs**: Web-scale image-text pairs.
- **dual_loss**: Combined contrastive + captioning loss.
- **coca_architecture**: CoCa architecture with attentional pooler + multimodal decoder.

## Optional inputs
- **caption_augmentation**: Additional caption data for generative quality.

## Outputs
- **coca_model**: Unified foundation model for retrieval and generation.
- **dual_representations**: Embeddings suitable for both retrieval and generation.

## Assumptions and prerequisites
- Contrastive and captioning objectives are complementary.
- Dual-objective training produces more versatile representations.
- A single model can excel at both retrieval and generation.

## Procedure
1. **Prepare image-text pairs**
   Action: Curate web-scale image-text data.
   Why: Both objectives operate on image-text pairs.
   Note: See paper for details.
2. **Apply contrastive loss**
   Action: Train the attentional pooler with contrastive loss.
   Why: Contrastive loss learns alignment for retrieval.
   Note: See paper for details.
3. **Apply captioning loss**
   Action: Train the multimodal decoder with captioning loss.
   Why: Captioning loss learns generation capability.
   Note: See paper for details.
4. **Joint training**
   Action: Train both objectives simultaneously.
   Why: Joint training produces versatile representations.
   Note: See paper for details.

## Parameters to set
- **contrastive_weight** — Role: Weight of contrastive loss. How to set: Balance with captioning loss. Default/range: 1.0. Effect: Higher weight emphasizes retrieval.
- **captioning_weight** — Role: Weight of captioning loss. How to set: Balance with contrastive loss. Default/range: 1.0. Effect: Higher weight emphasizes generation.

## Validation checks
- CoCa should match CLIP on retrieval tasks.
- CoCa should match generative models on captioning tasks.
- Dual-objective training should not degrade either capability.

## Failure modes
- The two objectives may interfere.
- Training may be slower than single-objective.
- The architecture adds complexity.

## Adaptation notes for VLM training
- CoCa's dual-objective approach is used in subsequent VLMs.
- The attentional pooler is reusable for other architectures.
- CoCa representations are used as recaptioning models.

## Implementation notes
- Balance loss weights carefully.
- Monitor both contrastive and generative metrics.
- Use the attentional pooler for efficient feature extraction.

## Evidence from the paper
- CoCa achieves state-of-the-art on both retrieval and generation tasks.
- Dual contrastive + captioning training produces more versatile representations.
- CoCa models are used as recaptioning engines in VLM data pipelines.
- The unified approach eliminates the need for separate contrastive and generative models.

## Source paper
- **Title**: CoCa: Contrastive Captioners are Image-Text Foundation Models
- **Year**: 2022
- **Venue**: TMLR
- **Paper ID**: arxiv-2205.01917v2
- **URL**: http://arxiv.org/abs/2205.01917v2
- **arXiv ID**: 2205.01917v2
