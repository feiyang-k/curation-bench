# GLIP: Grounded Language-Image Pre-training

## One-line decision
Use this skill when you want to unify object detection and phrase grounding training data for a model that detects objects from language descriptions. Avoid it when you do not need language-guided detection or grounding.

## Skill metadata
- **Skill type**: grounded-pretraining-data
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Unify object detection and phrase grounding by reformulating detection as phrase grounding, enabling training on both detection datasets (with category names as phrases) and grounding datasets (with natural language descriptions).

## Problem signature
- Modality: images with grounded text descriptions (detection categories reformulated as phrases).
- Data state: detection and grounding datasets unified into a single grounded language-image format.
- Scale regime: millions of annotated images from detection + grounding datasets.
- Model requirement: Detection transformer with language-aware fusion.

## Use when
- You want to unify detection and grounding training.
- You need language-guided object detection.
- You have both detection and grounding datasets.

## Do not use when
- Standard closed-set detection is sufficient.
- You do not need language-guided detection.
- You only have one type of annotation (detection or grounding).

## Required inputs
- **detection_datasets**: Object detection datasets with bounding boxes (Objects365, COCO, etc.).
- **grounding_datasets**: Phrase grounding datasets (Flickr30K Entities, etc.).
- **text_encoder**: Language encoder for processing text queries.

## Optional inputs
- **web_caption_data**: Web image-caption pairs for additional grounding signal.

## Outputs
- **glip_model**: Unified detection-grounding model.
- **unified_data_format**: Detection and grounding data in a single format.

## Assumptions and prerequisites
- Detection and grounding are the same task at different language levels.
- Category names can be treated as text phrases for unified training.
- Unifying data increases effective training set size.

## Procedure
1. **Reformulate detection as grounding**
   Action: Convert detection category names into text phrases.
   Why: Unifies the detection and grounding tasks.
   Note: See paper for details.
2. **Merge detection and grounding data**
   Action: Combine reformulated detection data with grounding data.
   Why: Larger unified dataset improves both capabilities.
   Note: See paper for details.
3. **Add language-aware fusion**
   Action: Implement deep fusion between text and visual features.
   Why: Language-visual fusion enables text-guided detection.
   Note: See paper for details.
4. **Train on unified data**
   Action: Train GLIP on the merged dataset.
   Why: Unified training produces a versatile detector.
   Note: See paper for details.

## Parameters to set
- **detection_data** — Role: Detection datasets to include. How to set: Include Objects365, COCO, and others. Default/range: Multiple datasets. Effect: More detection data improves localization.
- **grounding_data** — Role: Grounding datasets to include. How to set: Include Flickr30K Entities, GoldG. Default/range: Multiple datasets. Effect: More grounding data improves language understanding.
- **fusion_depth** — Role: Depth of language-visual fusion. How to set: Deep fusion in multiple layers. Default/range: Multiple layers. Effect: Deeper fusion improves text-conditioned detection.

## Validation checks
- GLIP should outperform detection-only models on language-guided tasks.
- Standard detection metrics should remain competitive.
- Zero-shot detection on novel categories should work.

## Failure modes
- Reformulated category names may be too simple as phrases.
- Detection and grounding data may have different quality distributions.
- Deep fusion adds computational cost.

## Adaptation notes for VLM training
- GLIP is used as a detection backbone in many VLM grounding pipelines.
- The unified data format is reusable for other grounding models.
- Extend with more grounding data for improved language understanding.

## Implementation notes
- Use the GLIP codebase for reproducible training.
- Pre-compute text features for efficiency.
- Evaluate on both detection and grounding benchmarks.

## Evidence from the paper
- GLIP unifies detection and grounding by reformulating detection as phrase grounding.
- The unified training significantly improves both detection and grounding.
- GLIP achieves strong zero-shot detection on novel categories.
- The approach has become foundational for VLM grounding pipelines.

## Source paper
- **Title**: GLIP: Grounded Language-Image Pre-training
- **Year**: 2022
- **Venue**: CVPR
- **Paper ID**: arxiv-2112.03857v2
- **URL**: http://arxiv.org/abs/2112.03857v2
- **arXiv ID**: 2112.03857v2
