# Label Noise SGD Provably Prefers Flat Global Minimizers

## One-line decision
Use this skill when you want to understand how label noise in training data affects optimization and generalization, particularly for noisy web data. Avoid it when you do not deal with noisy labels.

## Skill metadata
- **Skill type**: noise-robust-training
- **Paper kind**: operational-method
- **Actionability**: medium
- **Evidence quality**: full_paper

## Goal
Understand how label noise in training data affects SGD optimization, showing that moderate noise can bias toward flat minima that generalize better.

## Problem signature
- Modality: any modality with potentially noisy labels.
- Data state: training data with label noise.
- Scale regime: theoretical analysis applicable to any scale.
- Model requirement: Any SGD-trained model.

## Use when
- You train on noisy web-crawled data.
- You want to understand noise effects on generalization.
- You need theoretical grounding for noise tolerance.

## Do not use when
- Your data is clean.
- Noise theory is not relevant.
- You need practical noise reduction.

## Required inputs
- **noisy_data**: Training data with label noise.
- **sgd_training**: SGD optimizer.

## Optional inputs
- **noise_level_analysis**: Analysis at different noise levels.

## Outputs
- **theoretical_insights**: Understanding of noise effects on optimization.
- **practical_guidance**: Guidance for training with noisy data.

## Assumptions and prerequisites
- Moderate label noise can be beneficial for generalization.
- SGD with noise biases toward flat minima.
- Understanding noise effects improves training recipe design.

## Procedure
1. **Analyze noise effects**
   Action: Study how label noise affects SGD optimization.
   Why: Understanding noise informs training design.
   Note: See paper for details.
2. **Identify beneficial noise levels**
   Action: Determine when noise helps generalization.
   Why: Some noise may be beneficial.
   Note: See paper for details.
3. **Apply to practical training**
   Action: Use insights for training on noisy web data.
   Why: Practical application of theory.
   Note: See paper for details.

## Parameters to set
- **noise_level** — Role: Amount of label noise. How to set: Moderate noise may be tolerable. Default/range: Dataset-dependent. Effect: Too much noise hurts; some may help.

## Validation checks
- Moderate noise should not severely hurt generalization.
- Models should converge despite noise.
- Insights should apply to web-scale noisy data.

## Failure modes
- Too much noise degrades training.
- Theory may not apply perfectly to practice.
- Noise effects depend on model architecture.

## Adaptation notes for VLM training
- Noise tolerance insights apply to VLM training on noisy web data.
- Understanding noise helps design appropriate filtering thresholds.
- Some noise in image-text data may be tolerable or even beneficial.

## Implementation notes
- Monitor training with noisy data carefully.
- Compare to clean data baselines.
- Use noise analysis to set filtering thresholds.

## Evidence from the paper
- Label noise in SGD training biases toward flat, generalizable minima.
- Moderate noise can improve generalization.
- Understanding noise effects helps design training on noisy web data.
- The theoretical insights apply to practical noisy data training.

## Source paper
- **Title**: Label Noise SGD Provably Prefers Flat Global Minimizers
- **Year**: 2022
- **Venue**: NeurIPS
- **Paper ID**: arxiv-2106.06530v4
- **URL**: http://arxiv.org/abs/2106.06530v4
- **arXiv ID**: 2106.06530v4
