# LLaVA-Med: Training a Large Language-and-Vision Assistant for Biomedicine in One Day

## One-line decision
Use this skill when you want to generate biomedical visual instruction data by aligning PMC image-caption pairs with LLM-generated QA. Avoid it when you need general-purpose instruction data or lack biomedical image-caption sources.

## Skill metadata
- **Skill type**: domain-specific-instruction-synthesis
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Generate biomedical visual instruction-following data by using GPT-4 to create QA pairs from PubMed Central image-caption pairs, enabling a VLM specialized for biomedical visual understanding.

## Problem signature
- Modality: biomedical images with LLM-generated instruction-following data from PMC figure captions.
- Data state: PMC figure-caption pairs transformed into instruction data via GPT-4.
- Scale regime: 60K biomedical instruction samples.
- Model requirement: GPT-4 for data generation; LLaVA architecture for training.

## Use when
- You need biomedical visual instruction data.
- You have PMC or similar biomedical image-caption pairs.
- You want to adapt a general VLM for biomedical applications.

## Do not use when
- You need general-purpose instruction data.
- You lack biomedical image-caption sources.
- You need clinical-grade annotations requiring expert review.

## Required inputs
- **pmc_image_captions**: Figure-caption pairs from PubMed Central papers.
- **llm_for_generation**: GPT-4 or equivalent for generating QA pairs.
- **base_vlm**: Pre-trained LLaVA or similar VLM for fine-tuning.

## Optional inputs
- **expert_review**: Medical expert review of generated data.

## Outputs
- **biomedical_instruction_data**: 60K biomedical visual instruction samples.
- **llava_med_model**: Biomedical VLM fine-tuned on the generated data.

## Assumptions and prerequisites
- PMC figure captions provide sufficient context for generating meaningful QA.
- GPT-4 can generate medically relevant QA from figure captions.
- Domain-specific fine-tuning improves biomedical visual understanding.

## Procedure
1. **Collect PMC figure-caption pairs**
   Action: Extract figure images and their captions from PubMed Central papers.
   Why: PMC provides high-quality biomedical image-text pairs.
   Note: See paper for details.
2. **Generate instruction data with GPT-4**
   Action: Prompt GPT-4 with figure captions to generate diverse QA pairs.
   Why: LLM generates instruction data without manual annotation.
   Note: See paper for details.
3. **Self-instruct with inline mentions**
   Action: Use in-line figure references in papers as additional context.
   Why: Paper context provides richer information than captions alone.
   Note: See paper for details.
4. **Fine-tune LLaVA on biomedical data**
   Action: Train LLaVA-Med on the generated 60K instruction samples.
   Why: Domain-specific fine-tuning adapts the model for biomedicine.
   Note: See paper for details.

## Parameters to set
- **instruction_count** — Role: Number of generated instruction samples. How to set: 60K covers diverse biomedical topics. Default/range: 60K. Effect: More data improves domain coverage.
- **qa_types** — Role: Types of QA pairs generated. How to set: Include open-ended, multiple-choice, and yes/no. Default/range: Mixed. Effect: Diverse QA types improve versatility.

## Validation checks
- Generated QA should be medically accurate based on the figure captions.
- LLaVA-Med should outperform general LLaVA on biomedical benchmarks.
- The model should handle diverse biomedical imaging modalities.

## Failure modes
- GPT-4 may generate medically inaccurate QA pairs.
- PMC figures may be too specialized for the base VLM's vision encoder.
- Fine-tuning on 60K samples may not be sufficient for all biomedical subfields.

## Adaptation notes for VLM training
- The PMC-to-instruction pipeline can be adapted for other scientific domains.
- Replace GPT-4 with Claude for data generation.
- Extend to radiology, pathology, or other medical imaging specialties.

## Implementation notes
- Use PMC Open Access subset for legal compliance.
- Batch GPT-4 API calls for cost efficiency.
- Validate generated data with medical domain experts.

## Evidence from the paper
- LLaVA-Med generates 60K biomedical instruction samples from PMC figure-caption pairs.
- The model outperforms general VLMs on biomedical visual QA benchmarks.
- Domain-specific instruction tuning is achievable in one day of training.
- The self-instruct approach from PMC data transfers the LLaVA methodology to biomedicine.

## Source paper
- **Title**: LLaVA-Med: Training a Large Language-and-Vision Assistant for Biomedicine in One Day
- **Year**: 2023
- **Venue**: NeurIPS
- **Paper ID**: arxiv-2306.00890v2
- **URL**: http://arxiv.org/abs/2306.00890v2
- **arXiv ID**: 2306.00890v2
