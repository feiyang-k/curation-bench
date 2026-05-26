# RedCaps: Web-curated Image-Text Data Created by the People, for the People

## One-line decision
Use this skill when you want to curate image-caption data from Reddit with transparent provenance and community-driven quality. Avoid it when you need professionally written captions or cannot comply with Reddit's terms of use.

## Skill metadata
- **Skill type**: social-media-data-curation
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Curate a 12M image-text dataset from Reddit posts where users naturally pair images with descriptive titles, providing community-curated data with transparent provenance.

## Problem signature
- Modality: image-text pairs from Reddit posts with user-written titles as captions.
- Data state: Reddit image posts with titles curated through subreddit selection and filtering.
- Scale regime: 12 million image-text pairs from 350 curated subreddits.
- Model requirement: No model required for collection; validated with image-text pretraining.

## Use when
- You want image-text data with transparent provenance and community curation.
- You need data from diverse interest communities.
- You want an alternative to web crawl alt-text.

## Do not use when
- You need professional or expert-written captions.
- Reddit content is unsuitable for your domain.
- You need multi-million scale beyond 12M.

## Required inputs
- **reddit_api**: Reddit API access for post retrieval.
- **subreddit_list**: Curated list of 350 image-focused subreddits.
- **content_filters**: Filters for NSFW content, bots, and low-quality posts.

## Optional inputs
- **additional_subreddits**: More subreddits for domain expansion.

## Outputs
- **redcaps_dataset**: 12M image-text pairs from Reddit.
- **subreddit_metadata**: Metadata about source communities for provenance.

## Assumptions and prerequisites
- Reddit users naturally pair images with descriptive titles.
- Subreddit selection provides topical curation.
- Community moderation provides a layer of quality control.

## Procedure
1. **Select image-focused subreddits**
   Action: Curate 350 subreddits focused on sharing images with descriptive titles.
   Why: Subreddit selection controls content domain and quality.
   Note: See paper for details.
2. **Collect image posts**
   Action: Use Reddit API to collect image posts with titles from selected subreddits.
   Why: Reddit provides naturally paired image-text data.
   Note: See paper for details.
3. **Apply content filters**
   Action: Remove NSFW posts, bot-generated content, and low-effort titles.
   Why: Filtering improves data quality and safety.
   Note: See paper for details.
4. **Validate data quality**
   Action: Sample and review posts for caption quality and image relevance.
   Why: Ensures the curation pipeline produces useful data.
   Note: See paper for details.
5. **Release with provenance**
   Action: Release the dataset with full subreddit provenance metadata.
   Why: Transparency enables responsible use and reproduction.
   Note: See paper for details.

## Parameters to set
- **subreddit_count** — Role: Number of subreddits to include. How to set: Focus on image-sharing subreddits with descriptive titles. Default/range: 350. Effect: More subreddits increase diversity but may decrease quality.
- **min_upvotes** — Role: Minimum post upvotes for inclusion. How to set: Use community engagement as quality signal. Default/range: Not strictly specified. Effect: Higher minimums select more community-approved content.
- **nsfw_filter** — Role: Filter for inappropriate content. How to set: Remove all NSFW-tagged posts and flagged subreddits. Default/range: Strict. Effect: Ensures dataset safety.

## Validation checks
- Titles should describe image content rather than being clickbait or memes.
- The dataset should cover diverse visual domains through subreddit diversity.
- Models trained on RedCaps should achieve competitive performance.

## Failure modes
- Reddit titles may be humorous, sarcastic, or contextual rather than descriptive.
- Some subreddits may have niche jargon that doesn't generalize.
- Reddit content changes over time, affecting reproducibility.

## Adaptation notes for VLM training
- RedCaps provides an alternative data source to web crawl alt-text.
- Combine with other datasets for broader coverage.
- Use subreddit metadata for domain-specific filtering.

## Implementation notes
- Respect Reddit API rate limits and terms of service.
- Store post IDs rather than images for responsible release.
- Track subreddit distributions for analysis.

## Evidence from the paper
- RedCaps provides 12M image-text pairs from 350 curated Reddit subreddits.
- Reddit titles provide more natural and descriptive captions than web alt-text.
- The dataset offers transparent provenance through subreddit metadata.
- Models trained on RedCaps achieve competitive performance with CC3M-trained models.

## Source paper
- **Title**: RedCaps: Web-curated Image-Text Data Created by the People, for the People
- **Year**: 2021
- **Venue**: NeurIPS
- **Paper ID**: arxiv-2111.11431v1
- **URL**: http://arxiv.org/abs/2111.11431v1
- **arXiv ID**: 2111.11431v1
