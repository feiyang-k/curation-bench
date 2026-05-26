# LongVA: Long Context Transfer from Language to Vision

## One-line decision
Use this skill when you want to extend VLM context length for processing many images or long videos by transferring long context from language training. Avoid it when you do not need long-context visual processing.

## Skill metadata
- **Skill type**: long-context-visual-data
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Transfer long context capability from language model training to vision, enabling VLMs to process thousands of visual tokens from many images or long videos.

## Problem signature
- Modality: many images or long videos requiring extended context processing.
- Data state: training data with many images per example for long context.
- Scale regime: training with 2K+ images per example.
- Model requirement: VLM with extended context length (128K+ tokens).

## Use when
- You need to process many images in a single VLM context.
- You want long video understanding.
- You can extend your VLM's context length.

## Do not use when
- Single-image or short video processing is sufficient.
- You cannot extend context length.
- Your GPU memory is limited.

## Required inputs
- **long_context_llm**: LLM with extended context capability (128K+).
- **multi_image_data**: Training data with many images per example.
- **context_extension**: Method for extending context to visual tokens.

## Optional inputs
- **long_video_data**: Long video data for evaluation.

## Outputs
- **longva_model**: VLM with long context visual processing.
- **long_context_pipeline**: Pipeline for long context VLM training.

## Assumptions and prerequisites
- Language long context transfers to vision.
- Visual tokens can leverage the extended context window.
- Many-image and long video processing requires long context.

## Procedure
1. **Extend LLM context**
   Action: Train or adapt the LLM for 128K+ token context.
   Why: Long context is needed for many visual tokens.
   Note: See paper for details.
2. **Transfer to vision**
   Action: Apply the long context capability to visual token processing.
   Why: Visual tokens benefit from extended context.
   Note: See paper for details.
3. **Train on multi-image data**
   Action: Fine-tune on data with many images per example.
   Why: Multi-image data exercises long context visual processing.
   Note: See paper for details.
4. **Evaluate long context performance**
   Action: Test on many-image and long video benchmarks.
   Why: Validates long context visual capability.
   Note: See paper for details.

## Parameters to set
- **context_length** — Role: Maximum context length in tokens. How to set: 128K+ for long visual context. Default/range: 128K. Effect: Longer context enables more images.
- **images_per_context** — Role: Number of images processable in one context. How to set: 2K+ for comprehensive processing. Default/range: 2K+. Effect: More images enable richer multi-image understanding.

## Validation checks
- Long context should improve multi-image understanding.
- Performance should not degrade for single-image tasks.
- Long video understanding should benefit from extended context.

## Failure modes
- Extended context increases memory requirements.
- Attention over thousands of visual tokens is expensive.
- Long context may dilute attention for important tokens.

## Adaptation notes for VLM training
- Long context is essential for video understanding VLMs.
- Transfer long context from language to vision in any VLM architecture.
- Combine with efficient attention for practical deployment.

## Implementation notes
- Use RoPE scaling for context extension.
- Monitor memory usage with extended context.
- Evaluate on both short and long context tasks.

## Evidence from the paper
- LongVA transfers long context from language to vision processing.
- The model can process 2K+ images in a single context.
- Long context significantly improves multi-image and long video understanding.
- Language long context capability transfers effectively to visual tokens.

## Source paper
- **Title**: LongVA: Long Context Transfer from Language to Vision
- **Year**: 2024
- **Venue**: arXiv
- **Paper ID**: arxiv-2406.16852v2
- **URL**: http://arxiv.org/abs/2406.16852v2
- **arXiv ID**: 2406.16852v2
