Peptide Fragment Intensity Prediction

Predicting ECD fragment ion intensities from peptide sequence features using machine learning.

Developed as part of TUM's Problem-Based Learning course (Bioinformatics B.Sc) 

work in progress, current state: EDA complete, model has enzyme stratification, 0-filling to prevent false positives, normalized metrics,  improvement ongoing

EDA: distribution analysis, missing value handling, feature correlation

features: ion type, fragment number, charge, peptide length, relative position, enzymes, and local residue context

architecture: random forest regressor / XGboost

