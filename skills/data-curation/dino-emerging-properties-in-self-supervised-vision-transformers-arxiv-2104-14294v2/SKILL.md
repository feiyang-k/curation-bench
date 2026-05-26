# DINO: Emerging Properties in Self-Supervised Vision Transformers

## One-line decision
Use this skill when you want to train a self-supervised ViT that learns rich visual features with emerging object segmentation properties. Avoid it when CLIP-supervised features are sufficient for your VLM.

## Skill metadata
- **Skill type**: self-supervised-vision-features
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Train self-supervised Vision Transformers with knowledge distillation that develop rich visual features with emerging properties like object segmentation in attention maps.

## Problem signature
- Modality: images for self-supervised distillation pretraining.
- Data state: ImageNet images for DINO self-supervised training.
- Scale regime: ImageNet scale.
- Model requirement: ViT with self-distillation (student-teacher).

## Use when
- You want self-supervised features with segmentation properties.
- You need complementary features to CLIP.
- You want rich visual representations without labels.

## Do not use when
- CLIP features are sufficient.
- You need task-specific supervised features.
- Self-supervised pretraining is too expensive.

## Required inputs
- **pretraining_images**: ImageNet for self-supervised training.
- **student_teacher**: Student-teacher architecture for self-distillation.
- **augmentation**: Multi-crop augmentation for contrastive views.

## Optional inputs
- **downstream_data**: Data for evaluating features.

## Outputs
- **dino_model**: Self-supervised ViT with rich features.
- **attention_maps**: Attention maps with emerging segmentation.

## Assumptions and prerequisites
- Self-supervised ViTs learn object-centric features.
- Knowledge distillation improves feature quality.
- Emerging properties indicate genuine visual understanding.

## Procedure
1. **Set up student-teacher**
   Action: Create momentum teacher from student model.
   Why: Self-distillation drives feature learning.
   Note: See paper for details.
2. **Multi-crop augmentation**
   Action: Generate local and global crops for contrastive learning.
   Why: Multi-scale crops improve feature quality.
   Note: See paper for details.
3. **Train with DINO loss**
   Action: Train with cross-entropy between student and teacher.
   Why: Distillation loss drives self-supervised learning.
   Note: See paper for details.
4. **Evaluate features**
   Action: Test learned features on downstream tasks.
   Why: Validates feature quality.
   Note: See paper for details.

## Parameters to set
- **teacher_momentum** — Role: Momentum for teacher update. How to set: 0.996-0.999. Default/range: 0.996. Effect: Higher momentum provides more stable targets.
- **num_crops** — Role: Number of augmented crops. How to set: 2 global + 6-10 local. Default/range: 2+6. Effect: More crops improve multi-scale learning.

## Validation checks
- Attention maps should show object segmentation.
- Linear probe accuracy should be competitive.
- Features should complement CLIP features.

## Failure modes
- Training requires careful hyperparameter tuning.
- Self-supervised features may not capture all visual concepts.
- Multi-crop augmentation increases compute.

## Adaptation notes for VLM training
- DINO features are used alongside CLIP in VLMs (Cambrian-1).
- Self-supervised features capture different aspects than CLIP.
- DINO attention maps enable unsupervised segmentation.

## Implementation notes
- Use the DINO codebase for training.
- Monitor attention maps during training.
- Compare to CLIP features on downstream tasks.

## Evidence from the paper
- DINO learns self-supervised features with emerging segmentation.
- Attention maps naturally segment objects without supervision.
- DINO features complement CLIP in multi-encoder VLMs.
- Knowledge distillation produces rich, object-centric features.

## Source paper
- **Title**: DINO: Emerging Properties in Self-Supervised Vision Transformers
- **Year**: 2021
- **Venue**: ICCV
- **Paper ID**: arxiv-2104.14294v2
- **URL**: http://arxiv.org/abs/2104.14294v2
- **arXiv ID**: 2104.14294v2
