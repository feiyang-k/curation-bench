# Otter: A Multi-Modal Model with In-Context Instruction Tuning

## One-line decision
Use this skill when you want to create instruction data that includes in-context examples for multi-modal in-context learning. Avoid it when you do not need in-context learning capability in your VLM.

## Skill metadata
- **Skill type**: in-context-instruction-data
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Create instruction tuning data that includes in-context examples alongside the instruction, enabling a multi-modal model (based on Flamingo) to learn in-context instruction following.

## Problem signature
- Modality: multi-modal instruction data with in-context examples.
- Data state: instruction data augmented with in-context examples from MIMIC-IT.
- Scale regime: 2.8M instruction samples with in-context examples.
- Model requirement: OpenFlamingo architecture for in-context learning.

## Use when
- You want a VLM with in-context learning capability.
- You can create instruction data with in-context examples.
- You need few-shot adaptation without fine-tuning.

## Do not use when
- In-context learning is not needed.
- You cannot create in-context example data.
- Zero-shot performance is sufficient.

## Required inputs
- **base_instructions**: Standard instruction data.
- **in_context_examples**: Example input-output pairs for in-context learning.
- **flamingo_architecture**: OpenFlamingo for in-context processing.

## Optional inputs
- **example_selection**: Strategy for selecting in-context examples.

## Outputs
- **mimic_it_data**: 2.8M instruction samples with in-context examples.
- **otter_model**: VLM with in-context instruction following.

## Assumptions and prerequisites
- In-context examples improve instruction following.
- Multi-modal in-context learning is learnable.
- The OpenFlamingo architecture supports in-context examples.

## Procedure
1. **Create MIMIC-IT dataset**
   Action: Generate 2.8M instruction samples with paired in-context examples.
   Why: In-context examples teach the model to learn from examples.
   Note: See paper for details.
2. **Format with in-context structure**
   Action: Structure data as (context examples, query, response).
   Why: Explicit structure teaches in-context learning.
   Note: See paper for details.
3. **Train Otter**
   Action: Fine-tune OpenFlamingo on MIMIC-IT data.
   Why: In-context instruction tuning enables few-shot adaptation.
   Note: See paper for details.
4. **Evaluate in-context performance**
   Action: Test with varying numbers of in-context examples.
   Why: Validates in-context learning capability.
   Note: See paper for details.

## Parameters to set
- **num_context_examples** — Role: Number of in-context examples per instruction. How to set: 1-4 examples. Default/range: 2-4. Effect: More examples improve in-context performance.
- **data_scale** — Role: Total instruction samples. How to set: 2.8M for comprehensive coverage. Default/range: 2.8M. Effect: More data improves in-context generalization.

## Validation checks
- Performance should improve with more in-context examples.
- In-context learning should generalize to new tasks.
- The model should outperform zero-shot baselines with few examples.

## Failure modes
- In-context examples may not always be helpful.
- Example selection affects performance significantly.
- The Flamingo architecture adds complexity.

## Adaptation notes for VLM training
- MIMIC-IT provides a template for in-context instruction data creation.
- In-context learning capability is valuable for rapid VLM adaptation.
- The approach extends to any VLM architecture supporting multiple images.

## Implementation notes
- Use the OpenFlamingo codebase for training.
- Carefully select in-context examples for quality.
- Track per-example-count performance.

## Evidence from the paper
- Otter trains on 2.8M instruction samples with in-context examples.
- In-context instruction tuning enables few-shot multi-modal learning.
- MIMIC-IT provides comprehensive in-context instruction data.
- The model demonstrates improved performance with in-context examples.

## Source paper
- **Title**: Otter: A Multi-Modal Model with In-Context Instruction Tuning
- **Year**: 2023
- **Venue**: arXiv
- **Paper ID**: arxiv-2305.03726v2
- **URL**: http://arxiv.org/abs/2305.03726v2
- **arXiv ID**: 2305.03726v2
