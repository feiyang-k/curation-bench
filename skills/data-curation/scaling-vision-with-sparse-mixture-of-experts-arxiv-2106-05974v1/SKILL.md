# Scaling Vision with Sparse Mixture of Experts

## One-line decision
Use this skill when you want to scale vision models efficiently using sparse Mixture-of-Experts for handling more training data per compute. Avoid it when dense models are sufficient for your scale.

## Skill metadata
- **Skill type**: sparse-moe-vision-training
- **Paper kind**: operational-method
- **Actionability**: medium
- **Evidence quality**: full_paper

## Goal
Scale vision models efficiently using sparse Mixture-of-Experts, where only a subset of parameters is active per image, enabling processing of more data per unit of compute.

## Problem signature
- Modality: images processed by sparse MoE vision models.
- Data state: large-scale image data processed with sparse computation.
- Scale regime: JFT-300M and larger datasets.
- Model requirement: ViT with sparse MoE layers.

## Use when
- You want to scale vision models efficiently.
- You need more capacity without proportional compute increase.
- MoE architecture is feasible for your setup.

## Do not use when
- Dense models are sufficient.
- MoE adds too much complexity.
- You cannot handle MoE routing challenges.

## Required inputs
- **large_image_data**: Large-scale image data for training.
- **moe_architecture**: ViT with sparse MoE layers.
- **routing_mechanism**: Router for selecting expert subsets.

## Optional inputs
- **expert_balancing**: Loss for balancing expert usage.

## Outputs
- **moe_vision_model**: Sparse MoE vision model.
- **efficient_features**: Visual features from efficient sparse computation.

## Assumptions and prerequisites
- Sparse computation enables larger models per compute unit.
- Expert specialization improves efficiency.
- MoE scaling follows favorable laws.

## Procedure
1. **Add MoE layers to ViT**
   Action: Replace FFN layers with MoE layers.
   Why: MoE enables sparse scaling.
   Note: See paper for details.
2. **Train with routing**
   Action: Train with expert routing and load balancing.
   Why: Routing selects relevant experts per input.
   Note: See paper for details.
3. **Scale to large data**
   Action: Train on JFT-300M or larger.
   Why: MoE benefits from large-scale training.
   Note: See paper for details.
4. **Evaluate efficiency**
   Action: Compare to dense models at equal compute.
   Why: Validates MoE efficiency advantage.
   Note: See paper for details.

## Parameters to set
- **num_experts** — Role: Number of experts per MoE layer. How to set: 32-128. Default/range: 32. Effect: More experts provide more capacity.
- **top_k** — Role: Experts selected per input. How to set: 1-2. Default/range: 2. Effect: More selected experts increase compute.

## Validation checks
- MoE should outperform dense models at equal compute.
- Expert usage should be balanced.
- Scaling should follow favorable laws.

## Failure modes
- Expert routing may be suboptimal.
- Load imbalance across experts.
- MoE adds engineering complexity.

## Adaptation notes for VLM training
- MoE vision models provide efficient encoding for VLMs.
- Sparse computation enables larger models on the same hardware.
- MoE is a direction for scaling VLM vision components.

## Implementation notes
- Implement efficient expert routing.
- Balance expert loads during training.
- Compare to dense baselines at equal FLOPs.

## Evidence from the paper
- Sparse MoE enables efficient scaling of vision models.
- V-MoE processes more data per compute unit than dense models.
- Expert specialization improves efficiency.
- MoE scaling is favorable for large-scale vision.

## Source paper
- **Title**: Scaling Vision with Sparse Mixture of Experts
- **Year**: 2022
- **Venue**: NeurIPS
- **Paper ID**: arxiv-2106.05974v1
- **URL**: http://arxiv.org/abs/2106.05974v1
- **arXiv ID**: 2106.05974v1
