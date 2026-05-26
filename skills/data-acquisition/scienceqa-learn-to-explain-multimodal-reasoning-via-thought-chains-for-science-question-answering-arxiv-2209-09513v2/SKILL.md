# ScienceQA: Learn to Explain: Multimodal Reasoning via Thought Chains for Science Question Answering

## One-line decision
Use this skill when you need a multimodal science QA dataset with detailed explanations and chain-of-thought reasoning for training VLMs. Avoid it when you do not need science reasoning or chain-of-thought data.

## Skill metadata
- **Skill type**: science-qa-with-explanations
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Create a multimodal science QA dataset with 21K questions including images, detailed explanations, and chain-of-thought reasoning annotations covering natural science, language science, and social science.

## Problem signature
- Modality: images with science multiple-choice questions and chain-of-thought explanations.
- Data state: 21K science questions with images, explanations, and reasoning chains.
- Scale regime: 21K questions across 26 topics and 127 categories.
- Model requirement: Any VLM for multimodal science reasoning.

## Use when
- You need science reasoning training or evaluation data.
- You want chain-of-thought explanations with visual context.
- You need multi-subject science QA.

## Do not use when
- Science reasoning is not your focus.
- You need non-science domain QA.
- You have sufficient science QA data.

## Required inputs
- **science_questions**: Science questions from elementary and high school curricula.
- **images**: Diagrams, figures, and images supporting the questions.
- **explanations**: Detailed explanations and chain-of-thought reasoning.

## Optional inputs
- **subject_labels**: Per-question subject and topic labels.

## Outputs
- **scienceqa_dataset**: 21K science QA samples with images and explanations.
- **reasoning_chains**: Chain-of-thought reasoning annotations.

## Assumptions and prerequisites
- Science questions require both visual and textual reasoning.
- Chain-of-thought explanations improve model reasoning.
- Multi-subject coverage enables broad science understanding.

## Procedure
1. **Collect science questions**
   Action: Gather science questions from educational sources across multiple subjects.
   Why: Educational questions provide structured science reasoning tasks.
   Note: See paper for details.
2. **Add visual context**
   Action: Include relevant images, diagrams, and figures.
   Why: Many science questions require visual understanding.
   Note: See paper for details.
3. **Annotate explanations**
   Action: Write detailed explanations with chain-of-thought reasoning.
   Why: Explanations teach the reasoning process.
   Note: See paper for details.
4. **Categorize by subject**
   Action: Label questions by subject, topic, and difficulty.
   Why: Structured categorization enables targeted evaluation.
   Note: See paper for details.

## Parameters to set
- **num_subjects** — Role: Number of science subjects. How to set: Cover natural, language, and social sciences. Default/range: 3 broad areas, 26 topics. Effect: More subjects improve breadth.
- **explanation_detail** — Role: Level of detail in explanations. How to set: Include step-by-step reasoning. Default/range: Detailed chain-of-thought. Effect: More detail teaches finer reasoning.

## Validation checks
- Questions should require the image to answer correctly.
- Chain-of-thought reasoning should be logically sound.
- Subject coverage should be balanced.

## Failure modes
- Some questions may not require the image.
- Explanations may not cover all reasoning steps.
- Curriculum-based questions may have limited complexity.

## Adaptation notes for VLM training
- ScienceQA is used in VLM instruction tuning for reasoning capability.
- Chain-of-thought annotations enable reasoning distillation.
- Combine with other reasoning datasets for comprehensive training.

## Implementation notes
- Use subject labels for stratified evaluation.
- Monitor chain-of-thought quality during training.
- Compare with and without CoT explanations.

## Evidence from the paper
- ScienceQA provides 21K science questions with images and chain-of-thought explanations.
- The dataset covers 26 topics across natural, language, and social sciences.
- Chain-of-thought reasoning annotations significantly improve model performance.
- ScienceQA is a standard benchmark for VLM science reasoning.

## Source paper
- **Title**: ScienceQA: Learn to Explain: Multimodal Reasoning via Thought Chains for Science Question Answering
- **Year**: 2022
- **Venue**: NeurIPS
- **Paper ID**: arxiv-2209.09513v2
- **URL**: http://arxiv.org/abs/2209.09513v2
- **arXiv ID**: 2209.09513v2
