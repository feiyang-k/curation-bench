# Monkey: Image Resolution and Text Label Are Important Things for Large Multi-Modal Models

## One-line decision
Use this skill when you want to create instruction data for high-resolution VLMs that can handle documents, dense text, and detailed images. Avoid it when you only work with low-resolution images or do not need document understanding.

## Skill metadata
- **Skill type**: high-resolution-instruction-data
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Create instruction tuning data specifically designed for high-resolution VLM training, emphasizing document understanding, dense text reading, and detailed image descriptions at resolutions up to 1344x896.

## Problem signature
- Modality: high-resolution images with instruction data emphasizing text reading and detail.
- Data state: instruction data curated for high-resolution input including documents, charts, and text-rich images.
- Scale regime: hundreds of thousands of instruction samples.
- Model requirement: VLM with high-resolution input support (sliding window on CLIP).

## Use when
- You are training a VLM that handles high-resolution input.
- You need instruction data for document and text-rich image understanding.
- You want to improve OCR and detail recognition in your VLM.

## Do not use when
- Your VLM only supports low-resolution input (224x224).
- Document understanding is not a target capability.
- You do not need text reading ability.

## Required inputs
- **high_res_images**: High-resolution images including documents, charts, and detailed scenes.
- **text_rich_sources**: Sources with visible text (documents, signs, labels, etc.).
- **instruction_templates**: Templates for generating text-reading and detail-recognition instructions.

## Optional inputs
- **ocr_annotations**: OCR output for text-rich images.

## Outputs
- **high_res_instruction_data**: Instruction data for high-resolution VLM training.
- **monkey_model**: VLM trained with high-resolution input support.

## Assumptions and prerequisites
- High-resolution input is critical for document and text understanding.
- Instruction data should match the resolution capabilities of the model.
- Text-rich images require specific instruction data types.

## Procedure
1. **Curate high-resolution images**
   Action: Collect images that benefit from high resolution (documents, charts, detailed scenes).
   Why: These images lose critical information at low resolution.
   Note: See paper for details.
2. **Generate text-reading instructions**
   Action: Create QA pairs about text visible in high-resolution images.
   Why: Exercises the model's text reading capability.
   Note: See paper for details.
3. **Generate detail-recognition instructions**
   Action: Create instructions about fine-grained details visible only at high resolution.
   Why: Tests the model's ability to use high-resolution input.
   Note: See paper for details.
4. **Train with sliding window**
   Action: Use a sliding window approach on CLIP to handle high-resolution input.
   Why: Enables high-resolution processing without architectural changes.
   Note: See paper for details.

## Parameters to set
- **max_resolution** — Role: Maximum input resolution. How to set: 1344x896 for detailed understanding. Default/range: 1344x896. Effect: Higher resolution enables finer detail recognition.
- **sliding_window_size** — Role: Size of each window on the high-res image. How to set: Match CLIP's native resolution per window. Default/range: 448x448. Effect: Window size determines detail granularity.

## Validation checks
- Text reading accuracy should improve with higher resolution.
- Document understanding benchmarks should show clear improvements.
- The model should handle varied aspect ratios correctly.

## Failure modes
- High resolution increases compute and memory requirements.
- Sliding window may fragment objects or text across windows.
- Training data may not cover all high-resolution scenarios.

## Adaptation notes for VLM training
- High-resolution data curation applies to any VLM with dynamic resolution.
- Combine with standard-resolution instruction data for balanced training.
- The sliding window approach has been adopted by many subsequent VLMs.

## Implementation notes
- Implement efficient sliding window encoding.
- Track per-window attention to verify usage.
- Monitor resolution-specific performance metrics.

## Evidence from the paper
- Monkey demonstrates that high-resolution input significantly improves document and text understanding.
- Instruction data curated for high-resolution images improves OCR-dependent benchmarks.
- The sliding window approach enables high-resolution processing without architecture changes.
- Monkey achieves strong performance on TextVQA, DocVQA, and ChartQA.

## Source paper
- **Title**: Monkey: Image Resolution and Text Label Are Important Things for Large Multi-Modal Models
- **Year**: 2023
- **Venue**: CVPR
- **Paper ID**: arxiv-2311.06607v3
- **URL**: http://arxiv.org/abs/2311.06607v3
- **arXiv ID**: 2311.06607v3
