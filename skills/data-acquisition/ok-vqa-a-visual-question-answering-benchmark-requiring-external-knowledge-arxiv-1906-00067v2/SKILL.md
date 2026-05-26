# OK-VQA: A Visual Question Answering Benchmark Requiring External Knowledge

## One-line decision
Use this skill when you need a VQA dataset where questions require external knowledge sources like Wikipedia to answer. Avoid it when your VQA task does not require external knowledge retrieval.

## Skill metadata
- **Skill type**: external-knowledge-vqa
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Create OK-VQA, a VQA benchmark where answering questions requires retrieving and applying external knowledge from sources like Wikipedia, going beyond what is visible in the image.

## Problem signature
- Modality: images with questions requiring external knowledge sources.
- Data state: 14K questions requiring external knowledge to answer.
- Scale regime: 14K questions on COCO images.
- Model requirement: Any VLM, optionally with knowledge retrieval.

## Use when
- You need VQA testing external knowledge retrieval.
- You want to benchmark knowledge-augmented VLMs.
- You need training data for retrieval-augmented VQA.

## Do not use when
- Visual perception VQA is sufficient.
- You do not need external knowledge integration.
- You have A-OKVQA which supersedes OK-VQA.

## Required inputs
- **coco_images**: COCO images as visual basis.
- **knowledge_questions**: Questions requiring external knowledge.
- **answer_annotations**: Human-provided answers.

## Optional inputs
- **knowledge_sources**: External knowledge sources for retrieval-augmented models.

## Outputs
- **okvqa_dataset**: 14K external knowledge VQA questions.

## Assumptions and prerequisites
- Many visual questions require external knowledge to answer.
- Knowledge retrieval is an important VLM capability.
- COCO images provide diverse visual scenarios.

## Procedure
1. **Design knowledge-requiring questions**
   Action: Create questions about COCO images that need external knowledge.
   Why: Tests knowledge retrieval and application.
   Note: See paper for details.
2. **Validate knowledge requirement**
   Action: Ensure questions cannot be answered from the image alone.
   Why: Guarantees the benchmark tests knowledge.
   Note: See paper for details.
3. **Collect answers**
   Action: Gather multiple human answers per question.
   Why: Multiple answers account for variation.
   Note: See paper for details.
4. **Benchmark models**
   Action: Evaluate VLMs with and without knowledge retrieval.
   Why: Shows the impact of knowledge augmentation.
   Note: See paper for details.

## Parameters to set
- **knowledge_breadth** — Role: Diversity of knowledge types required. How to set: Include factual, commonsense, and encyclopedic knowledge. Default/range: Diverse. Effect: Broader knowledge tests more comprehensive understanding.

## Validation checks
- Knowledge-augmented models should significantly outperform non-augmented ones.
- Questions should genuinely require external knowledge.
- The dataset should complement visual perception benchmarks.

## Failure modes
- Some questions may have leaked answers in training data.
- Knowledge retrieval quality varies across models.
- The dataset is relatively small (14K).

## Adaptation notes for VLM training
- OK-VQA established the external knowledge VQA task.
- A-OKVQA is the improved successor with rationales.
- Both datasets are used in VLM instruction tuning data.

## Implementation notes
- Use VQA accuracy metric for evaluation.
- Consider retrieval-augmented approaches.
- Track performance with and without knowledge sources.

## Evidence from the paper
- OK-VQA provides 14K questions requiring external knowledge beyond image content.
- Knowledge-augmented models significantly outperform standard VQA models.
- The benchmark established the external knowledge VQA research direction.
- OK-VQA is a precursor to the improved A-OKVQA benchmark.

## Source paper
- **Title**: OK-VQA: A Visual Question Answering Benchmark Requiring External Knowledge
- **Year**: 2019
- **Venue**: CVPR
- **Paper ID**: arxiv-1906.00067v2
- **URL**: http://arxiv.org/abs/1906.00067v2
- **arXiv ID**: 1906.00067v2
