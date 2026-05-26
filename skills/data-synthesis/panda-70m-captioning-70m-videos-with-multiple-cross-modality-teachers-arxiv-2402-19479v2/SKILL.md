# Panda-70M: Captioning 70M Videos with Multiple Cross-Modality Teachers

## One-line decision
Use this skill when you want to generate captions for 70M video clips using multiple cross-modality teacher models. Avoid it when you only need image captions or cannot process video at this scale.

## Skill metadata
- **Skill type**: video-caption-generation
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Generate high-quality captions for 70 million video clips by leveraging multiple cross-modality teacher models and selecting the best caption through a student model.

## Problem signature
- Modality: video clips with generated captions from multiple teacher models.
- Data state: HD-VILA-100M videos split into clips and captioned by multiple teachers.
- Scale regime: 70 million video clips with generated captions.
- Model requirement: Multiple teacher models (text-based, video-based, multimodal) for caption generation; student model for selection.

## Use when
- You need a large-scale video-caption dataset for video-language pretraining.
- You want to leverage multiple captioning approaches for caption diversity.
- You need captions for tens of millions of video clips.

## Do not use when
- You only work with images, not videos.
- You need captions for a small number of videos.
- Manual video annotation is feasible at your scale.

## Required inputs
- **video_clips**: 70M video clips segmented from longer videos.
- **teacher_models**: Multiple captioning models (text-based, visual, multimodal).
- **student_selector**: Model for selecting the best caption from multiple candidates.

## Optional inputs
- **quality_filter**: Filter for removing low-quality captions.

## Outputs
- **panda_70m_dataset**: 70M video clips with high-quality generated captions.
- **video_captioning_pipeline**: Multi-teacher caption generation and selection pipeline.

## Assumptions and prerequisites
- Multiple teacher models provide complementary caption perspectives.
- A student selector can identify the best caption from multiple candidates.
- Large-scale video captioning enables video-language pretraining.

## Procedure
1. **Segment videos into clips**
   Action: Split long videos into semantically coherent clips.
   Why: Clips are the natural unit for video-language learning.
   Note: See paper for details.
2. **Generate captions with multiple teachers**
   Action: Run each teacher model on each clip to produce candidate captions.
   Why: Multiple perspectives increase caption quality and diversity.
   Note: See paper for details.
3. **Select best captions**
   Action: Train a student model to select the best caption from candidates.
   Why: Selection produces higher quality than any single teacher.
   Note: See paper for details.
4. **Filter and validate**
   Action: Remove low-quality captions and validate on samples.
   Why: Quality control ensures dataset utility.
   Note: See paper for details.
5. **Release Panda-70M**
   Action: Package and release the video-caption dataset.
   Why: Enables large-scale video-language research.
   Note: See paper for details.

## Parameters to set
- **num_teachers** — Role: Number of teacher models used. How to set: 3+ teachers for diverse perspectives. Default/range: 3+. Effect: More teachers increase diversity but also compute.
- **clip_duration** — Role: Length of video clips. How to set: 5-30 seconds for semantic coherence. Default/range: Variable. Effect: Shorter clips are easier to caption but may lack context.
- **selection_strategy** — Role: How the best caption is selected. How to set: Train a student model on human preferences. Default/range: Student model. Effect: Learned selection outperforms heuristics.

## Validation checks
- Selected captions should be more accurate than any single teacher.
- The dataset should cover diverse video content.
- Video-language models trained on Panda-70M should outperform those trained on smaller datasets.

## Failure modes
- All teachers may fail on the same difficult videos.
- Clip segmentation may split semantic units.
- Caption selection may prefer verbose over accurate captions.

## Adaptation notes for VLM training
- Panda-70M is designed for video-language model pretraining.
- The multi-teacher approach can be applied to image captioning at scale.
- Combine with image-text data for unified multimodal pretraining.

## Implementation notes
- Use distributed video processing for 70M clips.
- Cache teacher model outputs for efficient selection training.
- Store video metadata for reproducibility.

## Evidence from the paper
- Panda-70M provides 70M video clips with high-quality captions from multiple cross-modality teachers.
- The multi-teacher selection approach produces better captions than any single model.
- The dataset enables state-of-the-art video-language pretraining.
- Panda-70M is the largest publicly available video-caption dataset.

## Source paper
- **Title**: Panda-70M: Captioning 70M Videos with Multiple Cross-Modality Teachers
- **Year**: 2024
- **Venue**: CVPR
- **Paper ID**: arxiv-2402.19479v2
- **URL**: http://arxiv.org/abs/2402.19479v2
- **arXiv ID**: 2402.19479v2
