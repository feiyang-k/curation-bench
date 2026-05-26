# AutoAugment: Learning Augmentation Strategies from Data

## One-line decision
Use this skill when you want to learn optimal data augmentation policies using reinforcement learning to search over augmentation transforms. Avoid it when RandAugment's simpler approach is sufficient.

## Skill metadata
- **Skill type**: learned-augmentation-policy
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Automatically learn optimal data augmentation policies using reinforcement learning to search over a space of augmentation transforms and their parameters.

## Problem signature
- Modality: images with learned augmentation policies.
- Data state: training images augmented with learned transform compositions.
- Scale regime: any image dataset.
- Model requirement: RL controller + target model for augmentation search.

## Use when
- You want optimal augmentation tailored to your dataset.
- You can afford the RL search computation.
- You need augmentation beyond RandAugment.

## Do not use when
- RandAugment's simpler approach works well.
- The RL search is too expensive.
- You have a custom augmentation pipeline.

## Required inputs
- **training_images**: Image dataset to learn augmentation for.
- **transform_space**: Space of augmentation transforms.
- **rl_controller**: Reinforcement learning controller for policy search.

## Optional inputs
- **proxy_task**: Small proxy for efficient search.

## Outputs
- **augmentation_policy**: Learned augmentation policy.
- **augmented_data**: Images augmented with the learned policy.

## Assumptions and prerequisites
- Optimal augmentation varies by dataset.
- RL can efficiently search the augmentation space.
- Learned policies outperform hand-designed ones.

## Procedure
1. **Define augmentation space**
   Action: Specify the set of transforms and parameter ranges.
   Why: The space defines what can be learned.
   Note: See paper for details.
2. **Search with RL**
   Action: Use RL to find optimal transform compositions.
   Why: RL efficiently searches large augmentation spaces.
   Note: See paper for details.
3. **Apply learned policy**
   Action: Augment training data with the learned policy.
   Why: Applies the optimal augmentation.
   Note: See paper for details.
4. **Train with augmentation**
   Action: Train the target model with augmented data.
   Why: Validates the learned policy.
   Note: See paper for details.

## Parameters to set
- **search_space** — Role: Space of transforms to search. How to set: Include standard transforms. Default/range: 16 transforms. Effect: Larger space may find better policies.
- **search_cost** — Role: Compute for RL search. How to set: 5000 GPU hours typical. Default/range: 5000 GPU hours. Effect: More compute may find better policies.

## Validation checks
- Learned policy should outperform hand-designed augmentation.
- The policy should transfer to similar datasets.
- Search should converge to stable policies.

## Failure modes
- RL search is very expensive.
- Learned policies may not transfer across datasets.
- The search space may miss important transforms.

## Adaptation notes for VLM training
- AutoAugment inspired RandAugment and other efficient augmentation methods.
- Apply learned augmentation to VLM image preprocessing.
- The search methodology generalizes to multimodal augmentation.

## Implementation notes
- Use the AutoAugment codebase for search.
- Consider RandAugment as a simpler alternative.
- Validate on a held-out set.

## Evidence from the paper
- AutoAugment learns augmentation policies that improve ImageNet accuracy by ~0.5%.
- Learned policies outperform hand-designed augmentation.
- The approach inspired simpler methods like RandAugment and TrivialAugment.
- AutoAugment demonstrates that augmentation can be learned from data.

## Source paper
- **Title**: AutoAugment: Learning Augmentation Strategies from Data
- **Year**: 2019
- **Venue**: CVPR
- **Paper ID**: arxiv-1805.09501v3
- **URL**: http://arxiv.org/abs/1805.09501v3
- **arXiv ID**: 1805.09501v3
