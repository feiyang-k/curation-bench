# CLEVR: A Diagnostic Dataset for Compositional Language and Elementary Visual Reasoning

## One-line decision
Use this skill when you want to generate diagnostic visual reasoning data with programmatic scene and question generation for compositional reasoning evaluation. Avoid it when you need real-world images rather than synthetic scenes.

## Skill metadata
- **Skill type**: programmatic-visual-reasoning-data
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Generate a diagnostic dataset of synthetic 3D scenes with programmatically generated compositional questions, enabling controlled evaluation of visual reasoning capabilities.

## Problem signature
- Modality: synthetic 3D scene images with programmatic compositional questions.
- Data state: 100K synthetically rendered scenes with 850K programmatic questions.
- Scale regime: 100K scenes, 850K questions.
- Model requirement: No model for generation; validated with visual reasoning models.

## Use when
- You need controlled evaluation of compositional reasoning.
- You want programmatic question generation without annotation.
- You need diagnostic evaluation for VLM spatial reasoning.

## Do not use when
- You need real-world image evaluation.
- Compositional reasoning is not your focus.
- You need evaluation on complex natural scenes.

## Required inputs
- **scene_renderer**: 3D rendering engine for synthetic scenes.
- **question_grammar**: Grammar for generating compositional questions.
- **scene_graphs**: Structured scene descriptions for question generation.

## Optional inputs
- **difficulty_control**: Control over question complexity.

## Outputs
- **clevr_dataset**: 100K scenes with 850K compositional questions.
- **diagnostic_analysis**: Analysis of model reasoning capabilities.

## Assumptions and prerequisites
- Synthetic scenes enable controlled evaluation.
- Programmatic questions test specific reasoning capabilities.
- Compositional reasoning is a key VLM capability.

## Procedure
1. **Generate synthetic scenes**
   Action: Render 3D scenes with objects of different shapes, colors, sizes, and positions.
   Why: Synthetic scenes enable controlled evaluation.
   Note: See paper for details.
2. **Generate compositional questions**
   Action: Use a grammar to create multi-step reasoning questions.
   Why: Questions test specific reasoning capabilities.
   Note: See paper for details.
3. **Evaluate models**
   Action: Test VLMs on CLEVR questions.
   Why: Diagnostic evaluation reveals reasoning capabilities.
   Note: See paper for details.

## Parameters to set
- **scene_complexity** — Role: Number of objects per scene. How to set: 3-10 for varying difficulty. Default/range: 3-10. Effect: More objects increase reasoning difficulty.
- **question_depth** — Role: Reasoning steps per question. How to set: 1-5 steps. Default/range: 1-5. Effect: Deeper questions test harder reasoning.

## Validation checks
- Questions should require the specified reasoning steps.
- Models should be tested on each reasoning type.
- Diagnostic results should be actionable.

## Failure modes
- Synthetic scenes may not transfer to real-world reasoning.
- Programmatic questions may be artificially structured.
- The dataset may become saturated as models improve.

## Adaptation notes for VLM training
- CLEVR provides diagnostic evaluation for VLM spatial reasoning.
- Use CLEVR-style generation for controlled VLM evaluation.
- Extend to more complex synthetic scenes for harder reasoning.

## Implementation notes
- Use the CLEVR generation code for custom diagnostics.
- Test each reasoning type separately.
- Compare VLM reasoning vs human reasoning.

## Evidence from the paper
- CLEVR provides 100K synthetic scenes with 850K compositional questions.
- Programmatic generation enables controlled evaluation of specific reasoning types.
- The dataset reveals which reasoning capabilities models lack.
- CLEVR has influenced many subsequent diagnostic VLM benchmarks.

## Source paper
- **Title**: CLEVR: A Diagnostic Dataset for Compositional Language and Elementary Visual Reasoning
- **Year**: 2017
- **Venue**: CVPR
- **Paper ID**: arxiv-1612.06890v1
- **URL**: http://arxiv.org/abs/1612.06890v1
- **arXiv ID**: 1612.06890v1
