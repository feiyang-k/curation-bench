# MM1: Methods, Analysis and Insights from Multimodal LLM Pre-training

## One-line decision
Use this skill when you want to understand optimal data mixing recipes for multimodal LLM pretraining across interleaved, image-text, and text-only data. Avoid it when you only have one data type or cannot run ablation studies to tune the mix.

## Skill metadata
- **Skill type**: data-recipe-analysis
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Systematically analyze the impact of data mixing recipes (interleaved image-text, image-caption pairs, text-only data) on multimodal LLM pretraining performance to identify optimal configurations.

## Problem signature
- Modality: interleaved image-text documents, image-caption pairs, and text-only data mixed for pretraining.
- Data state: three data types available: interleaved documents, captioned image pairs, and text corpora.
- Scale regime: billions of tokens across all data types.
- Model requirement: Multimodal LLM with vision encoder, connector, and LLM backbone.

## Use when
- You are designing a data recipe for multimodal LLM pretraining.
- You have access to interleaved, paired, and text-only data.
- You want principled guidance on data mixing ratios.

## Do not use when
- You have only one data type (e.g., only image-caption pairs).
- You cannot afford ablation studies to validate the mix.
- You are training a contrastive model, not a generative LLM.

## Required inputs
- **interleaved_data**: Documents with interleaved images and text (e.g., web pages, articles).
- **image_caption_pairs**: Paired image-caption data from web crawl or curated sources.
- **text_only_data**: Pure text corpora for language modeling.

## Optional inputs
- **ablation_budget**: Compute budget for running data mix ablations at smaller scale.

## Outputs
- **optimal_data_recipe**: Recommended mixing ratios for the three data types.
- **trained_mm1_model**: Multimodal LLM trained with the optimal recipe.

## Assumptions and prerequisites
- The optimal data mix transfers from smaller ablation runs to full-scale training.
- All three data types (interleaved, paired, text-only) contribute complementary capabilities.
- Interleaved data is particularly important for few-shot in-context learning.

## Procedure
1. **Prepare three data types**
   Action: Collect interleaved image-text documents, image-caption pairs, and text-only data.
   Why: Each data type contributes different capabilities to the model.
   Note: See paper for details.
2. **Run data mix ablations**
   Action: Train small-scale models with different mixing ratios and evaluate on VL benchmarks.
   Why: Identifies the optimal balance before committing to full-scale training.
   Note: Vary interleaved:caption:text ratios systematically.
3. **Identify optimal recipe**
   Action: Select the mixing ratio that maximizes average performance across benchmarks.
   Why: The optimal mix balances in-context learning, captioning, and language capabilities.
   Note: See paper for details.
4. **Train full-scale model**
   Action: Train the full MM1 model with the identified optimal recipe.
   Why: Applies the validated recipe at production scale.
   Note: See paper for details.
5. **Evaluate comprehensively**
   Action: Test on VQA, captioning, retrieval, and few-shot benchmarks.
   Why: Validates the recipe across diverse capability dimensions.
   Note: See paper for details.

## Parameters to set
- **interleaved_ratio** — Role: Fraction of interleaved data in the mix. How to set: ~45% interleaved for balanced performance. Default/range: 0.4-0.5. Effect: More interleaved data improves few-shot learning.
- **caption_ratio** — Role: Fraction of image-caption pairs. How to set: ~45% for strong zero-shot. Default/range: 0.4-0.5. Effect: More captions improve zero-shot image understanding.
- **text_only_ratio** — Role: Fraction of text-only data. How to set: ~10% to preserve language ability. Default/range: 0.05-0.15. Effect: Text data maintains language modeling performance.

## Validation checks
- Few-shot VQA accuracy should improve with more interleaved data.
- Zero-shot captioning should improve with more image-caption pairs.
- Language-only benchmarks should not degrade significantly.

## Failure modes
- Optimal mix from small ablations may not transfer perfectly to full scale.
- Interleaved data is harder to collect and may have quality issues.
- Over-emphasis on one data type can degrade other capabilities.

## Adaptation notes for VLM training
- The data mixing insights generalize to other multimodal LLM architectures.
- For VLM training, prioritize the mix of interleaved and paired data.
- Use the ablation methodology to tune mixes for domain-specific applications.

## Implementation notes
- Run ablations at 1/10th scale to save compute.
- Track per-data-type loss curves during training.
- Use stratified sampling to ensure each batch contains all data types.

## Evidence from the paper
- MM1 finds that interleaved data is crucial for few-shot in-context learning.
- The optimal recipe uses roughly 45% interleaved, 45% caption, and 10% text-only data.
- Image resolution and the number of visual tokens have the most impact among architecture choices.
- MM1-30B achieves state-of-the-art performance among models up to 30B parameters.

## Source paper
- **Title**: MM1: Methods, Analysis and Insights from Multimodal LLM Pre-training
- **Year**: 2024
- **Venue**: ICML
- **Paper ID**: arxiv-2403.09611v3
- **URL**: http://arxiv.org/abs/2403.09611v3
- **arXiv ID**: 2403.09611v3
