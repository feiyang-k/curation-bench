# Learning Transferable Visual Models From Natural Language Supervision

## One-line decision
Use this skill when you need to construct a large-scale image-text dataset from the web for contrastive vision-language pretraining. Avoid it when you already have curated paired data or need fine-grained region-level annotations.

## Skill metadata
- **Skill type**: web-scale-data-collection
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Construct a web-scale image-text pair dataset (WIT-400M) and train a contrastive vision-language model (CLIP) that learns transferable visual representations from natural language supervision.

## Problem signature
- Modality: image-text pairs scraped from the internet.
- Data state: raw web pages with co-occurring images and text; must be filtered and paired.
- Scale regime: 400 million image-text pairs for pretraining.
- Model requirement: Dual-encoder (ViT or ResNet image encoder + text transformer) trained with contrastive loss.

## Use when
- You want to build a zero-shot visual classifier using natural language descriptions.
- You need to collect image-text pairs at web scale for contrastive pretraining.
- You want transferable visual representations without task-specific labeled data.

## Do not use when
- You need pixel-level annotations or bounding box supervision.
- Your domain has very specific terminology not covered by web-crawled alt-text.
- You need a generative model rather than a contrastive dual-encoder.

## Required inputs
- **web_crawl_source**: Web pages containing co-occurring images and text (alt-text, titles, captions).
- **query_list**: 500,000 queries constructed from WordNet synsets and Wikipedia to guide balanced data collection.
- **contrastive_training_recipe**: InfoNCE contrastive loss with large batch sizes (32K).

## Optional inputs
- **text_encoder_config**: Transformer architecture and tokenizer configuration for the text branch.
- **image_encoder_config**: ViT or ResNet variant for the image branch.

## Outputs
- **pretrained_clip_model**: Dual-encoder model producing aligned image and text embeddings.
- **wit_dataset**: 400M image-text pairs (WIT) collected from the web.

## Assumptions and prerequisites
- Web alt-text provides sufficient supervision for learning visual concepts.
- A balanced query set can mitigate long-tail distribution issues in web data.
- Contrastive learning at scale can match or exceed supervised ImageNet pretraining.

## Procedure
1. **Construct query list**
   Action: Build 500K queries from WordNet synsets and Wikipedia article titles to ensure broad concept coverage.
   Why: Balances data collection across visual concepts and avoids long-tail skew.
   Note: Queries include bi-grams to capture compound concepts.
2. **Crawl and pair images with text**
   Action: Search the web for each query and collect co-occurring image-text pairs.
   Why: Web-scale data is needed to train the contrastive model with sufficient diversity.
   Note: Each query contributes up to 20K pairs to ensure class balance.
3. **Filter low-quality pairs**
   Action: Remove duplicate images, very short captions, and NSFW content.
   Why: Noisy or degenerate pairs would degrade contrastive learning.
   Note: The paper does not specify all filtering rules in detail.
4. **Train with contrastive loss**
   Action: Train the dual-encoder CLIP model with InfoNCE loss on the filtered 400M pairs.
   Why: Contrastive learning aligns image and text representations in a shared embedding space.
   Note: Use large batch sizes (32,768) for effective negative sampling.
5. **Evaluate zero-shot transfer**
   Action: Evaluate on downstream datasets using text prompts as classifiers.
   Why: Zero-shot transfer measures the generality of learned representations.
   Note: See paper for details.

## Parameters to set
- **batch_size** — Role: Controls number of negatives in contrastive loss. How to set: Use 32,768 for best results. Default/range: 32768. Effect: Larger batches improve contrastive learning but require more memory.
- **num_pairs** — Role: Total image-text pairs for training. How to set: Collect up to 400M balanced pairs. Default/range: 400M. Effect: More data generally improves zero-shot performance.
- **query_balance_cap** — Role: Maximum pairs per query to prevent skew. How to set: Cap at 20K per query. Default/range: 20K. Effect: Ensures concept diversity across the dataset.

## Validation checks
- Zero-shot ImageNet accuracy should reach ~76% for ViT-L/14.
- The dataset should cover a broad distribution of visual concepts.
- Contrastive loss should decrease steadily during training.

## Failure modes
- Web alt-text is often noisy, generic, or unrelated to the image content.
- Long-tail concepts may still be underrepresented despite query balancing.
- The contrastive objective does not model fine-grained spatial relationships.

## Adaptation notes for VLM training
- CLIP embeddings are widely used as quality filters for other VLM training pipelines.
- The WIT-style collection strategy can be adapted for domain-specific image-text datasets.
- Use CLIP score filtering as a downstream data curation step for VLM pretraining.

## Implementation notes
- Cache CLIP embeddings for large pools to enable efficient downstream filtering.
- Monitor concept coverage statistics during collection to detect gaps.
- Use the OpenAI CLIP or OpenCLIP implementations for reproducibility.

## Evidence from the paper
- CLIP matches the accuracy of a ResNet-50 trained on ImageNet in a zero-shot setting, without using any of ImageNet's 1.28 million training examples.
- The model is trained on 400 million image-text pairs collected from the internet (WIT dataset).
- CLIP's representations transfer to 27 different datasets, matching or exceeding fully supervised baselines on most.
- Natural language supervision enables flexible zero-shot transfer via text prompts.

## Source paper
- **Title**: Learning Transferable Visual Models From Natural Language Supervision
- **Year**: 2021
- **Venue**: ICML
- **Paper ID**: arxiv-2103.00020v1
- **URL**: http://arxiv.org/abs/2103.00020v1
- **arXiv ID**: 2103.00020v1
