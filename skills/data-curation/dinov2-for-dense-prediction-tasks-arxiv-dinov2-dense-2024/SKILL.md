# DINOv2 for Dense Prediction Tasks

## One-line decision
Use this skill when you want to use DINOv2 self-supervised features for dense prediction tasks like segmentation and depth in VLM pipelines. Avoid it when CLIP features are sufficient for your VLM.

## Skill metadata
- **Skill type**: dense-prediction-features
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Leverage DINOv2's self-supervised features for dense prediction tasks (segmentation, depth estimation) in VLM pipelines, demonstrating strong performance without supervised training.

## Problem signature
- Modality: images with DINOv2 features for dense prediction.
- Data state: images processed with DINOv2 features for dense tasks.
- Scale regime: any image dataset.
- Model requirement: DINOv2 ViT encoder with linear probing or decoding.

## Use when
- You need dense features for segmentation or depth.
- You want self-supervised features for dense prediction.
- You want to complement CLIP features in your VLM.

## Do not use when
- CLIP features are sufficient.
- You need task-specific supervised features.
- Dense prediction is not needed.

## Required inputs
- **images**: Images for feature extraction.
- **dinov2_model**: Pre-trained DINOv2 ViT.
- **dense_decoder**: Decoder for dense prediction (segmentation, depth).

## Optional inputs
- **supervised_labels**: Supervised labels for fine-tuning.

## Outputs
- **dense_features**: DINOv2 features for dense prediction.
- **dense_predictions**: Segmentation, depth, or other dense outputs.

## Assumptions and prerequisites
- DINOv2 features capture dense visual information.
- Self-supervised features are competitive with supervised for dense tasks.
- DINOv2 complements CLIP for VLM pipelines.

## Procedure
1. **Extract DINOv2 features**
   Action: Process images through DINOv2 to get dense features.
   Why: DINOv2 provides rich dense features.
   Note: See paper for details.
2. **Add dense decoder**
   Action: Attach a decoder for the target dense task.
   Why: Decoder converts features to predictions.
   Note: See paper for details.
3. **Train decoder**
   Action: Train the decoder (frozen DINOv2) on task data.
   Why: Adapts features to the specific task.
   Note: See paper for details.
4. **Evaluate dense prediction**
   Action: Test on segmentation, depth, or other dense benchmarks.
   Why: Validates dense feature quality.
   Note: See paper for details.

## Parameters to set
- **encoder_size** — Role: DINOv2 model size. How to set: ViT-L or ViT-G for best quality. Default/range: ViT-L. Effect: Larger models provide richer features.
- **decoder_type** — Role: Dense prediction decoder. How to set: Linear or DPT-style. Default/range: Linear. Effect: More complex decoders improve predictions.

## Validation checks
- Dense features should produce strong segmentation/depth.
- Self-supervised should approach supervised quality.
- Features should complement CLIP in VLM pipelines.

## Failure modes
- DINOv2 features may lack semantic labels.
- Dense prediction quality depends on decoder quality.
- Self-supervised features may miss some categories.

## Adaptation notes for VLM training
- DINOv2 dense features complement CLIP in multi-encoder VLMs.
- Use for spatial understanding in VLM grounding pipelines.
- Dense features enable pixel-level VLM capabilities.

## Implementation notes
- Use frozen DINOv2 with trainable decoder.
- Compare to CLIP features on dense tasks.
- Evaluate on standard dense prediction benchmarks.

## Evidence from the paper
- DINOv2 provides strong self-supervised features for dense prediction.
- Linear probing on DINOv2 features achieves competitive segmentation.
- Self-supervised features complement CLIP for comprehensive visual understanding.
- DINOv2 is used alongside CLIP in multi-encoder VLMs.

## Source paper
- **Title**: DINOv2 for Dense Prediction Tasks
- **Year**: 2024
- **Venue**: arXiv
- **Paper ID**: arxiv-dinov2-dense-2024
- **URL**: http://arxiv.org/abs/2304.07193
- **arXiv ID**: N/A
