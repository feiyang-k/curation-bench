# Active Learning for Convolutional Neural Networks: A Core-Set Approach

## One-line decision
Use this skill when you want to select the most informative samples for annotation using coreset-based active learning in embedding space. Avoid it when you have unlimited annotation budget or random selection is sufficient.

## Skill metadata
- **Skill type**: coreset-active-learning
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Select the most informative samples for annotation using a core-set approach that maximizes coverage of the embedding space, enabling efficient training with fewer labeled examples.

## Problem signature
- Modality: images or any data with embeddings; applicable to VLM data.
- Data state: large unlabeled pool with budget for selective annotation.
- Scale regime: thousands to millions of candidate samples.
- Model requirement: Any model with embedding extraction capability.

## Use when
- You have a limited annotation budget.
- You want to maximize information gain from each annotated sample.
- You can compute embeddings for your data pool.

## Do not use when
- You have unlimited annotation budget.
- Random selection is sufficient for your needs.
- You cannot compute embeddings.

## Required inputs
- **unlabeled_pool**: Large pool of unlabeled data.
- **embedding_model**: Model for computing data embeddings.
- **annotation_budget**: Number of samples to select for annotation.

## Optional inputs
- **initial_labeled_set**: Small initially labeled set.

## Outputs
- **selected_samples**: Samples selected for annotation.
- **coreset**: Representative subset covering the embedding space.

## Assumptions and prerequisites
- Core-set selection in embedding space maximizes data coverage.
- Coverage correlates with training utility.
- Embeddings capture relevant data characteristics.

## Procedure
1. **Compute embeddings**
   Action: Embed all candidate samples using a pre-trained model.
   Why: Embeddings enable similarity computation.
   Note: See paper for details.
2. **Solve core-set problem**
   Action: Select samples that minimize the maximum distance from any point to the nearest selected point.
   Why: Core-set maximizes coverage of the data distribution.
   Note: See paper for details.
3. **Annotate selected samples**
   Action: Label the selected samples.
   Why: Annotation provides training supervision.
   Note: See paper for details.
4. **Train and iterate**
   Action: Train on annotated data and repeat selection.
   Why: Iterative selection adapts to model improvements.
   Note: See paper for details.

## Parameters to set
- **budget_per_round** — Role: Samples to select per active learning round. How to set: Based on annotation capacity. Default/range: Task-dependent. Effect: Larger budgets provide more data per round.
- **embedding_model** — Role: Model for computing embeddings. How to set: Use the best available pre-trained model. Default/range: Task-dependent. Effect: Better embeddings improve selection quality.

## Validation checks
- Core-set selection should outperform random selection.
- Coverage should increase with each selection round.
- Training performance should improve efficiently.

## Failure modes
- Embedding quality limits selection quality.
- The core-set problem is NP-hard; approximations may be suboptimal.
- Outliers may be over-selected.

## Adaptation notes for VLM training
- Apply core-set active learning to VLM data annotation.
- Use CLIP embeddings for multimodal core-set selection.
- Combine with other selection criteria for hybrid strategies.

## Implementation notes
- Use efficient k-center algorithms for core-set selection.
- Cache embeddings for repeated selection rounds.
- Track coverage metrics during selection.

## Evidence from the paper
- Core-set active learning outperforms random and uncertainty-based selection.
- The approach maximizes coverage of the data distribution.
- Embedding-based selection enables efficient annotation.
- The method scales to large unlabeled pools.

## Source paper
- **Title**: Active Learning for Convolutional Neural Networks: A Core-Set Approach
- **Year**: 2018
- **Venue**: ICLR
- **Paper ID**: arxiv-1708.00489v4
- **URL**: http://arxiv.org/abs/1708.00489v4
- **arXiv ID**: 1708.00489v4
