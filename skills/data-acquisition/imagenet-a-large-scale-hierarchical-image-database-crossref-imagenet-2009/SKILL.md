# ImageNet: A Large-Scale Hierarchical Image Database

## One-line decision
Use this skill when you need a large-scale hierarchical image dataset organized by WordNet synsets for vision model pretraining and evaluation. Avoid it when you need image-text pairs rather than image-label data.

## Skill metadata
- **Skill type**: hierarchical-image-dataset
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Construct a large-scale hierarchical image database organized by WordNet synsets, providing millions of labeled images across thousands of categories for vision research.

## Problem signature
- Modality: images with hierarchical category labels from WordNet.
- Data state: 14 million images organized by 21K+ WordNet synsets.
- Scale regime: 14 million images, 21K+ categories (1K subset most commonly used).
- Model requirement: No model required for dataset construction; foundational for vision model evaluation.

## Use when
- You need a standard image classification dataset for evaluation.
- You want hierarchical category organization.
- You need a pretraining dataset for vision models.

## Do not use when
- You need image-text pairs for VLM training.
- You need domain-specific image data.
- The 1K-class subset is insufficient for your needs.

## Required inputs
- **web_images**: Images from the web for each WordNet synset.
- **wordnet_hierarchy**: WordNet noun hierarchy for organizing categories.
- **annotation_platform**: AMT for labeling images by synset.

## Optional inputs
- **bounding_boxes**: Bounding box annotations for localization.

## Outputs
- **imagenet_dataset**: 14M images organized by 21K+ WordNet synsets.
- **evaluation_benchmark**: Standard 1K-class classification benchmark.

## Assumptions and prerequisites
- WordNet provides a meaningful semantic hierarchy for images.
- Web images can be reliably labeled by AMT workers.
- Large-scale labeled data is essential for vision research.

## Procedure
1. **Define category structure**
   Action: Use WordNet synsets to define image categories.
   Why: WordNet provides a principled semantic hierarchy.
   Note: See paper for details.
2. **Collect candidate images**
   Action: Search the web for images matching each synset.
   Why: Web search provides diverse image candidates.
   Note: See paper for details.
3. **Annotate with AMT**
   Action: Use crowd workers to verify image-synset matches.
   Why: Human verification ensures label quality.
   Note: See paper for details.
4. **Build hierarchy**
   Action: Organize labeled images according to the WordNet tree.
   Why: Hierarchy enables hierarchical evaluation.
   Note: See paper for details.

## Parameters to set
- **num_categories** — Role: Number of WordNet synsets covered. How to set: 21K+ for broad coverage; 1K for standard benchmark. Default/range: 1K or 21K. Effect: More categories increase dataset diversity.
- **images_per_category** — Role: Number of images per synset. How to set: 500-1300 for the 1K subset. Default/range: ~1000. Effect: More images improve per-class representation.

## Validation checks
- Labels should be accurate and consistent.
- The category distribution should reflect the WordNet hierarchy.
- The benchmark should discriminate between model capabilities.

## Failure modes
- Some categories may have noisy labels.
- The dataset has known biases (geographic, demographic).
- 1K categories may not cover all visual concepts.

## Adaptation notes for VLM training
- ImageNet is the primary evaluation benchmark for CLIP and VLM vision encoders.
- ImageNet-21K is used for vision encoder pretraining.
- Zero-shot ImageNet accuracy is the standard metric for CLIP-style models.

## Implementation notes
- Use the ILSVRC 2012 subset for standard evaluation.
- Consider ImageNet-V2, ImageNet-R, and other variants for robustness evaluation.
- Track top-1 and top-5 accuracy.

## Evidence from the paper
- ImageNet provides 14 million images organized by 21K+ WordNet synsets.
- The dataset has been foundational for the deep learning revolution in computer vision.
- ImageNet-1K remains the primary benchmark for vision model evaluation.
- Zero-shot ImageNet accuracy is the standard metric for CLIP and VLM vision encoders.

## Source paper
- **Title**: ImageNet: A Large-Scale Hierarchical Image Database
- **Year**: 2009
- **Venue**: CVPR
- **Paper ID**: crossref-imagenet-2009
- **URL**: https://www.image-net.org/
- **arXiv ID**: N/A
