# Hard Negative Mixing for Contrastive Learning

## One-line decision
Use this skill when you want to generate harder negative examples for contrastive learning by mixing embeddings of existing negatives. Avoid it when random negatives provide sufficient contrastive signal.

## Skill metadata
- **Skill type**: hard-negative-generation
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Generate harder negative examples for contrastive learning by mixing embeddings of existing negative examples, creating synthetic hard negatives that improve the discriminative quality of learned representations.

## Problem signature
- Modality: any embedding-based contrastive learning; applicable to CLIP-style training.
- Data state: training data with contrastive pairs augmented with synthetic hard negatives.
- Scale regime: any contrastive learning setup.
- Model requirement: Any contrastive model; operates in embedding space.

## Use when
- Random negatives are too easy for your contrastive model.
- You want to improve the discriminative quality of embeddings.
- You can generate negatives in embedding space.

## Do not use when
- Random negatives provide sufficient learning signal.
- Your contrastive setup does not use negative examples.
- Generating hard negatives would be too expensive.

## Required inputs
- **positive_pairs**: Positive examples for contrastive learning.
- **negative_pool**: Pool of negative examples.
- **embedding_model**: Model for computing embeddings.

## Optional inputs
- **hardness_schedule**: Schedule for increasing negative hardness during training.

## Outputs
- **hard_negatives**: Synthetically generated hard negative examples.
- **improved_embeddings**: Better discriminative embeddings.

## Assumptions and prerequisites
- Harder negatives improve contrastive learning.
- Mixing embeddings creates meaningful hard negatives.
- Synthetic negatives complement real negatives.

## Procedure
1. **Compute embeddings**
   Action: Embed all training examples.
   Why: Embeddings are needed for mixing.
   Note: See paper for details.
2. **Identify semi-hard negatives**
   Action: Find negatives that are close but not too close to positives.
   Why: Semi-hard negatives provide the best learning signal.
   Note: See paper for details.
3. **Mix negatives**
   Action: Create synthetic hard negatives by interpolating between negative embeddings.
   Why: Mixing creates harder examples between existing negatives and positives.
   Note: See paper for details.
4. **Train with hard negatives**
   Action: Include synthetic hard negatives in contrastive training.
   Why: Harder negatives improve discriminative learning.
   Note: See paper for details.

## Parameters to set
- **mixing_ratio** — Role: How to interpolate between negatives. How to set: Mix toward the positive for harder negatives. Default/range: Task-dependent. Effect: More positive-shifted mixing creates harder negatives.
- **hard_negative_fraction** — Role: Fraction of hard negatives in each batch. How to set: 10-50%. Default/range: 20-50%. Effect: More hard negatives increase difficulty.

## Validation checks
- Retrieval metrics should improve with hard negative training.
- Hard negatives should be meaningfully harder than random ones.
- Training should remain stable with hard negatives.

## Failure modes
- Too-hard negatives may destabilize training.
- Synthetic negatives may not represent real data distributions.
- Hard negative mining increases compute cost.

## Adaptation notes for VLM training
- Apply hard negative mixing to CLIP and VLM contrastive training.
- Use for improving image-text retrieval quality.
- Combine with curriculum learning for progressive hardness.

## Implementation notes
- Implement mixing in embedding space for efficiency.
- Use a hardness schedule to avoid early training instability.
- Monitor negative difficulty throughout training.

## Evidence from the paper
- Hard negative mixing improves contrastive learning by creating harder training signals.
- Synthetic hard negatives complement real negatives effectively.
- The approach improves retrieval and classification metrics.
- Hard negative mixing is applicable to CLIP-style vision-language training.

## Source paper
- **Title**: Hard Negative Mixing for Contrastive Learning
- **Year**: 2020
- **Venue**: NeurIPS
- **Paper ID**: arxiv-2010.01028v2
- **URL**: http://arxiv.org/abs/2010.01028v2
- **arXiv ID**: 2010.01028v2
