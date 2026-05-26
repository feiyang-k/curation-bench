# VQAv2: Making the V in VQA Matter

## One-line decision
Use this skill when you need a large-scale balanced VQA dataset where each question has complementary image pairs to reduce language bias. Avoid it when you do not need VQA data or simple VQA is sufficient.

## Skill metadata
- **Skill type**: balanced-vqa-dataset
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Create a balanced VQA dataset by pairing each question with complementary images that elicit different answers, reducing the ability to exploit language-only shortcuts.

## Problem signature
- Modality: images with visual questions and answers, balanced with complementary pairs.
- Data state: VQA v1 questions balanced with complementary image pairs.
- Scale regime: 1.1 million questions on 200K images.
- Model requirement: No model required for dataset construction; validated with VQA models.

## Use when
- You need a large-scale, balanced VQA dataset.
- You want to reduce language bias in VQA training.
- You need VQA data for VLM instruction tuning.

## Do not use when
- Simple VQA benchmarks are sufficient.
- You need domain-specific VQA.
- You do not need VQA capability.

## Required inputs
- **vqa_v1**: Original VQA v1 questions and images.
- **complementary_images**: Images that elicit different answers for the same question.
- **annotation_pipeline**: Pipeline for collecting complementary annotations.

## Optional inputs
- **answer_normalization**: Normalization rules for VQA evaluation.

## Outputs
- **vqav2_dataset**: 1.1M balanced VQA questions on 200K images.
- **evaluation_metrics**: VQA accuracy metric with answer normalization.

## Assumptions and prerequisites
- Language bias is a major issue in VQA datasets.
- Complementary image pairs reduce exploitable shortcuts.
- Balanced data produces more visually grounded models.

## Procedure
1. **Identify bias-exploitable questions**
   Action: Find questions where language alone can predict the answer.
   Why: These questions need complementary pairs.
   Note: See paper for details.
2. **Collect complementary images**
   Action: Find images where the same question has a different answer.
   Why: Complementary pairs balance the dataset.
   Note: See paper for details.
3. **Annotate answers**
   Action: Collect human answers for complementary image-question pairs.
   Why: Ground truth answers are needed for evaluation.
   Note: See paper for details.
4. **Balance the dataset**
   Action: Ensure each question type has balanced answer distributions.
   Why: Balanced distributions prevent shortcut learning.
   Note: See paper for details.

## Parameters to set
- **complementary_ratio** — Role: Fraction of questions with complementary pairs. How to set: As many as possible. Default/range: ~90%. Effect: More complementary pairs reduce bias more.
- **answers_per_question** — Role: Number of human answers per question. How to set: 10 for robust evaluation. Default/range: 10. Effect: More answers improve evaluation reliability.

## Validation checks
- Language-only baselines should perform much worse on VQAv2 than VQAv1.
- Visual grounding should be necessary for good performance.
- Answer distributions should be balanced.

## Failure modes
- Some question types may resist balancing.
- Complementary images may introduce confounding factors.
- The dataset may still have residual biases.

## Adaptation notes for VLM training
- VQAv2 is the most widely used VQA benchmark and training dataset.
- Include VQAv2 in VLM instruction tuning data mixes (LLaVA-1.5, etc.).
- The balancing approach can be applied to other VL datasets.

## Implementation notes
- Use the VQA accuracy evaluation metric.
- Include VQAv2 in instruction tuning with answer formatting.
- Track per-question-type accuracy.

## Evidence from the paper
- VQAv2 provides 1.1M questions balanced with complementary image pairs.
- Language bias is significantly reduced compared to VQAv1.
- VQAv2 is the standard VQA benchmark for VLM evaluation.
- Complementary pairing forces models to use visual information.

## Source paper
- **Title**: VQAv2: Making the V in VQA Matter
- **Year**: 2017
- **Venue**: CVPR
- **Paper ID**: arxiv-1612.00837v3
- **URL**: http://arxiv.org/abs/1612.00837v3
- **arXiv ID**: 1612.00837v3
