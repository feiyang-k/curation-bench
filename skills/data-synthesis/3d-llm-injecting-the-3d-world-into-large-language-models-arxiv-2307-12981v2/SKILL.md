# 3D-LLM: Injecting the 3D World into Large Language Models

## One-line decision
Use this skill when you want to create 3D-language instruction data for training LLMs to understand and reason about 3D environments. Avoid it when you only work with 2D images.

## Skill metadata
- **Skill type**: 3d-language-instruction-data
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Create 3D-language instruction data by rendering multi-view images from 3D scenes and using them with GPT-4 to generate 3D-grounded instruction data for training 3D-LLMs.

## Problem signature
- Modality: 3D scenes with language instructions for 3D understanding.
- Data state: 3D scenes converted to multi-view images with LLM-generated instructions.
- Scale regime: 300K 3D-language instruction data points.
- Model requirement: 3D feature extractor + LLM for 3D understanding.

## Use when
- You want to add 3D understanding to LLMs.
- You can render multi-view images from 3D scenes.
- You need 3D-grounded instruction data.

## Do not use when
- 2D understanding is sufficient.
- You do not have 3D scene data.
- 3D understanding is not needed.

## Required inputs
- **3d_scenes**: 3D scene data (ScanNet, Objaverse, etc.).
- **multi_view_renderer**: Renderer for creating multi-view images.
- **instruction_generator**: GPT-4 for generating 3D instructions from multi-view context.

## Optional inputs
- **3d_features**: Pre-computed 3D features for efficiency.

## Outputs
- **3d_instruction_data**: 300K 3D-language instruction data points.
- **3d_llm**: LLM with 3D spatial understanding.

## Assumptions and prerequisites
- Multi-view images capture 3D spatial information.
- GPT-4 can generate 3D-grounded instructions from multi-view context.
- 3D instruction data enables spatial reasoning in LLMs.

## Procedure
1. **Render multi-view images**
   Action: Render multiple views of 3D scenes.
   Why: Multi-view captures 3D spatial information.
   Note: See paper for details.
2. **Generate 3D instructions with GPT-4**
   Action: Use GPT-4 with multi-view context to create 3D instructions.
   Why: Generates spatially grounded instruction data.
   Note: See paper for details.
3. **Train 3D-LLM**
   Action: Train an LLM on 3D-language instruction data.
   Why: Adds 3D understanding to the LLM.
   Note: See paper for details.
4. **Evaluate 3D understanding**
   Action: Test on 3D QA, navigation, and grounding tasks.
   Why: Validates 3D spatial reasoning.
   Note: See paper for details.

## Parameters to set
- **num_views** — Role: Views per 3D scene. How to set: 8-16 views for coverage. Default/range: 8-16. Effect: More views capture more spatial information.
- **instruction_count** — Role: Total 3D instructions. How to set: 300K for diverse coverage. Default/range: 300K. Effect: More data improves 3D understanding.

## Validation checks
- The model should answer 3D spatial questions correctly.
- Multi-view features should capture 3D structure.
- 3D instruction data should improve over 2D-only data.

## Failure modes
- Multi-view images may not fully capture 3D structure.
- GPT-4 may generate spatially inaccurate instructions.
- 3D understanding may be limited by view count.

## Adaptation notes for VLM training
- 3D-LLM extends VLM capability to 3D spatial understanding.
- The multi-view instruction generation approach is reusable.
- Combine with 2D instruction data for comprehensive training.

## Implementation notes
- Use efficient multi-view rendering.
- Validate spatial accuracy of generated instructions.
- Evaluate on 3D-specific benchmarks.

## Evidence from the paper
- 3D-LLM creates 300K 3D-language instruction data from multi-view rendering.
- GPT-4 effectively generates 3D-grounded instructions from multi-view context.
- 3D instruction data enables spatial reasoning in LLMs.
- The approach adds 3D understanding to standard LLM architectures.

## Source paper
- **Title**: 3D-LLM: Injecting the 3D World into Large Language Models
- **Year**: 2023
- **Venue**: NeurIPS
- **Paper ID**: arxiv-2307.12981v2
- **URL**: http://arxiv.org/abs/2307.12981v2
- **arXiv ID**: 2307.12981v2
