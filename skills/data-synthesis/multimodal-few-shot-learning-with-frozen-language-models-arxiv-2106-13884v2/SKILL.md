# Multimodal Few-Shot Learning with Frozen Language Models

## One-line decision
Use this skill when you want to enable multimodal few-shot learning by training a visual encoder to produce prefix tokens for a frozen language model. Avoid it when you have abundant training data and do not need few-shot adaptation.

## Skill metadata
- **Skill type**: few-shot-multimodal-data
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Enable multimodal few-shot learning by training a visual encoder (Frozen model) to produce prefix tokens compatible with a frozen language model, allowing visual few-shot prompting.

## Problem signature
- Modality: images converted to prefix tokens for a frozen language model.
- Data state: image-text pairs used to train the visual prefix encoder.
- Scale regime: Conceptual Captions for visual prefix training.
- Model requirement: Frozen GPT-like LLM + trained visual prefix encoder.

## Use when
- You want few-shot multimodal learning without fine-tuning.
- You can train a visual prefix encoder.
- You need rapid adaptation with few examples.

## Do not use when
- You have abundant task-specific training data.
- Full fine-tuning is preferred.
- Few-shot is not your target use case.

## Required inputs
- **frozen_llm**: Pre-trained language model kept frozen.
- **visual_encoder**: Encoder trained to produce prefix tokens from images.
- **training_pairs**: Image-caption pairs for training the prefix encoder.

## Optional inputs
- **few_shot_examples**: In-context examples for few-shot prompting.

## Outputs
- **prefix_encoder**: Visual encoder producing LLM-compatible prefix tokens.
- **few_shot_model**: Model capable of multimodal few-shot learning.

## Assumptions and prerequisites
- Visual information can be encoded as prefix tokens.
- A frozen LLM can process visual prefix tokens.
- Few-shot learning emerges from prefix-based visual conditioning.

## Procedure
1. **Train visual prefix encoder**
   Action: Train an encoder to produce prefix tokens from images that a frozen LLM can process.
   Why: Prefix tokens bridge vision and frozen language.
   Note: See paper for details.
2. **Format few-shot prompts**
   Action: Create prompts with in-context image-text examples followed by the query image.
   Why: In-context examples enable few-shot learning.
   Note: See paper for details.
3. **Generate with frozen LLM**
   Action: Let the frozen LLM generate text conditioned on visual prefix tokens.
   Why: The LLM generates text using visual information.
   Note: See paper for details.
4. **Evaluate few-shot performance**
   Action: Test with varying numbers of in-context examples.
   Why: Validates few-shot learning capability.
   Note: See paper for details.

## Parameters to set
- **prefix_length** — Role: Number of prefix tokens per image. How to set: 8-32 tokens. Default/range: 32. Effect: More tokens capture more visual information.
- **few_shot_count** — Role: Number of in-context examples. How to set: 1-4 examples. Default/range: 2-4. Effect: More examples improve performance.

## Validation checks
- Few-shot performance should improve with more examples.
- The frozen LLM should generate coherent text from visual prefixes.
- Visual prefix training should converge on caption data.

## Failure modes
- Prefix tokens may not capture all visual information.
- The frozen LLM may not handle visual tokens well.
- Few-shot examples may need careful selection.

## Adaptation notes for VLM training
- The Frozen approach pioneered visual prefix encoding for LLMs.
- The prefix pattern influenced Flamingo, BLIP-2, and many VLMs.
- Few-shot multimodal learning reduces the need for task-specific data.

## Implementation notes
- Use a small number of prefix tokens for efficiency.
- Select diverse in-context examples.
- Compare to fine-tuned baselines.

## Evidence from the paper
- The Frozen approach enables multimodal few-shot learning with frozen LLMs.
- Visual prefix tokens effectively convey image information to language models.
- Few-shot performance improves with more in-context examples.
- The approach pioneered the visual prefix encoding paradigm.

## Source paper
- **Title**: Multimodal Few-Shot Learning with Frozen Language Models
- **Year**: 2021
- **Venue**: NeurIPS
- **Paper ID**: arxiv-2106.13884v2
- **URL**: http://arxiv.org/abs/2106.13884v2
- **arXiv ID**: 2106.13884v2
