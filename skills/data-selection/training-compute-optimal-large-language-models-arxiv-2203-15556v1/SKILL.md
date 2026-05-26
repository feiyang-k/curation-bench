# Training Compute-Optimal Large Language Models

## One-line decision
Use this skill when you want to know the compute-optimal ratio of model size to training data based on Chinchilla scaling laws. Avoid it when you are not making model/data scaling decisions.

## Skill metadata
- **Skill type**: compute-optimal-scaling
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Determine compute-optimal training configurations by showing that model size and training data should scale equally — the Chinchilla scaling law that shifted the field toward using more data.

## Problem signature
- Modality: text data scaling analysis; principles apply to multimodal.
- Data state: scaling studies varying model size and data size.
- Scale regime: up to 500B tokens and 70B parameters.
- Model requirement: Transformer LLMs at various scales.

## Use when
- You are deciding model size vs data size trade-offs.
- You want compute-optimal training configurations.
- You need to know if you have enough training data.

## Do not use when
- You have fixed model and data sizes.
- Your compute budget is unlimited.
- Scaling decisions are already made.

## Required inputs
- **scaling_experiments**: Training runs at multiple model and data sizes.
- **compute_budget**: Fixed compute budgets for optimization.
- **evaluation_metrics**: Performance metrics for scaling comparison.

## Optional inputs
- **data_quality**: Quality-adjusted data accounting.

## Outputs
- **chinchilla_law**: Compute-optimal model/data scaling relationship.
- **chinchilla_model**: 70B model trained compute-optimally on 1.4T tokens.

## Assumptions and prerequisites
- Model and data should scale equally for compute optimality.
- Previous models were under-trained (too large for their data).
- The scaling law holds across model scales.

## Procedure
1. **Vary model and data sizes**
   Action: Train models at many model/data combinations for fixed compute.
   Why: Maps the performance landscape.
   Note: See paper for details.
2. **Find compute-optimal frontier**
   Action: Identify the best model/data ratio for each compute level.
   Why: Determines compute-optimal configurations.
   Note: See paper for details.
3. **Train Chinchilla**
   Action: Train a 70B model on 1.4T tokens at the compute-optimal point.
   Why: Validates the scaling law.
   Note: See paper for details.
4. **Compare to existing models**
   Action: Show Chinchilla outperforms larger but under-trained models.
   Why: Demonstrates the value of compute-optimal training.
   Note: See paper for details.

## Parameters to set
- **optimal_ratio** — Role: Tokens per parameter at compute optimality. How to set: ~20 tokens per parameter. Default/range: 20:1. Effect: More tokens per parameter than previous practice.
- **total_compute** — Role: Fixed compute budget. How to set: Measured in FLOPs. Default/range: Variable. Effect: Budget determines achievable scale.

## Validation checks
- Chinchilla should outperform larger models trained on less data.
- The scaling law should predict performance accurately.
- Compute-optimal training should be more efficient.

## Failure modes
- The 20:1 ratio may not hold for all architectures.
- Data quality effects are not captured.
- Very large scales may deviate from the law.

## Adaptation notes for VLM training
- Chinchilla scaling informs VLM data collection decisions.
- Apply the 20:1 ratio to VLM pretraining data requirements.
- Consider data quality as well as quantity for optimal training.

## Implementation notes
- Use the Chinchilla ratio as a starting point for data planning.
- Adjust for data quality and repetition effects.
- Monitor training efficiency vs the compute-optimal frontier.

## Evidence from the paper
- Chinchilla shows that model and data should scale equally.
- Previous models were undertrained: too large for their data.
- Chinchilla 70B outperforms Gopher 280B while using less compute.
- The scaling law has reshaped how the field approaches data collection.

## Source paper
- **Title**: Training Compute-Optimal Large Language Models
- **Year**: 2022
- **Venue**: NeurIPS
- **Paper ID**: arxiv-2203.15556v1
- **URL**: http://arxiv.org/abs/2203.15556v1
- **arXiv ID**: 2203.15556v1
