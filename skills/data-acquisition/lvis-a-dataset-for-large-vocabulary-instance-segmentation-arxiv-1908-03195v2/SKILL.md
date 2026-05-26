# LVIS: A Dataset for Large Vocabulary Instance Segmentation

## One-line decision
Use this skill when you need a large-vocabulary instance segmentation dataset with 1,200+ categories handling the long tail of visual concepts. Avoid it when COCO's 80 categories are sufficient for your needs.

## Skill metadata
- **Skill type**: long-tail-detection-data
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Create a large vocabulary instance segmentation dataset with 1,200+ categories, specifically designed to handle the long-tail distribution of visual concepts.

## Problem signature
- Modality: images with instance segmentation masks for 1,200+ categories.
- Data state: 164K COCO images annotated with 1,200+ category instance masks.
- Scale regime: 164K images, 2M instance annotations, 1,203 categories.
- Model requirement: Instance segmentation models; used in VLM grounding pipelines.

## Use when
- You need detection/segmentation data with 1,200+ categories.
- You want to handle long-tail visual concept distributions.
- You need a comprehensive vocabulary for VLM grounding.

## Do not use when
- COCO's 80 categories are sufficient.
- You do not need instance segmentation.
- You need non-COCO images.

## Required inputs
- **coco_images**: 164K images from COCO.
- **large_vocabulary**: 1,203 object categories from WordNet.
- **instance_annotations**: Per-instance segmentation masks.

## Optional inputs
- **federated_annotations**: Annotations from federated workers.

## Outputs
- **lvis_dataset**: 164K images with 2M instance annotations across 1,203 categories.
- **long_tail_benchmark**: Benchmark for long-tail detection.

## Assumptions and prerequisites
- 1,200+ categories cover a broader range than COCO's 80.
- Long-tail distribution reflects real-world concept frequency.
- Instance segmentation enables fine-grained VLM grounding.

## Procedure
1. **Define large vocabulary**
   Action: Select 1,203 categories from WordNet synsets.
   Why: WordNet provides comprehensive category coverage.
   Note: See paper for details.
2. **Annotate instances**
   Action: Annotate all visible instances of each category in COCO images.
   Why: Exhaustive annotation provides complete supervision.
   Note: See paper for details.
3. **Handle long tail**
   Action: Design the dataset to naturally exhibit long-tail frequency distribution.
   Why: Reflects real-world concept frequency.
   Note: See paper for details.
4. **Benchmark detection**
   Action: Establish baselines for long-tail instance segmentation.
   Why: Benchmarks enable progress tracking.
   Note: See paper for details.

## Parameters to set
- **num_categories** — Role: Total categories in the vocabulary. How to set: 1,203 for comprehensive coverage. Default/range: 1,203. Effect: More categories cover more concepts.
- **annotation_strategy** — Role: How annotations are collected. How to set: Federated annotation with exhaustive labeling per category. Default/range: Federated. Effect: Ensures complete annotation.

## Validation checks
- Models should handle the long-tail distribution.
- Rare categories should be detectable, not just common ones.
- The vocabulary should cover diverse object types.

## Failure modes
- Rare categories have very few training examples.
- Annotation quality varies across categories.
- Long-tail imbalance challenges standard training.

## Adaptation notes for VLM training
- LVIS provides comprehensive vocabulary for VLM grounding training.
- Use LVIS categories for open-vocabulary detection.
- Combine with COCO and Objects365 for detection pretraining.

## Implementation notes
- Use the LVIS API for data loading.
- Apply category frequency rebalancing during training.
- Evaluate separately on frequent, common, and rare categories.

## Evidence from the paper
- LVIS provides 1,203 categories with 2M instance annotations on 164K images.
- The dataset exhibits natural long-tail frequency distribution.
- LVIS enables evaluation of rare concept detection.
- The dataset is used for training open-vocabulary detection models.

## Source paper
- **Title**: LVIS: A Dataset for Large Vocabulary Instance Segmentation
- **Year**: 2019
- **Venue**: CVPR
- **Paper ID**: arxiv-1908.03195v2
- **URL**: http://arxiv.org/abs/1908.03195v2
- **arXiv ID**: 1908.03195v2
