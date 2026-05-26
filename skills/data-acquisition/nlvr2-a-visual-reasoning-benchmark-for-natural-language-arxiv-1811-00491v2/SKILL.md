# NLVR2: A Visual Reasoning Benchmark for Natural Language

## One-line decision
Use this skill when you need a visual reasoning benchmark where the model must determine if a statement is true for a pair of images. Avoid it when single-image reasoning evaluation is sufficient.

## Skill metadata
- **Skill type**: paired-image-reasoning-data
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Create a visual reasoning benchmark where models must determine if a natural language statement is true or false when applied to a pair of real-world images.

## Problem signature
- Modality: pairs of images with true/false natural language statements.
- Data state: 107K statement-image-pair examples for visual reasoning.
- Scale regime: 107K examples with paired images.
- Model requirement: Any VLM capable of processing image pairs.

## Use when
- You need paired-image visual reasoning data.
- You want to test comparative visual reasoning.
- You need a challenging visual reasoning benchmark.

## Do not use when
- Single-image reasoning is sufficient.
- Your model cannot process image pairs.
- You need a larger-scale benchmark.

## Required inputs
- **image_pairs**: Pairs of web images.
- **statements**: Natural language statements about the image pairs.
- **truth_labels**: True/false labels for each statement-pair.

## Optional inputs
- **reasoning_types**: Categories of reasoning required.

## Outputs
- **nlvr2_dataset**: 107K visual reasoning examples with image pairs.
- **reasoning_benchmark**: Benchmark for paired-image reasoning.

## Assumptions and prerequisites
- Paired-image reasoning tests different capabilities than single-image.
- Natural language statements provide diverse reasoning challenges.
- True/false evaluation is clear and unambiguous.

## Procedure
1. **Collect image pairs**
   Action: Gather pairs of web images with visual similarities and differences.
   Why: Pairs enable comparative reasoning.
   Note: See paper for details.
2. **Write reasoning statements**
   Action: Create statements that may be true or false about the pairs.
   Why: Statements test specific reasoning capabilities.
   Note: See paper for details.
3. **Label truth values**
   Action: Determine if each statement is true or false for its image pair.
   Why: Labels provide evaluation signal.
   Note: See paper for details.
4. **Evaluate VLMs**
   Action: Test VLMs on the paired reasoning benchmark.
   Why: Measures comparative visual reasoning.
   Note: See paper for details.

## Parameters to set
- **statement_types** — Role: Types of reasoning statements. How to set: Include counting, comparison, spatial reasoning. Default/range: Diverse. Effect: More types test broader reasoning.
- **pair_diversity** — Role: Diversity of image pairs. How to set: Include similar and dissimilar pairs. Default/range: Diverse. Effect: Diverse pairs test different comparisons.

## Validation checks
- Models should perform above random (50%) baseline.
- Different reasoning types should show different difficulty levels.
- The benchmark should remain challenging.

## Failure modes
- Some statements may be ambiguous.
- Image pair selection may introduce biases.
- True/false format is limited for complex reasoning.

## Adaptation notes for VLM training
- NLVR2 tests paired-image reasoning important for multi-image VLMs.
- Include in evaluation for comparative visual understanding.
- The paired format is relevant for document comparison and change detection.

## Implementation notes
- Handle image pair input correctly.
- Report per-reasoning-type accuracy.
- Compare to single-image baselines.

## Evidence from the paper
- NLVR2 provides 107K paired-image visual reasoning examples.
- Statements test counting, comparison, and spatial reasoning.
- The benchmark remains challenging for current VLMs.
- Paired-image reasoning is a distinct capability from single-image.

## Source paper
- **Title**: NLVR2: A Visual Reasoning Benchmark for Natural Language
- **Year**: 2019
- **Venue**: ACL
- **Paper ID**: arxiv-1811.00491v2
- **URL**: http://arxiv.org/abs/1811.00491v2
- **arXiv ID**: 1811.00491v2
