# SynthText: Synthetic Data for Text Detection

## One-line decision
Use this skill when you want to generate synthetic images with realistic text overlaid on natural scenes for text detection/recognition training. Avoid it when you have sufficient real text detection data or need non-text image generation.

## Skill metadata
- **Skill type**: synthetic-text-in-images
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Generate large-scale synthetic training data for text detection by realistically overlaying text on natural scene images, using depth and segmentation for placement.

## Problem signature
- Modality: synthetic images with text overlaid on natural scenes.
- Data state: natural scene images augmented with synthetically rendered text.
- Scale regime: 800K synthetic images with text annotations.
- Model requirement: No ML model; uses rendering engine with depth and segmentation.

## Use when
- You need training data for text detection or recognition.
- You want to generate unlimited text-in-image training data.
- Real text detection data is insufficient.

## Do not use when
- You have sufficient real text detection data.
- You need other types of synthetic data.
- Your text is not scene text (e.g., documents).

## Required inputs
- **background_images**: Natural scene images for text placement.
- **depth_maps**: Depth estimation for realistic text placement.
- **segmentation_maps**: Segmentation for finding suitable text placement regions.
- **font_library**: Library of fonts for text rendering.

## Optional inputs
- **text_corpus**: Corpus of text strings to render.

## Outputs
- **synthetic_text_images**: 800K images with synthetically overlaid text.
- **text_annotations**: Bounding boxes and masks for rendered text.

## Assumptions and prerequisites
- Depth and segmentation enable realistic text placement.
- Synthetic text data transfers effectively to real text detection.
- Rendering diversity covers real-world text appearance variation.

## Procedure
1. **Estimate depth and segmentation**
   Action: Compute depth and segmentation maps for background images.
   Why: Enables realistic text placement on flat surfaces.
   Note: See paper for details.
2. **Select text placement regions**
   Action: Find suitable regions for text based on depth and segmentation.
   Why: Text should appear on flat, visible surfaces.
   Note: See paper for details.
3. **Render text realistically**
   Action: Overlay text with appropriate perspective, color, and effects.
   Why: Realistic rendering improves transfer to real images.
   Note: See paper for details.
4. **Generate annotations**
   Action: Create bounding box and mask annotations for rendered text.
   Why: Annotations provide training supervision.
   Note: See paper for details.

## Parameters to set
- **num_images** — Role: Total synthetic images to generate. How to set: 800K for comprehensive coverage. Default/range: 800K. Effect: More images increase diversity.
- **font_diversity** — Role: Number of fonts used. How to set: Include diverse fonts and styles. Default/range: Diverse. Effect: More fonts improve generalization.
- **placement_realism** — Role: Quality of text placement. How to set: Use depth and segmentation guidance. Default/range: Depth-guided. Effect: Realistic placement improves transfer.

## Validation checks
- Text detection models trained on synthetic data should transfer to real images.
- Rendered text should look realistic in context.
- Annotations should accurately match rendered text positions.

## Failure modes
- Rendering artifacts may not match real text appearance.
- Depth estimation errors may cause unrealistic placement.
- The domain gap between synthetic and real may limit transfer.

## Adaptation notes for VLM training
- SynthText is used to generate text-in-image training data for VLM OCR capability.
- Extend with diverse backgrounds for broader coverage.
- Combine with real text detection data for best results.

## Implementation notes
- Use the SynthText rendering engine for generation.
- Vary fonts, colors, and effects for diversity.
- Evaluate transfer to real text detection benchmarks.

## Evidence from the paper
- SynthText generates 800K synthetic images with realistically overlaid text.
- Models trained on SynthText transfer effectively to real text detection.
- Depth and segmentation guidance produces realistic text placement.
- SynthText has become a standard training data source for text detection.

## Source paper
- **Title**: SynthText: Synthetic Data for Text Detection
- **Year**: 2016
- **Venue**: CVPR
- **Paper ID**: arxiv-1604.06646v1
- **URL**: http://arxiv.org/abs/1604.06646v1
- **arXiv ID**: 1604.06646v1
