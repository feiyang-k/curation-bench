# InternLM-XComposer2: Mastering Free-form Text-Image Composition and Comprehension

## One-line decision
Use this skill when you want training data for a VLM that can both understand and compose interleaved text-image content like articles. Avoid it when you only need image understanding without composition.

## Skill metadata
- **Skill type**: text-image-composition-data
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Create training data for a VLM that masters both understanding and composing free-form interleaved text-image content, enabling article-style multimodal generation.

## Problem signature
- Modality: interleaved text-image content for both understanding and composition.
- Data state: instruction data for both comprehension and composition of text-image content.
- Scale regime: curated instruction data for comprehension and composition.
- Model requirement: InternLM-XComposer2 with partial LoRA.

## Use when
- You want a VLM that composes text-image articles.
- You need both comprehension and composition capability.
- You can curate composition training data.

## Do not use when
- Understanding-only is sufficient.
- You do not need article-style composition.
- Composition data is unavailable.

## Required inputs
- **comprehension_data**: Instruction data for image understanding.
- **composition_data**: Instruction data for composing text-image content.
- **interleaved_format**: Format for interleaved text-image composition.

## Optional inputs
- **article_examples**: Example articles for composition training.

## Outputs
- **xcomposer2_model**: VLM for text-image comprehension and composition.
- **composition_pipeline**: Pipeline for text-image article generation.

## Assumptions and prerequisites
- Comprehension and composition are complementary capabilities.
- Curated composition data enables article-style generation.
- Partial LoRA enables efficient capability addition.

## Procedure
1. **Curate comprehension data**
   Action: Collect standard VLM instruction data for understanding.
   Why: Foundation of visual understanding.
   Note: See paper for details.
2. **Curate composition data**
   Action: Create data for composing interleaved text-image content.
   Why: Teaches article-style composition.
   Note: See paper for details.
3. **Train with partial LoRA**
   Action: Use LoRA on specific modules for efficient training.
   Why: Efficient capability addition.
   Note: See paper for details.
4. **Evaluate both capabilities**
   Action: Test on comprehension and composition benchmarks.
   Why: Validates dual capability.
   Note: See paper for details.

## Parameters to set
- **comprehension_ratio** — Role: Ratio of comprehension to composition data. How to set: Balance both capabilities. Default/range: Balanced. Effect: Affects relative capability strength.

## Validation checks
- Comprehension should be competitive with specialized models.
- Composition should produce coherent text-image articles.
- Both capabilities should coexist without interference.

## Failure modes
- Composition may produce incoherent content.
- Training for two capabilities may cause interference.
- Composition data is harder to curate.

## Adaptation notes for VLM training
- Text-image composition extends VLM capability beyond understanding.
- Composition data can be generated from existing articles.
- The dual-capability approach is valuable for content creation.

## Implementation notes
- Use partial LoRA for efficient training.
- Balance comprehension and composition data.
- Evaluate with both automated and human metrics.

## Evidence from the paper
- InternLM-XComposer2 masters both comprehension and composition.
- Partial LoRA enables efficient dual-capability training.
- The model generates coherent interleaved text-image articles.
- Dual capability does not significantly degrade either task.

## Source paper
- **Title**: InternLM-XComposer2: Mastering Free-form Text-Image Composition and Comprehension
- **Year**: 2024
- **Venue**: CVPR
- **Paper ID**: arxiv-2401.16420v2
- **URL**: http://arxiv.org/abs/2401.16420v2
- **arXiv ID**: 2401.16420v2
