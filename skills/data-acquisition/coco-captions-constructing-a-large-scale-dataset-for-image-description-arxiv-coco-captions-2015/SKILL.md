# COCO Captions: Constructing a Large-Scale Dataset for Image Description

## One-line decision
Use this skill when you need gold-standard image captions collected through crowdsourcing for VLM training and evaluation. Avoid it when web-crawled captions are sufficient or you have your own caption data.

## Skill metadata
- **Skill type**: gold-standard-caption-collection
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Construct a large-scale image description dataset through crowdsourcing, providing 5 independent human-written captions per image for training and evaluating image captioning and VLMs.

## Problem signature
- Modality: images with 5 independent human-written captions each.
- Data state: 330K COCO images with 5 crowdsourced captions each.
- Scale regime: 1.5M human-written captions on 330K images.
- Model requirement: No model required; foundational training and evaluation data.

## Use when
- You need gold-standard image caption data.
- You want evaluation data for captioning and VLMs.
- You need high-quality alignment data for VLM training.

## Do not use when
- Web-crawled captions are sufficient.
- You need domain-specific captions.
- You need more than 330K images.

## Required inputs
- **coco_images**: 330K COCO images.
- **crowdsourcing_platform**: AMT for caption collection.
- **annotation_guidelines**: Guidelines for writing image descriptions.

## Optional inputs
- **quality_review**: Review process for caption quality.

## Outputs
- **coco_captions**: 1.5M human-written captions on 330K images.
- **evaluation_benchmark**: Standard captioning evaluation benchmark.

## Assumptions and prerequisites
- 5 independent captions capture diverse descriptions.
- Crowdsourced captions provide useful training signal.
- COCO images cover diverse everyday scenes.

## Procedure
1. **Select images**
   Action: Use COCO's 330K diverse images.
   Why: Diverse images ensure broad captioning.
   Note: See paper for details.
2. **Collect 5 captions per image**
   Action: Have 5 independent annotators write captions.
   Why: Multiple captions capture description diversity.
   Note: See paper for details.
3. **Quality review**
   Action: Review captions for quality and relevance.
   Why: Ensures caption quality.
   Note: See paper for details.
4. **Release for training and evaluation**
   Action: Package captions for research use.
   Why: Enables captioning research.
   Note: See paper for details.

## Parameters to set
- **captions_per_image** — Role: Number of independent captions. How to set: 5 for diversity. Default/range: 5. Effect: More captions capture more diverse descriptions.
- **annotation_quality** — Role: Quality of crowdsourced captions. How to set: Provide clear guidelines and review. Default/range: High quality. Effect: Quality captions provide better training signal.

## Validation checks
- Captions should accurately describe image content.
- 5 captions should show diversity in description.
- The dataset should support standard captioning metrics (CIDEr, BLEU).

## Failure modes
- Crowdsourced captions may be generic.
- Some images may be poorly described.
- Caption style may not match target applications.

## Adaptation notes for VLM training
- COCO captions are the standard for captioning evaluation.
- Used as alignment data in VLM pretraining (LLaVA, MiniGPT-4).
- 5-caption diversity provides robust evaluation.

## Implementation notes
- Use the COCO API for efficient access.
- Evaluate with CIDEr, BLEU, METEOR, and ROUGE.
- Use captions for VLM alignment pre-training.

## Evidence from the paper
- COCO Captions provides 1.5M human-written captions on 330K images.
- 5 independent captions per image ensure description diversity.
- The dataset is the standard benchmark for image captioning evaluation.
- COCO captions are widely used for VLM pretraining alignment.

## Source paper
- **Title**: COCO Captions: Constructing a Large-Scale Dataset for Image Description
- **Year**: 2015
- **Venue**: arXiv
- **Paper ID**: arxiv-coco-captions-2015
- **URL**: https://arxiv.org/abs/1504.00325
- **arXiv ID**: N/A
