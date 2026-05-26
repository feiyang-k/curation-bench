# OCR-VQA: Visual Question Answering by Reading Text in Images

## One-line decision
Use this skill when you need a VQA dataset about book covers requiring OCR to read titles, authors, and other text. Avoid it when you need general VQA or document VQA rather than book cover understanding.

## Skill metadata
- **Skill type**: book-cover-ocr-vqa
- **Paper kind**: operational-method
- **Actionability**: medium
- **Evidence quality**: full_paper

## Goal
Create a VQA dataset requiring reading text on book covers to answer questions about titles, authors, editions, and genres.

## Problem signature
- Modality: book cover images with questions about text content.
- Data state: book cover images with QA pairs about visible text.
- Scale regime: 1M+ QA pairs on 200K+ book cover images.
- Model requirement: No model required for dataset construction; validated with VQA + OCR models.

## Use when
- You need OCR-based VQA training data.
- You want to benchmark text reading in images.
- You need a large-scale text-reading VQA dataset.

## Do not use when
- You need general scene VQA.
- Book cover understanding is not your target.
- You need diverse document types beyond book covers.

## Required inputs
- **book_cover_images**: Images of book covers with visible text.
- **metadata**: Book metadata (title, author, genre, year) for QA generation.
- **qa_templates**: Templates for generating questions from metadata.

## Optional inputs
- **ocr_output**: OCR-extracted text from book covers.

## Outputs
- **ocrvqa_dataset**: 1M+ QA pairs on 200K+ book cover images.

## Assumptions and prerequisites
- Book covers contain structured text suitable for OCR-based QA.
- Metadata provides ground truth for automated QA generation.
- Large-scale OCR-VQA data improves VLM text reading.

## Procedure
1. **Collect book cover images**
   Action: Gather book cover images from online retailers.
   Why: Book covers contain structured text for QA.
   Note: See paper for details.
2. **Align with metadata**
   Action: Match book covers with title, author, and genre metadata.
   Why: Metadata provides ground truth answers.
   Note: See paper for details.
3. **Generate QA pairs**
   Action: Create template-based questions about book information.
   Why: Templates enable large-scale QA generation.
   Note: See paper for details.
4. **Validate answers**
   Action: Verify QA pairs against visible text in images.
   Why: Ensures answer correctness.
   Note: See paper for details.

## Parameters to set
- **qa_templates** — Role: Question templates for book information. How to set: Include title, author, genre, and year questions. Default/range: Multiple templates. Effect: More templates increase question diversity.

## Validation checks
- Answers should match text visible on the book cover.
- Models should require OCR to answer questions.
- The dataset should cover diverse book types.

## Failure modes
- Template-based questions may lack diversity.
- Some text on covers may be partially occluded.
- The domain is limited to book covers.

## Adaptation notes for VLM training
- OCR-VQA is used in VLM instruction tuning mixes (LLaVA-1.5, etc.).
- The template-based generation approach applies to other text-rich domains.
- Combine with TextVQA and DocVQA for comprehensive text understanding.

## Implementation notes
- Use metadata for automated QA generation.
- Include OCR tokens for model development.
- Track accuracy by question type.

## Evidence from the paper
- OCR-VQA provides over 1M QA pairs on 200K+ book cover images.
- The dataset requires reading text on book covers to answer questions.
- OCR-VQA is commonly used in VLM instruction tuning data mixes.
- Template-based generation enables large-scale dataset construction.

## Source paper
- **Title**: OCR-VQA: Visual Question Answering by Reading Text in Images
- **Year**: 2019
- **Venue**: ICDAR
- **Paper ID**: crossref-10-1109-icdar-2019
- **URL**: https://ocr-vqa.github.io/
- **arXiv ID**: N/A
