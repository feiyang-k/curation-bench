# ImageNet-21K Pretraining for the Masses

## One-line decision
Use this skill when you want to use ImageNet-21K for vision encoder pretraining with proper preprocessing and training recipes. Avoid it when ImageNet-1K or CLIP pretraining is sufficient.

## Skill metadata
- **Skill type**: imagenet21k-preprocessing
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Provide standardized preprocessing and training recipes for using ImageNet-21K (14M images, 21K classes) for vision model pretraining, making large-vocabulary supervised pretraining accessible.

## Problem signature
- Modality: ImageNet-21K images for supervised pretraining.
- Data state: ImageNet-21K cleaned and preprocessed for efficient training.
- Scale regime: 14M images, 21K classes.
- Model requirement: Any ViT or CNN for supervised pretraining.

## Use when
- You want supervised pretraining on 21K classes.
- ImageNet-1K is too small for your pretraining.
- You need a large-vocabulary vision encoder.

## Do not use when
- ImageNet-1K pretraining is sufficient.
- CLIP pretraining is preferred.
- 21K classes are unnecessary.

## Required inputs
- **imagenet_21k**: Full ImageNet-21K dataset.
- **preprocessing_pipeline**: Cleaning and preprocessing pipeline.
- **training_recipe**: Optimized training hyperparameters.

## Optional inputs
- **class_hierarchy**: WordNet class hierarchy for analysis.

## Outputs
- **preprocessed_21k**: Cleaned ImageNet-21K for training.
- **pretrained_model**: Vision model pretrained on 21K classes.

## Assumptions and prerequisites
- 21K classes provide richer supervision than 1K.
- Proper preprocessing significantly improves training.
- Supervised pretraining on 21K complements CLIP.

## Procedure
1. **Preprocess ImageNet-21K**
   Action: Clean, deduplicate, and balance the 21K dataset.
   Why: Raw 21K has quality issues.
   Note: See paper for details.
2. **Design training recipe**
   Action: Optimize hyperparameters for 21K pretraining.
   Why: 21K training needs different recipes than 1K.
   Note: See paper for details.
3. **Pretrain vision model**
   Action: Train ViT or CNN on preprocessed 21K.
   Why: Produces a strong vision encoder.
   Note: See paper for details.
4. **Transfer to downstream**
   Action: Fine-tune on target tasks.
   Why: Validates pretraining quality.
   Note: See paper for details.

## Parameters to set
- **preprocessing_steps** — Role: Cleaning steps for 21K. How to set: Remove broken, too-small images. Default/range: Standard cleaning. Effect: Cleaning improves training quality.
- **training_epochs** — Role: Pretraining duration. How to set: 80-300 epochs depending on model. Default/range: 80. Effect: More epochs improve features.

## Validation checks
- 21K-pretrained should outperform 1K-pretrained on transfer.
- Preprocessing should measurably improve training.
- The recipe should be reproducible.

## Failure modes
- 21K has noisier labels than 1K.
- Some classes have very few images.
- Preprocessing may remove valid data.

## Adaptation notes for VLM training
- ImageNet-21K provides supervised pretraining for VLM vision encoders.
- Use alongside CLIP pretraining for complementary features.
- 21K vocabulary covers more visual concepts.

## Implementation notes
- Use the provided preprocessing code.
- Apply the recommended training recipe.
- Compare to 1K-only pretraining.

## Evidence from the paper
- ImageNet-21K pretraining improves transfer over 1K.
- Proper preprocessing is critical for 21K training.
- 21K vocabulary provides richer supervision.
- Standardized recipes make 21K pretraining accessible.

## Source paper
- **Title**: ImageNet-21K Pretraining for the Masses
- **Year**: 2021
- **Venue**: NeurIPS Workshops
- **Paper ID**: arxiv-2104.10972v4
- **URL**: http://arxiv.org/abs/2104.10972v4
- **arXiv ID**: 2104.10972v4
