# PaLI-3: Smaller, Faster, Stronger

## One-line decision
Use this skill when you want insights on training a smaller but stronger VLM through improved data quality, SigLIP encoder, and efficient training recipe. Avoid it when you are not optimizing VLM training efficiency.

## Skill metadata
- **Skill type**: efficient-vlm-pretraining
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Train a smaller but stronger VLM (5B) by using SigLIP as the vision encoder, improved data quality, and an efficient training recipe, achieving strong performance with less compute.

## Problem signature
- Modality: optimized image-text data for efficient VLM training.
- Data state: high-quality image-text data with improved SigLIP encoding.
- Scale regime: efficient training at 5B parameters.
- Model requirement: SigLIP ViT + UL2 encoder-decoder LLM.

## Use when
- You want an efficient VLM training recipe.
- You need strong performance from a smaller model.
- SigLIP encoder is available.

## Do not use when
- Maximum capability is needed regardless of size.
- You prefer different architectures.
- Efficiency is not a priority.

## Required inputs
- **training_data**: High-quality image-text data.
- **siglip_encoder**: SigLIP ViT as vision encoder.
- **efficient_recipe**: Optimized training hyperparameters.

## Optional inputs
- **multi_res**: Multi-resolution training support.

## Outputs
- **pali3_model**: Efficient 5B VLM with strong performance.
- **training_insights**: Insights on efficient VLM training.

## Assumptions and prerequisites
- SigLIP provides better visual features than CLIP for VLMs.
- Data quality and training recipe can compensate for model size.
- 5B parameters is sufficient for competitive performance.

## Procedure
1. **Use SigLIP encoder**
   Action: Replace CLIP with SigLIP for vision encoding.
   Why: SigLIP provides stronger visual features.
   Note: See paper for details.
2. **Improve data quality**
   Action: Use higher quality training data.
   Why: Data quality drives performance.
   Note: See paper for details.
3. **Optimize training recipe**
   Action: Tune hyperparameters for efficiency.
   Why: Efficient training reduces compute needs.
   Note: See paper for details.
4. **Evaluate against larger models**
   Action: Compare to larger VLMs.
   Why: Validates efficiency claims.
   Note: See paper for details.

## Parameters to set
- **model_size** — Role: Total model parameters. How to set: 5B for efficiency. Default/range: 5B. Effect: Balanced size and capability.
- **vision_encoder** — Role: Vision encoder choice. How to set: SigLIP ViT. Default/range: SigLIP. Effect: SigLIP outperforms CLIP.

## Validation checks
- PaLI-3 should outperform larger PaLI-X on many tasks.
- SigLIP should provide measurable improvement over CLIP.
- Training should be efficient.

## Failure modes
- 5B may be insufficient for some complex tasks.
- SigLIP-specific improvements may not transfer.
- Efficiency optimizations may not generalize.

## Adaptation notes for VLM training
- PaLI-3 insights guide efficient VLM training.
- SigLIP adoption is increasingly standard.
- Data quality + efficient recipe = strong smaller model.

## Implementation notes
- Use SigLIP for vision encoding.
- Focus on data quality.
- Compare to larger baselines.

## Evidence from the paper
- PaLI-3 (5B) outperforms the 55B PaLI-X on many tasks.
- SigLIP encoder provides stronger features than CLIP.
- Data quality and training recipe compensate for smaller size.
- Efficient VLM training is viable at 5B scale.

## Source paper
- **Title**: PaLI-3: Smaller, Faster, Stronger
- **Year**: 2023
- **Venue**: arXiv
- **Paper ID**: arxiv-2310.09199v2
- **URL**: http://arxiv.org/abs/2310.09199v2
- **arXiv ID**: 2310.09199v2
