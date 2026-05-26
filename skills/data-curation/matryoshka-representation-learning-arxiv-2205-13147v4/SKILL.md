# Matryoshka Representation Learning

## One-line decision
Use this skill when you want to train embeddings that work at multiple dimensionalities, enabling flexible compute-quality tradeoffs at retrieval time. Avoid it when you only need fixed-dimension embeddings.

## Skill metadata
- **Skill type**: flexible-embedding-training
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Train embeddings that are effective at multiple dimensionalities simultaneously, enabling flexible compute-quality tradeoffs at deployment without retraining.

## Problem signature
- Modality: any embedding-based data; applicable to VLM embeddings.
- Data state: standard training data with multi-resolution embedding training.
- Scale regime: any dataset with embedding training.
- Model requirement: Any embedding model with multi-resolution training.

## Use when
- You want embeddings working at multiple dimensions.
- You need flexible compute-quality tradeoffs.
- You want deployment flexibility without retraining.

## Do not use when
- Fixed-dimension embeddings are sufficient.
- You do not need deployment flexibility.
- Compute is not a constraint.

## Required inputs
- **training_data**: Standard training data for embedding learning.
- **multi_res_loss**: Loss computed at multiple embedding dimensions.
- **embedding_model**: Model producing embeddings.

## Optional inputs
- **dimension_schedule**: Schedule for which dimensions to train at.

## Outputs
- **matryoshka_embeddings**: Embeddings effective at multiple dimensionalities.
- **flexible_retrieval**: Retrieval system with flexible compute-quality tradeoff.

## Assumptions and prerequisites
- Embeddings can be effective at multiple truncated dimensions.
- Multi-resolution training does not significantly hurt full-dimension quality.
- Flexible dimensionality enables deployment optimization.

## Procedure
1. **Design multi-resolution loss**
   Action: Compute loss at multiple embedding dimension truncations.
   Why: Multi-resolution training develops nested representations.
   Note: See paper for details.
2. **Train with Matryoshka loss**
   Action: Train the model with losses at d=8, 16, 32, ..., full.
   Why: Develops effective embeddings at all truncation levels.
   Note: See paper for details.
3. **Deploy at optimal dimension**
   Action: Choose embedding dimension based on compute budget at deployment.
   Why: Flexible dimensionality optimizes compute-quality tradeoff.
   Note: See paper for details.

## Parameters to set
- **dimension_set** — Role: Set of dimensions to train at. How to set: Powers of 2 from 8 to full. Default/range: [8, 16, 32, ..., 2048]. Effect: More dimensions provide finer granularity.
- **loss_weights** — Role: Weight of each dimension's loss. How to set: Equal or increasing with dimension. Default/range: Equal. Effect: Affects quality distribution across dimensions.

## Validation checks
- Retrieval should be effective at all trained dimensions.
- Full-dimension performance should not significantly degrade.
- Smaller dimensions should approach full-dimension quality.

## Failure modes
- Very low dimensions may lose too much information.
- Multi-resolution training may slightly hurt full dimension.
- Not all tasks benefit from flexible dimensionality.

## Adaptation notes for VLM training
- Apply Matryoshka training to CLIP/VLM embeddings for flexible retrieval.
- Enable compute-quality tradeoffs in VLM data processing pipelines.
- Flexible embeddings improve scalability of similarity search.

## Implementation notes
- Implement multi-resolution loss efficiently.
- Test at multiple truncation levels.
- Compare to fixed-dimension baselines.

## Evidence from the paper
- Matryoshka embeddings work effectively at multiple dimensionalities.
- Multi-resolution training has minimal impact on full-dimension quality.
- The approach enables 14x speedup with minimal quality loss.
- Flexible dimensionality is valuable for deployment optimization.

## Source paper
- **Title**: Matryoshka Representation Learning
- **Year**: 2022
- **Venue**: NeurIPS
- **Paper ID**: arxiv-2205.13147v4
- **URL**: http://arxiv.org/abs/2205.13147v4
- **arXiv ID**: 2205.13147v4
