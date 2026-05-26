# POPE: Polling-based Object Probing Evaluation for Object Hallucination

## One-line decision
Use this skill when you want to evaluate and reduce object hallucination in VLMs using a polling-based evaluation framework. Avoid it when you are not concerned about object hallucination or have other evaluation methods.

## Skill metadata
- **Skill type**: hallucination-evaluation
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Evaluate object hallucination in VLMs using a polling-based framework where the model is asked yes/no questions about object presence, revealing hallucination tendencies under different sampling strategies.

## Problem signature
- Modality: images with yes/no questions about object presence for hallucination evaluation.
- Data state: COCO images with generated yes/no questions about object presence.
- Scale regime: evaluation dataset based on COCO images.
- Model requirement: Any VLM to evaluate for hallucination.

## Use when
- You want to evaluate VLM hallucination rates.
- You need a standardized hallucination benchmark.
- You want to understand hallucination under different conditions.

## Do not use when
- Hallucination evaluation is not your priority.
- You need evaluation beyond object presence/absence.
- You have a domain-specific hallucination evaluation.

## Required inputs
- **coco_images**: COCO images with ground truth object annotations.
- **question_generator**: Pipeline for generating yes/no object presence questions.
- **vlm_to_evaluate**: VLM being evaluated for hallucination.

## Optional inputs
- **sampling_strategies**: Different negative sampling strategies (random, popular, adversarial).

## Outputs
- **hallucination_scores**: Per-model hallucination rates under different conditions.
- **evaluation_framework**: Reusable hallucination evaluation pipeline.

## Assumptions and prerequisites
- Yes/no object questions effectively measure hallucination.
- Different negative sampling strategies reveal different hallucination types.
- Co-occurring objects are the primary source of hallucination.

## Procedure
1. **Generate positive questions**
   Action: Create 'Is there a [object]?' questions for objects present in each image.
   Why: Positive questions establish the model's detection ability.
   Note: See paper for details.
2. **Generate negative questions with different strategies**
   Action: Create questions for absent objects using random, popular, and adversarial sampling.
   Why: Different strategies reveal different hallucination tendencies.
   Note: See paper for details.
3. **Evaluate VLMs**
   Action: Ask the VLM all questions and record answers.
   Why: Measures hallucination rate.
   Note: See paper for details.
4. **Analyze results**
   Action: Compute accuracy, precision, recall, and F1 under each strategy.
   Why: Multi-metric analysis reveals hallucination patterns.
   Note: See paper for details.

## Parameters to set
- **sampling_strategies** — Role: How negative objects are selected. How to set: Use random, popular (frequently occurring), and adversarial (co-occurring) strategies. Default/range: 3 strategies. Effect: Adversarial reveals more hallucination than random.
- **questions_per_image** — Role: Number of questions per image. How to set: Equal positive and negative questions. Default/range: Balanced. Effect: Balanced questions enable fair evaluation.

## Validation checks
- Random sampling should show less hallucination than adversarial.
- Popular objects should be hallucinated more frequently.
- Accuracy should decrease under adversarial conditions.

## Failure modes
- Yes/no questions may not capture all hallucination types.
- Object co-occurrence statistics may vary across datasets.
- The binary format may miss nuanced hallucination.

## Adaptation notes for VLM training
- POPE is a standard hallucination benchmark for VLMs.
- Use POPE evaluation during VLM data curation to assess data quality impact.
- The polling approach can be extended to attribute and relationship hallucination.

## Implementation notes
- Use the POPE evaluation toolkit for reproducibility.
- Report all three sampling strategies for comprehensive evaluation.
- Track hallucination trends across model iterations.

## Evidence from the paper
- POPE reveals that VLMs hallucinate objects that frequently co-occur with present objects.
- Adversarial sampling exposes significantly more hallucination than random sampling.
- POPE has become a standard benchmark for evaluating VLM hallucination.
- The polling-based approach provides a simple, effective hallucination evaluation.

## Source paper
- **Title**: POPE: Polling-based Object Probing Evaluation for Object Hallucination
- **Year**: 2023
- **Venue**: EMNLP
- **Paper ID**: arxiv-2305.10355v2
- **URL**: http://arxiv.org/abs/2305.10355v2
- **arXiv ID**: 2305.10355v2
