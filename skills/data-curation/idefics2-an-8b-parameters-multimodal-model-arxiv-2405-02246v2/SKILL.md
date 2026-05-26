# Idefics2: An 8B Parameters Multimodal Model

## One-line decision
Use this skill when you want an efficient 8B VLM training recipe with curated data combining web interleaved, paired, and instruction data. Avoid it when you need a larger model or have a different data strategy.

## Skill metadata
- **Skill type**: efficient-vlm-data-recipe
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Design an efficient data recipe for training an 8B parameter VLM, combining OBELICS interleaved data, paired image-text data, and instruction tuning data with systematic ablation of each component.

## Problem signature
- Modality: interleaved, paired, and instruction data for efficient VLM training.
- Data state: curated mix of web interleaved, paired image-text, and instruction data.
- Scale regime: billions of tokens across three data types.
- Model requirement: SigLIP ViT + Mistral-7B with learned pooling connector.

## Use when
- You want an efficient 8B VLM training recipe.
- You have access to interleaved, paired, and instruction data.
- You want systematic data recipe guidance.

## Do not use when
- You are training a much larger model.
- You have a well-established data recipe.
- You only have one data type.

## Required inputs
- **interleaved_data**: OBELICS or similar interleaved image-text documents.
- **paired_data**: Image-caption pairs from LAION, etc.
- **instruction_data**: Visual instruction-following data.

## Optional inputs
- **text_only_data**: Text data for language capability preservation.

## Outputs
- **idefics2_model**: Efficient 8B VLM.
- **data_recipe**: Validated data mixing recipe.

## Assumptions and prerequisites
- An 8B model can be competitive with careful data curation.
- Systematic ablation reveals the optimal data mix.
- Interleaved, paired, and instruction data are all necessary.

## Procedure
1. **Prepare three data types**
   Action: Curate interleaved, paired, and instruction data.
   Why: Each type contributes different capabilities.
   Note: See paper for details.
2. **Ablate data composition**
   Action: Systematically vary data mix ratios and measure impact.
   Why: Identifies optimal composition.
   Note: See paper for details.
3. **Optimize training recipe**
   Action: Select the best data mix based on ablation results.
   Why: Optimal mix maximizes 8B model capability.
   Note: See paper for details.
4. **Train Idefics2**
   Action: Train the final model with the optimized recipe.
   Why: Applies the validated recipe at full scale.
   Note: See paper for details.

## Parameters to set
- **data_mix** — Role: Ratio of interleaved to paired to instruction data. How to set: Ablate systematically. Default/range: Varies. Effect: Mix determines capability balance.
- **connector_type** — Role: Vision-language connector architecture. How to set: Use learned pooling. Default/range: Learned pooling. Effect: Better connectors improve vision-language integration.

## Validation checks
- Idefics2 should be competitive with larger models.
- Each data type should show measurable contribution.
- The ablation should reveal clear trends.

## Failure modes
- 8B may not have sufficient capacity for all capabilities.
- Optimal mix may be sensitive to specific data sources.
- Ablation at smaller scales may not transfer perfectly.

## Adaptation notes for VLM training
- The Idefics2 recipe provides a template for efficient VLM training.
- Data ablation methodology is reusable for any VLM.
- The three-data-type framework generalizes to other VLM architectures.

## Implementation notes
- Use the HuggingFace implementation for reproducibility.
- Run ablations at smaller scales before full training.
- Track per-data-type metrics during training.

## Evidence from the paper
- Idefics2 achieves competitive 8B VLM performance with careful data curation.
- Systematic ablation reveals the optimal mix of interleaved, paired, and instruction data.
- Learned pooling connector improves over simpler approaches.
- The 8B model matches or exceeds some larger models through data optimization.

## Source paper
- **Title**: Idefics2: An 8B Parameters Multimodal Model
- **Year**: 2024
- **Venue**: arXiv
- **Paper ID**: arxiv-2405.02246v2
- **URL**: http://arxiv.org/abs/2405.02246v2
- **arXiv ID**: 2405.02246v2
