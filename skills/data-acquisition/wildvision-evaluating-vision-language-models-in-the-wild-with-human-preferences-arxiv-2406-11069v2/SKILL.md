# WildVision: Evaluating Vision-Language Models in the Wild with Human Preferences

## One-line decision
Use this skill when you want to evaluate VLMs using real user interactions and preferences collected in the wild. Avoid it when you only need standard benchmark evaluation.

## Skill metadata
- **Skill type**: real-user-vlm-evaluation
- **Paper kind**: operational-method
- **Actionability**: medium
- **Evidence quality**: full_paper

## Goal
Evaluate VLMs using real user interactions and preferences collected from a public arena where users compare VLM outputs, providing ecologically valid evaluation data.

## Problem signature
- Modality: real user image-query-response interactions with preference annotations.
- Data state: user-submitted image-question pairs with VLM comparisons and preferences.
- Scale regime: thousands of real user interactions.
- Model requirement: Any VLM for evaluation in the arena.

## Use when
- You want ecologically valid VLM evaluation.
- You want to understand real user needs and preferences.
- You need evaluation beyond standard benchmarks.

## Do not use when
- Standard benchmarks are sufficient.
- You need controlled evaluation conditions.
- You need domain-specific evaluation.

## Required inputs
- **user_interactions**: Real user image-question submissions.
- **vlm_candidates**: Multiple VLMs for comparison.
- **preference_collection**: Platform for collecting user preferences.

## Optional inputs
- **elo_rating**: Elo rating system for ranking VLMs.

## Outputs
- **wildvision_data**: Real user interactions with VLM preferences.
- **vlm_rankings**: Elo-based VLM rankings from real user preferences.

## Assumptions and prerequisites
- Real user interactions provide ecologically valid evaluation.
- User preferences reflect practical VLM quality.
- An arena format enables fair model comparison.

## Procedure
1. **Deploy VLM arena**
   Action: Create a public platform where users submit image-question pairs.
   Why: Real user submissions provide ecologically valid queries.
   Note: See paper for details.
2. **Generate VLM responses**
   Action: Show outputs from two random VLMs for comparison.
   Why: Head-to-head comparison enables preference collection.
   Note: See paper for details.
3. **Collect user preferences**
   Action: Users choose which VLM output they prefer.
   Why: Preferences provide ranking signal.
   Note: See paper for details.
4. **Compute Elo ratings**
   Action: Update Elo ratings based on preference outcomes.
   Why: Elo provides a robust ranking system.
   Note: See paper for details.

## Parameters to set
- **num_interactions** — Role: Total user interactions collected. How to set: Thousands for reliable rankings. Default/range: Thousands. Effect: More interactions improve ranking reliability.
- **vlm_pool** — Role: VLMs available for comparison. How to set: Include major open and closed VLMs. Default/range: 10+. Effect: More VLMs enable broader comparison.

## Validation checks
- Rankings should stabilize with enough interactions.
- User preferences should be consistent.
- Real-world queries should differ from benchmark-style queries.

## Failure modes
- User query distribution may be biased.
- Preferences may vary across users.
- The arena may attract non-representative users.

## Adaptation notes for VLM training
- WildVision provides real-world evaluation data for VLM development.
- Use real user queries to identify capability gaps in your VLM data.
- Arena-style evaluation complements standard benchmarks.

## Implementation notes
- Use the WildVision platform or build your own arena.
- Track query types and user demographics.
- Monitor ranking stability over time.

## Evidence from the paper
- WildVision evaluates VLMs using real user interactions in an arena format.
- User preferences differ from standard benchmark evaluations.
- Elo ratings provide robust VLM rankings from pairwise comparisons.
- Real-world queries reveal capabilities not tested by standard benchmarks.

## Source paper
- **Title**: WildVision: Evaluating Vision-Language Models in the Wild with Human Preferences
- **Year**: 2024
- **Venue**: arXiv
- **Paper ID**: arxiv-2406.11069v2
- **URL**: http://arxiv.org/abs/2406.11069v2
- **arXiv ID**: 2406.11069v2
