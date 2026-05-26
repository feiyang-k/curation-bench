# Llama Guard: LLM-based Input-Output Safeguard for Human-AI Conversations

## One-line decision
Use this skill when you want to train a safety classifier for filtering harmful content in LLM/VLM inputs and outputs. Avoid it when you do not need safety filtering or have an existing safety classifier.

## Skill metadata
- **Skill type**: safety-classification-data
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Train an LLM-based safety classifier (Llama Guard) that can filter harmful content in both inputs to and outputs from LLMs/VLMs, using a taxonomy of safety categories.

## Problem signature
- Modality: text inputs and outputs classified for safety across multiple categories.
- Data state: labeled safety classification data across a taxonomy of harm categories.
- Scale regime: thousands of safety-labeled examples.
- Model requirement: Fine-tuned LLaMA for safety classification.

## Use when
- You need to filter harmful VLM inputs or outputs.
- You want a customizable safety taxonomy.
- You need production-grade content safety.

## Do not use when
- Safety filtering is not required.
- You have an existing safety classifier.
- You need visual safety classification (Llama Guard is text-focused).

## Required inputs
- **safety_taxonomy**: Taxonomy of harm categories.
- **labeled_examples**: Conversation examples labeled as safe or unsafe per category.
- **base_llm**: LLaMA model for fine-tuning as safety classifier.

## Optional inputs
- **custom_categories**: Additional domain-specific safety categories.

## Outputs
- **llama_guard**: Safety classifier for input-output filtering.
- **safety_labels**: Per-conversation safety classifications.

## Assumptions and prerequisites
- An LLM can be fine-tuned as an effective safety classifier.
- A taxonomy-based approach enables customizable safety.
- Both inputs and outputs need safety filtering.

## Procedure
1. **Define safety taxonomy**
   Action: Create a taxonomy of harm categories.
   Why: The taxonomy defines what is considered unsafe.
   Note: See paper for details.
2. **Collect labeled data**
   Action: Label conversations as safe/unsafe for each category.
   Why: Training data for the safety classifier.
   Note: See paper for details.
3. **Fine-tune Llama Guard**
   Action: Fine-tune LLaMA on the safety classification task.
   Why: Creates a specialized safety classifier.
   Note: See paper for details.
4. **Deploy for filtering**
   Action: Use Llama Guard to filter inputs and outputs in production.
   Why: Ensures safety in deployed VLM systems.
   Note: See paper for details.

## Parameters to set
- **safety_categories** — Role: Categories of harm to detect. How to set: Based on safety requirements and regulations. Default/range: 6 categories. Effect: More categories provide finer safety control.
- **threshold** — Role: Confidence threshold for unsafe classification. How to set: Balance safety with false positive rate. Default/range: Task-dependent. Effect: Lower threshold catches more but has more false positives.

## Validation checks
- The classifier should accurately detect unsafe content.
- False positive rate should be acceptable.
- All safety categories should be covered.

## Failure modes
- The classifier may miss subtle unsafe content.
- Overly strict filtering may reject safe content.
- The taxonomy may not cover all safety concerns.

## Adaptation notes for VLM training
- Use Llama Guard for VLM safety filtering.
- Extend the taxonomy for multimodal safety concerns.
- Combine with visual safety classifiers for complete VLM safety.

## Implementation notes
- Use the Llama Guard codebase for deployment.
- Monitor safety metrics in production.
- Update the taxonomy as new safety concerns emerge.

## Evidence from the paper
- Llama Guard provides LLM-based input-output safety classification.
- The taxonomy-based approach enables customizable safety filtering.
- The classifier achieves high accuracy on safety benchmarks.
- Llama Guard is widely used for LLM/VLM safety in production.

## Source paper
- **Title**: Llama Guard: LLM-based Input-Output Safeguard for Human-AI Conversations
- **Year**: 2024
- **Venue**: arXiv
- **Paper ID**: arxiv-2312.06674v2
- **URL**: http://arxiv.org/abs/2312.06674v2
- **arXiv ID**: 2312.06674v2
