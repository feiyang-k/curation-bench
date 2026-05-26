# D4: Improving LLM Pretraining via Document De-Duplication and Diversification

## One-line decision
Use this skill when you want to both deduplicate and diversify training data using embedding-based clustering and selection. Avoid it when simple deduplication is sufficient or you cannot compute embeddings for all data.

## Skill metadata
- **Skill type**: dedup-and-diversification
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Combine deduplication with diversification — first remove near-duplicates, then actively select a diverse subset from the remaining data using embedding-based clustering.

## Problem signature
- Modality: text data; principles apply to multimodal.
- Data state: large training corpus needing both deduplication and diversity optimization.
- Scale regime: billions of text documents.
- Model requirement: Embedding model for computing document representations; any LLM for training.

## Use when
- You want to both deduplicate and diversify your training data.
- You can compute embeddings for all documents.
- You want to actively select a diverse subset rather than just removing duplicates.

## Do not use when
- Simple deduplication is sufficient.
- You cannot afford embedding computation for the full corpus.
- You need all data without selection.

## Required inputs
- **training_corpus**: Large text corpus to deduplicate and diversify.
- **embedding_model**: Model for computing document embeddings.
- **selection_algorithm**: Algorithm for selecting a diverse subset from clusters.

## Optional inputs
- **target_size**: Target number of documents after dedup+diversification.

## Outputs
- **curated_corpus**: Deduplicated and diversified training corpus.
- **diversity_metrics**: Metrics measuring corpus diversity.

## Assumptions and prerequisites
- Deduplication and diversification address different quality aspects.
- Embedding-based selection captures semantic diversity.
- A diverse corpus produces a more capable model.

## Procedure
1. **Compute document embeddings**
   Action: Embed all documents using a pre-trained model.
   Why: Embeddings enable semantic similarity computation.
   Note: See paper for details.
2. **Deduplicate**
   Action: Remove near-duplicate documents based on embedding similarity.
   Why: Removes redundancy.
   Note: See paper for details.
3. **Cluster remaining documents**
   Action: Cluster the deduplicated documents by embedding similarity.
   Why: Clustering groups similar content for diversity selection.
   Note: See paper for details.
4. **Select diverse representatives**
   Action: Select a diverse subset by choosing representatives from each cluster.
   Why: Maximizes content diversity in the final corpus.
   Note: See paper for details.
5. **Validate with LLM training**
   Action: Train an LLM on the curated corpus and compare to baselines.
   Why: End-to-end validation proves the approach works.
   Note: See paper for details.

## Parameters to set
- **dedup_threshold** — Role: Similarity threshold for deduplication. How to set: 0.9+ for conservative dedup. Default/range: 0.9. Effect: Lower threshold removes more but may lose valid content.
- **num_clusters** — Role: Number of clusters for diversity selection. How to set: Scale with corpus size. Default/range: 10K-100K. Effect: More clusters enable finer-grained diversity.
- **selection_budget** — Role: Number of documents to select. How to set: Based on training compute budget. Default/range: Task-dependent. Effect: Smaller selection is more curated but less comprehensive.

## Validation checks
- The curated corpus should be more diverse than random subsampling.
- LLM trained on curated data should outperform full-data baselines.
- Deduplication+diversification should outperform dedup alone.

## Failure modes
- Embedding quality limits diversity selection accuracy.
- Very aggressive selection may miss important content.
- Clustering approximations may not capture all diversity dimensions.

## Adaptation notes for VLM training
- Apply D4 to VLM pretraining data (both image-text pairs and text).
- Use CLIP embeddings for multimodal D4.
- Combine with quality filtering for maximum data curation benefit.

## Implementation notes
- Use FAISS for efficient embedding clustering.
- Pre-compute and cache all embeddings.
- Monitor diversity metrics during selection.

## Evidence from the paper
- D4 combines deduplication and diversification for better data curation than either alone.
- The approach selects a diverse, non-redundant subset from large corpora.
- LLMs trained on D4-curated data outperform those trained on full or randomly subsampled data.
- The method is computationally feasible at web scale.

## Source paper
- **Title**: D4: Improving LLM Pretraining via Document De-Duplication and Diversification
- **Year**: 2023
- **Venue**: NeurIPS
- **Paper ID**: arxiv-2308.12284v2
- **URL**: http://arxiv.org/abs/2308.12284v2
- **arXiv ID**: 2308.12284v2
