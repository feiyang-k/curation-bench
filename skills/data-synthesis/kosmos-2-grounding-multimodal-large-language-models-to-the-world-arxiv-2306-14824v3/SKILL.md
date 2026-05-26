# Kosmos-2: Grounding Multimodal Large Language Models to the World

## One-line decision
Use this skill when you need to construct grounded image-text data with bounding box annotations linked to text spans for training grounding-capable VLMs. Avoid it when you do not need spatial grounding or bounding box outputs from your VLM.

## Skill metadata
- **Skill type**: grounded-data-construction
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Construct GrIT, a large-scale grounded image-text dataset where noun phrases in captions are linked to bounding boxes, enabling a multimodal LLM to output grounded text with spatial references.

## Problem signature
- Modality: images with captions where noun phrases are linked to bounding boxes.
- Data state: web-crawled image-text pairs augmented with grounding annotations linking text spans to image regions.
- Scale regime: millions of grounded image-text pairs.
- Model requirement: Multimodal LLM that processes interleaved text and location tokens.

## Use when
- You want a VLM that can output text with spatial grounding (bounding boxes).
- You need to construct grounded image-text training data at scale.
- You want to combine language generation with spatial understanding.

## Do not use when
- You do not need spatial grounding in your VLM outputs.
- You cannot run object detectors or grounding models for annotation.
- Plain captioning without localization is sufficient.

## Required inputs
- **image_text_pairs**: Web-crawled image-text pairs as the base data.
- **object_detector**: Detector for identifying objects and their bounding boxes in images.
- **noun_phrase_linker**: Tool for linking detected objects to noun phrases in captions.

## Optional inputs
- **grounding_model**: Pre-trained grounding model for higher quality linking.

## Outputs
- **grit_dataset**: Grounded image-text dataset with text spans linked to bounding boxes.
- **kosmos2_model**: VLM capable of generating text with inline spatial references.

## Assumptions and prerequisites
- Noun phrases in captions can be reliably linked to image regions.
- Location tokens can be naturally embedded in text sequences.
- Grounded pretraining improves spatial understanding.

## Procedure
1. **Detect objects in images**
   Action: Run an object detector to find objects and their bounding boxes.
   Why: Provides spatial annotations for grounding.
   Note: See paper for details.
2. **Link objects to text spans**
   Action: Match detected objects to noun phrases in the caption using text-region alignment.
   Why: Creates the grounded connection between language and space.
   Note: See paper for details.
3. **Format with location tokens**
   Action: Insert special location tokens (bounding box coordinates) inline with text.
   Why: Enables the model to learn grounded generation.
   Note: See paper for details.
4. **Train Kosmos-2 on GrIT**
   Action: Pre-train the multimodal LLM on the grounded data.
   Why: Grounded pretraining teaches spatial reasoning.
   Note: See paper for details.

## Parameters to set
- **bbox_format** — Role: How bounding boxes are encoded in text. How to set: Discretize coordinates into location tokens. Default/range: Discretized tokens. Effect: Token-based format integrates naturally with language modeling.
- **grounding_coverage** — Role: Fraction of noun phrases with grounding annotations. How to set: Link all detectable noun phrases. Default/range: All linkable phrases. Effect: More grounding improves spatial understanding.

## Validation checks
- Grounding accuracy should match specialist referring expression models.
- Caption quality should not degrade from grounding integration.
- Location tokens should correctly correspond to visual regions.

## Failure modes
- Noun phrase linking may create incorrect text-region associations.
- Not all noun phrases have visible referents in the image.
- Location token vocabulary may be insufficient for precise localization.

## Adaptation notes for VLM training
- The grounded data format is reusable for any VLM needing spatial outputs.
- Extend GrIT with segmentation masks for pixel-level grounding.
- Combine with standard caption data for balanced training.

## Implementation notes
- Use GLIP or similar for high-quality object-text linking.
- Discretize coordinates to a fixed vocabulary of location tokens.
- Evaluate grounding accuracy with RefCOCO/RefCOCO+ benchmarks.

## Evidence from the paper
- Kosmos-2 constructs GrIT, a large-scale grounded image-text dataset linking noun phrases to bounding boxes.
- The model outputs text with inline location tokens for spatial grounding.
- Kosmos-2 achieves competitive results on referring expression comprehension and grounded captioning.
- Grounded pretraining improves both language and spatial understanding.

## Source paper
- **Title**: Kosmos-2: Grounding Multimodal Large Language Models to the World
- **Year**: 2023
- **Venue**: ICLR
- **Paper ID**: arxiv-2306.14824v3
- **URL**: http://arxiv.org/abs/2306.14824v3
- **arXiv ID**: 2306.14824v3
