# Emu2: Generative Multimodal Models are In-Context Learners

## One-line decision
Use this skill when you want to train a generative multimodal model that can both understand and generate images with in-context learning from interleaved data. Avoid it when you only need understanding without generation.

## Skill metadata
- **Skill type**: generative-multimodal-pretraining
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Train a generative multimodal model that learns in-context by training on interleaved multimodal data, enabling both understanding and generation of images in context.

## Problem signature
- Modality: interleaved image-text data for generative multimodal training.
- Data state: large-scale interleaved multimodal data for unified training.
- Scale regime: billions of multimodal tokens.
- Model requirement: 37B parameter generative multimodal model.

## Use when
- You want both understanding and generation.
- You can train on interleaved multimodal data.
- You want in-context multimodal learning.

## Do not use when
- Understanding-only is sufficient.
- You cannot afford 37B model training.
- In-context learning is not needed.

## Required inputs
- **interleaved_data**: Large-scale interleaved image-text data.
- **image_tokenizer**: VQGAN for image tokenization.
- **base_model**: 37B parameter transformer.

## Optional inputs
- **instruction_data**: Task-specific instruction data.

## Outputs
- **emu2_model**: Generative multimodal model with in-context learning.
- **multimodal_pipeline**: Unified understanding and generation pipeline.

## Assumptions and prerequisites
- Interleaved training enables in-context multimodal learning.
- A single model can handle both understanding and generation.
- 37B parameters provide sufficient capacity.

## Procedure
1. **Prepare interleaved data**
   Action: Curate large-scale interleaved image-text data.
   Why: Interleaved data enables in-context learning.
   Note: See paper for details.
2. **Train generative model**
   Action: Train 37B model on interleaved multimodal data.
   Why: Large-scale training develops both capabilities.
   Note: See paper for details.
3. **Fine-tune for tasks**
   Action: Optionally fine-tune on specific tasks.
   Why: Task-specific adaptation improves downstream performance.
   Note: See paper for details.
4. **Evaluate both capabilities**
   Action: Test understanding and generation in-context.
   Why: Validates dual capability.
   Note: See paper for details.

## Parameters to set
- **model_scale** — Role: Model size. How to set: 37B for comprehensive capability. Default/range: 37B. Effect: Larger model enables both capabilities.
- **data_diversity** — Role: Diversity of interleaved data. How to set: Include diverse multimodal content. Default/range: Diverse. Effect: More diversity improves generalization.

## Validation checks
- In-context learning should work for multimodal tasks.
- Both understanding and generation should be strong.
- The model should handle diverse multimodal contexts.

## Failure modes
- 37B model is expensive to train and deploy.
- Image tokenization may limit generation quality.
- Interleaved data curation is complex.

## Adaptation notes for VLM training
- Emu2 demonstrates in-context multimodal learning.
- Interleaved training is key for in-context capability.
- The approach extends to more modalities.

## Implementation notes
- Use high-quality VQGAN tokenization.
- Curate diverse interleaved data.
- Evaluate in-context learning with varied examples.

## Evidence from the paper
- Emu2 achieves strong in-context multimodal learning at 37B parameters.
- Interleaved training enables both understanding and generation.
- The model demonstrates few-shot multimodal adaptation.
- Generative multimodal models learn in-context from interleaved data.

## Source paper
- **Title**: Emu2: Generative Multimodal Models are In-Context Learners
- **Year**: 2024
- **Venue**: CVPR
- **Paper ID**: arxiv-2312.13286v1
- **URL**: http://arxiv.org/abs/2312.13286v1
- **arXiv ID**: 2312.13286v1
