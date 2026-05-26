# Open-Vocabulary Object Detection Using Captions

## One-line decision
Use this skill when you want to train an object detector using image captions as weak supervision instead of bounding box annotations. Avoid it when you have abundant bounding box annotations.

## Skill metadata
- **Skill type**: caption-supervised-detection
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Train an open-vocabulary object detector using image captions as weak supervision, enabling detection of objects described in natural language without box annotations.

## Problem signature
- Modality: images with captions providing weak detection supervision.
- Data state: image-caption pairs used as weak supervision for detection.
- Scale regime: web-scale image-caption data.
- Model requirement: Detector with caption-based supervision.

## Use when
- You want detection without bounding box annotations.
- You have image-caption data at scale.
- You need open-vocabulary detection.

## Do not use when
- You have abundant bounding box annotations.
- Closed-set detection is sufficient.
- Caption supervision is too weak for your needs.

## Required inputs
- **image_caption_pairs**: Images with natural language captions.
- **caption_grounding**: Method for grounding captions to image regions.
- **detection_architecture**: Detection model adapted for caption supervision.

## Optional inputs
- **box_annotations**: Optional box annotations for better training.

## Outputs
- **caption_trained_detector**: Detector trained on caption supervision.
- **open_vocabulary_detection**: Detection of objects described in language.

## Assumptions and prerequisites
- Captions contain implicit object location information.
- Caption supervision can train reasonable detectors.
- Open-vocabulary capability emerges from caption diversity.

## Procedure
1. **Parse captions for objects**
   Action: Extract object mentions from captions.
   Why: Identifies what to detect from text.
   Note: See paper for details.
2. **Ground captions to regions**
   Action: Associate caption mentions with image regions.
   Why: Creates pseudo-box supervision.
   Note: See paper for details.
3. **Train with weak supervision**
   Action: Train detector on caption-grounded pseudo-boxes.
   Why: Caption supervision at scale.
   Note: See paper for details.
4. **Evaluate open-vocabulary**
   Action: Test on novel categories not in box-annotated data.
   Why: Validates open-vocabulary capability.
   Note: See paper for details.

## Parameters to set
- **grounding_method** — Role: How captions are grounded to regions. How to set: Use attention or proposal matching. Default/range: Attention-based. Effect: Better grounding improves training quality.
- **caption_parsing** — Role: How objects are extracted from captions. How to set: NER or noun phrase extraction. Default/range: Noun phrases. Effect: Parsing quality affects training signal.

## Validation checks
- Caption-supervised detection should work for mentioned objects.
- Open-vocabulary detection should generalize to novel categories.
- Performance should approach box-supervised models for common objects.

## Failure modes
- Caption grounding may be inaccurate.
- Captions may not mention all visible objects.
- Weak supervision quality limits detection accuracy.

## Adaptation notes for VLM training
- Caption-supervised detection generates training data for VLM grounding.
- The approach scales with image-caption data availability.
- Combine with box-supervised data for hybrid training.

## Implementation notes
- Use efficient caption parsing.
- Validate grounding quality.
- Compare to box-supervised baselines.

## Evidence from the paper
- OVR-CNN trains open-vocabulary detection from caption supervision.
- Captions provide useful weak supervision for detection at scale.
- Open-vocabulary detection enables finding objects described in language.
- Caption supervision scales better than manual box annotation.

## Source paper
- **Title**: Open-Vocabulary Object Detection Using Captions
- **Year**: 2021
- **Venue**: CVPR
- **Paper ID**: arxiv-2011.10678v2
- **URL**: http://arxiv.org/abs/2011.10678v2
- **arXiv ID**: 2011.10678v2
