# Referring Expression Comprehension: A Survey of Methods and Datasets

## One-line decision
Use this skill when you need an overview of referring expression datasets (RefCOCO, RefCOCO+, RefCOCOg) for VLM grounding training. Avoid it when you already know the referring expression dataset landscape.

## Skill metadata
- **Skill type**: referring-expression-datasets
- **Paper kind**: survey
- **Actionability**: medium
- **Evidence quality**: full_paper

## Goal
Survey the major referring expression comprehension datasets (RefCOCO, RefCOCO+, RefCOCOg) and methods, providing a comprehensive overview of data resources for training VLMs on spatial referring.

## Problem signature
- Modality: images with referring expressions linked to specific objects or regions.
- Data state: curated datasets with natural language referring expressions paired with target objects.
- Scale regime: RefCOCO: 142K expressions, RefCOCO+: 141K, RefCOCOg: 104K.
- Model requirement: No model required; survey of datasets and methods.

## Use when
- You need to understand the referring expression dataset landscape.
- You want to select the right grounding datasets for VLM training.
- You need to evaluate VLM referring expression comprehension.

## Do not use when
- You already know these datasets well.
- You need datasets beyond referring expressions.
- You need very large-scale grounding data.

## Required inputs
- **refcoco_datasets**: RefCOCO, RefCOCO+, and RefCOCOg datasets.
- **evaluation_framework**: Framework for evaluating referring expression comprehension.

## Optional inputs
- **additional_datasets**: Other referring expression datasets (Talk2Car, etc.).

## Outputs
- **dataset_comparison**: Comparison of major referring expression datasets.
- **method_survey**: Survey of referring expression comprehension methods.

## Assumptions and prerequisites
- Referring expressions are a fundamental visio-linguistic capability.
- Multiple datasets are needed to cover different aspects of referring.
- RefCOCO family datasets provide comprehensive evaluation.

## Procedure
1. **Review RefCOCO datasets**
   Action: Analyze RefCOCO, RefCOCO+, and RefCOCOg for data characteristics.
   Why: Understanding dataset properties guides selection.
   Note: See paper for details.
2. **Compare dataset properties**
   Action: Compare expression types, vocabulary, and spatial reasoning requirements.
   Why: Different datasets test different referring capabilities.
   Note: See paper for details.
3. **Survey comprehension methods**
   Action: Review model architectures and training approaches.
   Why: Provides context for dataset usage.
   Note: See paper for details.
4. **Identify best practices**
   Action: Recommend evaluation protocols and dataset combinations.
   Why: Guides VLM training on referring tasks.
   Note: See paper for details.

## Parameters to set
- **dataset_selection** — Role: Which referring expression datasets to use. How to set: Use all three RefCOCO variants for comprehensive evaluation. Default/range: RefCOCO + RefCOCO+ + RefCOCOg. Effect: All three provide complementary evaluation.

## Validation checks
- Models should be evaluated on all three RefCOCO variants.
- Accuracy should be reported separately for different split types.
- Comparison should use consistent evaluation metrics.

## Failure modes
- Individual datasets may not cover all referring expression types.
- Evaluation metrics may not capture all aspects of comprehension.
- Dataset biases may allow shortcut learning.

## Adaptation notes for VLM training
- RefCOCO datasets are standard grounding evaluation benchmarks for VLMs.
- Include referring expression data in VLM instruction tuning for grounding.
- Combine with other grounding data for comprehensive spatial understanding.

## Implementation notes
- Use the standard splits for reproducible evaluation.
- Report accuracy on all three datasets.
- Track performance by expression type (spatial, attribute, etc.).

## Evidence from the paper
- The survey covers RefCOCO (142K expressions), RefCOCO+ (141K), and RefCOCOg (104K).
- RefCOCO tests spatial referring, RefCOCO+ removes spatial words, RefCOCOg uses longer expressions.
- These datasets are the primary benchmarks for VLM grounding evaluation.
- Referring expression comprehension is a key capability for spatial VLM understanding.

## Source paper
- **Title**: Referring Expression Comprehension: A Survey of Methods and Datasets
- **Year**: 2020
- **Venue**: TPAMI
- **Paper ID**: arxiv-2007.09554v2
- **URL**: http://arxiv.org/abs/2007.09554v2
- **arXiv ID**: 2007.09554v2
