# Flickr30K Entities: Collecting Region-to-Phrase Correspondences for Richer Image-to-Sentence Models

## One-line decision
Use this skill when you need a dataset linking noun phrases in captions to bounding box regions in images for visual grounding. Avoid it when you do not need phrase-level grounding or the 31K image scale is too small.

## Skill metadata
- **Skill type**: region-phrase-grounding-data
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Extend Flickr30K with bounding box annotations linking noun phrases in captions to corresponding image regions, enabling phrase grounding research.

## Problem signature
- Modality: images with captions where noun phrases are linked to bounding box regions.
- Data state: Flickr30K images with additional region-phrase correspondence annotations.
- Scale regime: 31K images with 275K bounding boxes linked to phrases in 158K captions.
- Model requirement: No model required for dataset construction; used for grounding model training and evaluation.

## Use when
- You need region-phrase grounding data for VLM training.
- You want to evaluate phrase localization capabilities.
- You need a clean grounding dataset with human annotations.

## Do not use when
- You need larger-scale grounding data.
- Phrase grounding is not your target capability.
- You need pixel-level segmentation rather than bounding boxes.

## Required inputs
- **flickr30k_images**: 31K Flickr images with 5 captions each.
- **grounding_annotations**: Bounding boxes linked to noun phrases in captions.
- **annotation_platform**: Platform for collecting region-phrase correspondences.

## Optional inputs
- **coreference_annotations**: Coreference chains linking phrases across captions.

## Outputs
- **flickr30k_entities**: 31K images with region-phrase correspondences.
- **grounding_benchmark**: Standard evaluation for phrase grounding.

## Assumptions and prerequisites
- Noun phrases in captions have identifiable visual referents.
- Bounding boxes adequately capture phrase-level grounding.
- Human annotations provide reliable ground truth for grounding.

## Procedure
1. **Identify noun phrases in captions**
   Action: Parse captions to extract noun phrases.
   Why: Noun phrases are the units for grounding.
   Note: See paper for details.
2. **Annotate bounding boxes**
   Action: Have annotators draw bounding boxes for each noun phrase's referent.
   Why: Creates region-phrase correspondences.
   Note: See paper for details.
3. **Annotate coreference**
   Action: Link phrases referring to the same entity across captions.
   Why: Coreference enables multi-caption reasoning.
   Note: See paper for details.
4. **Validate annotations**
   Action: Review annotations for accuracy and consistency.
   Why: Ensures ground truth quality.
   Note: See paper for details.

## Parameters to set
- **phrases_per_caption** — Role: Average noun phrases per caption. How to set: Parse all noun phrases. Default/range: ~4-5. Effect: More phrases provide denser grounding.
- **box_quality** — Role: Quality of bounding box annotations. How to set: Tight boxes around referents. Default/range: Human-drawn. Effect: Tighter boxes improve evaluation precision.

## Validation checks
- Bounding boxes should tightly enclose the noun phrase referents.
- Phrases without visual referents should be marked appropriately.
- Coreference chains should correctly link equivalent phrases.

## Failure modes
- Some noun phrases may have ambiguous or absent visual referents.
- Bounding boxes may not perfectly capture irregular shapes.
- The 31K image scale limits pretraining utility.

## Adaptation notes for VLM training
- Flickr30K Entities is a standard grounding evaluation benchmark.
- Use for fine-tuning VLMs on phrase grounding.
- Combine with RefCOCO for comprehensive grounding evaluation.

## Implementation notes
- Use phrase type annotations (people, clothing, etc.) for analysis.
- Evaluate with Recall@K metrics for grounding.
- Track performance by phrase type.

## Evidence from the paper
- Flickr30K Entities extends Flickr30K with 275K bounding boxes linked to noun phrases in captions.
- The dataset enables phrase grounding research at the intersection of language and vision.
- Region-phrase correspondences provide fine-grained vision-language alignment.
- The dataset is a standard benchmark for evaluating VLM grounding capabilities.

## Source paper
- **Title**: Flickr30K Entities: Collecting Region-to-Phrase Correspondences for Richer Image-to-Sentence Models
- **Year**: 2017
- **Venue**: IJCV
- **Paper ID**: arxiv-1505.04870v3
- **URL**: http://arxiv.org/abs/1505.04870v3
- **arXiv ID**: 1505.04870v3
