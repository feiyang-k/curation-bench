# LaCLIP: Improving CLIP Training with Language Rewrites

## One-line decision
Use this skill when you want to augment CLIP training text by rewriting captions with an LLM to improve text diversity. Avoid it when your captions are already diverse and high-quality or you cannot afford LLM rewriting.

## Skill metadata
- **Skill type**: text-augmentation-for-clip
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Improve CLIP training by augmenting image-text pairs with LLM-rewritten captions, increasing text diversity and providing multiple views of each image's description.

## Problem signature
- Modality: image-text pairs with augmented captions from LLM rewrites.
- Data state: existing image-text pairs augmented with LLM-generated caption rewrites.
- Scale regime: applied to LAION-400M and CC3M/CC12M datasets.
- Model requirement: An LLM for rewriting captions; standard CLIP architecture for training.

## Use when
- Your CLIP training captions are short, generic, or repetitive.
- You want to increase text diversity without collecting new images.
- You can afford LLM inference for caption rewriting.

## Do not use when
- Your captions are already diverse and descriptive.
- You cannot afford LLM inference at your dataset scale.
- You are not training a contrastive model.

## Required inputs
- **original_pairs**: Image-text pairs with original captions.
- **rewriting_llm**: LLM for generating caption rewrites.
- **rewrite_prompt**: Prompt template for instructing the LLM to rewrite captions.

## Optional inputs
- **num_rewrites**: Number of caption variants to generate per image.
- **quality_filter**: Filter for removing bad rewrites.

## Outputs
- **augmented_dataset**: Image-text pairs with additional rewritten captions.
- **improved_clip**: CLIP model trained on augmented data with better performance.

## Assumptions and prerequisites
- Text diversity helps contrastive learning by providing more varied positive pairs.
- LLM rewrites preserve semantic content while varying expression.
- Caption augmentation is more efficient than collecting new images.

## Procedure
1. **Select captions for rewriting**
   Action: Choose which captions to rewrite (all or a subset).
   Why: Rewriting all captions maximizes diversity but increases cost.
   Note: See paper for details.
2. **Rewrite captions with LLM**
   Action: Prompt the LLM to rewrite each caption in a different style while preserving meaning.
   Why: Creates diverse text views of the same visual content.
   Note: See paper for details.
3. **Augment training data**
   Action: Add rewritten captions alongside or replacing original captions in training.
   Why: Increases effective text diversity in the training data.
   Note: See paper for details.
4. **Train CLIP on augmented data**
   Action: Train CLIP with standard contrastive loss on the augmented dataset.
   Why: More text diversity improves contrastive representation learning.
   Note: See paper for details.
5. **Evaluate improvements**
   Action: Compare augmented CLIP vs baseline on zero-shot benchmarks.
   Why: Validates that caption rewriting improves downstream performance.
   Note: See paper for details.

## Parameters to set
- **rewrites_per_caption** — Role: Number of rewrite variants per original caption. How to set: 1-2 rewrites per caption. Default/range: 1. Effect: More rewrites increase diversity but also cost.
- **rewrite_style** — Role: Style of caption rewriting. How to set: Preserve meaning while varying expression. Default/range: Paraphrasing. Effect: Style should maintain visual faithfulness.
- **augmentation_strategy** — Role: Whether to replace or supplement original captions. How to set: Supplement (keep both) for maximum diversity. Default/range: Supplement. Effect: Replacing may lose original information.

## Validation checks
- Rewrites should preserve the semantic content of original captions.
- CLIP trained on augmented data should outperform baseline on zero-shot tasks.
- Text embedding diversity should measurably increase.

## Failure modes
- LLM rewrites may introduce factual errors or shift meaning.
- Aggressive rewriting may create captions misaligned with the image.
- The cost of LLM rewriting at scale may be prohibitive.

## Adaptation notes for VLM training
- Caption rewriting can be applied to any image-text dataset for VLM training.
- Use Claude or GPT-4 for highest quality rewrites.
- Combine with visual augmentation for a full augmentation strategy.

## Implementation notes
- Batch LLM calls for efficiency.
- Cache rewrites for reproducibility.
- Compare original and rewritten captions to verify quality.

## Evidence from the paper
- LaCLIP improves CLIP zero-shot ImageNet accuracy by 2-4% through LLM caption rewrites.
- Language augmentation is complementary to visual augmentation methods.
- Rewriting increases effective text diversity without requiring new images.
- The approach is effective across multiple dataset scales (CC3M to LAION-400M).

## Source paper
- **Title**: LaCLIP: Improving CLIP Training with Language Rewrites
- **Year**: 2023
- **Venue**: NeurIPS
- **Paper ID**: arxiv-2305.20088v2
- **URL**: http://arxiv.org/abs/2305.20088v2
- **arXiv ID**: 2305.20088v2
