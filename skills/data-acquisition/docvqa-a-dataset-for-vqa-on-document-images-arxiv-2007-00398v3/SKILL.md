# DocVQA: A Dataset for VQA on Document Images

## One-line decision
Use this skill when you need a VQA dataset on document images for training and evaluating document understanding VLMs. Avoid it when you need scene-level VQA rather than document understanding.

## Skill metadata
- **Skill type**: document-vqa-dataset
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Create a VQA dataset on document images where questions require understanding document layout, text content, and structure.

## Problem signature
- Modality: document images (invoices, forms, reports, etc.) with questions about their content.
- Data state: 12.7K document images with 50K human-annotated QA pairs.
- Scale regime: 50K QA pairs on 12.7K document images.
- Model requirement: No model required for dataset construction; validated with document understanding models.

## Use when
- You need document VQA training or evaluation data.
- You want to benchmark VLM document understanding.
- You need questions about document layout and structured content.

## Do not use when
- You need scene-level VQA.
- Document understanding is not your target task.
- You need a much larger dataset.

## Required inputs
- **document_images**: Diverse document images (invoices, forms, reports, letters, etc.).
- **human_annotators**: Workers to write questions about document content.
- **answer_annotations**: Ground truth answers with evidence spans.

## Optional inputs
- **ocr_output**: OCR text and layout information for the documents.

## Outputs
- **docvqa_dataset**: 50K QA pairs on 12.7K document images.
- **evaluation_metrics**: ANLS (Average Normalized Levenshtein Similarity) metric.

## Assumptions and prerequisites
- Document understanding requires specialized VQA data beyond scene-level datasets.
- Questions about documents require layout and structure understanding.
- The ANLS metric better evaluates document VQA than exact match.

## Procedure
1. **Collect diverse document images**
   Action: Gather documents from various domains (industry, government, academic).
   Why: Diversity ensures broad document understanding.
   Note: See paper for details.
2. **Generate QA pairs**
   Action: Have annotators create questions answerable from the document.
   Why: Human questions ensure relevance and difficulty.
   Note: See paper for details.
3. **Annotate evidence**
   Action: Mark the evidence region in the document for each answer.
   Why: Evidence annotation enables interpretable evaluation.
   Note: See paper for details.
4. **Define evaluation metric**
   Action: Use ANLS instead of exact match for flexible evaluation.
   Why: ANLS accounts for minor OCR and transcription errors.
   Note: See paper for details.

## Parameters to set
- **document_types** — Role: Types of documents included. How to set: Include invoices, forms, reports, letters, scientific papers. Default/range: Diverse. Effect: More types improve generalization.
- **questions_per_doc** — Role: Average questions per document. How to set: 3-5 questions per document. Default/range: ~4. Effect: More questions increase dataset utility.

## Validation checks
- Questions should require understanding document structure, not just text.
- The ANLS metric should handle OCR noise appropriately.
- Models should need both text reading and layout understanding.

## Failure modes
- Some questions may be answerable from text alone without layout understanding.
- Document quality variation may affect recognition.
- The dataset may not cover all document types.

## Adaptation notes for VLM training
- DocVQA is a standard benchmark and training data for document VLMs.
- Include DocVQA in instruction tuning for document understanding capability.
- The ANLS metric is now used across document understanding benchmarks.

## Implementation notes
- Provide OCR and layout information alongside images.
- Use the ANLS metric for evaluation.
- Track performance by document type.

## Evidence from the paper
- DocVQA provides 50K QA pairs on 12.7K document images across diverse document types.
- The dataset requires understanding document layout and structure, not just text.
- The ANLS metric provides flexible evaluation accounting for OCR noise.
- DocVQA has become a standard benchmark for document understanding VLMs.

## Source paper
- **Title**: DocVQA: A Dataset for VQA on Document Images
- **Year**: 2021
- **Venue**: WACV
- **Paper ID**: arxiv-2007.00398v3
- **URL**: http://arxiv.org/abs/2007.00398v3
- **arXiv ID**: 2007.00398v3
