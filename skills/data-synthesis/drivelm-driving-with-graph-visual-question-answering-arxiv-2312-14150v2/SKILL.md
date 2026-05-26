# DriveLM: Driving with Graph Visual Question Answering

## One-line decision
Use this skill when you want to create structured QA data for autonomous driving VLMs using graph-based scene understanding. Avoid it when you do not work with autonomous driving or need general-purpose VQA.

## Skill metadata
- **Skill type**: driving-qa-data-generation
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Create structured visual QA data for autonomous driving by building graph representations of driving scenes and generating questions about perception, prediction, planning, and behavior.

## Problem signature
- Modality: driving scene images/videos with structured QA about driving tasks.
- Data state: driving scene data annotated with graph-based QA covering perception, prediction, and planning.
- Scale regime: thousands of driving scenes with comprehensive QA.
- Model requirement: VLM for driving scene understanding; graph annotation pipeline.

## Use when
- You need driving-specific visual QA data.
- You want structured reasoning about driving scenes.
- You need perception, prediction, and planning QA.

## Do not use when
- You do not work with autonomous driving.
- General VQA is sufficient for your needs.
- You lack driving scene data.

## Required inputs
- **driving_scenes**: Driving scene images/videos from nuScenes or similar.
- **graph_annotations**: Graph representations of scene objects and relationships.
- **qa_templates**: Templates for perception, prediction, planning, and behavior questions.

## Optional inputs
- **3d_annotations**: 3D bounding box and trajectory annotations.

## Outputs
- **drivelm_qa_data**: Structured driving QA dataset.
- **driving_vlm**: VLM fine-tuned for driving scene understanding.

## Assumptions and prerequisites
- Graph-based scene representation enables systematic QA generation.
- Driving tasks can be decomposed into perception, prediction, and planning.
- Structured QA teaches reasoning about driving scenarios.

## Procedure
1. **Build scene graphs**
   Action: Create graph representations of driving scenes with objects, relationships, and actions.
   Why: Graphs provide structured information for QA generation.
   Note: See paper for details.
2. **Generate perception questions**
   Action: Create questions about what objects are present, their attributes, and locations.
   Why: Perception is the foundation of driving understanding.
   Note: See paper for details.
3. **Generate prediction questions**
   Action: Create questions about what objects will do next.
   Why: Prediction is critical for safe driving.
   Note: See paper for details.
4. **Generate planning questions**
   Action: Create questions about appropriate driving actions.
   Why: Planning tests end-to-end driving reasoning.
   Note: See paper for details.
5. **Train driving VLM**
   Action: Fine-tune a VLM on the generated driving QA data.
   Why: Specialized training enables driving scene understanding.
   Note: See paper for details.

## Parameters to set
- **qa_categories** — Role: Categories of driving questions. How to set: Include perception, prediction, planning, behavior. Default/range: 4 categories. Effect: Comprehensive coverage tests all driving reasoning aspects.
- **scene_complexity** — Role: Complexity of driving scenarios. How to set: Include simple and complex traffic scenarios. Default/range: Diverse. Effect: Complex scenarios test deeper reasoning.

## Validation checks
- Perception questions should test correct object identification.
- Prediction questions should have verifiable future states.
- Planning questions should test safe driving decisions.

## Failure modes
- Graph annotations may miss important scene elements.
- Template-based QA may lack diversity.
- Driving reasoning may be too specialized for general VLMs.

## Adaptation notes for VLM training
- DriveLM-style data is essential for autonomous driving VLMs.
- The graph-to-QA approach generalizes to other structured domains.
- Combine with general instruction data for balanced training.

## Implementation notes
- Use nuScenes annotations as the basis for graphs.
- Generate diverse question phrasings for robustness.
- Track per-category QA accuracy.

## Evidence from the paper
- DriveLM creates structured driving QA data using graph-based scene understanding.
- Questions cover perception, prediction, planning, and behavior reasoning.
- The graph structure enables systematic and comprehensive QA generation.
- DriveLM enables end-to-end driving reasoning evaluation for VLMs.

## Source paper
- **Title**: DriveLM: Driving with Graph Visual Question Answering
- **Year**: 2023
- **Venue**: ECCV
- **Paper ID**: arxiv-2312.14150v2
- **URL**: http://arxiv.org/abs/2312.14150v2
- **arXiv ID**: 2312.14150v2
