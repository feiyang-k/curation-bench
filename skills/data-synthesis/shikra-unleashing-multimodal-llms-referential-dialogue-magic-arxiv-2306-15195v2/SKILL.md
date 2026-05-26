# Shikra: Unleashing Multimodal LLM's Referential Dialogue Magic

## One-line decision
Use this skill when you want to create referential dialogue data where the VLM and user exchange spatial references (bounding boxes) naturally within conversation. Avoid it when you do not need spatial references in conversation.

## Skill metadata
- **Skill type**: referential-dialogue-data
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Create referential dialogue data where both the user and VLM naturally exchange spatial references (bounding boxes as coordinates) within conversation, enabling intuitive spatial communication.

## Problem signature
- Modality: conversation data with inline spatial references as coordinate text.
- Data state: dialogue data with bounding box coordinates embedded in text.
- Scale regime: curated referential dialogue instruction data.
- Model requirement: VLM processing text with inline coordinate references.

## Use when
- You want natural spatial reference exchange in VLM conversations.
- You need both input and output spatial grounding.
- You want referential dialogue capability.

## Do not use when
- Spatial references are not needed.
- You prefer separate grounding and conversation modules.
- Simple captioning is sufficient.

## Required inputs
- **grounding_data**: Data with object bounding boxes.
- **dialogue_generator**: Pipeline for creating referential dialogues.
- **coordinate_format**: Format for embedding coordinates in text.

## Optional inputs
- **multi_turn_dialogues**: Multi-turn referential conversations.

## Outputs
- **referential_dialogues**: Conversation data with spatial references.
- **shikra_model**: VLM with referential dialogue capability.

## Assumptions and prerequisites
- Spatial references can be naturally embedded in text as coordinates.
- Both user input and model output can contain spatial references.
- Referential dialogue is a natural and useful interaction mode.

## Procedure
1. **Create referential dialogue data**
   Action: Generate conversations with inline spatial references.
   Why: Teaches natural spatial communication.
   Note: See paper for details.
2. **Format coordinates in text**
   Action: Embed bounding box coordinates as text tokens.
   Why: Enables coordinate exchange without special architecture.
   Note: See paper for details.
3. **Train referential VLM**
   Action: Train on referential dialogue data.
   Why: Develops referential dialogue capability.
   Note: See paper for details.
4. **Evaluate spatial dialogue**
   Action: Test referential understanding and generation.
   Why: Validates referential capability.
   Note: See paper for details.

## Parameters to set
- **coordinate_format** — Role: How coordinates are represented in text. How to set: Normalized [x1,y1,x2,y2] in text. Default/range: Normalized coordinates. Effect: Format affects learnability.
- **dialogue_types** — Role: Types of referential dialogues. How to set: Include pointing, describing, and asking about regions. Default/range: Diverse. Effect: More types improve flexibility.

## Validation checks
- The model should correctly interpret user spatial references.
- Model-generated spatial references should be accurate.
- Referential dialogue should feel natural.

## Failure modes
- Coordinate representation may be hard to learn precisely.
- Some spatial references may be ambiguous.
- Multi-turn referential dialogue adds complexity.

## Adaptation notes for VLM training
- Referential dialogue extends VLM spatial communication.
- The coordinate-in-text approach is simple and effective.
- Combine with other grounding data for comprehensive spatial understanding.

## Implementation notes
- Use normalized coordinates for resolution independence.
- Train on diverse referential dialogue types.
- Evaluate on referring expression benchmarks.

## Evidence from the paper
- Shikra creates referential dialogue data with inline spatial references.
- Both user and model naturally exchange bounding box coordinates in conversation.
- The approach enables intuitive spatial communication without special architecture.
- Referential dialogue is a natural and useful VLM interaction mode.

## Source paper
- **Title**: Shikra: Unleashing Multimodal LLM's Referential Dialogue Magic
- **Year**: 2023
- **Venue**: arXiv
- **Paper ID**: arxiv-2306.15195v2
- **URL**: http://arxiv.org/abs/2306.15195v2
- **arXiv ID**: 2306.15195v2
