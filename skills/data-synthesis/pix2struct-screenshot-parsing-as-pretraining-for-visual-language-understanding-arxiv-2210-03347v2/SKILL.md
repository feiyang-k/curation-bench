# Pix2Struct: Screenshot Parsing as Pretraining for Visual Language Understanding

## One-line decision
Use this skill when you want to pre-train a document understanding model by parsing web page screenshots into their HTML structure. Avoid it when you do not need document understanding or your documents are not web-like.

## Skill metadata
- **Skill type**: screenshot-parsing-pretraining
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Pre-train a vision encoder-decoder model by learning to parse web page screenshots into their underlying HTML structure, creating a strong foundation for document and visual language understanding.

## Problem signature
- Modality: web page screenshots paired with their HTML structure for pre-training.
- Data state: web pages rendered as screenshots with HTML source as target.
- Scale regime: 80M screenshot-HTML pairs from web pages.
- Model requirement: ViT encoder + text decoder trained on screenshot-to-structure parsing.

## Use when
- You need a model pre-trained for document and visual language understanding.
- You can render web pages into screenshot-HTML pairs.
- You need a model that understands visual layout and structure.

## Do not use when
- Your documents are not web-like (handwritten, etc.).
- You need a general-purpose image understanding model.
- Screenshot rendering at scale is infeasible.

## Required inputs
- **web_pages**: Web pages with HTML source for rendering and parsing.
- **screenshot_renderer**: Tool for rendering web pages as screenshots.
- **encoder_decoder**: ViT encoder + text decoder architecture.

## Optional inputs
- **downstream_tasks**: Specific document understanding tasks for fine-tuning.

## Outputs
- **pix2struct_model**: Pre-trained screenshot parsing model.
- **document_understanding_pipeline**: Pipeline for understanding document images.

## Assumptions and prerequisites
- Screenshot-to-HTML parsing teaches visual layout understanding.
- Web pages provide abundant, diverse training data.
- The parsing objective transfers to downstream document understanding.

## Procedure
1. **Render web pages as screenshots**
   Action: Render web pages at various resolutions and capture screenshots.
   Why: Creates input-output pairs for pre-training.
   Note: See paper for details.
2. **Extract HTML structure**
   Action: Parse HTML to create structured target sequences.
   Why: HTML structure provides the supervision signal.
   Note: See paper for details.
3. **Pre-train on screenshot parsing**
   Action: Train the model to predict HTML from screenshots.
   Why: Parsing teaches visual layout and text understanding.
   Note: See paper for details.
4. **Fine-tune on downstream tasks**
   Action: Fine-tune on specific document understanding tasks.
   Why: Transfers pre-trained knowledge to target tasks.
   Note: See paper for details.

## Parameters to set
- **screenshot_resolution** — Role: Resolution of rendered screenshots. How to set: Variable resolution to handle diverse layouts. Default/range: Variable. Effect: Higher resolution captures finer details.
- **html_depth** — Role: Depth of HTML structure in target. How to set: Include relevant structural elements. Default/range: Task-dependent. Effect: Deeper structure provides richer supervision.

## Validation checks
- The model should parse web page structures accurately.
- Fine-tuning should achieve strong results on document understanding tasks.
- The pre-training objective should transfer across document types.

## Failure modes
- Web pages with heavy JavaScript rendering may not render correctly.
- HTML structure may be inconsistent across web pages.
- The pre-training may overfit to web-specific layouts.

## Adaptation notes for VLM training
- Pix2Struct provides a strong pre-training recipe for document VLMs.
- The screenshot parsing approach can be adapted to other document types.
- Fine-tune on specific document tasks (charts, tables, forms) for best results.

## Implementation notes
- Use headless browser rendering for scalability.
- Normalize HTML structure for consistent targets.
- Monitor rendering quality for training data.

## Evidence from the paper
- Pix2Struct pre-trains on 80M web page screenshot-HTML pairs.
- Screenshot parsing pre-training transfers effectively to document understanding.
- The model achieves state-of-the-art on ChartQA, DocVQA, and other document benchmarks.
- Variable resolution input handling improves diverse document processing.

## Source paper
- **Title**: Pix2Struct: Screenshot Parsing as Pretraining for Visual Language Understanding
- **Year**: 2022
- **Venue**: ICML
- **Paper ID**: arxiv-2210.03347v2
- **URL**: http://arxiv.org/abs/2210.03347v2
- **arXiv ID**: 2210.03347v2
