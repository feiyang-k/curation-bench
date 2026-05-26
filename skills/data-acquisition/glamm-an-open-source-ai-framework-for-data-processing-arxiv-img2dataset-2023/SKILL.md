# GLaMM: An Open-Source AI Framework for Data Processing

## One-line decision
Use this skill when you need to efficiently download billions of images from URLs for building large-scale image-text datasets. Avoid it when you already have images locally or only need a small number.

## Skill metadata
- **Skill type**: efficient-image-download-pipeline
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Provide an efficient, scalable pipeline for downloading billions of images from URLs, supporting the construction of large-scale image-text datasets like LAION-5B.

## Problem signature
- Modality: images downloaded from web URLs with metadata.
- Data state: URL lists processed into downloaded, resized images with metadata.
- Scale regime: billions of images.
- Model requirement: No model; infrastructure tool for data pipeline.

## Use when
- You need to download billions of images from URLs.
- You are building a large-scale image-text dataset.
- You need efficient, distributed image downloading.

## Do not use when
- You already have images locally.
- You only need a small number of images.
- You are not building an image dataset.

## Required inputs
- **url_list**: List of image URLs to download.
- **storage**: Storage for downloaded images.
- **download_config**: Configuration for parallelism, resizing, and formats.

## Optional inputs
- **resize_config**: Target resolution for downloaded images.
- **metadata_fields**: Additional metadata to preserve.

## Outputs
- **downloaded_images**: Billions of downloaded and resized images.
- **metadata**: Associated metadata for each image.

## Assumptions and prerequisites
- Many URLs will return valid images.
- Distributed downloading enables billion-scale processing.
- Resizing during download saves storage.

## Procedure
1. **Prepare URL list**
   Action: Gather URLs from dataset metadata or web crawl.
   Why: URLs define what images to download.
   Note: See paper for details.
2. **Configure download pipeline**
   Action: Set parallelism, timeout, resize, and output format.
   Why: Configuration affects speed and quality.
   Note: See paper for details.
3. **Run distributed download**
   Action: Execute img2dataset across multiple workers.
   Why: Distributed processing enables billion-scale downloading.
   Note: See paper for details.
4. **Validate downloads**
   Action: Check for corrupted or invalid images.
   Why: Quality control ensures usable data.
   Note: See paper for details.

## Parameters to set
- **num_workers** — Role: Parallel download workers. How to set: Scale to available bandwidth. Default/range: 16+. Effect: More workers increase throughput.
- **target_size** — Role: Target image resolution after resize. How to set: 256 or 512 for training. Default/range: 256. Effect: Smaller sizes save storage.
- **output_format** — Role: Storage format for downloaded images. How to set: WebDataset for efficient loading. Default/range: WebDataset. Effect: Format affects downstream loading speed.

## Validation checks
- Download success rate should be tracked.
- Corrupted images should be detected and removed.
- Throughput should scale with workers.

## Failure modes
- URL decay reduces download success.
- Some servers may rate-limit or block.
- Storage requirements are significant at billion scale.

## Adaptation notes for VLM training
- img2dataset is the standard tool for building LAION-scale datasets.
- Use for any large-scale image-text dataset construction.
- Combine with CLIP score computation for quality filtering.

## Implementation notes
- Use WebDataset output format for efficient training.
- Monitor download success rate during processing.
- Handle timeouts and retries gracefully.

## Evidence from the paper
- img2dataset enables efficient downloading of billions of images.
- The tool was used to build LAION-5B and similar datasets.
- Distributed downloading scales to billions of URLs.
- WebDataset output format enables efficient downstream training.

## Source paper
- **Title**: GLaMM: An Open-Source AI Framework for Data Processing
- **Year**: 2022
- **Venue**: GitHub
- **Paper ID**: arxiv-img2dataset-2023
- **URL**: https://github.com/rom1504/img2dataset
- **arXiv ID**: N/A
