# LLaVA-Critic: Learning to Evaluate Multimodal Models

## One-line decision
Use this skill when you want to train a VLM to evaluate its own outputs for self-improvement without external AI judges. Avoid it when you have access to external AI judges or do not need self-evaluation.

## Skill metadata
- **Skill type**: self-evaluation-data
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Train a VLM as its own critic to evaluate multimodal outputs, enabling self-improvement through self-evaluation without requiring external AI judges like GPT-4V.

## Problem signature
- Modality: VLM outputs with self-generated evaluation scores and critiques.
- Data state: evaluation training data teaching the VLM to judge output quality.
- Scale regime: hundreds of thousands of evaluation training samples.
- Model requirement: LLaVA-based VLM trained for both response generation and evaluation.

## Use when
- You want your VLM to evaluate its own outputs.
- You want self-improvement without external AI judges.
- You need a critic model for preference data generation.

## Do not use when
- External AI judges are available and affordable.
- You do not need self-evaluation capability.
- Simple rule-based evaluation is sufficient.

## Required inputs
- **vlm_outputs**: VLM outputs to evaluate.
- **evaluation_training_data**: Data teaching the VLM to judge quality.
- **evaluation_criteria**: Criteria for output quality assessment.

## Optional inputs
- **reference_evaluations**: Reference evaluations from external judges for calibration.

## Outputs
- **critic_model**: VLM capable of self-evaluation.
- **evaluation_scores**: Self-generated quality scores for VLM outputs.

## Assumptions and prerequisites
- VLMs can learn to evaluate their own outputs.
- Self-evaluation enables self-improvement.
- Training with evaluation data teaches critical judgment.

## Procedure
1. **Collect evaluation training data**
   Action: Create data pairing VLM outputs with quality scores and critiques.
   Why: Teaches the VLM to evaluate outputs.
   Note: See paper for details.
2. **Train critic capability**
   Action: Fine-tune the VLM on evaluation data.
   Why: Adds self-evaluation to the model's capabilities.
   Note: See paper for details.
3. **Generate self-evaluations**
   Action: Use the critic to score and rank its own outputs.
   Why: Self-evaluation enables preference data generation.
   Note: See paper for details.
4. **Self-improve with DPO**
   Action: Use self-generated preferences for DPO alignment.
   Why: Self-improvement without external judges.
   Note: See paper for details.

## Parameters to set
- **evaluation_data_size** — Role: Amount of evaluation training data. How to set: Hundreds of thousands of samples. Default/range: Variable. Effect: More data improves evaluation quality.
- **evaluation_dimensions** — Role: Dimensions of quality assessed. How to set: Include accuracy, helpfulness, safety. Default/range: Multi-dimensional. Effect: More dimensions provide richer evaluation.

## Validation checks
- Self-evaluation should correlate with human judgment.
- Self-improvement should measurably improve output quality.
- The critic should generalize to unseen output types.

## Failure modes
- Self-evaluation may reinforce existing biases.
- The critic may not accurately judge its own errors.
- Self-improvement may plateau quickly.

## Adaptation notes for VLM training
- Self-evaluation enables scalable VLM alignment without external APIs.
- Train domain-specific critics for targeted self-improvement.
- Combine self-evaluation with external evaluation for robust alignment.

## Implementation notes
- Calibrate self-evaluations against human judgments.
- Use self-evaluation for iterative self-improvement.
- Monitor evaluation quality across improvement rounds.

## Evidence from the paper
- LLaVA-Critic trains a VLM to evaluate multimodal outputs.
- Self-evaluation enables preference data generation without external judges.
- Self-improvement through self-evaluation improves VLM quality.
- The approach provides a scalable alternative to external AI judge dependency.

## Source paper
- **Title**: LLaVA-Critic: Learning to Evaluate Multimodal Models
- **Year**: 2024
- **Venue**: arXiv
- **Paper ID**: arxiv-2410.02712v1
- **URL**: http://arxiv.org/abs/2410.02712v1
- **arXiv ID**: 2410.02712v1
