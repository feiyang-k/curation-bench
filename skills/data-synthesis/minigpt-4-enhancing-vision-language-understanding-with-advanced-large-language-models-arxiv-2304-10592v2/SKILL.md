# MiniGPT-4: Enhancing Vision-Language Understanding with Advanced Large Language Models

## One-line decision
Use this skill when you want to align a VLM using a small set of self-curated high-quality image-description pairs. Avoid it when you have abundant alignment data or do not need to fix generation quality issues.

## Skill metadata
- **Skill type**: self-curated-alignment-data
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Align a vision-language model by first identifying that poor generation quality stems from insufficient alignment data, then curating a small (3,500 samples) high-quality image-description dataset for a second-stage fine-tuning.

## Problem signature
- Modality: image-text pairs with detailed descriptions for alignment fine-tuning.
- Data state: small, carefully curated set of high-quality image-description pairs created through model self-generation and human refinement.
- Scale regime: only 3,500 high-quality alignment samples needed.
- Model requirement: Frozen ViT-G + Q-Former from BLIP-2 + Vicuna LLM, with a linear projection layer.

## Use when
- Your VLM generates repetitive, fragmented, or incoherent text after initial pretraining.
- You need to fix generation quality with minimal additional data.
- You can curate a small set of high-quality image-description pairs.

## Do not use when
- Your model already generates coherent, high-quality text.
- You have a large-scale alignment dataset available.
- You need to improve visual perception rather than text generation quality.

## Required inputs
- **pretrained_vlm**: VLM with vision encoder, connector, and LLM after initial pretraining on image-text pairs.
- **high_quality_pairs**: ~3,500 carefully curated image-description pairs.
- **alignment_prompt**: Prompt template for the alignment fine-tuning.

## Optional inputs
- **human_refinement**: Human post-editing of model-generated descriptions to improve quality.

## Outputs
- **aligned_vlm**: VLM with improved text generation quality after alignment.
- **alignment_dataset**: 3,500 high-quality image-description pairs.

## Assumptions and prerequisites
- Poor generation quality is an alignment problem, not a capability problem.
- A very small number of high-quality examples can fix alignment.
- The model already has visual understanding but lacks generation polish.

## Procedure
1. **Stage 1: Initial pretraining**
   Action: Train the linear projection on Conceptual Captions + SBU + LAION image-text pairs.
   Why: Establishes basic vision-language alignment.
   Note: See paper for details.
2. **Diagnose generation quality issues**
   Action: Observe that the model generates repetitive, fragmented outputs despite visual understanding.
   Why: Identifies alignment as the bottleneck.
   Note: See paper for details.
3. **Generate initial descriptions**
   Action: Use the model itself to generate detailed image descriptions for a set of Conceptual Captions images.
   Why: Self-generation provides a starting point for curation.
   Note: See paper for details.
4. **Curate and refine descriptions**
   Action: Manually select and refine ~3,500 high-quality descriptions using ChatGPT for polishing.
   Why: High-quality examples teach the model proper generation style.
   Note: See paper for details.
5. **Stage 2: Alignment fine-tuning**
   Action: Fine-tune the projection layer on the curated 3,500 samples with a conversational prompt.
   Why: Aligns generation quality to match the curated examples.
   Note: See paper for details.

## Parameters to set
- **alignment_samples** — Role: Number of curated samples for alignment. How to set: ~3,500 is sufficient. Default/range: 3500. Effect: More samples may help but diminishing returns expected.
- **stage2_epochs** — Role: Training epochs for alignment stage. How to set: Train for a few hundred steps. Default/range: Short training. Effect: Overfitting is a risk on such small data.
- **description_quality** — Role: Quality bar for curated descriptions. How to set: Detailed, coherent, and visually faithful. Default/range: High quality. Effect: Quality matters more than quantity.

## Validation checks
- Text generation should become coherent and natural after alignment.
- Visual understanding should not degrade after alignment fine-tuning.
- The model should handle diverse conversation topics.

## Failure modes
- Overfitting to the 3,500 samples may reduce diversity.
- Self-generated descriptions may contain hallucinations that persist after curation.
- The alignment may be fragile and degrade with further training.

## Adaptation notes for VLM training
- The two-stage (pretrain + align) pattern is now standard for VLM training.
- Extend the alignment set for better diversity.
- Use Claude or GPT-4 to assist in curating alignment data.

## Implementation notes
- Use a low learning rate for alignment to avoid catastrophic forgetting.
- Inspect generated outputs manually before and after alignment.
- Store the curated dataset for reproducibility.

## Evidence from the paper
- MiniGPT-4 demonstrates that just 3,500 high-quality examples can dramatically improve VLM generation quality.
- The model exhibits GPT-4-like capabilities in visual understanding and description after alignment.
- Two-stage training (pretraining + alignment) is more effective than single-stage training.
- The alignment insight influenced the development of many subsequent VLMs.

## Source paper
- **Title**: MiniGPT-4: Enhancing Vision-Language Understanding with Advanced Large Language Models
- **Year**: 2023
- **Venue**: ICLR
- **Paper ID**: arxiv-2304.10592v2
- **URL**: http://arxiv.org/abs/2304.10592v2
- **arXiv ID**: 2304.10592v2
