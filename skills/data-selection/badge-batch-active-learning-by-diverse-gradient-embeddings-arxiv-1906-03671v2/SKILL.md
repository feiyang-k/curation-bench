# BADGE: Batch Active Learning by Diverse Gradient Embeddings

## One-line decision
Use this skill when you want to select diverse, uncertain samples for annotation using gradient embeddings that capture both uncertainty and diversity. Avoid it when simple uncertainty sampling is sufficient or you cannot compute gradients.

## Skill metadata
- **Skill type**: gradient-based-active-learning
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Select batches of diverse, uncertain samples for annotation using gradient embeddings that jointly capture prediction uncertainty and feature space diversity.

## Problem signature
- Modality: any modality with gradient-based models.
- Data state: unlabeled pool with budget for batch annotation selection.
- Scale regime: thousands to millions of candidates.
- Model requirement: Any differentiable model for gradient computation.

## Use when
- You need batch active learning that captures both uncertainty and diversity.
- You can compute gradients for unlabeled samples.
- Random or simple uncertainty sampling is insufficient.

## Do not use when
- Simple uncertainty sampling works well.
- You cannot compute gradients.
- Your budget allows labeling all data.

## Required inputs
- **unlabeled_pool**: Pool of unlabeled candidates.
- **trained_model**: Current model for gradient computation.
- **batch_budget**: Number of samples to select per batch.

## Optional inputs
- **diversity_weight**: Weight balancing uncertainty and diversity.

## Outputs
- **selected_batch**: Batch of samples selected for annotation.
- **gradient_embeddings**: Per-sample gradient embeddings capturing uncertainty.

## Assumptions and prerequisites
- Gradient embeddings encode both uncertainty and feature information.
- Diverse uncertain samples provide maximum information gain.
- k-MEANS++ on gradient embeddings gives diverse batches.

## Procedure
1. **Compute gradient embeddings**
   Action: For each unlabeled sample, compute the gradient of the loss with respect to the last layer.
   Why: Gradients capture prediction uncertainty and feature space position.
   Note: See paper for details.
2. **Apply k-MEANS++ on gradients**
   Action: Select a diverse batch using k-MEANS++ on gradient embeddings.
   Why: k-MEANS++ ensures diversity in the selected batch.
   Note: See paper for details.
3. **Annotate selected batch**
   Action: Label the selected samples.
   Why: Annotation provides training supervision.
   Note: See paper for details.
4. **Retrain and iterate**
   Action: Update the model and repeat selection.
   Why: Model improvements change the optimal selection.
   Note: See paper for details.

## Parameters to set
- **batch_size** — Role: Number of samples per batch. How to set: Based on annotation capacity per round. Default/range: Task-dependent. Effect: Larger batches are more efficient but may miss adaptation.
- **gradient_layer** — Role: Which layer's gradients to use. How to set: Last classification layer. Default/range: Last layer. Effect: Different layers capture different uncertainty aspects.

## Validation checks
- BADGE should outperform random and uncertainty-only selection.
- Selected batches should be both uncertain and diverse.
- Training should improve efficiently with selected data.

## Failure modes
- Gradient computation adds overhead.
- k-MEANS++ may not find optimal diverse sets.
- The method assumes uncertainty is captured by gradients.

## Adaptation notes for VLM training
- Apply BADGE to VLM data selection for efficient annotation.
- Use CLIP gradients for multimodal active learning.
- Combine with other criteria for comprehensive selection.

## Implementation notes
- Compute hallucinated labels for gradient computation on unlabeled data.
- Use efficient k-MEANS++ implementations.
- Cache gradient embeddings for analysis.

## Evidence from the paper
- BADGE selects batches that are both uncertain and diverse using gradient embeddings.
- The approach outperforms random and uncertainty-based selection on multiple benchmarks.
- k-MEANS++ on gradient embeddings provides effective batch diversity.
- BADGE scales to large unlabeled pools with efficient gradient computation.

## Source paper
- **Title**: BADGE: Batch Active Learning by Diverse Gradient Embeddings
- **Year**: 2020
- **Venue**: ICLR
- **Paper ID**: arxiv-1906.03671v2
- **URL**: http://arxiv.org/abs/1906.03671v2
- **arXiv ID**: 1906.03671v2
