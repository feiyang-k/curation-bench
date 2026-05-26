# PaLI: A Jointly-Scaled Multilingual Language-Image Model

## One-line decision
Use this skill when you want to train a multilingual vision-language model using web-scale multilingual image-text data. Avoid it when you only need English language VLM capabilities.

## Skill metadata
- **Skill type**: multilingual-image-text-data
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Train a multilingual vision-language model using WebLI, a web-scale dataset of 10 billion image-text pairs spanning 100+ languages, jointly scaling both vision and language components.

## Problem signature
- Modality: multilingual image-text pairs from the web.
- Data state: 10B multilingual image-text pairs from the web.
- Scale regime: 10 billion image-text pairs across 100+ languages.
- Model requirement: ViT-e (4B) + mT5-XXL (13B) for joint vision-language training.

## Use when
- You need a multilingual VLM.
- You have access to or can build multilingual image-text data.
- You want vision-language capabilities in non-English languages.

## Do not use when
- You only need English VLM capabilities.
- You cannot collect multilingual image-text data.
- You need a lightweight model.

## Required inputs
- **webli_data**: 10B multilingual image-text pairs from the web.
- **multilingual_text_encoder**: mT5 or similar multilingual text model.
- **vit_encoder**: Large-scale ViT vision encoder.

## Optional inputs
- **language_specific_data**: Additional data for specific languages.

## Outputs
- **pali_model**: Multilingual VLM handling 100+ languages.
- **webli_dataset**: 10B multilingual image-text pairs.

## Assumptions and prerequisites
- Web data contains sufficient multilingual image-text pairs.
- Joint scaling of vision and language improves both.
- Multilingual training enables cross-lingual visual understanding.

## Procedure
1. **Collect WebLI**
   Action: Extract multilingual image-text pairs from the web across 100+ languages.
   Why: Multilingual web data provides broad language coverage.
   Note: See paper for details.
2. **Scale vision encoder**
   Action: Train ViT-e (4B parameters) for maximum visual capability.
   Why: Larger vision encoders capture more visual detail.
   Note: See paper for details.
3. **Scale language model**
   Action: Use mT5-XXL (13B) for multilingual text understanding.
   Why: Large multilingual LM handles diverse languages.
   Note: See paper for details.
4. **Joint training**
   Action: Train jointly on the multilingual image-text data.
   Why: Joint training aligns vision and multilingual language.
   Note: See paper for details.

## Parameters to set
- **num_languages** — Role: Number of languages in training data. How to set: 100+ for broad coverage. Default/range: 100+. Effect: More languages improve multilingual capability.
- **vision_scale** — Role: Size of vision encoder. How to set: ViT-e (4B) for maximum capability. Default/range: 4B. Effect: Larger encoder improves visual understanding.
- **data_scale** — Role: Total image-text pairs. How to set: 10B for comprehensive coverage. Default/range: 10B. Effect: More data improves both coverage and quality.

## Validation checks
- Multilingual captioning should work across diverse languages.
- VQA should be language-agnostic.
- Translation quality should be competitive.

## Failure modes
- Low-resource languages may have insufficient data.
- Multilingual training may dilute per-language performance.
- The model is very large and expensive to train.

## Adaptation notes for VLM training
- The WebLI collection approach applies to any multilingual VLM.
- Use PaLI's data recipe for building multilingual VLM training data.
- Multilingual capability is increasingly important for global VLM deployment.

## Implementation notes
- Balance training across languages to prevent English dominance.
- Monitor per-language performance.
- Use language tags for targeted evaluation.

## Evidence from the paper
- PaLI is trained on WebLI, 10 billion image-text pairs spanning 100+ languages.
- Joint scaling of vision (4B ViT-e) and language (13B mT5-XXL) produces strong results.
- The model achieves state-of-the-art on multilingual vision-language benchmarks.
- PaLI demonstrates effective multilingual visual understanding.

## Source paper
- **Title**: PaLI: A Jointly-Scaled Multilingual Language-Image Model
- **Year**: 2022
- **Venue**: ICLR
- **Paper ID**: arxiv-2209.06794v4
- **URL**: http://arxiv.org/abs/2209.06794v4
- **arXiv ID**: 2209.06794v4
