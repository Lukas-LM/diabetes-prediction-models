# -*- coding: utf-8 -*-
"""Diabetes-DecisionTree.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1skoTuDvFFQcw1X-iQXwokRFLzNOpLK2U
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score
def run_decision_tree():
    df = pd.read_csv('diabetes.csv')

    #every important col with unrealistic zero-values getting in a variable
    cols_with_zeros = ['Glucose','BloodPressure','SkinThickness','Insulin','BMI']

    #I change the zero-values in my selected cols to empty values with replace(0, np.nan)
    df[cols_with_zeros] = df[cols_with_zeros].replace(0, np.nan)

    #I fill every empty value with the mean of the other values
    df[cols_with_zeros] = df[cols_with_zeros].fillna(df.mean())
    
    X = df.drop("Outcome", axis=1)
    y = df["Outcome"].values
    #I split my dataset into 80% to train and 20% to test data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    results = []
    #I am searching the best number of depth by testing some numbers
    for depth in [3, 5, 7, 10]:
        #I define the model as a classifier of DecisionTree
        model = DecisionTreeClassifier(criterion="entropy", max_depth=depth)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        #the parameters show me the evaluation of the model or the models
        metrics = {
            #depth is the number of level of a DecisionTree
            "max_depth": depth
            #shows me the accuracy of every true predicted classification
            "accuracy": accuracy_score(y_test, y_pred),
            #recall shows me how many correct predictions my model makes in relation to the really correct ones
            "recall": recall_score(y_test, y_pred),
            #shows me the Accuracy of positiv predictions
            "precision": precision_score(y_test, y_pred),
            #combined precision and recall, it is important for unbalanced datasets
            "f1_score": f1_score(y_test, y_pred)
        }

        #I have to use Cross-Validation because some depth-values shows inconsistent results
        for cv in [3, 5, 7, 9, 12]:
            scores = cross_val_score(model, X, y, cv=cv)
            metrics[f"cv{cv}_mean_acc"] = scores.mean()

        results.append(metrics)

    return results
