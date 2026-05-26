# Orca: Progressive Learning from Complex Explanation Traces of GPT-4

## One-line decision
Use this skill when you want to distill reasoning capability by generating step-by-step explanation traces from a strong teacher model. Avoid it when you do not need reasoning capability or have sufficient reasoning data.

## Skill metadata
- **Skill type**: explanation-trace-distillation
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Distill reasoning capability from GPT-4 to a smaller model by generating step-by-step explanation traces that reveal the teacher's reasoning process, enabling the student to learn not just answers but how to reason.

## Problem signature
- Modality: text instructions with step-by-step explanation traces from GPT-4.
- Data state: instructions augmented with detailed GPT-4 explanation traces.
- Scale regime: 5M explanation traces from ChatGPT + 1M from GPT-4.
- Model requirement: GPT-4 and ChatGPT for trace generation; LLaMA-13B for student training.

## Use when
- You want to teach reasoning ability to a smaller model.
- You can generate explanation traces from a strong teacher.
- You need models that show their reasoning process.

## Do not use when
- Simple instruction following is sufficient.
- You cannot afford trace generation from strong models.
- Your task does not require step-by-step reasoning.

## Required inputs
- **task_instructions**: Instructions requiring step-by-step reasoning.
- **teacher_model**: GPT-4 for generating detailed explanation traces.
- **system_prompts**: System prompts guiding step-by-step explanation generation.

## Optional inputs
- **progressive_curriculum**: Schedule for training on easier then harder traces.

## Outputs
- **explanation_traces**: 5M ChatGPT + 1M GPT-4 explanation traces.
- **orca_model**: Student model trained on explanation traces.

## Assumptions and prerequisites
- Explanation traces teach reasoning process, not just answers.
- Progressive learning from easier to harder traces improves learning.
- GPT-4 traces contain transferable reasoning patterns.

## Procedure
1. **Design system prompts for reasoning**
   Action: Create system prompts that elicit step-by-step explanations.
   Why: System prompts control the detail and style of explanations.
   Note: See paper for details.
2. **Generate traces from teachers**
   Action: Generate 5M traces from ChatGPT and 1M from GPT-4.
   Why: Large-scale trace generation provides diverse reasoning examples.
   Note: See paper for details.
3. **Progressive training**
   Action: Train the student first on ChatGPT traces, then on GPT-4 traces.
   Why: Progressive difficulty improves learning efficiency.
   Note: See paper for details.
4. **Evaluate reasoning**
   Action: Test on reasoning benchmarks to measure transferred reasoning ability.
   Why: Validates that reasoning capability transfers through traces.
   Note: See paper for details.

## Parameters to set
- **trace_detail** — Role: Level of detail in explanation traces. How to set: Use system prompts requesting step-by-step reasoning. Default/range: Detailed step-by-step. Effect: More detail teaches finer-grained reasoning.
- **progressive_stages** — Role: Number of progressive training stages. How to set: 2 stages (ChatGPT then GPT-4). Default/range: 2. Effect: Progressive difficulty improves learning.
- **trace_count** — Role: Total number of explanation traces. How to set: 5M + 1M for comprehensive coverage. Default/range: 6M total. Effect: More traces improve reasoning diversity.

## Validation checks
- The student model should show improved reasoning compared to standard instruction tuning.
- Explanation traces should be detailed and logically coherent.
- Progressive training should outperform single-stage training.

## Failure modes
- GPT-4 may generate incorrect reasoning traces.
- The student may learn to mimic trace style without genuine reasoning.
- Very long traces may exceed context window limits.

## Adaptation notes for VLM training
- Apply explanation trace distillation to visual reasoning in VLMs.
- Generate visual reasoning traces for image-based tasks.
- The progressive learning approach generalizes to multimodal distillation.

## Implementation notes
- Use varied system prompts for diverse reasoning styles.
- Monitor reasoning quality in generated traces.
- Evaluate on diverse reasoning benchmarks.

## Evidence from the paper
- Orca learns from 5M ChatGPT and 1M GPT-4 explanation traces.
- Explanation traces teach reasoning process, not just correct answers.
- Progressive learning from easier to harder traces improves student performance.
- Orca-13B matches or exceeds ChatGPT on several reasoning benchmarks.

## Source paper
- **Title**: Orca: Progressive Learning from Complex Explanation Traces of GPT-4
- **Year**: 2023
- **Venue**: arXiv
- **Paper ID**: arxiv-2306.02707v1
- **URL**: http://arxiv.org/abs/2306.02707v1
- **arXiv ID**: 2306.02707v1
