# WizardLM: Empowering Large Language Models to Follow Complex Instructions

## One-line decision
Use this skill when you want to progressively increase instruction complexity through evolution prompts (deepening, widening, adding constraints). Avoid it when you need simple instructions or cannot afford iterative evolution.

## Skill metadata
- **Skill type**: evol-instruct-complexity-scaling
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Scale instruction complexity through Evol-Instruct, progressively evolving simple instructions into more complex ones via deepening, widening, adding constraints, and increasing reasoning steps.

## Problem signature
- Modality: text instructions evolved through multiple complexity stages.
- Data state: simple seed instructions evolved into complex multi-step instructions.
- Scale regime: 250K evolved instruction samples.
- Model requirement: LLM for instruction evolution; any LLM for fine-tuning.

## Use when
- You want to create complex, multi-step instructions.
- You have simple instructions to evolve into harder ones.
- You want progressive complexity scaling.

## Do not use when
- Simple instructions are sufficient.
- You cannot afford iterative LLM evolution.
- Domain-specific complexity cannot be captured by generic evolution.

## Required inputs
- **seed_instructions**: Simple starting instructions.
- **evolution_llm**: LLM for evolving instructions (GPT-3.5/4).
- **evolution_prompts**: Prompts for deepening, widening, and constraint-adding.

## Optional inputs
- **difficulty_filter**: Filter for removing too-easy or too-hard evolutions.

## Outputs
- **evolved_instructions**: 250K complexity-scaled instruction samples.
- **wizardlm_model**: LLM fine-tuned on evolved instructions.

## Assumptions and prerequisites
- Progressive complexity evolution creates harder, more valuable instructions.
- Evolution prompts can reliably increase instruction complexity.
- Complex instructions teach deeper reasoning abilities.

## Procedure
1. **Start with seed instructions**
   Action: Begin with a set of simple instructions.
   Why: Seeds provide the starting point for evolution.
   Note: See paper for details.
2. **Apply evolution prompts**
   Action: Use deepening, widening, constraint-adding, and reasoning prompts to evolve instructions.
   Why: Each evolution type increases complexity differently.
   Note: See paper for details.
3. **Filter evolved instructions**
   Action: Remove evolutions that are too simple, too complex, or incoherent.
   Why: Quality filtering ensures useful training data.
   Note: See paper for details.
4. **Iterate evolution**
   Action: Apply multiple rounds of evolution for progressive complexity.
   Why: Multiple rounds create increasingly complex instructions.
   Note: See paper for details.
5. **Fine-tune on evolved data**
   Action: Train the target model on the evolved instruction set.
   Why: Complex instructions teach advanced reasoning.
   Note: See paper for details.

## Parameters to set
- **evolution_types** — Role: Types of complexity evolution. How to set: Include deepening, widening, constraints, reasoning. Default/range: 4+ types. Effect: More types create diverse complexity.
- **evolution_rounds** — Role: Number of evolution iterations. How to set: 2-4 rounds per instruction. Default/range: 2-4. Effect: More rounds increase complexity.
- **difficulty_range** — Role: Target difficulty range. How to set: Filter very easy and very hard. Default/range: Medium to hard. Effect: Controls instruction difficulty distribution.

## Validation checks
- Evolved instructions should be genuinely more complex than seeds.
- The model should handle complex, multi-step instructions.
- Quality should be maintained through evolution rounds.

## Failure modes
- Evolution may produce incoherent or unsolvable instructions.
- Complexity may increase without adding meaningful difficulty.
- Multiple rounds may compound errors.

## Adaptation notes for VLM training
- Evol-Instruct can be adapted for visual instruction complexity scaling.
- Apply to VLM instruction data for more challenging visual reasoning tasks.
- The evolution approach generalizes to any instruction data domain.

## Implementation notes
- Track complexity metrics across evolution rounds.
- Use diverse evolution prompts for varied complexity types.
- Monitor instruction quality at each evolution stage.

## Evidence from the paper
- WizardLM's Evol-Instruct progressively increases instruction complexity.
- Complex evolved instructions improve model performance on challenging tasks.
- The approach creates 250K instructions spanning diverse difficulty levels.
- WizardLM outperforms Alpaca and Vicuna on complex instruction benchmarks.

## Source paper
- **Title**: WizardLM: Empowering Large Language Models to Follow Complex Instructions
- **Year**: 2023
- **Venue**: ICLR
- **Paper ID**: arxiv-2304.12244v2
- **URL**: http://arxiv.org/abs/2304.12244v2
- **arXiv ID**: 2304.12244v2
