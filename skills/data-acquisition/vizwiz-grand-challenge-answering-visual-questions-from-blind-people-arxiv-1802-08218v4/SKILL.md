# VizWiz Grand Challenge: Answering Visual Questions from Blind People

## One-line decision
Use this skill when you need VQA data from real blind users asking questions about photos they took, testing VLM accessibility applications. Avoid it when you do not need accessibility-focused VQA evaluation.

## Skill metadata
- **Skill type**: accessibility-focused-vqa-data
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Create a VQA dataset from real blind users who took photos and asked questions about them, providing evaluation data for accessibility-focused VLM applications.

## Problem signature
- Modality: photos from blind users with their visual questions.
- Data state: 31K VQA pairs from blind users' real-world photo queries.
- Scale regime: 31K questions from blind users.
- Model requirement: Any VLM for accessibility evaluation.

## Use when
- You want accessibility-focused VQA evaluation.
- You need real-world, user-generated visual queries.
- You want to test VLM accessibility applications.

## Do not use when
- Accessibility is not your focus.
- You need clean, studio-quality images.
- Standard VQA datasets are sufficient.

## Required inputs
- **blind_user_photos**: Photos taken by blind users.
- **user_questions**: Questions the users asked about their photos.
- **answer_annotations**: Human answers to the questions.

## Optional inputs
- **answerability_labels**: Labels indicating whether questions are answerable from the image.

## Outputs
- **vizwiz_dataset**: 31K VQA pairs from blind users.
- **accessibility_benchmark**: Benchmark for accessibility VLM evaluation.

## Assumptions and prerequisites
- Photos from blind users present unique challenges.
- Real user queries reflect practical accessibility needs.
- VLMs should be evaluated on accessibility scenarios.

## Procedure
1. **Collect user photos and questions**
   Action: Gather photos and questions from blind users.
   Why: Real user data reflects actual accessibility needs.
   Note: See paper for details.
2. **Annotate answers**
   Action: Collect multiple human answers per question.
   Why: Multiple answers provide robust evaluation.
   Note: See paper for details.
3. **Label answerability**
   Action: Mark which questions are answerable from the image.
   Why: Some photos may not contain the needed information.
   Note: See paper for details.
4. **Evaluate VLMs**
   Action: Test VLMs on the accessibility VQA benchmark.
   Why: Measures VLM accessibility capability.
   Note: See paper for details.

## Parameters to set
- **user_diversity** — Role: Diversity of blind users. How to set: Include diverse demographics and use cases. Default/range: Diverse. Effect: More diversity reflects broader needs.
- **question_types** — Role: Types of questions asked. How to set: Natural user queries without constraints. Default/range: Unconstrained. Effect: Natural queries test real capabilities.

## Validation checks
- VLMs should handle low-quality, poorly framed photos.
- Answerable questions should be correctly answered.
- Unanswerable questions should be identified.

## Failure modes
- Photos from blind users may be challenging for all models.
- Some questions may be inherently unanswerable.
- The dataset may not cover all accessibility needs.

## Adaptation notes for VLM training
- VizWiz is a standard accessibility VLM benchmark.
- Include VizWiz in VLM evaluation for accessibility testing.
- The real-user data perspective is unique and valuable.

## Implementation notes
- Handle unanswerable questions in evaluation.
- Use the VQA accuracy metric.
- Report per-question-type performance.

## Evidence from the paper
- VizWiz provides 31K VQA pairs from real blind users' photo queries.
- The dataset presents unique challenges from low-quality, user-generated photos.
- Accessibility-focused VQA tests different capabilities than standard VQA.
- VizWiz is a standard benchmark for evaluating VLM accessibility.

## Source paper
- **Title**: VizWiz Grand Challenge: Answering Visual Questions from Blind People
- **Year**: 2018
- **Venue**: CVPR
- **Paper ID**: arxiv-1802.08218v4
- **URL**: http://arxiv.org/abs/1802.08218v4
- **arXiv ID**: 1802.08218v4
