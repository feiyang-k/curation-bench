# Dolphins: Multimodal Language Model for Driving

## One-line decision
Use this skill when you want to create instruction data for an autonomous driving VLM using BDD-X driving dataset with explanations. Avoid it when you do not work with autonomous driving.

## Skill metadata
- **Skill type**: driving-instruction-data
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Create instruction data for autonomous driving VLMs using the BDD-X dataset which provides driving action explanations, enabling a VLM to understand and explain driving decisions.

## Problem signature
- Modality: driving video with action explanations for instruction tuning.
- Data state: driving videos with action-explanation pairs from BDD-X.
- Scale regime: driving instruction data from BDD-X.
- Model requirement: VLM adapted for driving with grounded reasoning.

## Use when
- You want a VLM that explains driving decisions.
- You have BDD-X driving data.
- You need interpretable driving AI.

## Do not use when
- Driving AI is not your focus.
- You lack driving video data.
- Simple perception is sufficient.

## Required inputs
- **bdd_x_data**: BDD-X driving videos with action explanations.
- **instruction_format**: Format for driving instruction tuning.
- **vlm_architecture**: VLM adapted for driving.

## Optional inputs
- **additional_driving_data**: Extra driving datasets for diversity.

## Outputs
- **driving_instructions**: Driving instruction data with explanations.
- **dolphins_model**: VLM for driving understanding and explanation.

## Assumptions and prerequisites
- BDD-X explanations provide useful training signal.
- VLMs can learn to explain driving decisions.
- Instruction format enables conversational driving understanding.

## Procedure
1. **Format BDD-X as instructions**
   Action: Convert BDD-X action-explanation data to instruction format.
   Why: Instruction format enables VLM training.
   Note: See paper for details.
2. **Train driving VLM**
   Action: Fine-tune VLM on driving instruction data.
   Why: Develops driving understanding.
   Note: See paper for details.
3. **Evaluate explanation quality**
   Action: Test driving explanations and reasoning.
   Why: Validates interpretable driving AI.
   Note: See paper for details.

## Parameters to set
- **explanation_detail** — Role: Detail level of driving explanations. How to set: Use BDD-X explanations as-is. Default/range: BDD-X level. Effect: More detail improves explanation quality.

## Validation checks
- Driving explanations should be accurate.
- The model should understand driving scenarios.
- Explanations should be helpful for understanding.

## Failure modes
- BDD-X explanations may not cover all scenarios.
- Driving data is domain-specific.
- Explanation quality depends on data quality.

## Adaptation notes for VLM training
- Driving instruction data extends VLM to autonomous driving.
- BDD-X provides ready driving explanations for training.
- Combine with general VLM data for balanced capability.

## Implementation notes
- Use BDD-X data with proper formatting.
- Evaluate on driving-specific benchmarks.
- Compare to general VLMs on driving tasks.

## Evidence from the paper
- Dolphins uses BDD-X driving explanations for VLM instruction tuning.
- The model learns to explain driving decisions.
- Driving instruction data enables domain-specific VLM capability.
- Interpretable driving AI benefits from VLM-based explanation.

## Source paper
- **Title**: Dolphins: Multimodal Language Model for Driving
- **Year**: 2023
- **Venue**: arXiv
- **Paper ID**: arxiv-2312.00438v2
- **URL**: http://arxiv.org/abs/2312.00438v2
- **arXiv ID**: 2312.00438v2
