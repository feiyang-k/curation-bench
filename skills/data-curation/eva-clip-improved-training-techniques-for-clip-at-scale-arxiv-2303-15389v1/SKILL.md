# EVA-CLIP: Improved Training Techniques for CLIP at Scale

## One-line decision
Use this skill when you want to improve CLIP training efficiency through better data, larger models, and optimized training techniques. Avoid it when you are training a small CLIP model and do not need advanced optimization.

## Skill metadata
- **Skill type**: training-recipe-optimization
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Improve CLIP training at scale through better training techniques including data quality improvements, masked image modeling initialization, and optimized training recipes.

## Problem signature
- Modality: image-text pairs for contrastive CLIP training with improved recipes.
- Data state: curated image-text pairs from multiple sources (LAION-2B, COYO, merged datasets).
- Scale regime: 2 billion+ image-text pairs for training EVA-CLIP models up to ViT-E (4.4B parameters).
- Model requirement: ViT models (ViT-B to ViT-E/4.4B) with EVA-style masked image modeling initialization.

## Use when
- You want to train a large-scale CLIP model with state-of-the-art efficiency.
- You can use EVA-style initialization from masked image modeling.
- You need a strong vision encoder for downstream VLM applications.

## Do not use when
- You are training a small CLIP model where advanced techniques are unnecessary.
- You cannot afford large-scale pretraining compute.
- You need a model architecture other than ViT.

## Required inputs
- **large_scale_data**: Billions of image-text pairs from LAION, COYO, or merged datasets.
- **eva_initialization**: EVA weights from masked image modeling pretraining.
- **training_recipe**: Optimized hyperparameters for CLIP training at scale.

## Optional inputs
- **data_filtering**: Additional filtering beyond the base datasets.

## Outputs
- **eva_clip_model**: CLIP model with improved zero-shot and few-shot performance.
- **eva_vit_encoder**: Strong vision encoder for use in downstream VLMs.

## Assumptions and prerequisites
- Masked image modeling pretraining provides better initialization than random.
- Training recipe optimization can significantly improve CLIP performance at fixed data.
- Larger ViT models benefit from better initialization more than smaller ones.

## Procedure
1. **Pre-train vision encoder with masked image modeling**
   Action: Train EVA ViT using masked image modeling on ImageNet-21K or similar.
   Why: Provides a better initialization for CLIP training than random weights.
   Note: See paper for details.
2. **Prepare merged training data**
   Action: Combine LAION-2B, COYO, and other datasets, applying deduplication.
   Why: Larger, more diverse data pools improve CLIP training.
   Note: See paper for details.
3. **Train CLIP with optimized recipe**
   Action: Train with the EVA-CLIP recipe including specific learning rates, warmup, and gradient clipping.
   Why: Optimized recipes extract more value from the same data.
   Note: See paper for details.
4. **Scale to larger models**
   Action: Apply the recipe to ViT-L, ViT-G, and ViT-E architectures.
   Why: Larger models capture more fine-grained visual concepts.
   Note: See paper for details.
5. **Evaluate zero-shot performance**
   Action: Test on ImageNet and transfer datasets.
   Why: Validates the improvements from training recipe optimization.
   Note: See paper for details.

## Parameters to set
- **initialization** — Role: Starting weights for the ViT. How to set: Use EVA masked image modeling weights. Default/range: EVA pretrained. Effect: Better initialization leads to faster convergence and higher final performance.
- **merged_data_size** — Role: Total training data after merging sources. How to set: Combine LAION-2B + COYO + others. Default/range: 2B+. Effect: More diverse data improves generalization.
- **training_epochs** — Role: Number of passes through the data. How to set: 6-8 epochs typical. Default/range: 6-8. Effect: More epochs improve performance but increase compute.

## Validation checks
- Zero-shot ImageNet accuracy should exceed previous CLIP models at the same scale.
- EVA initialization should show clear benefits over random initialization.
- The training recipe should generalize across model scales.

## Failure modes
- EVA initialization may not help for very small models.
- Merged datasets may have distribution shifts between sources.
- Recipe-specific hyperparameters may not transfer to different architectures.

## Adaptation notes for VLM training
- EVA-CLIP vision encoders are widely used as backbone encoders for VLMs.
- The training recipe insights apply to any large-scale contrastive learning.
- Use EVA-CLIP-ViT-G as a drop-in vision encoder for LLaVA-style architectures.

## Implementation notes
- Use DeepSpeed ZeRO for memory-efficient training of billion-parameter ViTs.
- Log training loss and zero-shot accuracy at regular intervals.
- Pre-compute EVA features for efficient downstream use.

## Evidence from the paper
- EVA-CLIP achieves 80.4% zero-shot ImageNet accuracy with ViT-E/14, setting a new state-of-the-art.
- Masked image modeling initialization consistently improves CLIP training across all model scales.
- The EVA-CLIP training recipe enables efficient scaling to 4.4B parameter vision models.
- EVA-CLIP encoders are used in InternVL, LLaVA, and many other VLMs.

## Source paper
- **Title**: EVA-CLIP: Improved Training Techniques for CLIP at Scale
- **Year**: 2023
- **Venue**: arXiv
- **Paper ID**: arxiv-2303.15389v1
- **URL**: http://arxiv.org/abs/2303.15389v1
- **arXiv ID**: 2303.15389v1
