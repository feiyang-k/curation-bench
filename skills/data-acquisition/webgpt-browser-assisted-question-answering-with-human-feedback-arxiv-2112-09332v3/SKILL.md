# WebGPT: Browser-assisted Question-answering with Human Feedback

## One-line decision
Use this skill when you want to create training data for LLMs to use web browsing for answering questions with citations. Avoid it when you do not need web-augmented question answering.

## Skill metadata
- **Skill type**: web-browsing-training-data
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Create training data for LLMs to perform web browsing and cite sources when answering questions, using human demonstrations and comparisons.

## Problem signature
- Modality: question-answer pairs with web browsing trajectories and citations.
- Data state: human demonstrations of web browsing for QA, plus comparison data.
- Scale regime: thousands of browsing demonstrations and comparisons.
- Model requirement: GPT-3 with web browsing interface.

## Use when
- You want LLMs to browse the web for answering questions.
- You need answers with source citations.
- You can collect human browsing demonstrations.

## Do not use when
- Closed-book QA is sufficient.
- You do not need web-augmented answers.
- Human demonstration collection is infeasible.

## Required inputs
- **questions**: Questions requiring web research.
- **browsing_interface**: Web browsing tool for the LLM.
- **human_demonstrations**: Human demonstrations of web browsing for QA.

## Optional inputs
- **comparison_data**: Human comparisons of browsing quality.

## Outputs
- **browsing_demonstrations**: Human browsing trajectories for training.
- **webgpt_model**: LLM trained to browse and cite.

## Assumptions and prerequisites
- Human demonstrations teach effective browsing strategies.
- Web browsing enables more accurate and cited answers.
- Comparison data improves answer quality through RLHF.

## Procedure
1. **Collect browsing demonstrations**
   Action: Have humans demonstrate web browsing to answer questions.
   Why: Demonstrations provide training signal for browsing.
   Note: See paper for details.
2. **Train browsing model**
   Action: Fine-tune LLM on browsing demonstrations.
   Why: Teaches the model to browse effectively.
   Note: See paper for details.
3. **Collect comparison data**
   Action: Have humans compare model answers for quality.
   Why: Comparisons enable RLHF improvement.
   Note: See paper for details.
4. **Apply RLHF**
   Action: Fine-tune with RLHF using comparison data.
   Why: Improves answer quality through human feedback.
   Note: See paper for details.

## Parameters to set
- **demonstration_count** — Role: Number of human demonstrations. How to set: Thousands. Default/range: Thousands. Effect: More demonstrations improve browsing quality.
- **comparison_count** — Role: Number of human comparisons. How to set: Thousands. Default/range: Thousands. Effect: More comparisons improve RLHF.

## Validation checks
- WebGPT should provide more accurate answers than closed-book.
- Answers should include valid citations.
- RLHF should improve answer quality over demonstrations alone.

## Failure modes
- Web browsing may retrieve irrelevant information.
- Citations may be from unreliable sources.
- Browsing demonstrations are expensive to collect.

## Adaptation notes for VLM training
- Web browsing data applies to VLMs that need to retrieve information.
- The demonstration-then-RLHF approach generalizes to any tool use.
- Citation training improves VLM trustworthiness.

## Implementation notes
- Build a browsing interface for demonstrations.
- Collect high-quality demonstrations from trained annotators.
- Monitor citation accuracy.

## Evidence from the paper
- WebGPT learns to browse the web and cite sources for QA.
- Human demonstrations effectively teach browsing strategies.
- RLHF on comparisons improves answer quality.
- Web-augmented answers are preferred over closed-book 56% of the time.

## Source paper
- **Title**: WebGPT: Browser-assisted Question-answering with Human Feedback
- **Year**: 2022
- **Venue**: arXiv
- **Paper ID**: arxiv-2112.09332v3
- **URL**: http://arxiv.org/abs/2112.09332v3
- **arXiv ID**: 2112.09332v3
