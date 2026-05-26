# BiomedCLIP: A Multimodal Biomedical Foundation Model Pretrained from Fifteen Million Scientific Image-Text Pairs

## One-line decision
Use this skill when you want to build a biomedical CLIP model trained on 15M scientific image-text pairs from PMC. Avoid it when you need a general-purpose CLIP model or lack access to PMC data.

## Skill metadata
- **Skill type**: scientific-image-text-collection
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Curate PMC-15M, a dataset of 15 million biomedical image-text pairs from PubMed Central, and train BiomedCLIP, a domain-specific contrastive model for biomedical visual understanding.

## Problem signature
- Modality: biomedical images paired with figure captions from PubMed Central.
- Data state: 15M figure-caption pairs extracted and curated from PMC papers.
- Scale regime: 15 million biomedical image-text pairs.
- Model requirement: CLIP architecture (ViT + PubMedBERT) trained with contrastive loss.

## Use when
- You need a biomedical vision-language model.
- You want to use PMC figure-caption pairs for domain-specific pretraining.
- You need biomedical image-text retrieval or zero-shot classification.

## Do not use when
- You need a general-purpose CLIP model.
- You lack access to PMC papers.
- You need a generative model rather than contrastive.

## Required inputs
- **pmc_papers**: PubMed Central papers with figure-caption pairs.
- **extraction_pipeline**: Pipeline for extracting figures and captions from papers.
- **clip_architecture**: ViT + PubMedBERT dual-encoder architecture.

## Optional inputs
- **quality_filters**: Filters for removing low-quality figure-caption pairs.

## Outputs
- **pmc_15m_dataset**: 15M biomedical image-text pairs from PMC.
- **biomedclip_model**: Biomedical contrastive model.

## Assumptions and prerequisites
- PMC figure-caption pairs provide high-quality biomedical supervision.
- Domain-specific pretraining outperforms general CLIP for biomedical tasks.
- 15M pairs are sufficient for effective biomedical CLIP training.

## Procedure
1. **Extract figures from PMC papers**
   Action: Parse PMC papers to extract figure images and associated captions.
   Why: PMC is the largest source of open-access biomedical figures.
   Note: See paper for details.
2. **Clean and filter pairs**
   Action: Remove low-resolution figures, uninformative captions, and duplicates.
   Why: Quality filtering improves training data.
   Note: See paper for details.
3. **Train BiomedCLIP**
   Action: Train ViT + PubMedBERT with contrastive loss on PMC-15M.
   Why: Domain-specific CLIP captures biomedical visual-textual patterns.
   Note: See paper for details.
4. **Evaluate on biomedical benchmarks**
   Action: Test on medical image classification, retrieval, and VQA.
   Why: Validates domain-specific pretraining effectiveness.
   Note: See paper for details.

## Parameters to set
- **dataset_size** — Role: Number of PMC image-text pairs. How to set: Extract all available figures from PMC-OA. Default/range: 15M. Effect: More data improves domain coverage.
- **text_encoder** — Role: Text encoder architecture. How to set: Use PubMedBERT for biomedical text understanding. Default/range: PubMedBERT. Effect: Domain-specific text encoder improves alignment.

## Validation checks
- BiomedCLIP should outperform general CLIP on biomedical benchmarks.
- The dataset should cover diverse biomedical imaging modalities.
- Zero-shot classification should be effective for medical image types.

## Failure modes
- Some PMC figures are diagrams or charts rather than medical images.
- Caption quality varies across papers and journals.
- The model may overfit to the PMC data distribution.

## Adaptation notes for VLM training
- BiomedCLIP is used as a vision encoder for biomedical VLMs.
- The PMC extraction pipeline can be extended to other scientific databases.
- Combine with clinical data for broader medical coverage.

## Implementation notes
- Use the S2ORC pipeline for efficient PMC processing.
- Filter by figure type (photograph, diagram, chart) for targeted datasets.
- Cache extracted figure-caption pairs for reuse.

## Evidence from the paper
- BiomedCLIP is trained on PMC-15M, 15 million figure-caption pairs from PubMed Central.
- The model outperforms general CLIP on medical image classification by large margins.
- PubMedBERT as text encoder improves biomedical text understanding.
- BiomedCLIP achieves state-of-the-art on multiple biomedical VL benchmarks.

## Source paper
- **Title**: BiomedCLIP: A Multimodal Biomedical Foundation Model Pretrained from Fifteen Million Scientific Image-Text Pairs
- **Year**: 2023
- **Venue**: arXiv
- **Paper ID**: arxiv-2303.00915v4
- **URL**: http://arxiv.org/abs/2303.00915v4
- **arXiv ID**: 2303.00915v4
