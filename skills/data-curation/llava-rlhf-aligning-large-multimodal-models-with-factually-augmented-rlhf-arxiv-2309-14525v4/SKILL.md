# LLaVA-RLHF: Aligning Large Multimodal Models with Factually Augmented RLHF

## One-line decision
Use this skill when you want to align a VLM using RLHF with factually augmented reward signals that penalize hallucination. Avoid it when you do not need RLHF-based alignment for your VLM.

## Skill metadata
- **Skill type**: factually-augmented-rlhf
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Align a VLM using RLHF with factually augmented reward signals that combine human preference with factual accuracy checks to reduce hallucination while improving helpfulness.

## Problem signature
- Modality: VLM outputs with preference and factual accuracy annotations.
- Data state: human preference data augmented with factual accuracy labels.
- Scale regime: 10K preference pairs with factual augmentation.
- Model requirement: LLaVA + reward model + PPO for RLHF.

## Use when
- You want RLHF alignment for a VLM.
- You need to balance helpfulness with factual accuracy.
- You can collect preference data with factual annotations.

## Do not use when
- Standard instruction tuning is sufficient.
- You cannot collect preference data.
- Factual accuracy is not a concern.

## Required inputs
- **preference_data**: Human preference pairs for VLM outputs.
- **factual_labels**: Factual accuracy annotations augmenting preferences.
- **reward_model**: Reward model trained on augmented preferences.

## Optional inputs
- **ppo_config**: PPO hyperparameters for RLHF.

## Outputs
- **augmented_preferences**: 10K preference pairs with factual augmentation.
- **aligned_vlm**: VLM aligned for both helpfulness and factual accuracy.

## Assumptions and prerequisites
- Factual augmentation of preferences improves alignment quality.
- RLHF can balance helpfulness and accuracy.
- PPO effectively optimizes the augmented reward.

## Procedure
1. **Collect human preferences**
   Action: Gather preference pairs between VLM outputs for the same input.
   Why: Preferences provide the training signal for RLHF.
   Note: See paper for details.
2. **Augment with factual accuracy**
   Action: Add factual accuracy labels to preference data.
   Why: Factual augmentation penalizes hallucination.
   Note: See paper for details.
3. **Train reward model**
   Action: Train on factually augmented preference data.
   Why: The reward model learns to value accuracy alongside helpfulness.
   Note: See paper for details.
4. **Run PPO**
   Action: Fine-tune the VLM using PPO with the augmented reward.
   Why: PPO optimizes the VLM for the augmented reward signal.
   Note: See paper for details.

## Parameters to set
- **preference_pairs** — Role: Number of preference pairs. How to set: 10K for effective alignment. Default/range: 10K. Effect: More pairs improve reward model quality.
- **factual_weight** — Role: Weight of factual accuracy in the reward. How to set: Balance with helpfulness. Default/range: Balanced. Effect: Higher weight reduces hallucination.

## Validation checks
- Hallucination should decrease after RLHF.
- Helpfulness should be maintained or improved.
- The reward model should correlate with human judgment.

## Failure modes
- RLHF may over-optimize the reward model.
- Factual accuracy annotation is subjective.
- PPO training can be unstable.

## Adaptation notes for VLM training
- Factually augmented RLHF applies to any VLM alignment.
- Combine with DPO for simpler optimization.
- Extend factual augmentation to more quality dimensions.

## Implementation notes
- Use Fact-Augmented RLHF for VLM alignment.
- Monitor both helpfulness and accuracy during training.
- Compare against standard RLHF baselines.

## Evidence from the paper
- LLaVA-RLHF improves both helpfulness and factual accuracy through augmented preferences.
- Factual augmentation of RLHF reduces hallucination more than standard RLHF.
- 10K augmented preference pairs provide effective alignment signal.
- The approach balances helpfulness with trustworthiness.

## Source paper
- **Title**: LLaVA-RLHF: Aligning Large Multimodal Models with Factually Augmented RLHF
- **Year**: 2023
- **Venue**: arXiv
- **Paper ID**: arxiv-2309.14525v4
- **URL**: http://arxiv.org/abs/2309.14525v4
- **arXiv ID**: 2309.14525v4
