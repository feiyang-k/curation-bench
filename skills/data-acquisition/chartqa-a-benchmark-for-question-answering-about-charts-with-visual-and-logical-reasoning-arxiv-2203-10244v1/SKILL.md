# ChartQA: A Benchmark for Question Answering about Charts with Visual and Logical Reasoning

## One-line decision
Use this skill when you need a QA dataset about charts requiring both visual perception and logical reasoning. Avoid it when you need VQA for natural images rather than charts and graphs.

## Skill metadata
- **Skill type**: chart-qa-dataset
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Create a benchmark for question answering about charts that tests both visual perception (reading values from charts) and logical reasoning (computing, comparing, inferring from chart data).

## Problem signature
- Modality: chart images with questions requiring visual and logical reasoning.
- Data state: charts from web sources with human-written and machine-generated QA pairs.
- Scale regime: 32K QA pairs on charts.
- Model requirement: No model required for dataset construction; validated with chart understanding models.

## Use when
- You need chart/graph understanding training or evaluation data.
- You want to benchmark VLM chart reasoning capabilities.
- You need questions requiring both visual and logical reasoning.

## Do not use when
- You need VQA for natural images.
- Chart understanding is not your target task.
- You need larger-scale chart data.

## Required inputs
- **chart_images**: Charts from web sources (bar, line, pie, etc.).
- **human_questions**: Human-written questions requiring reasoning about chart data.
- **machine_questions**: Machine-generated questions for augmentation.

## Optional inputs
- **chart_data_tables**: Underlying data tables for answer verification.

## Outputs
- **chartqa_dataset**: 32K QA pairs on chart images.
- **evaluation_results**: Baselines for chart understanding models.

## Assumptions and prerequisites
- Chart understanding requires both visual perception and logical reasoning.
- Human-written questions test deeper reasoning than template-generated ones.
- Charts are an important document type for VLM evaluation.

## Procedure
1. **Collect chart images**
   Action: Gather diverse charts from web sources.
   Why: Diverse charts ensure broad coverage of chart types.
   Note: See paper for details.
2. **Generate human questions**
   Action: Have annotators write questions requiring reasoning about chart data.
   Why: Human questions test deeper understanding.
   Note: See paper for details.
3. **Generate machine questions**
   Action: Create template-based questions from chart data tables.
   Why: Machine questions augment the dataset at scale.
   Note: See paper for details.
4. **Evaluate baseline models**
   Action: Test chart understanding models on ChartQA.
   Why: Establishes baselines for future work.
   Note: See paper for details.

## Parameters to set
- **chart_types** — Role: Types of charts included. How to set: Include bar, line, pie, scatter, and other types. Default/range: Diverse. Effect: More types improve generalization.
- **reasoning_types** — Role: Types of reasoning required. How to set: Include visual, logical, and compositional reasoning. Default/range: Mixed. Effect: Diverse reasoning tests comprehensive understanding.

## Validation checks
- Questions should require visual perception of chart elements.
- Logical reasoning questions should not be answerable without the chart.
- The dataset should cover diverse chart types and reasoning patterns.

## Failure modes
- Machine-generated questions may be too simple or repetitive.
- Chart quality and rendering styles vary significantly.
- Complex multi-part reasoning may be rare in the dataset.

## Adaptation notes for VLM training
- ChartQA is used as instruction tuning data for VLMs with chart understanding.
- Combine with other document understanding data for comprehensive VLM training.
- The chart reasoning patterns transfer to infographic and data visualization understanding.

## Implementation notes
- Separate human and machine questions for analysis.
- Use relaxed accuracy metrics for numerical answers.
- Track performance by chart type and reasoning type.

## Evidence from the paper
- ChartQA provides 32K QA pairs testing visual and logical reasoning about charts.
- Human-written questions require deeper reasoning than machine-generated ones.
- The dataset reveals gaps in current models' chart understanding capabilities.
- ChartQA is a standard benchmark for VLM chart and graph understanding.

## Source paper
- **Title**: ChartQA: A Benchmark for Question Answering about Charts with Visual and Logical Reasoning
- **Year**: 2022
- **Venue**: ACL
- **Paper ID**: arxiv-2203.10244v1
- **URL**: http://arxiv.org/abs/2203.10244v1
- **arXiv ID**: 2203.10244v1
