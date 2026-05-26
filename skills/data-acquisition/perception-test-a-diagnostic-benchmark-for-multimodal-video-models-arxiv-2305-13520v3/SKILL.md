# Perception Test: A Diagnostic Benchmark for Multimodal Video Models

## One-line decision
Use this skill when you need a diagnostic benchmark testing fine-grained perception in video models across memory, abstraction, physics, and semantics. Avoid it when standard video QA benchmarks are sufficient.

## Skill metadata
- **Skill type**: perceptual-video-benchmark
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Create a diagnostic benchmark for fine-grained perceptual understanding in video models, testing memory, abstraction, physics, and semantic understanding through carefully designed evaluation tasks.

## Problem signature
- Modality: videos with diagnostic perception evaluation tasks.
- Data state: 11.6K video clips with perceptual evaluation tasks.
- Scale regime: 11.6K diagnostic video clips.
- Model requirement: Any video understanding model.

## Use when
- You need diagnostic video perception evaluation.
- You want to test fine-grained perceptual abilities.
- Standard video QA is insufficient for your evaluation needs.

## Do not use when
- Standard video benchmarks are sufficient.
- You do not evaluate video models.
- Perception-specific evaluation is not needed.

## Required inputs
- **perception_videos**: 11.6K carefully designed diagnostic videos.
- **perception_tasks**: Tasks testing memory, abstraction, physics, semantics.
- **evaluation_framework**: Framework for diagnostic evaluation.

## Optional inputs
- **task_categories**: Categories of perceptual abilities tested.

## Outputs
- **perception_scores**: Per-task perception evaluation scores.
- **diagnostic_analysis**: Analysis of model perceptual abilities.

## Assumptions and prerequisites
- Fine-grained perception testing reveals more than standard QA.
- Different perceptual abilities can be tested separately.
- Diagnostic evaluation guides targeted improvement.

## Procedure
1. **Design perception tasks**
   Action: Create tasks testing specific perceptual abilities.
   Why: Targeted tasks reveal specific capabilities.
   Note: See paper for details.
2. **Collect diagnostic videos**
   Action: Create or curate 11.6K videos for perception testing.
   Why: High-quality diagnostic videos enable accurate evaluation.
   Note: See paper for details.
3. **Evaluate models**
   Action: Test video models on perception tasks.
   Why: Measures fine-grained perceptual abilities.
   Note: See paper for details.
4. **Analyze perception gaps**
   Action: Identify which perceptual abilities are lacking.
   Why: Guides targeted model improvement.
   Note: See paper for details.

## Parameters to set
- **perception_types** — Role: Types of perception tested. How to set: Include memory, abstraction, physics, semantics. Default/range: 4 broad categories. Effect: More types provide broader evaluation.
- **num_clips** — Role: Total diagnostic clips. How to set: 11.6K for reliable evaluation. Default/range: 11.6K. Effect: More clips improve reliability.

## Validation checks
- Tasks should test genuine perceptual abilities.
- Results should differ from standard video QA.
- Diagnostic evaluation should be informative.

## Failure modes
- Some perception types may be hard to test.
- Carefully designed videos are expensive to create.
- The benchmark may not cover all perceptual abilities.

## Adaptation notes for VLM training
- Perception Test evaluates video VLM perceptual data quality.
- Diagnostic evaluation reveals which training data improves which abilities.
- Fine-grained perception testing guides video data curation.

## Implementation notes
- Use the Perception Test framework.
- Report per-ability scores.
- Compare to standard video QA benchmarks.

## Evidence from the paper
- Perception Test provides diagnostic evaluation across memory, abstraction, physics, and semantics.
- Fine-grained perception testing reveals capabilities not tested by standard QA.
- 11.6K carefully designed clips enable accurate diagnostic evaluation.
- The benchmark guides targeted improvement of video perceptual abilities.

## Source paper
- **Title**: Perception Test: A Diagnostic Benchmark for Multimodal Video Models
- **Year**: 2023
- **Venue**: arXiv
- **Paper ID**: arxiv-2305.13520v3
- **URL**: http://arxiv.org/abs/2305.13520v3
- **arXiv ID**: 2305.13520v3
