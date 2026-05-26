# SA-1B: Segment Anything 1 Billion Masks Dataset

## One-line decision
Use this skill when you need the largest segmentation mask dataset (1.1B masks) for training or augmenting VLM grounding data. Avoid it when existing segmentation datasets are sufficient.

## Skill metadata
- **Skill type**: billion-scale-mask-dataset
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Provide SA-1B, the largest segmentation dataset with 1.1 billion masks on 11 million images, generated through SAM's model-in-the-loop annotation process.

## Problem signature
- Modality: images with 1.1 billion automatically generated segmentation masks.
- Data state: 11M images with 1.1B masks from SAM automatic generation.
- Scale regime: 1.1 billion masks.
- Model requirement: SAM model for mask generation; any model for downstream use.

## Use when
- You need massive-scale segmentation data.
- You want to augment VLM grounding data.
- You need class-agnostic masks.

## Do not use when
- Existing segmentation data is sufficient.
- You need class-labeled masks.
- You cannot process billion-scale data.

## Required inputs
- **sa1b_data**: 1.1B masks on 11M images.
- **mask_format**: RLE-encoded segmentation masks.
- **image_access**: Access to the 11M source images.

## Optional inputs
- **class_labels**: Labels for masks (from other annotation).

## Outputs
- **sa1b_masks**: 1.1 billion segmentation masks.
- **grounding_data**: Masks usable for VLM grounding training.

## Assumptions and prerequisites
- 1.1B masks provide comprehensive segmentation coverage.
- Class-agnostic masks are useful for grounding.
- SAM-generated masks are high quality.

## Procedure
1. **Access SA-1B**
   Action: Download the SA-1B dataset.
   Why: Provides 1.1B masks.
   Note: See paper for details.
2. **Use for grounding**
   Action: Combine masks with text descriptions for VLM grounding.
   Why: Masks enable pixel-level grounding.
   Note: See paper for details.
3. **Augment training data**
   Action: Use SA-1B masks to augment VLM training.
   Why: Massive scale improves grounding quality.
   Note: See paper for details.

## Parameters to set
- **num_masks** — Role: Total masks available. How to set: Use all 1.1B or sample. Default/range: 1.1B. Effect: More masks improve coverage.
- **mask_quality** — Role: Quality of SAM-generated masks. How to set: Filter by predicted IoU. Default/range: High quality. Effect: Quality filtering improves data.

## Validation checks
- Masks should accurately segment objects.
- Using SA-1B should improve grounding quality.
- The data should be processable at scale.

## Failure modes
- Class-agnostic masks lack semantic labels.
- 1.1B masks require significant storage.
- Some masks may be over-segmented.

## Adaptation notes for VLM training
- SA-1B is the primary source of large-scale mask data for VLMs.
- Combine with text descriptions for grounded VLM training.
- Use for training VLM pixel-level understanding.

## Implementation notes
- Use efficient RLE decoding.
- Sample masks for manageable training sets.
- Combine with text annotations from other sources.

## Evidence from the paper
- SA-1B provides 1.1 billion segmentation masks on 11 million images.
- The dataset is 400x larger than any previous segmentation dataset.
- SAM-generated masks are high quality despite automatic generation.
- SA-1B enables massive-scale grounding data for VLMs.

## Source paper
- **Title**: SA-1B: Segment Anything 1 Billion Masks Dataset
- **Year**: 2023
- **Venue**: ICCV
- **Paper ID**: arxiv-sa1b-2023
- **URL**: http://arxiv.org/abs/2304.02643
- **arXiv ID**: N/A
