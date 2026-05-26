# TextVQA: Towards Reasoning about Text in Images

## One-line decision
Use this skill when you need a VQA dataset requiring models to read and reason about text visible in images. Avoid it when your VQA task does not involve reading text in images.

## Skill metadata
- **Skill type**: text-rich-vqa-dataset
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Create a VQA dataset where answering questions requires reading and reasoning about text visible in images, addressing a gap in existing VQA benchmarks.

## Problem signature
- Modality: images with visible text and questions requiring text reading and reasoning.
- Data state: images from OpenImages with human-written questions about visible text.
- Scale regime: 45K questions on 28K images from OpenImages.
- Model requirement: No model required for dataset construction; validated with VQA models + OCR.

## Use when
- You need VQA data requiring text reading in images.
- You want to benchmark VLM OCR and text reasoning capabilities.
- You need training data for text-rich visual understanding.

## Do not use when
- Your VQA task does not involve text in images.
- You need a larger-scale text-reading dataset.
- You need document-specific rather than scene text understanding.

## Required inputs
- **text_rich_images**: Images containing visible text (signs, labels, screens, etc.).
- **human_annotators**: Workers to write questions requiring text reading.
- **answer_annotations**: Ground truth answers for each question.

## Optional inputs
- **ocr_tokens**: OCR-extracted text to assist model development.

## Outputs
- **textvqa_dataset**: 45K questions on 28K images requiring text reading.
- **evaluation_metrics**: VQA accuracy metrics for text-reading evaluation.

## Assumptions and prerequisites
- Existing VQA datasets do not sufficiently test text reading in images.
- Questions requiring text reading are a distinct and important capability.
- OCR tokens can assist models in answering text-based questions.

## Procedure
1. **Select text-rich images**
   Action: Choose images from OpenImages containing visible text.
   Why: Text-rich images are needed for text-reading questions.
   Note: See paper for details.
2. **Collect questions**
   Action: Have annotators write questions that require reading text in the image.
   Why: Human-written questions ensure natural, meaningful queries.
   Note: See paper for details.
3. **Collect answers**
   Action: Gather multiple answers per question from different annotators.
   Why: Multiple answers account for answer variation.
   Note: See paper for details.
4. **Evaluate baseline models**
   Action: Test existing VQA models with and without OCR on TextVQA.
   Why: Establishes baselines and demonstrates the need for text reading.
   Note: See paper for details.

## Parameters to set
- **images_count** — Role: Number of text-rich images. How to set: Select diverse images with visible text. Default/range: 28K. Effect: More images increase diversity.
- **questions_per_image** — Role: Average questions per image. How to set: 1-2 questions focused on text. Default/range: ~1.6. Effect: More questions increase dataset utility.

## Validation checks
- Questions should require reading text visible in the image to answer.
- Models without OCR should perform significantly worse than those with OCR.
- The dataset should cover diverse text appearances (signs, labels, screens).

## Failure modes
- Some visible text may be too small or blurry to read.
- Questions may be answerable from context without reading the specific text.
- OCR errors may propagate to model answers.

## Adaptation notes for VLM training
- TextVQA is a standard benchmark and training data source for VLMs with OCR capability.
- Include TextVQA in instruction tuning mixes for text reading ability.
- The dataset format has influenced DocVQA, ChartQA, and similar benchmarks.

## Implementation notes
- Provide OCR tokens alongside images for model development.
- Use the VQA accuracy metric for evaluation.
- Track per-text-type performance (signs, labels, screens).

## Evidence from the paper
- TextVQA provides 45K questions requiring reading and reasoning about text in images.
- Models without OCR capability struggle on TextVQA.
- The dataset reveals a significant gap in existing VQA models' text reading ability.
- TextVQA has become a standard benchmark for VLM text understanding.

## Source paper
- **Title**: TextVQA: Towards Reasoning about Text in Images
- **Year**: 2019
- **Venue**: CVPR
- **Paper ID**: arxiv-1904.08920v2
- **URL**: http://arxiv.org/abs/1904.08920v2
- **arXiv ID**: 1904.08920v2
