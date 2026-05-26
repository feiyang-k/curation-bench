# VATEX: A Large-Scale, High-Quality Multilingual Dataset for Video-and-Language Research

## One-line decision
Use this skill when you need a multilingual video captioning dataset with English and Chinese captions for training video-language models. Avoid it when English-only video captions are sufficient.

## Skill metadata
- **Skill type**: multilingual-video-caption-data
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Create a large-scale multilingual video captioning dataset with both English and Chinese captions, enabling multilingual video-language research.

## Problem signature
- Modality: videos with multilingual (English + Chinese) captions.
- Data state: 41K videos with 826K multilingual captions.
- Scale regime: 41K videos, 826K captions in English and Chinese.
- Model requirement: Any video-language model for multilingual training.

## Use when
- You need multilingual video captions.
- You want English-Chinese video-language data.
- You need high-quality video descriptions.

## Do not use when
- English-only is sufficient.
- You do not work with video.
- You need other languages besides English and Chinese.

## Required inputs
- **videos**: 41K diverse video clips.
- **english_captions**: English captions for each video.
- **chinese_captions**: Chinese captions for each video.

## Optional inputs
- **translation_pairs**: Aligned English-Chinese translation pairs.

## Outputs
- **vatex_dataset**: 41K videos with 826K multilingual captions.
- **multilingual_benchmark**: Multilingual video captioning benchmark.

## Assumptions and prerequisites
- Multilingual video captions enable cross-lingual video understanding.
- English and Chinese cover a large fraction of VLM users.
- High-quality captions improve video understanding.

## Procedure
1. **Collect diverse videos**
   Action: Gather 41K diverse video clips.
   Why: Diversity ensures broad coverage.
   Note: See paper for details.
2. **Collect English captions**
   Action: Have annotators write English descriptions.
   Why: English captions are the primary language.
   Note: See paper for details.
3. **Collect Chinese captions**
   Action: Have annotators write Chinese descriptions.
   Why: Chinese captions enable multilingual capability.
   Note: See paper for details.
4. **Create multilingual benchmark**
   Action: Define captioning and retrieval benchmarks.
   Why: Enables standardized evaluation.
   Note: See paper for details.

## Parameters to set
- **num_videos** — Role: Total video clips. How to set: 41K for diversity. Default/range: 41K. Effect: More videos improve coverage.
- **captions_per_video** — Role: Captions per video per language. How to set: 10 English + 10 Chinese. Default/range: 20 total. Effect: More captions improve diversity.

## Validation checks
- Captions should accurately describe video content.
- Multilingual captions should be consistent in meaning.
- The dataset should cover diverse activities and scenes.

## Failure modes
- Translation quality may vary.
- Some videos may be culturally specific.
- Multilingual annotation is expensive.

## Adaptation notes for VLM training
- VATEX enables multilingual video VLM training.
- English-Chinese bilingual data serves two major language groups.
- Combine with other video datasets for comprehensive training.

## Implementation notes
- Handle multilingual text correctly.
- Evaluate in both languages.
- Track per-language captioning quality.

## Evidence from the paper
- VATEX provides 41K videos with 826K multilingual captions.
- English and Chinese captions enable bilingual video understanding.
- High-quality captions improve video-language training.
- The dataset enables multilingual video captioning research.

## Source paper
- **Title**: VATEX: A Large-Scale, High-Quality Multilingual Dataset for Video-and-Language Research
- **Year**: 2019
- **Venue**: ICCV
- **Paper ID**: arxiv-1904.03493v6
- **URL**: http://arxiv.org/abs/1904.03493v6
- **arXiv ID**: 1904.03493v6
