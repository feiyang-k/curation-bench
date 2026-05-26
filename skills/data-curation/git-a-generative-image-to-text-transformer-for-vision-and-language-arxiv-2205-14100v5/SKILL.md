# GIT: A Generative Image-to-text Transformer for Vision and Language

## One-line decision
Use this skill when you want a simple generative image-to-text model trained on large-scale image-text data with minimal architectural complexity. Avoid it when you need a more complex architecture with cross-attention or dual encoders.

## Skill metadata
- **Skill type**: simple-generative-vlm-data
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Train a simple generative image-to-text model using just a vision encoder and a text decoder, demonstrating that scaling data and compute with a simple architecture achieves strong performance.

## Problem signature
- Modality: image-text pairs for simple generative training.
- Data state: web-scale image-text pairs for generative training.
- Scale regime: 800M image-text pairs for pretraining.
- Model requirement: CLIP ViT image encoder + text transformer decoder.

## Use when
- You want a simple VLM architecture without complexity.
- You can scale data to compensate for architectural simplicity.
- You need a strong generative image-to-text model.

## Do not use when
- You need cross-attention or dual-encoder capabilities.
- You want discriminative rather than generative training.
- You need a complex multi-task architecture.

## Required inputs
- **image_text_pairs**: Web-scale image-text pairs.
- **vision_encoder**: CLIP ViT for image encoding.
- **text_decoder**: Transformer decoder for text generation.

## Optional inputs
- **downstream_data**: Task-specific data for fine-tuning.

## Outputs
- **git_model**: Simple generative image-to-text model.
- **captioning_pipeline**: Image captioning pipeline.

## Assumptions and prerequisites
- A simple architecture can achieve strong performance with sufficient data.
- Generative pretraining on image-text data enables diverse downstream tasks.
- Data scale compensates for architectural simplicity.

## Procedure
1. **Prepare large-scale data**
   Action: Curate 800M image-text pairs from the web.
   Why: Scale compensates for simple architecture.
   Note: See paper for details.
2. **Train generative model**
   Action: Train ViT encoder + text decoder with generative loss.
   Why: Generative training enables captioning and VQA.
   Note: See paper for details.
3. **Scale up**
   Action: Train larger models on more data.
   Why: Scaling improves performance.
   Note: See paper for details.
4. **Fine-tune on downstream tasks**
   Action: Fine-tune on captioning, VQA, and other tasks.
   Why: Fine-tuning adapts the model to specific tasks.
   Note: See paper for details.

## Parameters to set
- **data_scale** — Role: Number of training image-text pairs. How to set: 800M for strong performance. Default/range: 800M. Effect: More data improves the simple architecture.
- **model_scale** — Role: Size of the model. How to set: Scale up for better performance. Default/range: Variable. Effect: Larger models capture more.

## Validation checks
- The simple architecture should be competitive with more complex models.
- Data scaling should show clear benefits.
- Fine-tuning should achieve strong downstream performance.

## Failure modes
- Simple architecture may miss complex cross-modal interactions.
- Very large data is required to compensate for simplicity.
- The generative-only approach may limit discriminative tasks.

## Adaptation notes for VLM training
- GIT demonstrates that simplicity + data scale is a viable VLM strategy.
- The simple architecture is easy to implement and modify.
- GIT's approach validates the importance of data scale for VLMs.

## Implementation notes
- Use the GIT codebase for reproducibility.
- Scale data progressively.
- Monitor captioning quality during training.

## Evidence from the paper
- GIT achieves strong performance with a simple encoder-decoder architecture.
- 800M image-text pairs compensate for architectural simplicity.
- The model achieves state-of-the-art on captioning benchmarks.
- Simplicity + data scale is a viable VLM strategy.

## Source paper
- **Title**: GIT: A Generative Image-to-text Transformer for Vision and Language
- **Year**: 2022
- **Venue**: TMLR
- **Paper ID**: arxiv-2205.14100v5
- **URL**: http://arxiv.org/abs/2205.14100v5
- **arXiv ID**: 2205.14100v5
