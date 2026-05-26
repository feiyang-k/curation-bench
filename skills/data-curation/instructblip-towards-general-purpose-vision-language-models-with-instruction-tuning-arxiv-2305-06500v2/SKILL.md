# InstructBLIP: Towards General-purpose Vision-Language Models with Instruction Tuning

## One-line decision
Use this skill when you want to curate multi-task instruction data and make the vision encoder instruction-aware for better VLM fine-tuning. Avoid it when you have a single task and do not need instruction-conditioned visual feature extraction.

## Skill metadata
- **Skill type**: instruction-aware-feature-extraction
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Transform 26 existing vision-language datasets into instruction-tuning format and train an instruction-aware Q-Former that extracts visual features conditioned on the instruction text.

## Problem signature
- Modality: image-text instruction-response pairs from 26 transformed academic datasets.
- Data state: existing VL datasets reformatted as instruction-following tasks grouped into held-in and held-out clusters.
- Scale regime: 26 datasets spanning 13 held-in tasks for training and 13 held-out tasks for evaluation.
- Model requirement: BLIP-2 architecture with instruction-aware Q-Former and frozen LLM.

## Use when
- You have multiple VL datasets to combine via instruction formatting.
- You want the vision encoder to extract task-relevant features based on the instruction.
- You need zero-shot transfer to unseen VL tasks.

## Do not use when
- You have a single-task setup where instruction-conditioning is unnecessary.
- You lack the 26 academic datasets for training.
- You need a simpler architecture without Q-Former complexity.

## Required inputs
- **vl_datasets**: 26 vision-language datasets transformed into instruction format.
- **blip2_pretrained**: BLIP-2 pre-trained weights for initialization.
- **instruction_templates**: Templates for converting each dataset into instruction-response format.

## Optional inputs
- **held_out_tasks**: 13 unseen tasks for zero-shot evaluation.

## Outputs
- **instructblip_model**: Instruction-aware VLM with Q-Former.
- **instruction_formatted_data**: 26 datasets in unified instruction format.

## Assumptions and prerequisites
- Instruction-conditioning helps the vision encoder extract task-relevant features.
- Multi-task instruction tuning improves zero-shot transfer.
- Academic datasets provide diverse, high-quality supervision.

## Procedure
1. **Transform datasets into instruction format**
   Action: Convert 26 VL datasets into instruction-response pairs using task-specific templates.
   Why: Unified format enables multi-task training.
   Note: See paper for details.
2. **Make Q-Former instruction-aware**
   Action: Feed instruction text to Q-Former alongside image to condition feature extraction.
   Why: Task-relevant visual features improve downstream performance.
   Note: See paper for details.
3. **Balance multi-task training**
   Action: Sample from datasets using balanced ratios to prevent dominant tasks from overwhelming.
   Why: Balanced sampling ensures diverse capability development.
   Note: See paper for details.
4. **Train on held-in tasks**
   Action: Fine-tune InstructBLIP on 13 held-in task clusters.
   Why: Multi-task training builds broad VL capabilities.
   Note: See paper for details.
5. **Evaluate on held-out tasks**
   Action: Test zero-shot performance on 13 unseen task clusters.
   Why: Measures instruction-following generalization.
   Note: See paper for details.

## Parameters to set
- **num_datasets** — Role: Number of datasets in the instruction mix. How to set: Include all available high-quality VL datasets. Default/range: 26. Effect: More datasets improve diversity and generalization.
- **sampling_ratio** — Role: Relative sampling probability per dataset. How to set: Balance by dataset size and task difficulty. Default/range: Task-dependent. Effect: Imbalanced sampling biases toward dominant datasets.
- **instruction_template_style** — Role: Format of instruction prompts. How to set: Natural language questions and instructions. Default/range: Multiple templates per task. Effect: Template diversity improves robustness.

## Validation checks
- Held-out task performance should exceed non-instruction-tuned baselines.
- The instruction-aware Q-Former should outperform a static Q-Former.
- All held-in tasks should maintain competitive performance.

## Failure modes
- Some datasets may dominate training if sampling is unbalanced.
- Instruction templates may not generalize to novel phrasings.
- The Q-Former may overfit to common instruction patterns.

## Adaptation notes for VLM training
- The multi-dataset instruction formatting approach is reusable for any VLM.
- Extend the dataset collection with additional domain-specific datasets.
- The instruction-aware feature extraction idea generalizes beyond Q-Former.

## Implementation notes
- Use stratified batch sampling to include all datasets in each epoch.
- Store instruction templates separately for easy modification.
- Track per-dataset performance during training.

## Evidence from the paper
- InstructBLIP achieves state-of-the-art zero-shot performance on 13 held-out VL benchmarks.
- Instruction-aware Q-Former extracts more task-relevant visual features than a static Q-Former.
- Transforming 26 datasets into instruction format enables effective multi-task training.
- InstructBLIP outperforms BLIP-2, MiniGPT-4, and LLaVA on most benchmarks.

## Source paper
- **Title**: InstructBLIP: Towards General-purpose Vision-Language Models with Instruction Tuning
- **Year**: 2023
- **Venue**: NeurIPS
- **Paper ID**: arxiv-2305.06500v2
- **URL**: http://arxiv.org/abs/2305.06500v2
- **arXiv ID**: 2305.06500v2
