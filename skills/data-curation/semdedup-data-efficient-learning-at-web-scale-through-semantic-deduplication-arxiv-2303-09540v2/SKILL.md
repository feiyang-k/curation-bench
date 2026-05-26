# SemDeDup: Data-efficient Learning at Web-scale through Semantic Deduplication

## One-line decision
Use this skill when you want to remove semantically redundant examples from large-scale training data using embedding-based deduplication. Avoid it when you only need exact or near-exact duplicate removal or your dataset is small enough that redundancy is not a concern.

## Skill metadata
- **Skill type**: semantic-deduplication
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Remove semantically redundant training examples from web-scale datasets by clustering embeddings and removing near-duplicates within clusters, improving training efficiency without sacrificing model quality.

## Problem signature
- Modality: any modality with embeddings; demonstrated on image-text pairs and text corpora.
- Data state: large-scale web-crawled data with significant semantic redundancy.
- Scale regime: hundreds of millions to billions of training examples.
- Model requirement: Pre-trained embedding model (e.g., CLIP, SentenceBERT) for computing semantic similarity.

## Use when
- You have web-scale training data with significant semantic redundancy.
- You want to train on less data without losing performance.
- You have pre-trained embeddings available for your data modality.

## Do not use when
- Your dataset is small and hand-curated without redundancy.
- You only need exact duplicate removal (use hash-based methods instead).
- You lack suitable embeddings for computing semantic similarity.

## Required inputs
- **training_data**: Large-scale dataset to be deduplicated.
- **embedding_model**: Pre-trained model to compute embeddings for semantic similarity (e.g., CLIP for images, SentenceBERT for text).
- **similarity_threshold**: Cosine similarity threshold above which examples are considered semantically redundant.

## Optional inputs
- **num_clusters**: Number of clusters for k-means clustering of embeddings.
- **cluster_algorithm**: Clustering algorithm (k-means default; other options possible).

## Outputs
- **deduplicated_dataset**: Subset of the original data with semantic duplicates removed.
- **dedup_statistics**: Statistics on removed examples, cluster sizes, and redundancy rates.

## Assumptions and prerequisites
- Semantically similar examples in embedding space are redundant for training.
- Clustering can efficiently group similar examples for pairwise comparison.
- Removing redundancy improves training efficiency without harming final performance.

## Procedure
1. **Compute embeddings**
   Action: Extract embeddings for all training examples using a pre-trained model.
   Why: Embeddings capture semantic content for similarity computation.
   Note: Use CLIP image embeddings for image-text data.
2. **Cluster embeddings**
   Action: Run k-means clustering on the embeddings to group similar examples.
   Why: Clustering reduces the number of pairwise comparisons needed.
   Note: Choose k based on dataset size; larger k gives finer groups.
3. **Remove within-cluster duplicates**
   Action: Within each cluster, compute pairwise cosine similarities and remove examples above the similarity threshold, keeping one representative.
   Why: Eliminates semantic redundancy within each cluster.
   Note: See paper for details.
4. **Merge deduplicated clusters**
   Action: Combine the representative examples from all clusters to form the deduplicated dataset.
   Why: Creates the final training set.
   Note: See paper for details.
5. **Validate deduplication**
   Action: Train models on the deduplicated set and compare performance to training on the full set.
   Why: Confirms that deduplication maintains model quality while reducing data.
   Note: See paper for details.

## Parameters to set
- **similarity_threshold** — Role: Cosine similarity above which pairs are considered duplicates. How to set: 0.95 for conservative; 0.85 for aggressive dedup. Default/range: 0.85-0.95. Effect: Lower threshold removes more data but may discard useful variation.
- **num_clusters_k** — Role: Number of k-means clusters. How to set: Scale with dataset size; 50K-100K clusters typical. Default/range: 50000. Effect: More clusters reduce pairwise comparisons but increase clustering time.
- **dedup_fraction_target** — Role: Target fraction of data to keep after dedup. How to set: 50-75% is typical for web data. Default/range: 50-75%. Effect: More aggressive dedup saves more compute at some quality risk.

## Validation checks
- Models trained on deduplicated data should match or exceed full-data baselines in accuracy per training step.
- The deduplicated set should have lower redundancy as measured by pairwise similarity statistics.
- Deduplication should not systematically remove rare or minority concepts.

## Failure modes
- Aggressive deduplication may remove valid variations that aid generalization.
- Embedding quality limits the accuracy of semantic similarity judgments.
- The clustering step introduces approximation error in near-boundary cases.

## Adaptation notes for VLM training
- Apply SemDeDup to VLM pretraining data using CLIP embeddings for both images and text.
- Combine with exact deduplication (hash-based) for a two-stage pipeline.
- Use SemDeDup on instruction-tuning data to remove redundant instruction patterns.

## Implementation notes
- Use FAISS for efficient k-means clustering and similarity search at scale.
- Pre-compute and cache all embeddings before clustering.
- Parallelize within-cluster deduplication across multiple workers.

## Evidence from the paper
- SemDeDup can remove 50% of the data with minimal performance loss, effectively halving training compute.
- On C4 (language) and LAION (vision-language), semantic deduplication outperforms random subsampling.
- Embedding-based deduplication captures redundancy that exact dedup methods miss.
- SemDeDup is complementary to existing data filtering methods like CLIP score filtering.

## Source paper
- **Title**: SemDeDup: Data-efficient Learning at Web-scale through Semantic Deduplication
- **Year**: 2023
- **Venue**: ICLR
- **Paper ID**: arxiv-2303.09540v2
- **URL**: http://arxiv.org/abs/2303.09540v2
- **arXiv ID**: 2303.09540v2
