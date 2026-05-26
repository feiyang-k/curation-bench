# Donut: Document Understanding Transformer without OCR

## One-line decision
Use this skill when you want to pre-train a document understanding model on synthetic document images without OCR using a vision encoder-decoder. Avoid it when you have good OCR and only need text extraction without visual understanding.

## Skill metadata
- **Skill type**: synthetic-document-pretraining
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Pre-train a document understanding model using synthetically rendered document images, bypassing OCR entirely by training an end-to-end vision encoder-decoder to read and understand documents.

## Problem signature
- Modality: document images (synthetic and real) processed directly by a vision encoder-decoder.
- Data state: synthetically rendered documents for pre-training; real documents for fine-tuning.
- Scale regime: millions of synthetic document pages for pre-training.
- Model requirement: Swin Transformer encoder + BART decoder for end-to-end document understanding.

## Use when
- You want document understanding without OCR dependency.
- You can generate synthetic document images for pre-training.
- You need to handle diverse document layouts.

## Do not use when
- High-quality OCR is already available and sufficient.
- You only need text extraction without layout understanding.
- Your documents are handwritten rather than printed.

## Required inputs
- **synthetic_documents**: Rendered document images with ground truth text for pre-training.
- **document_renderer**: Tool for rendering text into document images with diverse layouts.
- **encoder_decoder**: Swin Transformer encoder + BART-style decoder.

## Optional inputs
- **real_documents**: Real document datasets for fine-tuning and evaluation.

## Outputs
- **donut_model**: OCR-free document understanding model.
- **document_understanding_pipeline**: End-to-end document processing pipeline.

## Assumptions and prerequisites
- Synthetic document pre-training transfers to real document understanding.
- Vision encoder-decoders can learn to read text from images.
- Eliminating OCR reduces pipeline complexity and error propagation.

## Procedure
1. **Generate synthetic documents**
   Action: Render diverse document images with known text content.
   Why: Synthetic data provides unlimited supervised pre-training data.
   Note: See paper for details.
2. **Pre-train on synthetic data**
   Action: Train the vision encoder-decoder to read synthetic documents.
   Why: Synthetic pre-training teaches the model to decode text from images.
   Note: See paper for details.
3. **Fine-tune on real documents**
   Action: Fine-tune on specific document understanding tasks (receipts, forms, etc.).
   Why: Task-specific fine-tuning adapts to real document characteristics.
   Note: See paper for details.
4. **Evaluate document understanding**
   Action: Test on document classification, information extraction, and VQA.
   Why: Validates OCR-free document understanding.
   Note: See paper for details.

## Parameters to set
- **synthetic_data_volume** — Role: Amount of synthetic pre-training data. How to set: Millions of rendered pages. Default/range: 11M+ pages. Effect: More synthetic data improves pre-training quality.
- **rendering_diversity** — Role: Diversity of document layouts and fonts. How to set: Vary fonts, sizes, layouts, and noise. Default/range: Diverse. Effect: More diversity improves generalization to real documents.

## Validation checks
- The model should correctly read text from document images.
- Fine-tuning on real documents should achieve competitive accuracy.
- Performance should match or exceed OCR-dependent baselines.

## Failure modes
- Very small text or low-resolution images may be unreadable.
- Complex table layouts may challenge the encoder.
- Non-Latin scripts may require additional pre-training data.

## Adaptation notes for VLM training
- The Donut architecture is the foundation for Nougat, Pix2Struct, and similar models.
- Synthetic document generation can be adapted for any document type.
- Use Donut-style models for document understanding in VLM pipelines.

## Implementation notes
- Use diverse fonts and layouts in synthetic rendering.
- Pre-train with reading order objectives.
- Monitor character-level accuracy during evaluation.

## Evidence from the paper
- Donut achieves competitive document understanding without any OCR dependency.
- Synthetic document pre-training effectively transfers to real document tasks.
- The end-to-end approach reduces pipeline complexity and error propagation.
- Donut achieves state-of-the-art on document classification and information extraction.

## Source paper
- **Title**: Donut: Document Understanding Transformer without OCR
- **Year**: 2022
- **Venue**: ECCV
- **Paper ID**: arxiv-2111.15664v2
- **URL**: http://arxiv.org/abs/2111.15664v2
- **arXiv ID**: 2111.15664v2
