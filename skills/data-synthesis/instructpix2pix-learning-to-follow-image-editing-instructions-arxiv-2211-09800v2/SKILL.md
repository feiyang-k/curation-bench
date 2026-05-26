# InstructPix2Pix: Learning to Follow Image Editing Instructions

## One-line decision
Use this skill when you want to generate synthetic image editing instruction data by combining GPT-3 text editing with Prompt-to-Prompt image editing. Avoid it when you have real image editing data or do not need editing capability.

## Skill metadata
- **Skill type**: synthetic-image-editing-data
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Generate synthetic image editing instruction data by using GPT-3 to create text editing instructions and Prompt-to-Prompt to produce corresponding edited images, training a model to follow image editing instructions.

## Problem signature
- Modality: image editing triplets: (input image, editing instruction, edited image).
- Data state: synthetically generated editing instruction-image triplets.
- Scale regime: 454K synthetic editing triplets.
- Model requirement: Stable Diffusion fine-tuned for conditional image editing.

## Use when
- You need image editing instruction data.
- You can generate synthetic editing pairs.
- You want a model that follows natural language editing instructions.

## Do not use when
- You have real editing datasets.
- Image editing is not your focus.
- Synthetic editing quality is insufficient.

## Required inputs
- **gpt3_api**: GPT-3 for generating editing instructions.
- **prompt_to_prompt**: Prompt-to-Prompt for generating edited images.
- **stable_diffusion**: Stable Diffusion base model.

## Optional inputs
- **quality_filter**: Filter for removing bad editing pairs.

## Outputs
- **editing_dataset**: 454K synthetic editing instruction triplets.
- **instructpix2pix**: Model that follows image editing instructions.

## Assumptions and prerequisites
- GPT-3 can generate diverse editing instructions.
- Prompt-to-Prompt produces corresponding edited images.
- Synthetic editing data enables learning instruction-following editing.

## Procedure
1. **Generate editing instructions with GPT-3**
   Action: Create text descriptions of image edits.
   Why: GPT-3 produces diverse editing instructions.
   Note: See paper for details.
2. **Generate image pairs with Prompt-to-Prompt**
   Action: Use P2P to create input-output image pairs matching the edits.
   Why: P2P generates corresponding edited images.
   Note: See paper for details.
3. **Filter synthetic pairs**
   Action: Remove low-quality or inconsistent triplets.
   Why: Quality filtering improves training data.
   Note: See paper for details.
4. **Train InstructPix2Pix**
   Action: Fine-tune Stable Diffusion on the editing triplets.
   Why: Learns to follow editing instructions.
   Note: See paper for details.

## Parameters to set
- **triplet_count** — Role: Total editing triplets. How to set: 454K for diverse coverage. Default/range: 454K. Effect: More triplets improve editing diversity.
- **editing_types** — Role: Types of edits generated. How to set: Include style, object, attribute, and compositional edits. Default/range: Diverse. Effect: More types improve editing versatility.

## Validation checks
- Edited images should match the editing instruction.
- The model should handle diverse editing types.
- Synthetic quality should be sufficient for training.

## Failure modes
- Prompt-to-Prompt may not accurately reflect all edits.
- Some editing instructions may be too complex.
- Synthetic pairs may have artifacts.

## Adaptation notes for VLM training
- Image editing data extends VLM capabilities to generation.
- The synthetic data generation approach applies to any paired task.
- Combine editing capability with understanding for versatile VLMs.

## Implementation notes
- Use GPT-3 for diverse instruction generation.
- Apply Prompt-to-Prompt for consistent editing.
- Filter rigorously for quality.

## Evidence from the paper
- InstructPix2Pix generates 454K synthetic editing instruction triplets.
- The model learns to follow diverse image editing instructions.
- Synthetic generation combines GPT-3 text editing with P2P image editing.
- The approach enables instruction-following image editing without real editing data.

## Source paper
- **Title**: InstructPix2Pix: Learning to Follow Image Editing Instructions
- **Year**: 2023
- **Venue**: CVPR
- **Paper ID**: arxiv-2211.09800v2
- **URL**: http://arxiv.org/abs/2211.09800v2
- **arXiv ID**: 2211.09800v2
