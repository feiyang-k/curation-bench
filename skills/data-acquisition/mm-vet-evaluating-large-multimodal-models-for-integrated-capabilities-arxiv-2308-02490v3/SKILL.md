# MM-Vet: Evaluating Large Multimodal Models for Integrated Capabilities

## One-line decision
Use this skill when you need a benchmark evaluating VLMs on tasks requiring integrated use of multiple capabilities simultaneously. Avoid it when individual capability testing is sufficient.

## Skill metadata
- **Skill type**: integrated-capability-evaluation
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Create a benchmark that evaluates VLMs on tasks requiring the integrated use of multiple capabilities simultaneously, testing how well models combine recognition, OCR, spatial understanding, language, and knowledge.

## Problem signature
- Modality: images with tasks requiring integrated multi-capability reasoning.
- Data state: 200 evaluation examples requiring integrated capabilities.
- Scale regime: 200 carefully designed evaluation examples.
- Model requirement: Any VLM for evaluation.

## Use when
- You want to test integrated multi-capability use.
- Individual capability tests are insufficient.
- You need to evaluate holistic VLM quality.

## Do not use when
- Individual capability testing is sufficient.
- You need large-scale evaluation.
- Specific capability testing is preferred.

## Required inputs
- **integrated_examples**: 200 examples requiring multiple capabilities.
- **capability_taxonomy**: Taxonomy of VLM capabilities tested.
- **llm_judge**: LLM for scoring open-ended responses.

## Optional inputs
- **per_capability_analysis**: Analysis of performance by required capabilities.

## Outputs
- **mm_vet_scores**: Integrated capability evaluation scores.
- **capability_analysis**: Analysis of which capability combinations are challenging.

## Assumptions and prerequisites
- Real-world tasks require integrated use of multiple capabilities.
- Testing individual capabilities misses integration challenges.
- 200 carefully designed examples provide meaningful evaluation.

## Procedure
1. **Design integrated tasks**
   Action: Create tasks requiring multiple VLM capabilities simultaneously.
   Why: Tests capability integration.
   Note: See paper for details.
2. **Define capability requirements**
   Action: Label which capabilities each task requires.
   Why: Enables per-capability analysis.
   Note: See paper for details.
3. **Evaluate with LLM judge**
   Action: Use GPT-4 to score open-ended VLM responses.
   Why: Open-ended evaluation captures nuanced quality.
   Note: See paper for details.
4. **Analyze integration quality**
   Action: Study which capability combinations are most challenging.
   Why: Guides targeted improvement.
   Note: See paper for details.

## Parameters to set
- **num_examples** — Role: Total evaluation examples. How to set: 200 for quality evaluation. Default/range: 200. Effect: Quality matters more than quantity for integration testing.
- **capabilities_tested** — Role: VLM capabilities evaluated. How to set: Include recognition, OCR, spatial, language, knowledge. Default/range: 6 capabilities. Effect: More capabilities test broader integration.

## Validation checks
- Scores should correlate with human judgment.
- Integration testing should reveal different rankings than individual tests.
- The benchmark should differentiate model quality.

## Failure modes
- 200 examples may be insufficient for statistical significance.
- LLM judge may have biases.
- Some capability combinations may be underrepresented.

## Adaptation notes for VLM training
- MM-Vet tests holistic VLM quality important for real-world use.
- Integration evaluation complements individual capability benchmarks.
- Use to evaluate whether training data develops integrated capabilities.

## Implementation notes
- Use GPT-4 for scoring with the MM-Vet rubric.
- Report per-capability combination scores.
- Compare to individual capability benchmarks.

## Evidence from the paper
- MM-Vet evaluates integrated use of multiple VLM capabilities.
- Real-world tasks require capability integration.
- 200 examples provide meaningful evaluation of integration quality.
- The benchmark reveals challenges in capability combination.

## Source paper
- **Title**: MM-Vet: Evaluating Large Multimodal Models for Integrated Capabilities
- **Year**: 2023
- **Venue**: arXiv
- **Paper ID**: arxiv-2308.02490v3
- **URL**: http://arxiv.org/abs/2308.02490v3
- **arXiv ID**: 2308.02490v3
