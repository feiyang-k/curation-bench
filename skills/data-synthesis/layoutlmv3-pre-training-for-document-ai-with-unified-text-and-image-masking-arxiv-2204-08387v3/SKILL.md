# LayoutLMv3: Pre-training for Document AI with Unified Text and Image Masking

## One-line decision
Use this skill when you want to pre-train a document understanding model using unified text and image masking on document images with OCR. Avoid it when you do not need document layout understanding or OCR-dependent processing.

## Skill metadata
- **Skill type**: document-layout-pretraining
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Pre-train a document AI model using unified text and image masking objectives on document images with OCR text, learning the relationship between text content, visual appearance, and spatial layout.

## Problem signature
- Modality: document images with OCR text and spatial layout information.
- Data state: document images with OCR-extracted text and bounding box positions.
- Scale regime: 11M document pages for pre-training.
- Model requirement: Transformer encoder processing text, image patches, and layout jointly.

## Use when
- You need a model that understands document layout and text.
- You have OCR output for your documents.
- You want to pre-train on document-specific objectives.

## Do not use when
- You want OCR-free document understanding (use Donut/Nougat).
- Your documents are natural scenes rather than documents.
- You do not need layout understanding.

## Required inputs
- **document_images**: Document images for pre-training.
- **ocr_output**: OCR-extracted text with bounding box positions.
- **masking_objectives**: Unified text and image masking for pre-training.

## Optional inputs
- **downstream_tasks**: Specific document understanding tasks for fine-tuning.

## Outputs
- **layoutlmv3_model**: Pre-trained document understanding model.
- **document_representations**: Layout-aware document representations.

## Assumptions and prerequisites
- Unified text-image masking teaches text-layout-image relationships.
- OCR provides reliable text and position information.
- Document-specific pre-training transfers to diverse document tasks.

## Procedure
1. **Extract OCR and layout**
   Action: Process document images with OCR to get text and positions.
   Why: Text and layout information are needed for multi-modal pre-training.
   Note: See paper for details.
2. **Design masking objectives**
   Action: Implement unified text masking (MLM) and image masking (MIM).
   Why: Joint masking teaches relationships between modalities.
   Note: See paper for details.
3. **Pre-train on documents**
   Action: Train the model on 11M document pages with joint objectives.
   Why: Large-scale pre-training builds document understanding.
   Note: See paper for details.
4. **Fine-tune on downstream tasks**
   Action: Fine-tune for form understanding, receipt parsing, etc.
   Why: Transfers pre-trained knowledge to specific tasks.
   Note: See paper for details.

## Parameters to set
- **pretraining_pages** — Role: Number of document pages for pre-training. How to set: 11M+ for comprehensive coverage. Default/range: 11M. Effect: More pages improve document understanding.
- **masking_ratio** — Role: Fraction of text/image tokens masked. How to set: 15% text, 40% image typical. Default/range: 15%/40%. Effect: Higher masking increases difficulty.

## Validation checks
- Fine-tuning should achieve strong results on document benchmarks.
- The model should understand text-layout relationships.
- Pre-training should transfer across document types.

## Failure modes
- OCR errors propagate to the model.
- The model depends on OCR quality.
- Document layouts may vary significantly across types.

## Adaptation notes for VLM training
- LayoutLMv3 provides document understanding for VLM pipelines.
- Combine with VLMs for document-aware multimodal understanding.
- The layout-aware approach is essential for form and receipt processing.

## Implementation notes
- Use Azure OCR or similar for reliable text extraction.
- Pre-train on diverse document types for generalization.
- Monitor per-task metrics during fine-tuning.

## Evidence from the paper
- LayoutLMv3 achieves state-of-the-art on multiple document AI benchmarks.
- Unified text and image masking effectively teaches text-layout-image relationships.
- The model handles diverse document types from forms to receipts to scientific papers.
- Document-specific pre-training is essential for accurate layout understanding.

## Source paper
- **Title**: LayoutLMv3: Pre-training for Document AI with Unified Text and Image Masking
- **Year**: 2022
- **Venue**: ACM MM
- **Paper ID**: arxiv-2204.08387v3
- **URL**: http://arxiv.org/abs/2204.08387v3
- **arXiv ID**: 2204.08387v3
