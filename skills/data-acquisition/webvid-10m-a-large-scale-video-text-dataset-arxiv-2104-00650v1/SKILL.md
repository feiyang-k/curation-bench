# WebVid-10M: A Large-Scale Video-Text Dataset

## One-line decision
Use this skill when you want to collect video-text pairs from the web at 10M scale using stock video alt-text as captions. Avoid it when you need high-quality descriptions rather than stock video alt-text.

## Skill metadata
- **Skill type**: video-alt-text-collection
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Collect 10 million video-text pairs from the web by scraping stock footage websites where videos have descriptive alt-text, providing a large-scale video-text dataset.

## Problem signature
- Modality: video clips with alt-text descriptions from stock footage websites.
- Data state: stock footage videos with descriptive alt-text scraped from the web.
- Scale regime: 10.7 million video-text pairs.
- Model requirement: No model required for collection; used for video-text pretraining.

## Use when
- You need large-scale video-text data for pretraining.
- Stock footage alt-text quality is sufficient for your needs.
- You need a diverse video dataset.

## Do not use when
- You need narrative or instructional video descriptions.
- Stock footage style is too generic for your domain.
- You need very high quality captions.

## Required inputs
- **web_scraper**: Scraper for stock footage websites.
- **video_downloader**: Infrastructure for downloading 10M videos.
- **text_extractor**: Parser for extracting alt-text from web pages.

## Optional inputs
- **quality_filters**: Filters for video quality and caption relevance.

## Outputs
- **webvid_dataset**: 10.7M video-text pairs from stock footage websites.

## Assumptions and prerequisites
- Stock footage alt-text is more descriptive than typical web alt-text.
- Video content from stock sites is diverse and high quality.
- 10M scale is sufficient for effective video-text pretraining.

## Procedure
1. **Identify stock footage sources**
   Action: Select stock footage websites with descriptive alt-text.
   Why: Stock sites have better text descriptions than general web.
   Note: See paper for details.
2. **Scrape video-text pairs**
   Action: Extract video URLs and associated alt-text from the websites.
   Why: Automated scraping enables collection at scale.
   Note: See paper for details.
3. **Download and validate videos**
   Action: Download videos and verify they are valid and playable.
   Why: Ensures data quality and usability.
   Note: See paper for details.
4. **Clean and filter**
   Action: Remove duplicates, very short videos, and low-quality pairs.
   Why: Basic quality filtering improves dataset utility.
   Note: See paper for details.
5. **Release dataset**
   Action: Package the video-text dataset for research use.
   Why: Enables video-language research.
   Note: See paper for details.

## Parameters to set
- **min_video_duration** — Role: Minimum video length. How to set: 1-3 seconds minimum. Default/range: 1 second. Effect: Very short videos may lack meaningful content.
- **caption_quality** — Role: Quality of alt-text descriptions. How to set: Stock footage text tends to be descriptive. Default/range: Stock alt-text. Effect: Description quality directly affects training quality.

## Validation checks
- Video-text pairs should be semantically aligned.
- The dataset should cover diverse visual content.
- Models trained on WebVid should achieve competitive video-text retrieval.

## Failure modes
- Stock footage alt-text may be generic or keyword-stuffed.
- Video availability may change over time.
- Watermarked videos may affect visual quality.

## Adaptation notes for VLM training
- WebVid is widely used for video-language model pretraining.
- Combine with HowTo100M for complementary video-text data.
- The stock footage scraping approach can be extended to other sources.

## Implementation notes
- Use distributed downloading for 10M videos.
- Store video metadata for reproducibility.
- Handle watermarked frames during preprocessing.

## Evidence from the paper
- WebVid provides 10.7M video-text pairs from stock footage websites.
- Stock footage alt-text provides more descriptive captions than typical web alt-text.
- The dataset enables effective video-text pretraining and retrieval.
- WebVid has been used to train Stable Video Diffusion and other video models.

## Source paper
- **Title**: WebVid-10M: A Large-Scale Video-Text Dataset
- **Year**: 2021
- **Venue**: arXiv
- **Paper ID**: arxiv-2104.00650v1
- **URL**: http://arxiv.org/abs/2104.00650v1
- **arXiv ID**: 2104.00650v1
