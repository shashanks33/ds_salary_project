# -*- coding: utf-8 -*-
"""
Created on Thu May 28 23:06:26 2020

@author: Dell 1
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

df = pd.read_csv('eda_data.csv')

# Tasks to be done
# A: Choose relevant columns
df.columns
df_model = df[['avg_salary','Rating', 'Size', 'Type of ownership', 'Industry', 'Sector', 'Revenue', 'num_comp','hourly', 'employer_provided_salary', 'company_state',
'same_state', 'age', 'python', 'spark', 'aws', 'excel', 'job_simplify', 'seniority', 'desc_length']]


# B: Get dummy data (separate cols for caregorical values)
# We could use one hot encoding too
df_dum = pd.get_dummies(df_model)

# C: Train test split
X = df_dum.drop('avg_salary', axis=1)
y = df_dum['avg_salary'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# D: Multilinear regression model


# E: Lasso model
# F: Random forest model
# G: Tune the models using Gridsearchcv
# H: Test ensembles