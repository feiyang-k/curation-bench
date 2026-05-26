# Woodpecker: Hallucination Correction for Multimodal Large Language Models

## One-line decision
Use this skill when you want to correct VLM hallucinations post-hoc by extracting claims, verifying them against the image, and rewriting responses. Avoid it when you want to prevent hallucination during training rather than correct it post-hoc.

## Skill metadata
- **Skill type**: hallucination-correction-pipeline
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Correct VLM hallucinations post-hoc by extracting factual claims from responses, verifying each claim against the image using specialized tools, and rewriting the response to remove hallucinated content.

## Problem signature
- Modality: VLM outputs corrected through claim extraction and visual verification.
- Data state: VLM responses processed through a verification pipeline.
- Scale regime: any number of VLM responses to verify.
- Model requirement: VLM for initial response + verification tools (detection, etc.).

## Use when
- You want to correct VLM hallucinations after generation.
- You can use verification tools to check claims.
- You need trustworthy VLM outputs.

## Do not use when
- You want to prevent hallucination during training.
- Post-hoc correction is too slow for your use case.
- Verification tools are unavailable.

## Required inputs
- **vlm_responses**: VLM-generated descriptions or answers.
- **source_images**: Images the VLM responded to.
- **verification_tools**: Object detectors, OCR, etc. for claim verification.

## Optional inputs
- **rewriting_model**: LLM for rewriting corrected responses.

## Outputs
- **corrected_responses**: VLM responses with hallucinations removed.
- **verification_report**: Per-claim verification results.

## Assumptions and prerequisites
- VLM hallucinations can be detected by verifying claims against images.
- Specialized tools can verify specific claims.
- Rewriting can remove hallucinated content while preserving accurate content.

## Procedure
1. **Extract factual claims**
   Action: Parse VLM response into individual factual claims.
   Why: Claims are the units for verification.
   Note: See paper for details.
2. **Verify claims against image**
   Action: Use detection, OCR, and other tools to verify each claim.
   Why: Visual verification identifies hallucinated claims.
   Note: See paper for details.
3. **Identify hallucinations**
   Action: Flag claims that fail verification.
   Why: Failed claims are likely hallucinated.
   Note: See paper for details.
4. **Rewrite response**
   Action: Remove hallucinated claims and rewrite coherently.
   Why: Produces a corrected, trustworthy response.
   Note: See paper for details.

## Parameters to set
- **verification_tools** — Role: Tools for claim verification. How to set: Include object detection, OCR, attribute recognition. Default/range: Multiple tools. Effect: More tools verify more claim types.
- **confidence_threshold** — Role: Threshold for accepting/rejecting claims. How to set: Tune for precision-recall balance. Default/range: Task-dependent. Effect: Higher threshold rejects more but may over-correct.

## Validation checks
- Corrected responses should have fewer hallucinations.
- Accurate content should be preserved.
- Verification should correctly identify hallucinated claims.

## Failure modes
- Verification tools may miss some hallucinations.
- Claim extraction may be imprecise.
- Rewriting may introduce new issues.

## Adaptation notes for VLM training
- Woodpecker's pipeline can generate correction data for VLM training.
- Use corrected responses as preference data for DPO alignment.
- The verification approach provides a template for VLM quality assurance.

## Implementation notes
- Integrate multiple verification tools.
- Use efficient claim extraction.
- Monitor correction quality on samples.

## Evidence from the paper
- Woodpecker corrects VLM hallucinations through claim verification.
- Post-hoc correction significantly reduces hallucination rates.
- Specialized tools effectively verify visual claims.
- The approach provides a practical VLM quality assurance pipeline.

## Source paper
- **Title**: Woodpecker: Hallucination Correction for Multimodal Large Language Models
- **Year**: 2023
- **Venue**: arXiv
- **Paper ID**: arxiv-2310.16045v2
- **URL**: http://arxiv.org/abs/2310.16045v2
- **arXiv ID**: 2310.16045v2
