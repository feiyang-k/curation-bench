# RLHF-V: Towards Trustworthy MLLMs via Behavior Alignment from Fine-grained Correctional Human Feedback

## One-line decision
Use this skill when you want to collect fine-grained human feedback on VLM outputs to reduce hallucination through RLHF. Avoid it when you do not need RLHF or hallucination is not a concern.

## Skill metadata
- **Skill type**: fine-grained-human-feedback
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Collect fine-grained correctional human feedback on VLM outputs at the segment level to train reward models that reduce hallucination through RLHF.

## Problem signature
- Modality: VLM outputs with segment-level human correctional feedback.
- Data state: VLM outputs annotated with fine-grained human corrections.
- Scale regime: 1.4K fine-grained feedback samples.
- Model requirement: VLM + reward model for RLHF training.

## Use when
- You want to reduce VLM hallucination through RLHF.
- You can collect fine-grained human feedback.
- You need trustworthy VLM outputs.

## Do not use when
- Hallucination is not a concern.
- You cannot collect human feedback.
- Simpler correction methods are sufficient.

## Required inputs
- **vlm_outputs**: VLM-generated descriptions of images.
- **human_annotators**: Annotators providing segment-level corrections.
- **reward_model**: Model trained on correctional feedback.

## Optional inputs
- **preference_data**: Traditional preference pairs for comparison.

## Outputs
- **feedback_data**: 1.4K segment-level correctional feedback samples.
- **aligned_vlm**: VLM aligned through RLHF to reduce hallucination.

## Assumptions and prerequisites
- Fine-grained segment-level feedback is more effective than holistic preferences.
- Human corrections identify specific hallucination patterns.
- RLHF can effectively reduce VLM hallucination.

## Procedure
1. **Generate VLM outputs**
   Action: Have the VLM describe images in detail.
   Why: Generates outputs for human evaluation.
   Note: See paper for details.
2. **Collect segment-level feedback**
   Action: Annotators mark hallucinated segments and provide corrections.
   Why: Fine-grained feedback identifies specific errors.
   Note: See paper for details.
3. **Train reward model**
   Action: Train a reward model on the correctional feedback.
   Why: The reward model scores outputs for hallucination.
   Note: See paper for details.
4. **Apply RLHF**
   Action: Fine-tune the VLM using the reward model.
   Why: RLHF aligns the VLM to reduce hallucination.
   Note: See paper for details.

## Parameters to set
- **feedback_granularity** — Role: Level of feedback detail. How to set: Segment-level for fine-grained correction. Default/range: Segment-level. Effect: Finer granularity provides better learning signal.
- **feedback_samples** — Role: Number of feedback samples. How to set: 1.4K for initial alignment. Default/range: 1.4K. Effect: More samples improve alignment quality.

## Validation checks
- Hallucination rate should decrease after RLHF.
- The model should maintain factual accuracy.
- POPE and similar hallucination benchmarks should improve.

## Failure modes
- Human feedback collection is expensive.
- Fine-grained annotation requires careful training.
- RLHF may over-optimize for the reward model.

## Adaptation notes for VLM training
- Fine-grained feedback is more effective than holistic preferences for VLMs.
- Extend to other VLM quality dimensions beyond hallucination.
- Combine with DPO for more efficient alignment.

## Implementation notes
- Train annotators on consistent feedback criteria.
- Use segment-level markup tools for efficient annotation.
- Monitor hallucination metrics during RLHF.

## Evidence from the paper
- RLHF-V reduces VLM hallucination through fine-grained correctional feedback.
- Segment-level feedback is more effective than holistic preference data.
- 1.4K fine-grained samples significantly improve trustworthiness.
- The approach outperforms standard RLHF on hallucination reduction.

## Source paper
- **Title**: RLHF-V: Towards Trustworthy MLLMs via Behavior Alignment from Fine-grained Correctional Human Feedback
- **Year**: 2023
- **Venue**: CVPR
- **Paper ID**: arxiv-2312.00849v2
- **URL**: http://arxiv.org/abs/2312.00849v2
- **arXiv ID**: 2312.00849v2
