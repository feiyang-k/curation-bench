# BLIP: Bootstrapping Language-Image Pre-training for Unified Vision-Language Understanding and Generation

## One-line decision
Use this skill when you want to bootstrap better captions from noisy web data using a captioner-filter loop. Avoid it when you have clean gold-standard captions and do not need bootstrapping.

## Skill metadata
- **Skill type**: caption-bootstrapping
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Bootstrap high-quality captions from noisy web image-text pairs using a captioner to generate synthetic captions and a filter to remove noisy ones, creating a cleaner training dataset for vision-language pretraining.

## Problem signature
- Modality: image-text pairs with both web-crawled noisy captions and synthetic generated captions.
- Data state: noisy web-crawled image-text pairs that need caption quality improvement.
- Scale regime: 14M images from web datasets (CC3M, CC12M, SBU, LAION) plus COCO.
- Model requirement: Multimodal mixture of encoder-decoder (MED) architecture with captioner and filter components.

## Use when
- Your web-crawled image-text data has noisy or low-quality captions.
- You want to generate synthetic captions and filter out bad ones in a bootstrapping loop.
- You need a unified model for both vision-language understanding and generation.

## Do not use when
- Your captions are already high-quality gold annotations.
- You lack compute for the bootstrapping captioner-filter loop.
- You need only a contrastive model without generation capability.

## Required inputs
- **noisy_web_data**: Web-crawled image-text pairs with potentially noisy captions (e.g., from CC3M, CC12M, SBU).
- **clean_seed_data**: Small set of clean image-caption pairs (e.g., COCO) for bootstrapping the captioner.
- **med_architecture**: Multimodal mixture of encoder-decoder supporting captioning and filtering.

## Optional inputs
- **filter_threshold**: Confidence threshold for the filter to accept or reject captions.
- **num_bootstrap_rounds**: Number of captioner-filter iterations.

## Outputs
- **cleaned_dataset**: Web image-text pairs with noisy captions replaced or supplemented by synthetic captions that passed filtering.
- **blip_model**: Pretrained vision-language model for understanding and generation tasks.

## Assumptions and prerequisites
- A captioner trained on clean seed data can generate better captions than noisy web text.
- A filter trained on clean vs. noisy distinction can reliably reject bad captions.
- Bootstrapping improves caption quality over raw web data.

## Procedure
1. **Pre-train on noisy web data**
   Action: Train the MED model on raw noisy web image-text pairs with ITC, ITM, and LM losses.
   Why: Provides initial vision-language alignment despite noise.
   Note: See paper for details.
2. **Fine-tune captioner on clean data**
   Action: Fine-tune the captioner component on COCO or other clean image-caption data.
   Why: The captioner learns to produce high-quality captions from the clean seed.
   Note: See paper for details.
3. **Fine-tune filter on clean vs noisy**
   Action: Train the filter to distinguish clean captions from noisy web captions.
   Why: The filter will be used to remove bad captions from the training set.
   Note: See paper for details.
4. **Generate and filter captions**
   Action: Use the captioner to generate synthetic captions for web images, then apply the filter to accept or reject each caption.
   Why: Bootstrapping produces cleaner captions than raw web text.
   Note: See paper for details.
5. **Re-train on cleaned dataset**
   Action: Pre-train the model again on the cleaned dataset with synthetic + filtered captions.
   Why: Training on cleaner data improves downstream performance.
   Note: See paper for details.

## Parameters to set
- **filter_confidence** — Role: Threshold for accepting a caption as clean. How to set: Tune on a held-out set of clean/noisy pairs. Default/range: Not specified. Effect: Higher confidence keeps fewer but cleaner captions.
- **caption_generation_strategy** — Role: Decoding strategy for the captioner. How to set: Use nucleus sampling for diversity. Default/range: Nucleus sampling. Effect: Sampling produces more diverse captions than beam search.
- **bootstrap_iterations** — Role: Number of captioner-filter rounds. How to set: One round is typically sufficient. Default/range: 1. Effect: Additional rounds may help but with diminishing returns.

## Validation checks
- Captions that pass the filter should be more visually faithful than the original noisy captions.
- Downstream VQA and retrieval performance should improve after bootstrapping.
- The filter rejection rate should be meaningful (not trivially keeping or rejecting everything).

## Failure modes
- The captioner may generate generic or hallucinated captions.
- The filter may inherit biases from the clean seed data.
- Over-filtering can reduce dataset diversity.

## Adaptation notes for VLM training
- The captioner-filter bootstrap can be applied to any noisy web image-text dataset.
- For VLM training, use the bootstrapped captions alongside original text for maximum diversity.
- Audit generated captions for visual faithfulness before merging into VLM training data.

## Implementation notes
- Cache generated captions and filter scores for reproducibility.
- Run the filter on both original web captions and generated captions.
- Keep both original and synthetic captions to allow rollback.

## Evidence from the paper
- BLIP introduces a captioner-filter (CapFilt) bootstrapping method that improves the quality of noisy web captions.
- CapFilt bootstrapping consistently improves downstream performance on VQA, image-text retrieval, and image captioning.
- BLIP achieves state-of-the-art results on multiple vision-language benchmarks using bootstrapped data.
- The captioner generates synthetic captions and the filter removes noisy ones, yielding a cleaner training corpus.

## Source paper
- **Title**: BLIP: Bootstrapping Language-Image Pre-training for Unified Vision-Language Understanding and Generation
- **Year**: 2022
- **Venue**: ICML
- **Paper ID**: arxiv-2201.12086v1
- **URL**: http://arxiv.org/abs/2201.12086v1
- **arXiv ID**: 2201.12086v1
