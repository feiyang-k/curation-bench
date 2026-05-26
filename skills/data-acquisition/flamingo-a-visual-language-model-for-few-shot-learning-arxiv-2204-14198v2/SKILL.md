# Flamingo: A Visual Language Model for Few-Shot Learning

## One-line decision
Use this skill when you need to collect and train on interleaved image-text web data for few-shot visual learning. Avoid it when you only have paired image-caption data without interleaved document structure.

## Skill metadata
- **Skill type**: interleaved-data-collection
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Collect interleaved image-text web documents and combine with paired image-text data to train a visual language model capable of rapid few-shot adaptation to visual tasks.

## Problem signature
- Modality: interleaved image-text sequences from web pages plus standard image-text pairs.
- Data state: web pages with naturally interleaved images and text, plus curated image-text pair datasets.
- Scale regime: 185M image-text pairs + 43M web pages with interleaved images and text.
- Model requirement: Perceiver-based vision encoder cross-attending to a frozen Chinchilla LLM.

## Use when
- You want a VLM capable of few-shot learning from interleaved image-text examples.
- You can collect web pages with naturally interleaved images and text.
- You need in-context visual learning without fine-tuning.

## Do not use when
- You only have isolated image-caption pairs without document structure.
- You need a model for single-image understanding only.
- You cannot afford training on both interleaved and paired data.

## Required inputs
- **interleaved_web_documents**: Web pages containing naturally interleaved images and text (M3W dataset: 43M pages).
- **paired_image_text**: Standard image-caption pair datasets (LAION-2B, etc.).
- **frozen_llm**: Pre-trained language model to serve as the base (Chinchilla 70B).

## Optional inputs
- **video_text_pairs**: Video-text pairs for temporal understanding.

## Outputs
- **flamingo_model**: VLM capable of few-shot visual reasoning from interleaved examples.
- **m3w_dataset**: 43M interleaved web documents with images.

## Assumptions and prerequisites
- Interleaved image-text web data teaches in-context multimodal reasoning.
- Combining interleaved and paired data produces complementary capabilities.
- Few-shot learning emerges from training on naturally interleaved sequences.

## Procedure
1. **Collect M3W dataset**
   Action: Extract web pages with interleaved images and text from Common Crawl, keeping document structure.
   Why: Interleaved data enables few-shot in-context learning.
   Note: Keep images in their original position within the text.
2. **Curate paired image-text data**
   Action: Combine LAION-2B and other paired datasets filtered for quality.
   Why: Paired data provides clean image-text alignment.
   Note: See paper for details.
3. **Mix interleaved and paired data**
   Action: Alternate between interleaved and paired batches during training.
   Why: Both data types contribute complementary capabilities.
   Note: See paper for details.
4. **Train with frozen LLM**
   Action: Train perceiver resampler and cross-attention layers while keeping the LLM frozen.
   Why: Preserves the LLM's language capabilities while adding vision.
   Note: See paper for details.
5. **Evaluate few-shot performance**
   Action: Test few-shot visual QA, captioning, and classification with in-context examples.
   Why: Few-shot ability is the key capability enabled by interleaved training.
   Note: See paper for details.

## Parameters to set
- **interleaved_ratio** — Role: Fraction of training from interleaved vs paired data. How to set: Mix interleaved and paired data in training batches. Default/range: Not specified exactly. Effect: More interleaved data improves few-shot; more paired improves zero-shot.
- **max_images_per_sequence** — Role: Maximum images in one interleaved sequence. How to set: 5-10 images per sequence. Default/range: 5. Effect: More images per sequence enable longer few-shot contexts.
- **perceiver_queries** — Role: Number of queries in perceiver resampler. How to set: 64 queries per image. Default/range: 64. Effect: Fewer queries compress visual information more aggressively.

## Validation checks
- Few-shot VQA accuracy should increase with more in-context examples.
- The model should outperform fine-tuned baselines in low-data regimes.
- Zero-shot performance should be competitive with CLIP-based models.

## Failure modes
- Interleaved web data may contain noisy or irrelevant image-text associations.
- The perceiver resampler may discard fine-grained visual details.
- Few-shot performance is sensitive to the format and ordering of in-context examples.

## Adaptation notes for VLM training
- The interleaved data format has been adopted by many subsequent VLMs (Emu, IDEFICS, etc.).
- Collect domain-specific interleaved documents for specialized few-shot capabilities.
- The perceiver resampler pattern is reusable across VLM architectures.

## Implementation notes
- Preserve document structure (image positions) during web crawling.
- Use cross-attention rather than concatenation for efficiency with multiple images.
- Pre-compute vision features and cache them for faster training iterations.

## Evidence from the paper
- Flamingo achieves state-of-the-art few-shot performance on 16 multimodal benchmarks.
- Interleaved image-text training (M3W) is critical for few-shot in-context learning.
- The model handles arbitrary numbers of interleaved images and text.
- Flamingo 80B sets new state-of-the-art with just 4 few-shot examples on many tasks.

## Source paper
- **Title**: Flamingo: A Visual Language Model for Few-Shot Learning
- **Year**: 2022
- **Venue**: NeurIPS
- **Paper ID**: arxiv-2204.14198v2
- **URL**: http://arxiv.org/abs/2204.14198v2
- **arXiv ID**: 2204.14198v2
