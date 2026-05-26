# GPT-4V(ision) System Card

## One-line decision
Use this skill when you want to understand safety evaluation and mitigation strategies for deploying multimodal LLMs. Avoid it when safety evaluation is not your focus.

## Skill metadata
- **Skill type**: multimodal-safety-evaluation
- **Paper kind**: operational-method
- **Actionability**: medium
- **Evidence quality**: full_paper

## Goal
Document safety evaluation and mitigation strategies for deploying GPT-4V, covering multimodal safety risks, evaluation methodologies, and mitigations for responsible VLM deployment.

## Problem signature
- Modality: multimodal safety evaluation data and methodologies.
- Data state: safety evaluation datasets and red-team results.
- Scale regime: comprehensive safety evaluation.
- Model requirement: GPT-4V for evaluation; principles apply to any VLM.

## Use when
- You are deploying a VLM and need safety evaluation.
- You want to understand multimodal safety risks.
- You need safety mitigation strategies.

## Do not use when
- Safety evaluation is not your current focus.
- You have established safety evaluation processes.
- You need implementation rather than evaluation guidance.

## Required inputs
- **vlm_to_evaluate**: VLM being evaluated for safety.
- **safety_datasets**: Datasets testing various safety dimensions.
- **red_team**: Red-team evaluators for adversarial testing.

## Optional inputs
- **mitigation_strategies**: Strategies for addressing identified risks.

## Outputs
- **safety_assessment**: Comprehensive safety evaluation results.
- **mitigation_plan**: Plan for addressing safety risks.

## Assumptions and prerequisites
- Multimodal models introduce new safety risks beyond text-only.
- Comprehensive evaluation identifies actionable risks.
- Mitigations can reduce but not eliminate all risks.

## Procedure
1. **Evaluate visual safety risks**
   Action: Test for risks specific to visual inputs (deepfakes, privacy, etc.).
   Why: Visual modality introduces unique risks.
   Note: See paper for details.
2. **Red-team testing**
   Action: Have adversarial testers probe for safety failures.
   Why: Red-teaming reveals risks not caught by automated tests.
   Note: See paper for details.
3. **Assess cross-modal risks**
   Action: Test for risks that emerge from combining modalities.
   Why: Cross-modal interactions can create new risks.
   Note: See paper for details.
4. **Develop mitigations**
   Action: Design and implement safety mitigations.
   Why: Mitigations reduce identified risks.
   Note: See paper for details.

## Parameters to set
- **evaluation_dimensions** — Role: Safety dimensions evaluated. How to set: Cover content safety, privacy, fairness, misuse. Default/range: Comprehensive. Effect: More dimensions provide broader safety coverage.
- **red_team_diversity** — Role: Diversity of red-team evaluators. How to set: Include diverse perspectives and expertise. Default/range: Diverse. Effect: Diverse red-teaming catches more risks.

## Validation checks
- Identified risks should be reproducible.
- Mitigations should reduce risk levels.
- Evaluation should cover multimodal-specific risks.

## Failure modes
- Some risks may not be caught by evaluation.
- Mitigations may have side effects.
- Safety evaluation may lag behind capability development.

## Adaptation notes for VLM training
- Apply GPT-4V safety evaluation methodology to your VLM.
- Use multimodal safety datasets for training safety filters.
- Safety evaluation should be continuous, not one-time.

## Implementation notes
- Build a comprehensive safety evaluation pipeline.
- Include red-teaming in your evaluation process.
- Monitor safety metrics post-deployment.

## Evidence from the paper
- GPT-4V System Card documents comprehensive multimodal safety evaluation.
- Multimodal models introduce unique safety risks beyond text-only.
- Red-teaming reveals risks not caught by automated evaluation.
- Safety mitigations reduce but cannot eliminate all risks.

## Source paper
- **Title**: GPT-4V(ision) System Card
- **Year**: 2023
- **Venue**: OpenAI
- **Paper ID**: openai-gpt4v-2023
- **URL**: https://openai.com/research/gpt-4v-system-card
- **arXiv ID**: N/A
