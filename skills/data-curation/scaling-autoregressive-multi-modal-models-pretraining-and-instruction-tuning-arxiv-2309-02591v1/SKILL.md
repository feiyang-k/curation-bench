# Scaling Autoregressive Multi-Modal Models: Pretraining and Instruction Tuning

## One-line decision
Use this skill when you need a systematic approach to curating paired image-text and interleaved data at web scale for autoregressive VLM pretraining. Avoid it when you only need a small fine-tuning dataset.

## Skill metadata
- **Skill type**: multi-modal-data-curation-at-scale
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Curate web-scale pretraining data combining image-text pairs and interleaved image-text documents for training autoregressive multimodal models (CM3Leon / Chameleon style).

## Problem signature
- Modality: image-text pairs and interleaved image-text documents for autoregressive training.
- Data state: web-crawled data processed into both paired and interleaved formats for autoregressive pretraining.
- Scale regime: billions of tokens from mixed paired and interleaved sources.
- Model requirement: Autoregressive transformer processing interleaved image and text tokens.

## Use when
- You are building an autoregressive multimodal model (not contrastive).
- You need both paired and interleaved data for pretraining.
- You want a model capable of both understanding and generation.

## Do not use when
- You are training a contrastive model like CLIP.
- You only have paired data without interleaved documents.
- You need a lightweight model without large-scale pretraining.

## Required inputs
- **paired_data**: Image-text pairs from web crawl (filtered and deduplicated).
- **interleaved_documents**: Web pages with naturally interleaved images and text.
- **tokenizer**: Image tokenizer (e.g., VQVAE) and text tokenizer for unified token sequences.

## Optional inputs
- **instruction_data**: Task-specific instruction data for fine-tuning stage.

## Outputs
- **curated_pretraining_corpus**: Mixed paired and interleaved data ready for autoregressive training.
- **pretrained_model**: Autoregressive multimodal model capable of both understanding and generation.

## Assumptions and prerequisites
- Autoregressive models benefit from both paired and interleaved data types.
- Web-crawled interleaved documents provide natural multimodal reasoning examples.
- Image tokenization enables unified autoregressive training over both modalities.

## Procedure
1. **Collect and filter paired data**
   Action: Gather image-text pairs from web crawl with quality filtering.
   Why: Paired data provides clean image-text alignment signal.
   Note: See paper for details.
2. **Collect interleaved documents**
   Action: Extract web pages with naturally interleaved images and text.
   Why: Interleaved data teaches multimodal reasoning in context.
   Note: See paper for details.
3. **Tokenize images**
   Action: Convert images to discrete tokens using VQVAE or similar tokenizer.
   Why: Enables unified autoregressive training over image and text tokens.
   Note: See paper for details.
4. **Mix data types for training**
   Action: Combine paired and interleaved data with appropriate mixing ratios.
   Why: Both data types contribute complementary capabilities.
   Note: See paper for details.
5. **Pretrain autoregressive model**
   Action: Train the transformer on the mixed token sequences.
   Why: Autoregressive pretraining enables both understanding and generation.
   Note: See paper for details.

## Parameters to set
- **paired_interleaved_ratio** — Role: Mixing ratio between paired and interleaved data. How to set: Vary based on target capabilities. Default/range: Task-dependent. Effect: More interleaved data improves in-context reasoning; more paired improves alignment.
- **image_tokenizer** — Role: Model for converting images to tokens. How to set: Use VQVAE or VQGAN variants. Default/range: VQVAE. Effect: Token quality affects generation quality.
- **sequence_length** — Role: Maximum token sequence length. How to set: 4096+ for interleaved documents. Default/range: 4096. Effect: Longer sequences handle more images per document.

## Validation checks
- The model should handle both image understanding and generation tasks.
- In-context learning should improve with more interleaved training data.
- Image generation quality should be reasonable from the autoregressive approach.

## Failure modes
- Image tokenization introduces a quality bottleneck for generation.
- Interleaved web data may contain noisy or irrelevant image-text associations.
- The mixing ratio between data types requires careful tuning.

## Adaptation notes for VLM training
- The paired + interleaved recipe applies to Chameleon, Emu, and similar autoregressive VLMs.
- Adapt the data pipeline for domain-specific autoregressive multimodal models.
- Consider text-only data as a third stream for language capability preservation.

## Implementation notes
- Pre-tokenize images to avoid bottlenecking on tokenizer during training.
- Use sequence packing to minimize padding waste.
- Monitor generation quality throughout training with periodic sampling.

## Evidence from the paper
- CM3Leon demonstrates that web-scale autoregressive pretraining on mixed data produces strong multimodal models.
- The retrieval-augmented approach further improves performance by conditioning on retrieved relevant documents.
- Instruction tuning after pretraining enables the model to follow diverse user instructions.
- The data curation pipeline is critical for achieving competitive image generation from an autoregressive model.

## Source paper
- **Title**: Scaling Autoregressive Multi-Modal Models: Pretraining and Instruction Tuning
- **Year**: 2023
- **Venue**: arXiv
- **Paper ID**: arxiv-2309.02591v1
- **URL**: http://arxiv.org/abs/2309.02591v1
- **arXiv ID**: 2309.02591v1
