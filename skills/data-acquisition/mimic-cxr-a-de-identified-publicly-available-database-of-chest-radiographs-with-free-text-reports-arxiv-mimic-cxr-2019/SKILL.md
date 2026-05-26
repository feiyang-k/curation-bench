# MIMIC-CXR: A De-identified Publicly Available Database of Chest Radiographs with Free-Text Reports

## One-line decision
Use this skill when you need a large-scale medical image-report dataset for training biomedical VLMs on chest X-ray understanding. Avoid it when you do not work with medical imaging.

## Skill metadata
- **Skill type**: medical-image-report-dataset
- **Paper kind**: operational-method
- **Actionability**: high
- **Evidence quality**: full_paper

## Goal
Provide a large-scale, de-identified dataset of 377K chest radiographs with associated free-text radiology reports, enabling medical VLM training and evaluation.

## Problem signature
- Modality: chest X-ray images paired with radiology reports.
- Data state: 377K chest X-rays with de-identified radiology reports.
- Scale regime: 377K chest radiograph-report pairs.
- Model requirement: Any medical VLM for training on radiology data.

## Use when
- You need medical image-report training data.
- You are building a medical VLM.
- You need chest X-ray understanding data.

## Do not use when
- You do not work with medical imaging.
- You need other imaging modalities.
- Non-medical VLM data is sufficient.

## Required inputs
- **chest_xrays**: 377K de-identified chest radiographs.
- **radiology_reports**: Free-text reports for each radiograph.
- **access_approval**: PhysioNet credential for data access.

## Optional inputs
- **labels**: Automated labels from CheXpert labeler.

## Outputs
- **mimic_cxr**: 377K chest X-ray-report pairs.
- **medical_vlm_data**: Training data for medical VLMs.

## Assumptions and prerequisites
- Chest X-rays with reports provide supervised medical VLM training.
- De-identification enables responsible data sharing.
- Radiology reports provide rich textual supervision.

## Procedure
1. **De-identify patient data**
   Action: Remove all patient identifying information.
   Why: Privacy protection enables sharing.
   Note: See paper for details.
2. **Pair images with reports**
   Action: Link each chest X-ray with its radiology report.
   Why: Creates supervised image-text pairs.
   Note: See paper for details.
3. **Apply automated labels**
   Action: Use CheXpert labeler for structured findings.
   Why: Labels enable additional supervision.
   Note: See paper for details.
4. **Release through PhysioNet**
   Action: Share through credentialed access.
   Why: Controlled access ensures responsible use.
   Note: See paper for details.

## Parameters to set
- **dataset_size** — Role: Total image-report pairs. How to set: 377K from MIMIC database. Default/range: 377K. Effect: Largest publicly available CXR dataset.
- **de_identification** — Role: Level of privacy protection. How to set: Full de-identification. Default/range: Complete. Effect: Enables responsible sharing.

## Validation checks
- De-identification should be complete.
- Reports should match their images.
- The dataset should cover diverse pathologies.

## Failure modes
- Medical data requires careful handling.
- Access requires credentialing.
- Radiology-specific language may challenge general models.

## Adaptation notes for VLM training
- MIMIC-CXR is the primary dataset for medical VLM training.
- Combine with PMC data for broader biomedical coverage.
- Medical VLM training requires domain-specific data.

## Implementation notes
- Obtain PhysioNet credentials for access.
- Use CheXpert labels for structured supervision.
- Handle medical image formats appropriately.

## Evidence from the paper
- MIMIC-CXR provides 377K chest X-rays with radiology reports.
- The dataset is the largest publicly available CXR-report dataset.
- De-identification enables responsible medical AI research.
- MIMIC-CXR is foundational for medical VLM development.

## Source paper
- **Title**: MIMIC-CXR: A De-identified Publicly Available Database of Chest Radiographs with Free-Text Reports
- **Year**: 2019
- **Venue**: Scientific Data
- **Paper ID**: arxiv-mimic-cxr-2019
- **URL**: https://physionet.org/content/mimic-cxr/2.0.0/
- **arXiv ID**: N/A
