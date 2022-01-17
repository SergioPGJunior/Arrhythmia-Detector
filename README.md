# Arrhythmia detector for hemodialysis patients
Python-based arrhythmia detector based on ECG data for hemodialysis patients.

In this study eight classifiers were evaluated for the task of arrhythmia detection in ECG signals. First, a grid search associated with 10-fold cross-validation was used to tune the hyperparameters and find the best classifier. After this, tests of statistical significance were performed in order to identify if the differences in the models' results were significant. Finally, it was decided to deal with the classes' imbalance.

## Classifiers:

* Support Vector Machines
* Random Forests
* K-NearestNeighbors
* Decision tree
* Adaboost
* Gradient boosting
* MLP neural network
* Logistic Regression

* Statistical significance tests:
  * Freidman test
  * Nemenyi post-hoc test

## Imbalanced Classification:

* Undersampling
* Upsampling:
  * SMOTE
