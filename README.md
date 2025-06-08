# diabetes-prediction-models
Machine Learning models to predict diabetes using different classifiers (Decision Tree, Random Forest, Logistic Regression).
# Diabetes Diagnosis Machine Learning Models

This repository contains implementations of several machine learning models to predict diabetes diagnoses based on a given dataset. The project includes Decision Tree, Random Forest, and Logistic Regression classifiers, implemented as separate Python modules and demonstrated in a main Jupyter notebook.

## Project Structure

- `diabetes.csv` – The dataset used for training and testing.
- `diabetes_decisiontree.py` – Decision Tree model implementation.
- `diabetes_randomforest.py` – Random Forest model implementation.
- `diabetes_logisticregression.py` – Logistic Regression model implementation.
- `Diabetes_Main.ipynb` – Jupyter notebook that loads data, runs all models, and compares their performance.

## Features

- Data preprocessing and splitting
- Model training and evaluation using accuracy, recall, precision, and F1-score
- Comparison of model performances with clear reasoning
- Suitable for running in Google Colab or local Jupyter environment

## Requirements

- Python 3.7+
- scikit-learn
- pandas
- numpy

Install dependencies with:

```bash
pip install -r requirements.txt
