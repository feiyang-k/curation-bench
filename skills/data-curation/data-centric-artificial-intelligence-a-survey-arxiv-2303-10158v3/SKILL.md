# Data-Centric Artificial Intelligence: A Survey

## One-line decision
Use this skill when you need a comprehensive overview of data-centric AI techniques including data quality, augmentation, selection, and engineering. Avoid it when you are looking for a specific method rather than a broad overview.

## Skill metadata
- **Skill type**: data-centric-ai-survey
- **Paper kind**: survey
- **Actionability**: medium
- **Evidence quality**: full_paper

## Goal
Provide a comprehensive survey of data-centric AI techniques spanning data collection, labeling, preparation, reduction, augmentation, and pipeline engineering.

## Problem signature
- Modality: general survey covering all data modalities.
- Data state: survey of methods applicable to data in any state.
- Scale regime: methods applicable at any scale.
- Model requirement: Survey; no specific model requirement.

## Use when
- You need a broad overview of data-centric techniques.
- You want to understand the landscape of data engineering methods.
- You are planning a data-centric approach to ML.

## Do not use when
- You need a specific method, not a survey.
- You already have extensive data-centric knowledge.
- You need implementation details for a specific technique.

## Required inputs
- **research_corpus**: Literature on data-centric AI methods.

## Optional inputs
- **domain_focus**: Specific domain to focus the survey on.

## Outputs
- **taxonomy**: Taxonomy of data-centric AI techniques.
- **best_practices**: Guidelines for data-centric AI development.

## Assumptions and prerequisites
- Data quality is as important as model architecture.
- A systematic taxonomy helps practitioners choose methods.
- Data-centric approaches complement model-centric ones.

## Procedure
1. **Review data collection methods**
   Action: Survey techniques for data collection and annotation.
   Why: Collection is the first step in the data pipeline.
   Note: See paper for details.
2. **Review data preparation**
   Action: Survey cleaning, normalization, and transformation methods.
   Why: Preparation improves data quality.
   Note: See paper for details.
3. **Review data augmentation**
   Action: Survey augmentation and synthesis techniques.
   Why: Augmentation increases effective data size.
   Note: See paper for details.
4. **Review data selection**
   Action: Survey subset selection and active learning methods.
   Why: Selection focuses resources on valuable data.
   Note: See paper for details.

## Parameters to set
- **scope** — Role: Breadth of the survey. How to set: Cover all major data-centric areas. Default/range: Comprehensive. Effect: Broader scope provides more guidance.

## Validation checks
- The survey should cover all major data-centric techniques.
- Techniques should be organized in a usable taxonomy.
- Best practices should be actionable.

## Failure modes
- The survey may not cover the latest methods.
- General guidelines may not apply to specific domains.
- The breadth may sacrifice depth.

## Adaptation notes for VLM training
- Use the taxonomy to plan VLM data curation strategies.
- Apply data-centric principles to multimodal data engineering.
- The survey provides a framework for systematic data improvement.

## Implementation notes
- Use the taxonomy as a checklist for data pipeline design.
- Refer to cited papers for implementation details.
- Update the survey with new methods as they appear.

## Evidence from the paper
- The survey provides a comprehensive taxonomy of data-centric AI techniques.
- Data-centric approaches are increasingly recognized as essential for ML success.
- The survey covers collection, preparation, augmentation, selection, and engineering.
- Best practices are synthesized from extensive literature review.

## Source paper
- **Title**: Data-Centric Artificial Intelligence: A Survey
- **Year**: 2023
- **Venue**: arXiv
- **Paper ID**: arxiv-2303.10158v3
- **URL**: http://arxiv.org/abs/2303.10158v3
- **arXiv ID**: 2303.10158v3
