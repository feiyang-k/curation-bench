# Nocaps: Novel Object Captioning at Scale

## One-line decision
Use this skill when you need a captioning benchmark testing generalization to novel objects not seen during training. Avoid it when you only evaluate on in-domain captioning.

## Skill metadata
- **Skill type**: novel-object-captioning-benchmark
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Create a captioning benchmark that specifically tests generalization to novel objects not seen during training, using OpenImages objects not present in COCO.

## Problem signature
- Modality: images with novel objects requiring out-of-domain captioning.
- Data state: images from OpenImages with captions featuring novel objects not in COCO.
- Scale regime: 15K evaluation images with novel objects.
- Model requirement: Any captioning model or VLM.

## Use when
- You need to evaluate captioning on novel objects.
- You want to test VLM generalization beyond training categories.
- You need out-of-domain captioning evaluation.

## Do not use when
- In-domain COCO captioning evaluation is sufficient.
- You do not need novel object evaluation.
- Your model's vocabulary already covers diverse objects.

## Required inputs
- **openimages_images**: Images containing objects not in COCO training.
- **human_captions**: Captions for images with novel objects.
- **novel_object_list**: List of objects not seen in COCO training.

## Optional inputs
- **in_domain_split**: Split with in-domain objects for comparison.

## Outputs
- **nocaps_benchmark**: 15K captioning examples with novel objects.
- **generalization_metrics**: Metrics for novel object captioning.

## Assumptions and prerequisites
- Captioning models should generalize to novel objects.
- COCO-only training may not cover all visual concepts.
- Novel object evaluation reveals generalization capability.

## Procedure
1. **Identify novel objects**
   Action: Find OpenImages objects not present in COCO training.
   Why: Defines what constitutes 'novel' for this benchmark.
   Note: See paper for details.
2. **Collect images with novel objects**
   Action: Select images containing these novel objects.
   Why: Creates the evaluation set.
   Note: See paper for details.
3. **Annotate captions**
   Action: Collect human captions for images with novel objects.
   Why: Ground truth for evaluation.
   Note: See paper for details.
4. **Evaluate captioning**
   Action: Test models on novel object captioning.
   Why: Measures generalization capability.
   Note: See paper for details.

## Parameters to set
- **novel_object_count** — Role: Number of novel object categories. How to set: Based on COCO vs OpenImages overlap. Default/range: ~400 novel objects. Effect: More novel objects test broader generalization.
- **split_types** — Role: In-domain, near-domain, out-of-domain splits. How to set: Separate by novelty level. Default/range: 3 splits. Effect: Splits reveal generalization at different levels.

## Validation checks
- Models should caption novel objects they were not trained on.
- Performance should decrease from in-domain to out-of-domain.
- Web-scale pretraining should help with novel objects.

## Failure modes
- Models may fail on truly novel objects.
- Some 'novel' objects may be indirectly seen in training.
- Captioning metrics may not capture novel object naming.

## Adaptation notes for VLM training
- NoCaps evaluates VLM generalization to unseen concepts.
- Use to assess whether training data covers sufficient visual concepts.
- Web-scale pretraining should improve NoCaps performance.

## Implementation notes
- Use the NoCaps evaluation server.
- Report per-split performance.
- Compare web-pretrained vs COCO-only models.

## Evidence from the paper
- NoCaps evaluates captioning on novel objects not seen during training.
- The benchmark reveals generalization capability beyond training categories.
- Web-scale pretraining significantly improves novel object captioning.
- NoCaps is a standard benchmark for VLM generalization evaluation.

## Source paper
- **Title**: Nocaps: Novel Object Captioning at Scale
- **Year**: 2019
- **Venue**: ICCV
- **Paper ID**: arxiv-1812.08658v2
- **URL**: http://arxiv.org/abs/1812.08658v2
- **arXiv ID**: 1812.08658v2
