# MiniCPM-V: A GPT-4V Level MLLM on Your Phone

## One-line decision
Use this skill when you want a data recipe for training a phone-deployable VLM that approaches GPT-4V quality on key benchmarks. Avoid it when you are not targeting mobile deployment.

## Skill metadata
- **Skill type**: mobile-vlm-data-recipe
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Design a data recipe for training a compact VLM deployable on phones that approaches GPT-4V quality, emphasizing data quality and efficient architecture.

## Problem signature
- Modality: high-quality instruction data for compact VLM training.
- Data state: curated high-quality instruction data for mobile VLM.
- Scale regime: curated instruction data emphasizing quality.
- Model requirement: MiniCPM (2.4B) + SigLIP ViT.

## Use when
- You want phone-deployable VLM quality.
- Data quality is critical for your compact model.
- You need efficient VLM deployment.

## Do not use when
- Maximum capability without size constraint.
- Mobile deployment is not your target.
- You have unlimited compute.

## Required inputs
- **high_quality_data**: Curated instruction data for compact training.
- **compact_llm**: MiniCPM 2.4B language model.
- **efficient_encoder**: SigLIP ViT for visual encoding.

## Optional inputs
- **quantization**: Quantization for mobile deployment.

## Outputs
- **minicpmv_model**: Phone-deployable VLM.
- **mobile_data_recipe**: Data recipe for compact VLMs.

## Assumptions and prerequisites
- High-quality data enables compact models to approach larger model quality.
- Mobile deployment requires extreme efficiency.
- Quality-focused data curation is most important for small models.

## Procedure
1. **Curate high-quality data**
   Action: Select the highest quality instruction data available.
   Why: Quality is critical for compact models.
   Note: See paper for details.
2. **Train compact VLM**
   Action: Train MiniCPM-V on curated data.
   Why: Validates the compact data recipe.
   Note: See paper for details.
3. **Optimize for mobile**
   Action: Apply quantization and optimization for phone deployment.
   Why: Enables actual mobile deployment.
   Note: See paper for details.
4. **Evaluate quality**
   Action: Compare to GPT-4V on key benchmarks.
   Why: Validates approaching frontier quality.
   Note: See paper for details.

## Parameters to set
- **model_size** — Role: Compact model size. How to set: 2.4B for mobile. Default/range: 2.4B. Effect: Small enough for phones.
- **data_quality** — Role: Quality of training data. How to set: Maximally curated. Default/range: Highest quality. Effect: Quality compensates for small model size.

## Validation checks
- Should approach GPT-4V on key benchmarks.
- Should deploy on phones.
- Data quality should demonstrably drive performance.

## Failure modes
- 2.4B may be insufficient for complex tasks.
- Mobile optimization may reduce quality.
- Quality data curation is expensive.

## Adaptation notes for VLM training
- MiniCPM-V demonstrates compact VLM viability.
- The data recipe is transferable to other compact architectures.
- Quality-focused curation is the key insight.

## Implementation notes
- Use INT4 quantization for mobile.
- Focus on data quality metrics.
- Benchmark against GPT-4V.

## Evidence from the paper
- MiniCPM-V approaches GPT-4V quality at 2.4B parameters.
- Data quality is the primary driver of compact model capability.
- The model deploys on phones with quantization.
- Compact VLMs with quality data are viable for mobile.

## Source paper
- **Title**: MiniCPM-V: A GPT-4V Level MLLM on Your Phone
- **Year**: 2024
- **Venue**: arXiv
- **Paper ID**: arxiv-2408.01800v3
- **URL**: http://arxiv.org/abs/2408.01800v3
- **arXiv ID**: 2408.01800v3
