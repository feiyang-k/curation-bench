# Data-Juicer: A One-Stop Data Processing System for Large Language Models

## One-line decision
Use this skill when you need a configurable data processing pipeline with 50+ operators for cleaning, filtering, and preparing LLM/VLM training data. Avoid it when you have a simple dataset that does not need complex multi-stage processing.

## Skill metadata
- **Skill type**: data-processing-system
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Provide a one-stop, configurable data processing system with 50+ built-in operators for cleaning, filtering, deduplication, and preparing training data for LLMs and VLMs.

## Problem signature
- Modality: text and multimodal data processing.
- Data state: raw data from various sources needing cleaning, filtering, and preparation.
- Scale regime: terabyte-scale data processing.
- Model requirement: No model required; the system processes data for any downstream model.

## Use when
- You need a comprehensive data processing pipeline for LLM/VLM data.
- You want configurable, composable data processing operators.
- You need to process data at terabyte scale.

## Do not use when
- Your data processing needs are simple (single filter).
- You have a custom pipeline that already works well.
- You need real-time data processing.

## Required inputs
- **raw_data**: Raw text or multimodal data to be processed.
- **processing_config**: YAML configuration specifying operators and parameters.
- **operator_library**: Data-Juicer's 50+ built-in operators.

## Optional inputs
- **custom_operators**: User-defined processing operators.
- **quality_metrics**: Metrics for monitoring processing quality.

## Outputs
- **processed_data**: Clean, filtered, deduplicated training data.
- **processing_report**: Statistics and quality metrics from processing.

## Assumptions and prerequisites
- Data processing requires multiple composable operators.
- A configurable system enables rapid iteration on processing recipes.
- Standard operators cover most data processing needs.

## Procedure
1. **Define processing recipe**
   Action: Create a YAML configuration specifying operators and their parameters.
   Why: Configuration enables reproducible, tunable processing.
   Note: See paper for details.
2. **Run processing pipeline**
   Action: Execute the configured operators on the raw data.
   Why: Multi-stage processing cleans and prepares the data.
   Note: See paper for details.
3. **Analyze processing results**
   Action: Review statistics and quality metrics from the processing run.
   Why: Analysis reveals data quality and processing effectiveness.
   Note: See paper for details.
4. **Iterate and refine**
   Action: Adjust operators and parameters based on analysis.
   Why: Iterative refinement improves data quality.
   Note: See paper for details.

## Parameters to set
- **operators** — Role: Processing operators to apply. How to set: Select from 50+ built-in operators. Default/range: Task-dependent. Effect: Different operators address different quality issues.
- **operator_params** — Role: Parameters for each operator. How to set: Configure thresholds, rules, and modes. Default/range: Operator-specific defaults. Effect: Parameters control processing aggressiveness.

## Validation checks
- Processed data should be cleaner than raw input.
- Processing should not remove too much valid data.
- Statistics should show meaningful quality improvements.

## Failure modes
- Over-aggressive filtering may remove valid data.
- Operator ordering may affect results.
- Processing at terabyte scale requires significant compute.

## Adaptation notes for VLM training
- Use Data-Juicer for VLM pretraining data processing.
- Extend with custom operators for domain-specific processing.
- The configurable approach enables rapid experimentation.

## Implementation notes
- Use YAML configs for reproducible processing.
- Monitor per-operator statistics for debugging.
- Process data in parallel for scalability.

## Evidence from the paper
- Data-Juicer provides 50+ built-in operators for comprehensive data processing.
- The system handles terabyte-scale data processing.
- Configurable YAML recipes enable rapid iteration on processing strategies.
- Data-Juicer is used for preparing training data for several LLMs.

## Source paper
- **Title**: Data-Juicer: A One-Stop Data Processing System for Large Language Models
- **Year**: 2023
- **Venue**: arXiv
- **Paper ID**: arxiv-2309.02033v5
- **URL**: http://arxiv.org/abs/2309.02033v5
- **arXiv ID**: 2309.02033v5
