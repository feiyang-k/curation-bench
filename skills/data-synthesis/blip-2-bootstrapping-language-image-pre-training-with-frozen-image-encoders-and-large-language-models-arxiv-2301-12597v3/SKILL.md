# BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models

## One-line decision
Use this skill when you need to bridge a frozen image encoder to a frozen LLM for VLM training with limited paired data. Avoid it when you can afford end-to-end training of the full model or have abundant paired data.

## Skill metadata
- **Skill type**: bridge-pretraining
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Bridge frozen pre-trained image encoders and frozen large language models using a lightweight Querying Transformer (Q-Former) to enable efficient vision-language pretraining with significantly less training data.

## Problem signature
- Modality: image-text pairs for bridge pre-training between frozen vision and language models.
- Data state: standard image-text datasets (COCO, CC3M, CC12M, SBU, LAION-400M subset) used to train only the Q-Former bridge.
- Scale regime: 129M images total; significantly less than end-to-end approaches.
- Model requirement: Frozen image encoder (ViT-g) + lightweight Q-Former + frozen LLM (OPT or FlanT5).

## Use when
- You want to leverage existing frozen image encoders and LLMs without end-to-end training.
- You have limited paired image-text data but strong pre-trained unimodal models.
- You need compute-efficient VLM training.

## Do not use when
- You can afford full end-to-end training with abundant data.
- You need the image encoder to adapt to your specific domain.
- You require pixel-level or region-level understanding.

## Required inputs
- **frozen_image_encoder**: Pre-trained vision transformer (e.g., ViT-g from EVA-CLIP).
- **frozen_llm**: Pre-trained large language model (e.g., OPT-2.7B or FlanT5-XXL).
- **image_text_pairs**: Standard image-text pairs for Q-Former pre-training.

## Optional inputs
- **instruction_data**: Optional instruction-following data for Q-Former fine-tuning.
- **additional_text_data**: Extra text data for the LLM component.

## Outputs
- **q_former_bridge**: Trained Q-Former that extracts visual tokens from the frozen image encoder for the frozen LLM.
- **blip2_model**: Complete VLM capable of image captioning, VQA, and visual reasoning.

## Assumptions and prerequisites
- Frozen pre-trained unimodal models contain sufficient knowledge for vision-language tasks.
- A lightweight bridge module can effectively translate between vision and language representations.
- Two-stage pre-training (vision-language representation learning, then vision-to-language generative learning) is effective.

## Procedure
1. **Stage 1: Vision-language representation learning**
   Action: Pre-train Q-Former with frozen image encoder using ITC, ITM, and ITG losses.
   Why: Learns to extract visual features most relevant to text.
   Note: Uses learnable query tokens to interact with frozen image features.
2. **Stage 2: Vision-to-language generative learning**
   Action: Connect Q-Former output to frozen LLM via a linear projection and train on image-grounded text generation.
   Why: Enables the LLM to generate text conditioned on visual information.
   Note: Only the projection layer and Q-Former are trained.
3. **Instruction tuning**
   Action: Optionally fine-tune on instruction-following datasets for better zero-shot generalization.
   Why: Instruction tuning improves the model's ability to follow diverse user queries.
   Note: See paper for details.
4. **Evaluate on VL benchmarks**
   Action: Test on VQAv2, image captioning (COCO), and other VL benchmarks.
   Why: Measures the quality of the bridge between vision and language.
   Note: See paper for details.

## Parameters to set
- **num_query_tokens** — Role: Number of learnable queries in Q-Former. How to set: 32 queries works well. Default/range: 32. Effect: More queries capture more visual detail but increase compute.
- **q_former_layers** — Role: Depth of Q-Former transformer. How to set: Use BERT-base architecture. Default/range: 12 layers. Effect: Deeper Q-Former can model more complex vision-language interactions.
- **training_epochs_stage1** — Role: Pre-training duration for stage 1. How to set: Train until ITC/ITM/ITG losses plateau. Default/range: Not specified. Effect: Longer training improves representation quality.

## Validation checks
- Q-Former should extract visual tokens that are informative for the LLM.
- Image captioning quality should approach end-to-end trained models.
- VQA accuracy should be competitive with models trained on much more data.

## Failure modes
- The frozen image encoder may lack features needed for specific domains.
- Q-Former may become a bottleneck if the number of query tokens is too small.
- Frozen LLM may not generalize well to visual reasoning without fine-tuning.

## Adaptation notes for VLM training
- The Q-Former bridge pattern is widely adopted in subsequent VLMs (MiniGPT-4, InstructBLIP, etc.).
- Consider unfreezing the image encoder for domain-specific applications.
- The two-stage pretraining strategy reduces data requirements for VLM construction.

## Implementation notes
- Use gradient checkpointing for the Q-Former to reduce memory usage.
- The Q-Former can be pre-trained on a single 8-GPU node due to frozen components.
- Cache image encoder outputs to accelerate Q-Former training.

## Evidence from the paper
- BLIP-2 achieves state-of-the-art performance on various vision-language tasks with significantly fewer trainable parameters.
- The model uses 54x fewer trainable parameters than Flamingo80B while achieving better zero-shot VQAv2 performance.
- Two-stage pre-training with a Q-Former bridge effectively connects frozen image encoders to frozen LLMs.
- BLIP-2 with FlanT5-XXL achieves 65.0% on VQAv2 in a zero-shot setting.

## Source paper
- **Title**: BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models
- **Year**: 2023
- **Venue**: ICML
- **Paper ID**: arxiv-2301.12597v3
- **URL**: http://arxiv.org/abs/2301.12597v3
- **arXiv ID**: 2301.12597v3
