# A-OKVQA: A Benchmark for Visual Question Answering using World Knowledge

## One-line decision
Use this skill when you need a VQA dataset requiring world knowledge and commonsense reasoning beyond what is visible in the image. Avoid it when your VQA task only requires visual perception without external knowledge.

## Skill metadata
- **Skill type**: knowledge-intensive-vqa
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Create a VQA benchmark requiring both visual understanding and world knowledge, with questions that need commonsense reasoning, factual knowledge, or cultural understanding beyond what is directly visible.

## Problem signature
- Modality: images with questions requiring world knowledge to answer.
- Data state: 25K questions requiring both visual understanding and world knowledge.
- Scale regime: 25K questions on ~24K COCO images.
- Model requirement: Any VLM for evaluation.

## Use when
- You need VQA data testing world knowledge.
- You want to evaluate VLM knowledge beyond visual perception.
- You need training data for knowledge-intensive visual reasoning.

## Do not use when
- Your VQA only needs visual perception.
- You do not need knowledge-intensive evaluation.
- You need a larger-scale knowledge VQA dataset.

## Required inputs
- **coco_images**: COCO images as the visual basis.
- **knowledge_questions**: Questions requiring world knowledge to answer.
- **rationale_annotations**: Rationales explaining why the answer requires knowledge.

## Optional inputs
- **multiple_choice**: Multiple-choice format for structured evaluation.

## Outputs
- **aokvqa_dataset**: 25K knowledge-intensive VQA questions.
- **rationales**: Explanation rationales for each question.

## Assumptions and prerequisites
- Visual understanding alone is insufficient for many real-world questions.
- World knowledge and commonsense are important VLM capabilities.
- Rationales help understand what knowledge is needed.

## Procedure
1. **Design knowledge-requiring questions**
   Action: Create questions that need information beyond what is visible.
   Why: Tests knowledge beyond visual perception.
   Note: See paper for details.
2. **Collect answers and rationales**
   Action: Gather answers with explanations of the knowledge needed.
   Why: Rationales reveal what type of knowledge is required.
   Note: See paper for details.
3. **Validate knowledge requirement**
   Action: Verify that questions genuinely require external knowledge.
   Why: Ensures the benchmark tests knowledge, not just perception.
   Note: See paper for details.
4. **Evaluate models**
   Action: Test VLMs on the benchmark in open-ended and multiple-choice settings.
   Why: Measures knowledge integration in visual reasoning.
   Note: See paper for details.

## Parameters to set
- **knowledge_types** — Role: Types of knowledge required. How to set: Include commonsense, factual, and cultural knowledge. Default/range: Diverse. Effect: More types test broader knowledge.
- **question_difficulty** — Role: Difficulty level of questions. How to set: Require genuine world knowledge. Default/range: Challenging. Effect: Harder questions discriminate better.

## Validation checks
- Questions should genuinely require external knowledge.
- Models with more knowledge should perform better.
- Rationales should correctly identify needed knowledge.

## Failure modes
- Some questions may be answerable without the stated knowledge.
- Knowledge requirements may not be uniformly distributed.
- Multiple-choice format may allow guessing.

## Adaptation notes for VLM training
- A-OKVQA tests whether VLM training data includes sufficient world knowledge.
- Include knowledge-intensive QA in instruction tuning for broader capability.
- The rationale format is useful for chain-of-thought training.

## Implementation notes
- Evaluate in both open-ended and multiple-choice settings.
- Use rationales for training chain-of-thought reasoning.
- Track per-knowledge-type performance.

## Evidence from the paper
- A-OKVQA provides 25K questions requiring visual understanding plus world knowledge.
- The benchmark tests commonsense, factual, and cultural knowledge.
- Rationale annotations reveal what knowledge each question requires.
- A-OKVQA is a standard benchmark for VLM knowledge evaluation.

## Source paper
- **Title**: A-OKVQA: A Benchmark for Visual Question Answering using World Knowledge
- **Year**: 2022
- **Venue**: ECCV
- **Paper ID**: arxiv-2206.01718v2
- **URL**: http://arxiv.org/abs/2206.01718v2
- **arXiv ID**: 2206.01718v2
