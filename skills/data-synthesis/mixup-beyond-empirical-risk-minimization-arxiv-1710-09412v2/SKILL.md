# Mixup: Beyond Empirical Risk Minimization

## One-line decision
Use this skill when you want to augment training data by linearly interpolating between pairs of training examples and their labels. Avoid it when you need discrete, unmodified training examples.

## Skill metadata
- **Skill type**: interpolation-augmentation
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Regularize training by creating new examples as linear interpolations of pairs of training examples and their labels, extending training beyond empirical risk minimization.

## Problem signature
- Modality: any modality; demonstrated on images and text.
- Data state: training data augmented with convex combinations of example pairs.
- Scale regime: any dataset size.
- Model requirement: Any differentiable model.

## Use when
- You want a simple, effective data augmentation method.
- You want to regularize training beyond standard techniques.
- Your model overfits on the training data.

## Do not use when
- Simple augmentation is sufficient.
- Your labels are not convex-combinable.
- You need discrete, interpretable training examples.

## Required inputs
- **training_data**: Any labeled training dataset.
- **mixing_distribution**: Beta distribution for mixing coefficient.

## Optional inputs
- **manifold_mixing**: Option to mix in hidden layer space.

## Outputs
- **mixed_examples**: Interpolated training examples with mixed labels.
- **regularized_model**: Model trained with Mixup regularization.

## Assumptions and prerequisites
- Linear interpolation in input space is meaningful.
- Mixed labels provide valid supervision.
- Vicinal risk minimization improves generalization.

## Procedure
1. **Sample mixing coefficient**
   Action: Sample lambda from Beta(alpha, alpha) distribution.
   Why: Beta distribution controls the mixing strength.
   Note: See paper for details.
2. **Interpolate examples**
   Action: Create new examples as lambda*x1 + (1-lambda)*x2.
   Why: Linear interpolation creates virtual training examples.
   Note: See paper for details.
3. **Interpolate labels**
   Action: Create new labels as lambda*y1 + (1-lambda)*y2.
   Why: Mixed labels match the mixed inputs.
   Note: See paper for details.
4. **Train on mixed data**
   Action: Train the model on the mixed examples.
   Why: Mixup regularizes and improves generalization.
   Note: See paper for details.

## Parameters to set
- **alpha** — Role: Beta distribution parameter. How to set: 0.1-0.4 for mild mixing; 1.0 for uniform. Default/range: 0.2-1.0. Effect: Higher alpha creates more aggressive mixing.

## Validation checks
- Mixup should improve generalization metrics.
- Training should be more stable with Mixup.
- The model should be more calibrated.

## Failure modes
- Very aggressive mixing may confuse the model.
- Mixing may not be meaningful for all data types.
- Label smoothing from Mixup may not be desired for all tasks.

## Adaptation notes for VLM training
- Mixup can be applied to VLM pretraining image data.
- Extend to multimodal Mixup by mixing both images and text.
- Combine with CutMix and other augmentation methods.

## Implementation notes
- Implement in the data loader for efficiency.
- Apply Mixup to batches rather than individual examples.
- Use the standard Beta distribution implementation.

## Evidence from the paper
- Mixup improves generalization on ImageNet, CIFAR-10, and many other datasets.
- The method provides a simple form of data augmentation and regularization.
- Mixup improves model calibration and reduces memorization.
- The approach is widely adopted in image classification training.

## Source paper
- **Title**: Mixup: Beyond Empirical Risk Minimization
- **Year**: 2018
- **Venue**: ICLR
- **Paper ID**: arxiv-1710.09412v2
- **URL**: http://arxiv.org/abs/1710.09412v2
- **arXiv ID**: 1710.09412v2
