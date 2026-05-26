# InternVL: Scaling up Vision Foundation Models and Aligning for Generic Visual-Linguistic Tasks

## One-line decision
Use this skill when you need a progressive data pipeline that aligns a large vision encoder with an LLM through contrastive, generative, and instruction-tuning stages. Avoid it when you are building a small model and cannot afford multi-stage pretraining.

## Skill metadata
- **Skill type**: progressive-alignment-data
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Scale up vision foundation models and progressively align them with LLMs through multi-stage data pipelines covering contrastive learning, generative pretraining, and instruction tuning.

## Problem signature
- Modality: image-text pairs, interleaved image-text, and instruction-following data across multiple training stages.
- Data state: multiple data sources aggregated and staged: web-crawled pairs for contrastive, curated pairs for generative, instruction data for fine-tuning.
- Scale regime: billions of image-text pairs for contrastive stage; millions for generative and instruction stages.
- Model requirement: InternViT-6B vision encoder + LLM (InternLM or LLaMA) with progressive alignment.

## Use when
- You need to train a large-scale vision encoder aligned with an LLM.
- You have access to multi-stage data spanning contrastive, generative, and instruction formats.
- You want a general-purpose VLM competitive with proprietary models.

## Do not use when
- You cannot afford multi-stage pretraining with billions of pairs.
- You need a lightweight model for deployment.
- Single-stage training meets your requirements.

## Required inputs
- **contrastive_data**: Billions of image-text pairs for contrastive pretraining (LAION, COYO, etc.).
- **generative_data**: Curated image-text pairs for generative alignment.
- **instruction_data**: Visual instruction-following data for fine-tuning.

## Optional inputs
- **interleaved_data**: Interleaved image-text documents for in-context learning capability.

## Outputs
- **internvl_model**: Aligned vision-language model with InternViT-6B.
- **internvit_encoder**: Standalone strong vision encoder usable for other VLMs.

## Assumptions and prerequisites
- Progressive alignment across stages is more effective than single-stage training.
- A 6B parameter vision encoder captures richer visual features than smaller encoders.
- Multi-source data diversity improves generalization.

## Procedure
1. **Stage 1: Contrastive pretraining**
   Action: Train InternViT-6B with contrastive loss on billions of image-text pairs.
   Why: Learns broad visual-semantic alignment.
   Note: See paper for details.
2. **Stage 2: Generative alignment**
   Action: Fine-tune with generative objectives on curated image-text data.
   Why: Bridges contrastive representations to generative language modeling.
   Note: See paper for details.
3. **Stage 3: Instruction tuning**
   Action: Fine-tune on visual instruction-following data.
   Why: Enables the model to follow diverse user instructions.
   Note: See paper for details.
4. **Evaluate across benchmarks**
   Action: Test on image classification, VQA, captioning, and retrieval.
   Why: Validates multi-stage alignment effectiveness.
   Note: See paper for details.

## Parameters to set
- **vision_encoder_size** — Role: Capacity of the vision encoder. How to set: 6B for maximum capability. Default/range: 6B. Effect: Larger encoder captures more visual detail.
- **alignment_stages** — Role: Number of training stages. How to set: 3 stages (contrastive, generative, instruction). Default/range: 3. Effect: More stages enable progressive alignment.

## Validation checks
- InternViT should achieve competitive ImageNet accuracy as a standalone encoder.
- The aligned model should improve across VQA, captioning, and retrieval benchmarks.
- Each stage should show measurable improvement over the previous.

## Failure modes
- Multi-stage training is expensive and errors in early stages propagate.
- The 6B vision encoder may be oversized for some deployment scenarios.
- Data quality in each stage directly impacts alignment quality.

## Adaptation notes for VLM training
- InternViT-6B can be used as a drop-in vision encoder for other VLM architectures.
- The progressive alignment strategy applies to any large vision encoder + LLM combination.
- Adapt the data pipeline to include domain-specific data in each stage.

## Implementation notes
- Use DeepSpeed or FSDP for training the 6B vision encoder.
- Cache stage 1 outputs to accelerate stage 2 training.
- Monitor alignment metrics between stages.

## Evidence from the paper
- InternVL achieves state-of-the-art performance on 18 vision-language benchmarks.
- InternViT-6B is the largest open-source vision encoder at the time of publication.
- Progressive alignment through contrastive, generative, and instruction stages is effective.
- The model achieves 64.1% on MMMU, competitive with GPT-4V.

## Source paper
- **Title**: InternVL: Scaling up Vision Foundation Models and Aligning for Generic Visual-Linguistic Tasks
- **Year**: 2024
- **Venue**: CVPR
- **Paper ID**: arxiv-2312.14238v5
- **URL**: http://arxiv.org/abs/2312.14238v5
- **arXiv ID**: 2312.14238v5
