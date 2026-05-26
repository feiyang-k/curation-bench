# LLaVA-NeXT: Improved Reasoning, OCR, and World Knowledge

## One-line decision
Use this skill when you want to scale up instruction tuning data with higher quality and diversity for improved VLM reasoning. Avoid it when you have limited compute and cannot handle dynamic high-resolution image processing.

## Skill metadata
- **Skill type**: high-quality-data-scaling
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Scale up VLM instruction tuning with higher quality data, dynamic high-resolution input, and improved training recipes to advance reasoning, OCR, and world knowledge capabilities.

## Problem signature
- Modality: image-text instruction-response pairs with dynamic high-resolution image encoding.
- Data state: curated high-quality instruction data scaled up from LLaVA-1.5's 665K to approximately 760K samples.
- Scale regime: 760K high-quality instruction samples with dynamic resolution up to 672x672.
- Model requirement: CLIP ViT-L/14 with AnyRes dynamic tiling + various LLM backends (Vicuna, Mistral, Nous-Hermes-2-Yi-34B).

## Use when
- You want to improve VLM performance on reasoning, OCR, and knowledge-intensive tasks.
- You can process high-resolution images with dynamic tiling.
- You need better instruction tuning data beyond the LLaVA-1.5 recipe.

## Do not use when
- You are constrained to fixed low-resolution input (224x224 or 336x336).
- You cannot afford the increased compute from dynamic high-resolution processing.
- You need a simple baseline without dynamic resolution complexity.

## Required inputs
- **high_quality_instruction_data**: Curated instruction data emphasizing reasoning, OCR, chart understanding, and world knowledge.
- **dynamic_resolution_encoder**: CLIP ViT-L/14 with AnyRes dynamic tiling for high-resolution input.
- **llm_backend**: Strong LLM (Vicuna-13B, Mistral-7B, or Yi-34B) as the language backbone.

## Optional inputs
- **additional_reasoning_data**: Extra math, logic, and reasoning instruction samples.
- **sgd_warmup_config**: Learning rate warmup configuration for stable training.

## Outputs
- **llava_next_model**: Improved VLM with stronger reasoning, OCR, and world knowledge.
- **dynamic_resolution_pipeline**: Pipeline for processing images at multiple resolutions with tiling.

## Assumptions and prerequisites
- Higher resolution input directly improves OCR and fine-grained visual understanding.
- Better quality instruction data improves reasoning more than simply scaling quantity.
- Dynamic tiling preserves aspect ratio information important for document understanding.

## Procedure
1. **Curate higher quality instruction data**
   Action: Expand LLaVA-1.5 data mix with higher quality reasoning, OCR, and knowledge data.
   Why: Data quality improvements yield larger gains than architecture changes.
   Note: See paper for details.
2. **Implement dynamic resolution with AnyRes**
   Action: Tile input images into patches that fit the CLIP encoder, processing multiple tiles per image.
   Why: Preserves fine-grained details at high resolution without fixed aspect ratios.
   Note: See paper for details.
3. **Pre-train visual projection**
   Action: Train MLP projection with the dynamic resolution encoder.
   Why: Aligns high-resolution visual features with the language model.
   Note: See paper for details.
4. **Fine-tune on curated instruction mix**
   Action: Fine-tune the full model on the expanded 760K instruction dataset.
   Why: High-quality, diverse instruction data improves all capabilities.
   Note: See paper for details.
5. **Evaluate on expanded benchmarks**
   Action: Test on reasoning (MathVista), OCR (TextVQA, DocVQA), and knowledge benchmarks.
   Why: Comprehensive evaluation shows improvements across capability dimensions.
   Note: See paper for details.

## Parameters to set
- **max_tiles** — Role: Maximum number of image tiles for dynamic resolution. How to set: Balance detail vs compute; 4-9 tiles typical. Default/range: Variable. Effect: More tiles capture finer details but increase compute.
- **base_resolution** — Role: Resolution of each tile. How to set: Use 336x336 per tile. Default/range: 336. Effect: Matches CLIP encoder's native resolution.
- **instruction_data_size** — Role: Total instruction samples. How to set: ~760K with focus on quality over quantity. Default/range: 760K. Effect: Quality improvements matter more than scaling to millions.

## Validation checks
- TextVQA and DocVQA scores should improve significantly with higher resolution.
- MathVista and reasoning benchmarks should improve with better data.
- The model should handle various aspect ratios correctly.

## Failure modes
- Dynamic tiling increases inference cost proportionally to number of tiles.
- Very high resolution may expose CLIP's positional embedding limitations.
- The tiling strategy may fragment objects across tile boundaries.

## Adaptation notes for VLM training
- The AnyRes dynamic tiling approach has been widely adopted by subsequent VLMs.
- Combine with LoRA for parameter-efficient fine-tuning on domain-specific data.
- The data quality focus validates prioritizing curation over quantity for instruction tuning.

## Implementation notes
- Implement efficient tile batching to minimize padding waste.
- Use the LLaVA-NeXT codebase for reproducible training.
- Monitor per-tile attention patterns to verify the model uses all tiles.

## Evidence from the paper
- LLaVA-NeXT improves over LLaVA-1.5 on all major benchmarks with better data and dynamic resolution.
- Dynamic high-resolution processing (AnyRes) significantly improves OCR tasks.
- Scaling to 34B parameters with Yi-34B achieves state-of-the-art open-source VLM performance.
- The key improvements come from data quality, dynamic resolution, and scaling the LLM backbone.

## Source paper
- **Title**: LLaVA-NeXT: Improved Reasoning, OCR, and World Knowledge
- **Year**: 2024
- **Venue**: arXiv
- **Paper ID**: arxiv-2401.06209v1
- **URL**: http://arxiv.org/abs/2401.06209v1
- **arXiv ID**: 2401.06209v1
