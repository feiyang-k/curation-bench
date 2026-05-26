# SNLI-VE: Visual Entailment Dataset

## One-line decision
Use this skill when you need a visual entailment dataset where the model must determine if a text hypothesis is entailed, contradicted, or neutral with respect to an image premise. Avoid it when you do not need visual entailment or NLI-style evaluation.

## Skill metadata
- **Skill type**: visual-entailment-data
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Create a visual entailment dataset by adapting SNLI text entailment to the visual domain, where an image serves as the premise and the model determines entailment, contradiction, or neutrality.

## Problem signature
- Modality: images (premises) with text hypotheses labeled for entailment.
- Data state: Flickr30K images paired with SNLI hypotheses for visual entailment.
- Scale regime: 550K image-hypothesis pairs with entailment labels.
- Model requirement: Any VLM for visual entailment.

## Use when
- You need visual entailment training or evaluation data.
- You want to test VLM reasoning about image-text consistency.
- You need a large-scale visual reasoning dataset.

## Do not use when
- Visual entailment is not your focus.
- Standard VQA evaluation is sufficient.
- You need more complex reasoning tasks.

## Required inputs
- **flickr30k_images**: Flickr30K images as visual premises.
- **snli_hypotheses**: Text hypotheses from SNLI adapted for visual entailment.
- **entailment_labels**: Labels: entailment, contradiction, or neutral.

## Optional inputs
- **reasoning_chains**: Explanations for entailment decisions.

## Outputs
- **snli_ve_dataset**: 550K visual entailment examples.
- **ve_benchmark**: Visual entailment benchmark.

## Assumptions and prerequisites
- Visual entailment tests image-text consistency understanding.
- SNLI hypotheses can be adapted for visual premises.
- Entailment reasoning is an important VLM capability.

## Procedure
1. **Pair images with hypotheses**
   Action: Match Flickr30K images with SNLI text hypotheses.
   Why: Creates visual entailment examples.
   Note: See paper for details.
2. **Label entailment**
   Action: Label each pair as entailment, contradiction, or neutral.
   Why: Labels provide the training/evaluation signal.
   Note: See paper for details.
3. **Validate labels**
   Action: Review labels for accuracy.
   Why: Quality control ensures benchmark reliability.
   Note: See paper for details.
4. **Benchmark VLMs**
   Action: Evaluate VLMs on visual entailment.
   Why: Tests image-text consistency reasoning.
   Note: See paper for details.

## Parameters to set
- **label_distribution** — Role: Balance of entailment labels. How to set: Roughly balanced across three classes. Default/range: ~1/3 each. Effect: Balance prevents shortcut learning.

## Validation checks
- VLMs should discriminate between entailment, contradiction, and neutral.
- Label accuracy should be high.
- The benchmark should be challenging for current models.

## Failure modes
- Some image-hypothesis pairs may be ambiguous.
- SNLI hypotheses may not always fit visual premises.
- Visual entailment may be easier than text entailment.

## Adaptation notes for VLM training
- Visual entailment data can be used for VLM reasoning training.
- Include in instruction tuning mixes for consistency reasoning.
- The entailment format tests important VLM capabilities.

## Implementation notes
- Use standard NLI evaluation metrics.
- Balance label distribution in training.
- Compare to text-only NLI performance.

## Evidence from the paper
- SNLI-VE provides 550K visual entailment examples.
- The dataset tests VLM reasoning about image-text consistency.
- Visual entailment is a distinct capability from VQA.
- The benchmark is widely used for VLM reasoning evaluation.

## Source paper
- **Title**: SNLI-VE: Visual Entailment Dataset
- **Year**: 2019
- **Venue**: AAAI
- **Paper ID**: arxiv-1901.06706v1
- **URL**: http://arxiv.org/abs/1901.06706v1
- **arXiv ID**: 1901.06706v1
