# Improved Baselines with Visual Instruction Tuning

## One-line decision
Use this skill when you want to curate a high-quality academic-task-oriented instruction dataset for VLM fine-tuning. Avoid it when you need only synthetic conversation data or cannot access the academic VQA datasets.

## Skill metadata
- **Skill type**: instruction-data-curation
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Curate a high-quality, diverse instruction-tuning dataset by combining academic task-oriented VQA data with GPT-4V-generated visual conversations to improve VLM fine-tuning baselines.

## Problem signature
- Modality: image-text instruction-response pairs mixing academic VQA and synthetic conversation data.
- Data state: combination of existing academic VQA datasets reformatted as instructions plus synthetic conversation data.
- Scale regime: 665K instruction samples for fine-tuning.
- Model requirement: CLIP ViT-L/14@336 + Vicuna/LLaMA with two-layer MLP projection.

## Use when
- You want to improve VLM instruction-following by incorporating academic VQA datasets.
- You need a curated mix of data types (VQA, OCR, region-level, conversation) for fine-tuning.
- You want simple but effective improvements over the original LLaVA recipe.

## Do not use when
- You cannot access the academic datasets (VQAv2, GQA, OCR-VQA, etc.).
- You only need a model for a single specific task.
- You need multi-image or video understanding.

## Required inputs
- **academic_vqa_datasets**: Reformatted VQAv2, GQA, OCR-VQA, TextVQA, and VisualGenome QA as instruction-following format.
- **synthetic_conversation_data**: GPT-4V-generated visual conversation data (LLaVA-Instruct-150K).
- **pretrained_components**: CLIP ViT-L/14@336 and Vicuna/LLaMA language model.

## Optional inputs
- **sharegpt_data**: Additional ShareGPT text-only conversation data mixed in for language ability preservation.

## Outputs
- **curated_instruction_mix**: 665K instruction-following samples balancing academic and synthetic data.
- **llava_1_5_model**: Improved VLM baseline (LLaVA-1.5) achieving strong benchmark performance.

## Assumptions and prerequisites
- Academic VQA datasets provide grounded, factual supervision that reduces hallucination.
- A balanced mix of data types produces a more capable generalist model.
- Simple architectural improvements (MLP projection, higher resolution) compound with better data.

## Procedure
1. **Reformat academic datasets as instructions**
   Action: Convert VQAv2, GQA, OCR-VQA, TextVQA, and VisualGenome region QA into instruction-response format.
   Why: Standardizes diverse datasets into a unified training format.
   Note: See paper for details.
2. **Combine with synthetic conversation data**
   Action: Mix reformatted academic data with LLaVA-Instruct-150K conversation data.
   Why: Provides both factual grounding and conversational ability.
   Note: See paper for details.
3. **Add text-only conversation data**
   Action: Include ShareGPT text-only data to preserve language model capabilities.
   Why: Prevents catastrophic forgetting of language abilities during visual fine-tuning.
   Note: See paper for details.
4. **Pre-train projection with CC595K**
   Action: Train 2-layer MLP projection on a filtered 595K subset of CC3M.
   Why: Aligns visual features to language model space.
   Note: Higher resolution (336px) and MLP projection are key improvements.
5. **Fine-tune on curated instruction mix**
   Action: Fine-tune the full model on the 665K curated instruction dataset.
   Why: Teaches the model to follow diverse visual instructions.
   Note: See paper for details.

## Parameters to set
- **image_resolution** — Role: Input image resolution for CLIP encoder. How to set: Use 336x336 for improved detail recognition. Default/range: 336. Effect: Higher resolution significantly improves OCR and fine-grained tasks.
- **projection_type** — Role: Vision-language bridge architecture. How to set: Use 2-layer MLP instead of linear. Default/range: 2-layer MLP. Effect: MLP projection outperforms linear projection.
- **data_mix** — Role: Ratio of academic vs synthetic data. How to set: Include all academic data plus conversation data. Default/range: ~515K academic + 150K synthetic. Effect: Academic data grounds the model; synthetic data teaches conversation.

## Validation checks
- Performance should improve on VQAv2, GQA, TextVQA, and conversational benchmarks.
- Hallucination rate should decrease with academic data inclusion.
- The model should maintain strong language capabilities from ShareGPT mixing.

## Failure modes
- Over-reliance on academic data may reduce conversational naturalness.
- Dataset-specific biases from VQA benchmarks may transfer to the model.
- The mix ratio needs tuning; wrong balance can hurt specific capabilities.

## Adaptation notes for VLM training
- The LLaVA-1.5 data recipe has become a standard baseline for VLM instruction tuning.
- Extend with additional academic datasets (DocVQA, ChartQA) for document understanding.
- The MLP projection + academic data recipe transfers to other VLM architectures.

## Implementation notes
- Use the LLaVA codebase for data formatting and training pipeline.
- Academic datasets need careful reformatting to preserve answer quality.
- Monitor per-dataset performance during training to detect imbalances.

## Evidence from the paper
- LLaVA-1.5 achieves state-of-the-art results across 11 benchmarks with a simple recipe: MLP projection, academic task data, and higher resolution.
- Adding academic VQA data (VQAv2, GQA, OCR-VQA, TextVQA) to instruction tuning significantly improves grounded understanding.
- The 665K instruction mix balances factual accuracy from academic data with conversational ability from synthetic data.
- LLaVA-1.5 13B achieves 80.0% on VQAv2, 63.3% on GQA, and 61.3% on TextVQA.

## Source paper
- **Title**: Improved Baselines with Visual Instruction Tuning
- **Year**: 2023
- **Venue**: CVPR
- **Paper ID**: arxiv-2310.03744v2
- **URL**: http://arxiv.org/abs/2310.03744v2
- **arXiv ID**: 2310.03744v2
