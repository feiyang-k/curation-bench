# OpenCLIP: An Open Source Implementation of CLIP

## One-line decision
Use this skill when you want to train CLIP models on open datasets (LAION) with reproducible training recipes and systematic data ablations. Avoid it when you are using pre-trained CLIP models and do not need to train your own.

## Skill metadata
- **Skill type**: open-source-clip-training
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Provide an open-source implementation of CLIP training with reproducible recipes on open datasets (LAION-2B, LAION-400M), enabling systematic studies of training data, scale, and recipe effects on CLIP performance.

## Problem signature
- Modality: image-text pairs for contrastive CLIP training.
- Data state: open datasets (LAION-2B, LAION-400M, DataComp) used with reproducible training.
- Scale regime: 400M to 2B image-text pairs for training.
- Model requirement: ViT variants (ViT-B to ViT-G) trained with contrastive loss.

## Use when
- You want to train your own CLIP model with open data.
- You need reproducible CLIP training recipes.
- You want to study the effect of data on CLIP performance.

## Do not use when
- Pre-trained CLIP models meet your needs.
- You cannot afford CLIP training compute.
- You need a generative rather than contrastive model.

## Required inputs
- **training_data**: Open image-text datasets (LAION-2B, DataComp).
- **training_code**: OpenCLIP training framework.
- **compute**: GPU cluster for CLIP training.

## Optional inputs
- **custom_data**: Custom image-text datasets for training.

## Outputs
- **openclip_models**: Trained CLIP models with reproducible recipes.
- **training_analysis**: Analysis of data, scale, and recipe effects.

## Assumptions and prerequisites
- Open-source CLIP training enables reproducible vision-language research.
- LAION data can match or exceed proprietary datasets for CLIP training.
- Systematic ablations reveal best practices for CLIP training.

## Procedure
1. **Select training data**
   Action: Choose from LAION-2B, LAION-400M, DataComp, or custom data.
   Why: Data choice significantly affects CLIP quality.
   Note: See paper for details.
2. **Configure training recipe**
   Action: Set learning rate, batch size, epochs, and other hyperparameters.
   Why: Training recipe affects convergence and final performance.
   Note: See paper for details.
3. **Train CLIP models**
   Action: Train ViT variants with contrastive loss on the selected data.
   Why: Produces open, reproducible CLIP models.
   Note: See paper for details.
4. **Evaluate and compare**
   Action: Benchmark on ImageNet and transfer datasets.
   Why: Standardized evaluation enables fair comparison.
   Note: See paper for details.

## Parameters to set
- **model_scale** — Role: Size of ViT model. How to set: ViT-B/32 for fast iteration; ViT-G/14 for best quality. Default/range: ViT-B/32 to ViT-G/14. Effect: Larger models achieve higher accuracy.
- **training_data** — Role: Dataset for CLIP training. How to set: LAION-2B for best results. Default/range: LAION-2B. Effect: Larger, cleaner data improves performance.
- **batch_size** — Role: Contrastive batch size. How to set: 32K-88K for best performance. Default/range: 32768. Effect: Larger batches improve contrastive learning.

## Validation checks
- OpenCLIP models should match or exceed OpenAI CLIP at similar scales.
- Training should be reproducible across runs.
- Data ablations should show clear effects on performance.

## Failure modes
- LAION data quality may limit maximum performance.
- Large-scale training requires significant compute investment.
- Recipe hyperparameters may not transfer across data changes.

## Adaptation notes for VLM training
- OpenCLIP models are widely used as vision encoders for VLMs.
- Use OpenCLIP for training domain-specific CLIP models.
- The training recipes provide a starting point for custom CLIP training.

## Implementation notes
- Use the OpenCLIP codebase for reproducible training.
- Leverage the pre-trained model zoo for transfer learning.
- Monitor zero-shot accuracy throughout training.

## Evidence from the paper
- OpenCLIP provides reproducible CLIP training on open datasets.
- OpenCLIP ViT-G/14 achieves 80.1% zero-shot ImageNet accuracy.
- The framework enables systematic data and recipe ablation studies.
- OpenCLIP models are the most widely used open vision encoders for VLMs.

## Source paper
- **Title**: OpenCLIP: An Open Source Implementation of CLIP
- **Year**: 2023
- **Venue**: arXiv
- **Paper ID**: arxiv-2212.07143v2
- **URL**: http://arxiv.org/abs/2212.07143v2
- **arXiv ID**: 2212.07143v2
