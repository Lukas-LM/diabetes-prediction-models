# Diabetes Diagnosis Classifier

This project implements a machine learning classifier to predict potential diabetes diagnoses based on structured medical data. The goal is to compare multiple classification models in terms of their performance on the same dataset.

## Project Overview

- Type: Binary classification (medical diagnosis)
- Dataset: CSV file with patient features such as glucose level, BMI, age, etc.
- Language: Python
- Libraries: NumPy, pandas, scikit-learn

## Models Used

- Decision Tree Classifier  
- Logistic Regression  
- Random Forest Classifier

## Workflow

1. Data Preprocessing
   - Handling missing values
   - Basic cleaning and formatting

2. Model Training
   - Train/test split
   - Fitting the three models using scikit-learn

3. Model Evaluation
   - Accuracy
   - Precision
   - Recall
   - F1-Score

4. Result Comparison
   - Evaluate and compare all models using the same metrics

## Folder Structure (Example)

```
diabetes-classifier/
├── diabetes.csv
├── decision_tree.py
├── logistic_regression.py
├── random_forest.py
├── main_notebook.ipynb
└── README.md
```

## Goal

The aim of this project was to build a reliable baseline for medical classification problems using standard ML tools, with a focus on modular, testable and reproducible code. This project may serve as a foundation for future improvements or integration into a web application.
