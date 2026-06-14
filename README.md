Peptide Fragment Intensity Prediction

Predicting ECD fragment ion intensities from peptide sequence features using machine learning. ~9 million ion rows from ECD fragmentation experiments. Each row represents a fragment ion with associated peptide features and measured intensity.
Developed as part of TUM's Problem-Based Learning course (Bioinformatics B.Sc) 

work in progress, Current state: EDA complete, baseline model trained. Model improvement ongoing.

EDA: distribution analysis, missing value handling, feature correlation
features: ion type, fragment number, charge, peptide length, relative position, enzymes, and local residue context
architecture: random Forest regressor

Spectral Angle	0.80
Pearson r	0.78

pip install -r requirements.txt

