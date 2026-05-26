# Gemini: A Family of Highly Capable Multimodal Models

## One-line decision
Use this skill when you want to understand Google's industrial-scale multimodal training data strategy for frontier VLMs. Avoid it when you need open, reproducible data strategies.

## Skill metadata
- **Skill type**: industrial-multimodal-data-recipe
- **Paper kind**: operational-method
- **Actionability**: medium
- **Evidence quality**: full_paper

## Goal
Document the multimodal training approach for Gemini, covering the integration of text, image, audio, and video data at industrial scale for training frontier multimodal models.

## Problem signature
- Modality: text, image, audio, and video data at industrial scale.
- Data state: industrial-scale curated multimodal training data.
- Scale regime: trillions of multimodal tokens.
- Model requirement: Gemini architecture with natively multimodal training.

## Use when
- You want insights into industrial-scale multimodal training.
- You need to understand frontier VLM data strategies.
- You are planning large-scale multimodal training.

## Do not use when
- You need open, reproducible data strategies.
- Industrial scale is not relevant to your work.
- You need specific implementation details.

## Required inputs
- **multimodal_data**: Industrial-scale text, image, audio, video data.
- **quality_pipelines**: Industrial quality filtering and curation.
- **training_infrastructure**: Large-scale distributed training.

## Optional inputs
- **safety_data**: Safety alignment data.

## Outputs
- **gemini_insights**: Industrial multimodal training insights.
- **frontier_capability**: Frontier multimodal model capabilities.

## Assumptions and prerequisites
- Industrial-scale data enables frontier capabilities.
- Natively multimodal training is effective.
- Quality curation at scale is achievable.

## Procedure
1. **Curate multimodal data**
   Action: Collect and curate text, image, audio, and video data.
   Why: Diverse multimodal data enables broad capabilities.
   Note: See paper for details.
2. **Apply quality filtering**
   Action: Filter all modalities for quality.
   Why: Quality curation improves training effectiveness.
   Note: See paper for details.
3. **Train natively multimodal**
   Action: Train Gemini on all modalities simultaneously.
   Why: Native multimodal training enables tight cross-modal integration.
   Note: See paper for details.
4. **Evaluate comprehensively**
   Action: Test across all modalities and benchmarks.
   Why: Validates frontier capability.
   Note: See paper for details.

## Parameters to set
- **data_scale** — Role: Total training data scale. How to set: Trillions of tokens. Default/range: Trillions. Effect: Scale enables frontier capability.
- **modality_coverage** — Role: Modalities included. How to set: Text, image, audio, video. Default/range: 4+ modalities. Effect: More modalities enable broader capability.

## Validation checks
- Gemini should achieve state-of-the-art across multimodal benchmarks.
- All modalities should be individually strong.
- Cross-modal capabilities should emerge.

## Failure modes
- Industrial strategies may not transfer to smaller scales.
- Proprietary data makes reproduction impossible.
- Details may be insufficient for implementation.

## Adaptation notes for VLM training
- Gemini insights inform open-source VLM training strategies.
- The natively multimodal approach is a direction for future VLMs.
- Industrial quality curation sets the bar for data quality.

## Implementation notes
- Use Gemini results as targets for open-source development.
- Adapt principles to your scale and data availability.
- Focus on transferable insights rather than exact reproduction.

## Evidence from the paper
- Gemini achieves state-of-the-art across multimodal benchmarks.
- Natively multimodal training with industrial-scale data enables frontier capabilities.
- The training approach covers text, image, audio, and video simultaneously.
- Gemini Ultra exceeds human expert performance on MMMU.

## Source paper
- **Title**: Gemini: A Family of Highly Capable Multimodal Models
- **Year**: 2024
- **Venue**: arXiv
- **Paper ID**: arxiv-2312.11805v3
- **URL**: http://arxiv.org/abs/2312.11805v3
- **arXiv ID**: 2312.11805v3
