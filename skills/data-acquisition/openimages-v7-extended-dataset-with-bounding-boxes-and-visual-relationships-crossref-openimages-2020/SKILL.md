# OpenImages V7: Extended Dataset with Bounding Boxes and Visual Relationships

## One-line decision
Use this skill when you need a massive multi-label detection dataset with 9M images, 600 categories, and visual relationship annotations. Avoid it when COCO or Objects365 provide sufficient detection coverage.

## Skill metadata
- **Skill type**: massive-detection-dataset
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Provide a massive multi-label object detection and visual relationship dataset with 9 million images, 600+ categories, and relationship annotations.

## Problem signature
- Modality: images with multi-label classification, bounding boxes, and visual relationships.
- Data state: 9M images with 16M bounding boxes, 600+ categories, visual relationships.
- Scale regime: 9 million images, 16 million bounding boxes.
- Model requirement: Any detection model; used in VLM grounding pipelines.

## Use when
- You need massive-scale detection data.
- You want visual relationship annotations.
- You need multi-label classification data.

## Do not use when
- Smaller detection datasets are sufficient.
- You need instance segmentation (limited in OpenImages).
- You need domain-specific detection data.

## Required inputs
- **open_images_v7**: 9M images with multi-type annotations.
- **bbox_annotations**: 16M bounding boxes across 600+ categories.
- **relationship_annotations**: Visual relationship triplets.

## Optional inputs
- **segmentation_masks**: Instance segmentation for a subset.

## Outputs
- **openimages_v7**: 9M images with detection, classification, and relationship annotations.
- **detection_benchmark**: Large-scale detection benchmark.

## Assumptions and prerequisites
- 9M images provide comprehensive visual coverage.
- Multi-label annotation reflects real-world complexity.
- Visual relationships enrich understanding beyond detection.

## Procedure
1. **Collect 9M images**
   Action: Gather 9 million images from Flickr.
   Why: Massive scale ensures visual diversity.
   Note: See paper for details.
2. **Annotate bounding boxes**
   Action: Annotate 16M bounding boxes across 600+ categories.
   Why: Detection annotations enable localization.
   Note: See paper for details.
3. **Annotate relationships**
   Action: Annotate visual relationships between objects.
   Why: Relationships capture scene structure.
   Note: See paper for details.
4. **Multi-label classification**
   Action: Assign multiple category labels per image.
   Why: Multi-label reflects real-world co-occurrence.
   Note: See paper for details.

## Parameters to set
- **num_images** — Role: Total images. How to set: 9M for comprehensive coverage. Default/range: 9M. Effect: More images increase diversity.
- **num_categories** — Role: Detection categories. How to set: 600+ for broad vocabulary. Default/range: 600+. Effect: More categories improve coverage.

## Validation checks
- Detection models trained on OpenImages should generalize broadly.
- Visual relationships should capture meaningful object interactions.
- The dataset should complement COCO and Objects365.

## Failure modes
- Multi-label annotation may have missing labels.
- The dataset is very large, requiring significant storage.
- Annotation quality may vary across categories.

## Adaptation notes for VLM training
- OpenImages provides massive detection data for VLM grounding.
- Visual relationships are useful for VLM scene understanding.
- Combine with COCO and LVIS for comprehensive detection coverage.

## Implementation notes
- Use the OpenImages API for efficient data access.
- Handle the multi-label format appropriately.
- Evaluate with OpenImages detection metrics.

## Evidence from the paper
- OpenImages V7 provides 9M images with 16M bounding boxes across 600+ categories.
- Visual relationship annotations capture object interactions.
- The dataset is the largest publicly available detection dataset.
- OpenImages complements COCO and Objects365 for comprehensive detection training.

## Source paper
- **Title**: OpenImages V7: Extended Dataset with Bounding Boxes and Visual Relationships
- **Year**: 2020
- **Venue**: IJCV
- **Paper ID**: crossref-openimages-2020
- **URL**: https://storage.googleapis.com/openimages/web/index.html
- **arXiv ID**: N/A
