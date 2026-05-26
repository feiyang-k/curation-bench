# Vary: Scaling up the Vision Vocabulary for Large Vision-Language Models

## One-line decision
Use this skill when you want to expand a VLM's vision vocabulary by training additional vision tokens for document, chart, and dense text understanding. Avoid it when CLIP's visual vocabulary is sufficient for your needs.

## Skill metadata
- **Skill type**: vision-vocabulary-scaling-data
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Scale up a VLM's vision vocabulary by generating and training additional vision tokens specifically for document, chart, and dense text content, expanding beyond CLIP's natural image vocabulary.

## Problem signature
- Modality: documents, charts, and dense text images with expanded vision tokens.
- Data state: domain-specific images with new vision token training.
- Scale regime: additional vision token training on domain-specific data.
- Model requirement: VLM with expandable vision vocabulary.

## Use when
- CLIP's vocabulary misses your visual domain.
- You need document, chart, or dense text understanding.
- You want to add domain-specific vision tokens.

## Do not use when
- CLIP's vocabulary covers your needs.
- You do not need domain-specific vision.
- Expanding vocabulary is too complex.

## Required inputs
- **domain_images**: Document, chart, and dense text images.
- **new_vision_tokens**: Additional vision tokens for the new domain.
- **base_vlm**: Existing VLM to expand.

## Optional inputs
- **domain_instruction_data**: Instruction data for the new domain.

## Outputs
- **expanded_vlm**: VLM with expanded vision vocabulary.
- **domain_vision_tokens**: New vision tokens for specialized domains.

## Assumptions and prerequisites
- CLIP's vocabulary may not cover specialized visual domains.
- Additional vision tokens can be trained for new domains.
- Vision vocabulary expansion improves domain-specific understanding.

## Procedure
1. **Identify vocabulary gaps**
   Action: Find visual domains not well covered by CLIP.
   Why: Identifies what needs expansion.
   Note: See paper for details.
2. **Train new vision tokens**
   Action: Generate and train additional tokens for the new domain.
   Why: Expands the vision vocabulary.
   Note: See paper for details.
3. **Integrate with existing VLM**
   Action: Add new tokens to the existing VLM pipeline.
   Why: Extends without disrupting existing capability.
   Note: See paper for details.
4. **Evaluate domain performance**
   Action: Test on domain-specific benchmarks.
   Why: Validates vocabulary expansion benefit.
   Note: See paper for details.

## Parameters to set
- **new_token_count** — Role: Number of new vision tokens. How to set: Based on domain complexity. Default/range: Domain-dependent. Effect: More tokens capture more domain-specific content.
- **domain_data_size** — Role: Amount of domain-specific data. How to set: Sufficient for token training. Default/range: Variable. Effect: More data improves token quality.

## Validation checks
- New tokens should improve domain-specific performance.
- Existing capabilities should not degrade.
- Document/chart understanding should significantly improve.

## Failure modes
- New tokens may conflict with existing vocabulary.
- Domain-specific training may degrade general capability.
- Token expansion increases model complexity.

## Adaptation notes for VLM training
- Vision vocabulary expansion is valuable for specialized VLM domains.
- Apply to medical, scientific, or other specialized visual domains.
- The approach extends any VLM to new visual vocabularies.

## Implementation notes
- Train new tokens without disrupting existing ones.
- Validate on both general and domain-specific benchmarks.
- Monitor for capability regression.

## Evidence from the paper
- Vary expands VLM vision vocabulary for document and chart understanding.
- New vision tokens significantly improve domain-specific performance.
- Vision vocabulary expansion is complementary to instruction tuning.
- The approach extends VLMs to visual domains beyond CLIP's training.

## Source paper
- **Title**: Vary: Scaling up the Vision Vocabulary for Large Vision-Language Models
- **Year**: 2024
- **Venue**: ECCV
- **Paper ID**: arxiv-2312.06109v2
- **URL**: http://arxiv.org/abs/2312.06109v2
- **arXiv ID**: 2312.06109v2
