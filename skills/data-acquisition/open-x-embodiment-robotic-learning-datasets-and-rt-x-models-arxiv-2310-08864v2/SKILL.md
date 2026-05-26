# Open X-Embodiment: Robotic Learning Datasets and RT-X Models

## One-line decision
Use this skill when you want to aggregate robot learning data across different embodiments and labs for training generalist robot policies. Avoid it when you are not working with robotics or have data from a single robot type.

## Skill metadata
- **Skill type**: cross-embodiment-robot-data
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Aggregate robotic learning datasets from 22 different robot embodiments across 21 institutions into a unified dataset for training generalist robot policies that transfer across embodiments.

## Problem signature
- Modality: robot trajectories with images, actions, and language instructions across multiple embodiments.
- Data state: aggregated robot demonstration data standardized across 22 embodiments.
- Scale regime: over 1 million robot trajectories from 22 embodiments.
- Model requirement: RT-X models (RT-1, RT-2) trained on cross-embodiment data.

## Use when
- You want to train a generalist robot policy.
- You have robot data from multiple embodiments.
- You need cross-embodiment transfer.

## Do not use when
- You only have data from a single robot.
- Your task is not related to robotics.
- You need real-time policy training rather than offline data.

## Required inputs
- **robot_datasets**: Demonstration datasets from multiple robot embodiments and labs.
- **standardization_format**: Common format for actions, observations, and instructions.
- **aggregation_pipeline**: Pipeline for combining datasets with different formats.

## Optional inputs
- **task_descriptions**: Natural language descriptions of robot tasks.

## Outputs
- **open_x_dataset**: 1M+ trajectories from 22 robot embodiments.
- **rt_x_models**: Generalist robot policies trained on cross-embodiment data.

## Assumptions and prerequisites
- Cross-embodiment data enables better generalization than single-embodiment.
- A common format can accommodate diverse robot embodiments.
- Scale across embodiments improves zero-shot transfer.

## Procedure
1. **Standardize data formats**
   Action: Convert all robot datasets to a common observation-action-language format.
   Why: Standardization enables joint training across embodiments.
   Note: See paper for details.
2. **Aggregate datasets**
   Action: Combine datasets from 22 embodiments and 21 institutions.
   Why: Scale and diversity enable generalist policies.
   Note: See paper for details.
3. **Train RT-X models**
   Action: Train RT-1 and RT-2 on the aggregated data.
   Why: Cross-embodiment training tests generalization.
   Note: See paper for details.
4. **Evaluate transfer**
   Action: Test zero-shot and few-shot transfer to new tasks and embodiments.
   Why: Validates the benefit of cross-embodiment training.
   Note: See paper for details.

## Parameters to set
- **num_embodiments** — Role: Number of robot embodiments. How to set: Include as many diverse embodiments as available. Default/range: 22. Effect: More embodiments improve generalization.
- **total_trajectories** — Role: Total demonstration trajectories. How to set: Aggregate all available data. Default/range: 1M+. Effect: More data enables better policy learning.

## Validation checks
- RT-X should outperform single-embodiment baselines on transfer tasks.
- The aggregated dataset should cover diverse manipulation and navigation tasks.
- Cross-embodiment training should show positive transfer.

## Failure modes
- Action space differences across embodiments may be hard to standardize.
- Some embodiments may dominate training if not balanced.
- Transfer may be limited to similar embodiment types.

## Adaptation notes for VLM training
- The cross-embodiment data aggregation approach applies to any multi-source robot learning.
- VLM-based robot models can leverage this data for vision-language-action training.
- The standardization format is reusable for new embodiments.

## Implementation notes
- Use the RLDS format for standardized data storage.
- Balance sampling across embodiments during training.
- Track per-embodiment performance during evaluation.

## Evidence from the paper
- Open X-Embodiment aggregates data from 22 robot embodiments across 21 institutions.
- RT-X models trained on the aggregated data show significant positive transfer.
- Cross-embodiment training improves performance by 50%+ on multiple evaluation settings.
- The dataset contains over 1 million robot trajectories with diverse tasks.

## Source paper
- **Title**: Open X-Embodiment: Robotic Learning Datasets and RT-X Models
- **Year**: 2023
- **Venue**: ICRA
- **Paper ID**: arxiv-2310.08864v2
- **URL**: http://arxiv.org/abs/2310.08864v2
- **arXiv ID**: 2310.08864v2
