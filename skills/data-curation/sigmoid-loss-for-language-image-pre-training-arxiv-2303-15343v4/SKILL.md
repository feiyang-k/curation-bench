# Sigmoid Loss for Language Image Pre-Training

## One-line decision
Use this skill when you want a contrastive loss that handles noisy image-text pairs better by using sigmoid instead of softmax. Avoid it when you are already using softmax contrastive loss successfully on clean data.

## Skill metadata
- **Skill type**: loss-function-for-noisy-data
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Replace the standard softmax contrastive loss in CLIP with a sigmoid-based loss (SigLIP) that operates on independent image-text pairs rather than requiring a softmax over the full batch, enabling better handling of noisy data and more efficient training.

## Problem signature
- Modality: image-text pairs with sigmoid-based contrastive training.
- Data state: web-crawled image-text pairs that may contain noise; the sigmoid loss is more robust to false negatives.
- Scale regime: billions of image-text pairs; the sigmoid loss enables larger effective batch sizes.
- Model requirement: Dual-encoder (ViT + text transformer) trained with sigmoid loss instead of softmax contrastive loss.

## Use when
- Your image-text training data contains false negatives (different images with similar captions).
- You want to scale batch sizes beyond softmax contrastive limits.
- You want a simpler loss function that doesn't require global synchronization.

## Do not use when
- Softmax contrastive loss is already working well on your clean data.
- You need fine-grained ranking between candidates (sigmoid treats each pair independently).
- You are using very small batch sizes where softmax provides useful normalization.

## Required inputs
- **image_text_pairs**: Image-text pairs for training.
- **sigmoid_loss_config**: Sigmoid loss with learnable temperature and bias parameters.
- **dual_encoder**: ViT + text encoder architecture.

## Optional inputs
- **chunked_loss_computation**: Method for computing sigmoid loss over large batches without full materialization.

## Outputs
- **siglip_model**: Dual-encoder model trained with sigmoid loss.
- **improved_embeddings**: Image and text embeddings with better noise robustness.

## Assumptions and prerequisites
- Softmax contrastive loss creates false negatives when different images have similar captions.
- Sigmoid loss treating each pair independently avoids this problem.
- Sigmoid loss enables simpler distributed training without global batch synchronization.

## Procedure
1. **Replace softmax with sigmoid loss**
   Action: Change the contrastive loss from softmax (InfoNCE) to binary sigmoid on each image-text pair.
   Why: Sigmoid loss avoids false negative issues inherent in softmax over large batches.
   Note: See paper for details.
2. **Add learnable temperature and bias**
   Action: Include learnable temperature and bias parameters in the sigmoid loss.
   Why: Adaptable parameters allow the loss to calibrate during training.
   Note: See paper for details.
3. **Implement chunked computation**
   Action: Compute sigmoid loss in chunks to handle large batch sizes efficiently.
   Why: Avoids materializing the full batch similarity matrix.
   Note: See paper for details.
4. **Train on web-scale data**
   Action: Train SigLIP on the same data as CLIP but with the new loss function.
   Why: Demonstrates that the loss change alone improves performance.
   Note: See paper for details.
5. **Evaluate zero-shot transfer**
   Action: Compare SigLIP vs CLIP on zero-shot ImageNet and transfer benchmarks.
   Why: Validates that sigmoid loss improves over softmax contrastive loss.
   Note: See paper for details.

## Parameters to set
- **temperature** — Role: Learnable temperature for sigmoid scaling. How to set: Initialize and learn during training. Default/range: Learnable. Effect: Controls the sharpness of positive/negative discrimination.
- **bias** — Role: Learnable bias in the sigmoid. How to set: Initialize and learn during training. Default/range: Learnable. Effect: Shifts the decision boundary for positive vs negative pairs.
- **batch_size** — Role: Training batch size (can be very large with sigmoid). How to set: Scale as large as GPU memory allows. Default/range: 32K+. Effect: Larger batches improve performance more with sigmoid than softmax.

## Validation checks
- SigLIP should match or exceed CLIP accuracy on ImageNet zero-shot.
- Performance should scale better with batch size compared to softmax loss.
- The model should be more robust to noisy/ambiguous image-text pairs.

## Failure modes
- Sigmoid loss may converge slower than softmax in the early stages.
- Very small batch sizes may not provide enough negatives for sigmoid.
- The learnable bias may need careful initialization.

## Adaptation notes for VLM training
- SigLIP encoders are now preferred over CLIP encoders in many VLMs.
- The sigmoid loss principle applies to any contrastive multimodal learning.
- Use SigLIP as the vision encoder for LLaVA-style architectures.

## Implementation notes
- Implement chunked sigmoid computation for memory efficiency.
- Use gradient checkpointing for very large models.
- Monitor the learned temperature and bias values during training.

## Evidence from the paper
- SigLIP achieves 84.5% zero-shot ImageNet accuracy with ViT-g/14, outperforming CLIP.
- Sigmoid loss avoids false negatives from softmax normalization over large batches.
- SigLIP enables simpler distributed training by removing the need for global batch synchronization.
- The sigmoid loss scales better to very large batch sizes than softmax contrastive loss.

## Source paper
- **Title**: Sigmoid Loss for Language Image Pre-Training
- **Year**: 2023
- **Venue**: ICCV
- **Paper ID**: arxiv-2303.15343v4
- **URL**: http://arxiv.org/abs/2303.15343v4
- **arXiv ID**: 2303.15343v4
