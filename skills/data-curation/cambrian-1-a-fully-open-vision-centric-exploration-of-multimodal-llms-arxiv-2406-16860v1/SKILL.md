# Cambrian-1: A Fully Open, Vision-Centric Exploration of Multimodal LLMs

## One-line decision
Use this skill when you want a data-centric approach to VLM design that systematically evaluates vision encoders, connectors, and instruction data. Avoid it when you want a simple plug-and-play VLM without extensive ablation studies.

## Skill metadata
- **Skill type**: data-centric-vlm-design
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Provide a fully open, data-centric exploration of multimodal LLM design covering vision encoder selection, connector architecture, and instruction tuning data curation with Cambrian-7M dataset.

## Problem signature
- Modality: image-text instruction-following data across diverse visual tasks.
- Data state: curated instruction data (Cambrian-7M) combining internet, general knowledge, OCR, chart, math, and science data.
- Scale regime: 7 million curated instruction samples for fine-tuning.
- Model requirement: Multiple vision encoders (CLIP, DINOv2, SigLIP, etc.) + LLM with spatial vision aggregator (SVA) connector.

## Use when
- You want to systematically evaluate which vision encoders work best for VLM tasks.
- You need a large, curated instruction dataset covering diverse visual domains.
- You want to understand the impact of data composition on VLM performance.

## Do not use when
- You have already chosen your vision encoder and connector architecture.
- You need a lightweight model without multi-encoder complexity.
- You cannot run extensive ablation studies.

## Required inputs
- **vision_encoders**: Multiple pre-trained vision encoders to evaluate (CLIP, DINOv2, SigLIP, ConvNeXt, etc.).
- **instruction_data_sources**: Multiple instruction data sources across visual domains.
- **llm_backbone**: LLM backbone (LLaMA-3, etc.) for the language component.

## Optional inputs
- **evaluation_suite**: Comprehensive benchmark suite including CV-Bench for vision-centric evaluation.

## Outputs
- **cambrian_model**: VLM trained with optimal encoder combination and data mix.
- **cambrian_7m_dataset**: 7M curated instruction samples across visual domains.
- **design_insights**: Systematic analysis of encoder, connector, and data choices.

## Assumptions and prerequisites
- Multiple vision encoders capture complementary visual features.
- Data composition strongly affects which capabilities the model develops.
- Vision-centric evaluation is needed beyond existing language-centric benchmarks.

## Procedure
1. **Evaluate vision encoders**
   Action: Benchmark multiple vision encoders (CLIP, DINOv2, SigLIP, etc.) on VLM tasks.
   Why: Different encoders capture different visual features; the best combination is not obvious.
   Note: See paper for details.
2. **Design spatial vision aggregator**
   Action: Implement SVA connector to combine features from multiple vision encoders.
   Why: Multi-encoder aggregation captures complementary visual information.
   Note: See paper for details.
3. **Curate Cambrian-7M dataset**
   Action: Collect and curate 7M instruction samples across internet, general knowledge, OCR, chart, math, science, and language domains.
   Why: Diverse data coverage produces a more capable generalist model.
   Note: See paper for details.
4. **Run data composition ablations**
   Action: Vary the ratio of different data domains and measure impact on benchmarks.
   Why: Identifies the optimal data mix for balanced performance.
   Note: See paper for details.
5. **Train final model with optimal configuration**
   Action: Train Cambrian-1 with the best encoder combination, SVA connector, and data mix.
   Why: Combines all design insights into the final model.
   Note: See paper for details.

## Parameters to set
- **data_domains** — Role: Categories of instruction data to include. How to set: Balance across internet, OCR, chart, math, science. Default/range: 7 domains. Effect: Skewed domains produce skewed model capabilities.
- **num_encoders** — Role: Number of vision encoders to combine. How to set: 2-4 encoders provide good coverage. Default/range: 2-4. Effect: More encoders add compute but improve visual coverage.

## Validation checks
- Performance should improve across multiple benchmarks, not just one.
- The SVA should outperform simpler connector architectures.
- Data diversity should show clear benefits on vision-centric benchmarks.

## Failure modes
- Multi-encoder architecture increases compute and memory requirements.
- Balancing 7M samples across domains requires careful tuning.
- Vision-centric evaluation may not align with user-facing quality.

## Adaptation notes for VLM training
- The Cambrian-7M dataset provides a strong starting point for VLM instruction tuning.
- The multi-encoder approach can be applied to any VLM architecture.
- Use the data composition analysis to guide custom data mixes.

## Implementation notes
- Use the Cambrian codebase for reproducible training and evaluation.
- Track per-domain performance during training.
- The SVA adds minimal parameters compared to the LLM.

## Evidence from the paper
- Cambrian-1 provides the first fully open, vision-centric analysis of multimodal LLM design.
- Combining multiple vision encoders (CLIP + DINOv2) outperforms any single encoder.
- Data composition significantly impacts model capabilities across benchmarks.
- Cambrian-7M with balanced domain coverage produces strong generalist performance.

## Source paper
- **Title**: Cambrian-1: A Fully Open, Vision-Centric Exploration of Multimodal LLMs
- **Year**: 2024
- **Venue**: arXiv
- **Paper ID**: arxiv-2406.16860v1
- **URL**: http://arxiv.org/abs/2406.16860v1
- **arXiv ID**: 2406.16860v1
