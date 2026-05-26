# Visual Instruction Tuning

## One-line decision
Use this skill when you want to generate multimodal instruction-following data by prompting a text-only LLM with image captions and bounding boxes. Avoid it when you have abundant human-annotated instruction data or need the LLM to see actual images during data generation.

## Skill metadata
- **Skill type**: instruction-data-synthesis
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Generate multimodal instruction-following data by leveraging text-only GPT-4 with image captions and bounding boxes as context, then use this synthetic data to train a vision-language model (LLaVA) for visual instruction following.

## Problem signature
- Modality: image-text instruction-following pairs synthesized from image captions and bounding box annotations.
- Data state: COCO images with existing captions and bounding box annotations used to generate instruction data via LLM.
- Scale regime: 158K instruction-following samples synthesized from COCO images.
- Model requirement: A text-only LLM (GPT-4) for data generation; CLIP ViT-L + Vicuna for the trained VLM.

## Use when
- You need instruction-following data for visual tasks but lack human annotations.
- You have image captions and object annotations that can seed LLM-based data generation.
- You want to fine-tune a VLM for conversational visual understanding.

## Do not use when
- You have abundant human-annotated visual instruction data.
- The images lack any existing annotations (captions, boxes) to ground the LLM generation.
- You need pixel-perfect or region-level instruction data.

## Required inputs
- **source_images**: Images with existing annotations (e.g., COCO images with captions and bounding boxes).
- **text_llm**: A powerful text-only LLM (e.g., GPT-4) to generate instruction-response pairs from textual descriptions of images.
- **prompt_templates**: Prompt templates for conversation, detail description, and complex reasoning data types.

## Optional inputs
- **human_seed_examples**: Small set of human-written examples to guide the LLM in each data type.
- **quality_filter**: Rules to filter out low-quality or hallucinated instruction-response pairs.

## Outputs
- **instruction_following_data**: 158K multimodal instruction-following samples covering conversation (58K), detail description (23K), and complex reasoning (77K).
- **trained_vlm**: LLaVA model fine-tuned on the synthetic instruction data.

## Assumptions and prerequisites
- A text-only LLM can generate faithful visual instruction data from textual descriptions of images.
- Image captions and bounding boxes provide sufficient context for the LLM to reason about the image.
- Three types of instruction data (conversation, detail, reasoning) provide comprehensive coverage.

## Procedure
1. **Prepare image context as text**
   Action: Convert image annotations (captions, bounding boxes with labels) into textual descriptions for the LLM.
   Why: Text-only LLMs cannot process images directly.
   Note: Use COCO captions and detection annotations.
2. **Design prompt templates for three data types**
   Action: Create few-shot prompts for conversation, detailed description, and complex reasoning.
   Why: Different data types teach different visual understanding capabilities.
   Note: See paper for details.
3. **Generate instruction data with LLM**
   Action: Prompt GPT-4 with image context and templates to generate question-answer pairs.
   Why: LLM generates diverse, high-quality instruction-response pairs.
   Note: Generate 158K samples total across three types.
4. **Pre-train visual projection**
   Action: Train a linear projection from CLIP ViT-L to Vicuna using CC3M caption data.
   Why: Aligns visual features with the language model's input space.
   Note: See paper for details.
5. **Fine-tune on instruction data**
   Action: Fine-tune the full LLaVA model on the 158K synthetic instruction samples.
   Why: Teaches the model to follow visual instructions in conversation.
   Note: See paper for details.

## Parameters to set
- **data_type_ratio** — Role: Balance between conversation, detail, and reasoning samples. How to set: Use roughly 37% conversation, 14% detail, 49% reasoning. Default/range: 58K:23K:77K. Effect: Reasoning-heavy mix improves complex visual understanding.
- **projection_type** — Role: Architecture bridging vision encoder to LLM. How to set: Start with linear projection; MLP may improve later. Default/range: Linear. Effect: Linear is simple and effective for initial alignment.
- **base_llm** — Role: Language model backbone. How to set: Use Vicuna-13B for best quality. Default/range: Vicuna-7B or 13B. Effect: Larger LLMs generate better responses.

## Validation checks
- Generated instruction data should be visually grounded (not hallucinated from text alone).
- LLaVA should improve on visual conversation benchmarks after fine-tuning.
- The three data types should be distinguishable in style and complexity.

## Failure modes
- The text-only LLM may hallucinate visual details not present in the captions or boxes.
- Generated data inherits biases from COCO annotations and the LLM.
- Complex reasoning data may contain logical errors when the LLM lacks visual grounding.

## Adaptation notes for VLM training
- This data generation pipeline has been widely adopted and extended (LLaVA-1.5, LLaVA-NeXT, etc.).
- Replace GPT-4 with Claude or open-source LLMs for cost-effective generation.
- Extend the pipeline to video, 3D, or document understanding by changing the context format.

## Implementation notes
- Use structured prompts with clear role separation (system, human, assistant).
- Generate data in batches and inspect random samples for quality.
- Store raw LLM responses alongside parsed instruction pairs for debugging.

## Evidence from the paper
- LLaVA generates 158K language-image instruction-following samples using GPT-4 with image captions and bounding boxes as context.
- The generated data covers three types: multi-turn conversation (58K), detailed description (23K), and complex reasoning (77K).
- LLaVA, trained on this synthetic data, achieves an 85.1% relative score compared to GPT-4 on a synthetic multimodal benchmark.
- Visual instruction tuning with machine-generated data is an effective and affordable approach to building general-purpose visual assistants.

## Source paper
- **Title**: Visual Instruction Tuning
- **Year**: 2023
- **Venue**: NeurIPS
- **Paper ID**: arxiv-2304.08485v2
- **URL**: http://arxiv.org/abs/2304.08485v2
- **arXiv ID**: 2304.08485v2
