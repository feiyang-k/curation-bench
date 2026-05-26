# Direct Preference Optimization: Your Language Model is Secretly a Reward Model

## One-line decision
Use this skill when you want to align a language/vision-language model using preference data without training a separate reward model. Avoid it when you prefer RLHF with explicit reward models or do not have preference data.

## Skill metadata
- **Skill type**: preference-optimization-training
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Align language and vision-language models using preference data directly through DPO, bypassing the need for a separate reward model and the complexity of PPO optimization.

## Problem signature
- Modality: preference pairs (chosen/rejected) for any LLM/VLM task.
- Data state: preference pairs comparing better and worse model outputs.
- Scale regime: thousands to hundreds of thousands of preference pairs.
- Model requirement: Any LLM/VLM for DPO fine-tuning.

## Use when
- You have preference data (chosen/rejected pairs).
- You want simpler alignment than RLHF+PPO.
- You want to avoid training a separate reward model.

## Do not use when
- You prefer explicit reward modeling.
- You do not have preference data.
- Online RL is preferred over offline optimization.

## Required inputs
- **preference_pairs**: Chosen/rejected output pairs for the same inputs.
- **base_model**: Pre-trained LLM/VLM to align.
- **dpo_loss**: DPO loss function.

## Optional inputs
- **reference_model**: Frozen reference model for KL regularization.

## Outputs
- **aligned_model**: LLM/VLM aligned through DPO.
- **preference_log**: Training log with DPO loss and preference accuracy.

## Assumptions and prerequisites
- Preferences implicitly define a reward function.
- DPO's closed-form solution avoids the instability of PPO.
- Offline preference optimization is effective for alignment.

## Procedure
1. **Collect preference pairs**
   Action: Gather chosen/rejected pairs from human or AI feedback.
   Why: Preferences provide the alignment signal.
   Note: See paper for details.
2. **Format for DPO**
   Action: Structure data as (input, chosen, rejected) triples.
   Why: DPO requires paired comparisons.
   Note: See paper for details.
3. **Train with DPO loss**
   Action: Optimize the DPO objective on the preference data.
   Why: DPO directly aligns the model without a reward model.
   Note: See paper for details.
4. **Evaluate alignment**
   Action: Test for improved output quality and reduced issues.
   Why: Validates the alignment effect.
   Note: See paper for details.

## Parameters to set
- **beta** — Role: KL regularization strength in DPO. How to set: 0.1-0.5. Default/range: 0.1. Effect: Higher beta prevents over-optimization.
- **learning_rate** — Role: Learning rate for DPO fine-tuning. How to set: Lower than standard fine-tuning. Default/range: 5e-7. Effect: Too high may destabilize.

## Validation checks
- Aligned model should prefer chosen over rejected outputs.
- Output quality should improve post-alignment.
- The model should not degrade on general capabilities.

## Failure modes
- DPO is sensitive to preference data quality.
- High beta may prevent meaningful alignment.
- The method assumes binary preferences are well-calibrated.

## Adaptation notes for VLM training
- DPO is widely used for VLM alignment (LLaVA-RLHF, Silkie, etc.).
- Generate preference pairs using AI judges for scalable DPO data.
- DPO is simpler and more stable than PPO-based RLHF.

## Implementation notes
- Use the TRL library for DPO implementation.
- Start with beta=0.1 and adjust based on results.
- Monitor preference accuracy during training.

## Evidence from the paper
- DPO aligns language models using preference data without reward model training.
- The approach is simpler and more stable than RLHF with PPO.
- DPO has been widely adopted for both LLM and VLM alignment.
- DPO matches or exceeds PPO-based RLHF on alignment benchmarks.

## Source paper
- **Title**: Direct Preference Optimization: Your Language Model is Secretly a Reward Model
- **Year**: 2023
- **Venue**: NeurIPS
- **Paper ID**: arxiv-2305.18290v2
- **URL**: http://arxiv.org/abs/2305.18290v2
- **arXiv ID**: 2305.18290v2
