# Peptide Fragment Intensity Prediction

Predicting ECD fragment ion intensities from peptide sequence features.

Developed for TUM's Problem-Based Learning course (Bioinformatics B.Sc.).

## Notebooks
- `01-EDA.ipynb` — distributions, missing values, feature correlation
- `02-baseline.ipynb` — Random Forest / XGBoost, with a random-uniform dummy as a floor
- `03-embedding.ipynb` — PyTorch model with learned amino-acid embeddings

## Features
Ion type, fragment number, charge, peptide length, relative position, enzyme, and local residue window.

## Evaluation
Per-spectrum spectral angle and Pearson correlation (`src/metrics.py`). Split by peptide, stratified by enzyme; unobserved fragments are zero-filled.

## Status
Work in progress.

## Data
Reads `data_for_student.parquet` and `metadata_for_student.parquet` (not tracked in git).
