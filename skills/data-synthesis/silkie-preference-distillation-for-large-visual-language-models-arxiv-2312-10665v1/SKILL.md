# Silkie: Preference Distillation for Large Visual Language Models

## One-line decision
Use this skill when you want to generate preference data for VLM alignment using AI feedback instead of human feedback. Avoid it when you can collect human preferences or do not need preference-based alignment.

## Skill metadata
- **Skill type**: ai-generated-preference-data
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Generate preference data for VLM alignment using AI feedback from a strong VLM judge, enabling DPO-based alignment without expensive human preference collection.

## Problem signature
- Modality: VLM outputs with AI-generated preference rankings.
- Data state: VLM outputs scored by an AI judge for preference distillation.
- Scale regime: 80K AI-generated preference samples.
- Model requirement: Strong VLM judge (GPT-4V) for scoring; target VLM for DPO training.

## Use when
- You want preference data without human annotation.
- You can use an AI judge for preference scoring.
- You want DPO-based VLM alignment.

## Do not use when
- You can collect human preferences.
- AI feedback quality is insufficient.
- You do not need preference-based alignment.

## Required inputs
- **vlm_outputs**: Multiple VLM outputs for the same inputs.
- **ai_judge**: Strong VLM (GPT-4V) for preference scoring.
- **dpo_framework**: DPO implementation for preference-based training.

## Optional inputs
- **scoring_criteria**: Criteria for the AI judge to evaluate outputs.

## Outputs
- **ai_preferences**: 80K AI-scored preference pairs.
- **aligned_vlm**: VLM aligned through DPO on AI preferences.

## Assumptions and prerequisites
- AI judges can provide reliable preference signals.
- DPO effectively uses AI-generated preferences.
- AI feedback is a scalable alternative to human feedback.

## Procedure
1. **Generate multiple VLM outputs**
   Action: Generate multiple responses from VLMs for each input.
   Why: Multiple outputs provide candidates for preference ranking.
   Note: See paper for details.
2. **Score with AI judge**
   Action: Use GPT-4V to score and rank the outputs.
   Why: AI feedback provides scalable preference data.
   Note: See paper for details.
3. **Format preference pairs**
   Action: Create chosen/rejected pairs from AI rankings.
   Why: DPO requires preference pairs.
   Note: See paper for details.
4. **Train with DPO**
   Action: Fine-tune the target VLM using DPO on AI preferences.
   Why: DPO aligns the model to prefer high-quality outputs.
   Note: See paper for details.

## Parameters to set
- **num_candidates** — Role: Number of VLM outputs per input. How to set: 2-5 candidates. Default/range: 3-5. Effect: More candidates enable better preference selection.
- **judge_model** — Role: AI model for preference scoring. How to set: Use the strongest available VLM. Default/range: GPT-4V. Effect: Better judges produce better preferences.
- **preference_samples** — Role: Total preference pairs. How to set: 80K for effective alignment. Default/range: 80K. Effect: More pairs improve alignment quality.

## Validation checks
- AI preferences should correlate with human preferences.
- DPO training should improve output quality.
- Hallucination should decrease after alignment.

## Failure modes
- AI judges may have systematic biases.
- The judge's capabilities limit preference quality.
- DPO may not fully capture complex preferences.

## Adaptation notes for VLM training
- AI-generated preferences are increasingly used for VLM alignment.
- Replace GPT-4V with Claude as the AI judge.
- Combine AI and human preferences for hybrid alignment.

## Implementation notes
- Design clear scoring criteria for the AI judge.
- Compare AI vs human preferences on a subset.
- Monitor alignment quality across training.

## Evidence from the paper
- Silkie generates 80K preference pairs using GPT-4V as an AI judge.
- DPO on AI-generated preferences effectively aligns VLMs.
- AI feedback provides a scalable alternative to human preference collection.
- The approach reduces hallucination and improves output quality.

## Source paper
- **Title**: Silkie: Preference Distillation for Large Visual Language Models
- **Year**: 2023
- **Venue**: arXiv
- **Paper ID**: arxiv-2312.10665v1
- **URL**: http://arxiv.org/abs/2312.10665v1
- **arXiv ID**: 2312.10665v1
