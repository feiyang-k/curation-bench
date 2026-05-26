# GQA: A New Dataset for Real-World Visual Reasoning and Compositional Question Answering

## One-line decision
Use this skill when you want to generate balanced, compositional visual QA data from scene graphs using programmatic question generation. Avoid it when you need free-form questions that cannot be generated from scene graph templates.

## Skill metadata
- **Skill type**: programmatic-qa-generation
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Generate balanced, compositional visual question-answer pairs from scene graphs using programmatic generation, producing training data that requires multi-step spatial and relational reasoning.

## Problem signature
- Modality: images with programmatically generated QA pairs derived from scene graph annotations.
- Data state: scene graphs from Visual Genome used to generate 22M QA pairs.
- Scale regime: 22M QA pairs from 113K images.
- Model requirement: No model required for generation; scene graph + grammar-based question programs.

## Use when
- You need balanced visual QA data that avoids language bias shortcuts.
- You want compositional questions requiring multi-step reasoning.
- You have scene graph annotations to generate from.

## Do not use when
- You need free-form conversational questions.
- You lack scene graph annotations for your images.
- You need questions about concepts not in the scene graph vocabulary.

## Required inputs
- **scene_graphs**: Visual Genome scene graphs with objects, attributes, and relationships.
- **question_grammar**: Grammar for generating compositional question programs.
- **answer_extraction**: Logic for extracting answers from scene graphs.

## Optional inputs
- **balancing_algorithm**: Algorithm to balance answer distributions and question types.

## Outputs
- **gqa_dataset**: 22M balanced, compositional visual QA pairs.
- **question_programs**: Structured programs showing the reasoning steps for each question.

## Assumptions and prerequisites
- Scene graphs contain sufficient information for generating meaningful questions.
- Programmatic generation avoids the language bias present in human-written QA.
- Balancing ensures models cannot exploit answer distribution shortcuts.

## Procedure
1. **Extract scene graph information**
   Action: Parse Visual Genome scene graphs for objects, attributes, and relationships.
   Why: Scene graphs provide structured facts for question generation.
   Note: See paper for details.
2. **Generate question programs**
   Action: Use a compositional grammar to create multi-step reasoning programs.
   Why: Programs ensure questions require specific reasoning skills.
   Note: See paper for details.
3. **Execute programs on scene graphs**
   Action: Run each program on the scene graph to extract the answer.
   Why: Automated execution ensures answer correctness.
   Note: See paper for details.
4. **Balance the dataset**
   Action: Balance answer distributions, question types, and reasoning steps.
   Why: Prevents models from exploiting distribution shortcuts.
   Note: See paper for details.
5. **Validate and release**
   Action: Human-verify a sample and release the full dataset.
   Why: Quality verification ensures usability.
   Note: See paper for details.

## Parameters to set
- **question_complexity** — Role: Number of reasoning steps per question. How to set: Vary from 1-step to multi-step. Default/range: 1-5 steps. Effect: More steps test deeper reasoning but are harder.
- **balancing_strategy** — Role: How to balance answer and question type distributions. How to set: Equalize major answer categories. Default/range: Balanced. Effect: Prevents shortcut learning.

## Validation checks
- Questions should require the specified reasoning steps to answer.
- Answer distributions should be balanced across categories.
- Models should not be able to exploit language-only biases.

## Failure modes
- Scene graph errors propagate to generated QA pairs.
- Programmatic questions may feel unnatural or repetitive.
- The vocabulary is limited to Visual Genome's annotations.

## Adaptation notes for VLM training
- GQA is widely used as instruction tuning data for VLMs (LLaVA-1.5, etc.).
- The programmatic generation approach can be applied to other structured data.
- Use GQA-style balanced data to reduce VLM hallucination.

## Implementation notes
- Use the GQA question engine for generating new question types.
- Balance sampling during VLM training to match GQA's balanced distribution.
- Track per-reasoning-type accuracy during evaluation.

## Evidence from the paper
- GQA provides 22M balanced, compositional QA pairs from Visual Genome scene graphs.
- Programmatic generation eliminates language bias shortcuts present in VQA and VQAv2.
- Questions require multi-step spatial and relational reasoning.
- GQA is a standard component in VLM instruction tuning data mixes.

## Source paper
- **Title**: GQA: A New Dataset for Real-World Visual Reasoning and Compositional Question Answering
- **Year**: 2019
- **Venue**: CVPR
- **Paper ID**: arxiv-1902.09506v3
- **URL**: http://arxiv.org/abs/1902.09506v3
- **arXiv ID**: 1902.09506v3
