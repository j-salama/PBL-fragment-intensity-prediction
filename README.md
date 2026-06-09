Peptide Fragment Intensity Prediction
Predicting ECD fragment ion intensities from peptide sequence features using machine learning. Developed as part of TUM's Problem-Based Learning course (Bioinformatics B.Sc)

Project Status
Work in progress. Current state: EDA complete, baseline model trained. Model improvement ongoing.
Data
~9 million ion rows from ECD fragmentation experiments. Each row represents a fragment ion with associated peptide features and measured intensity.

Approach

EDA — distribution analysis, missing value handling, feature correlation
Feature Engineering —  features including ion type, fragment number, charge, peptide length, relative position, and local residue context
Baseline Model — Random Forest regressor

Results (Baseline)
Metric	Score
Spectral Angle	0.76
Pearson r	0.40
R²	0.10

Structure
01-EDA.ipynb       # Exploratory data analysis
02-model.ipynb     # Feature engineering + model training
src/               # Helper modules
requirements.txt   # Dependencies

Requirements
pip install -r requirements.txt

