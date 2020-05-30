# -*- coding: utf-8 -*-
"""
Created on Thu May 28 23:06:26 2020

@author: Dell 1
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

from sklearn.metrics import mean_absolute_error

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
# Using model from stats models and sklearn both
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression, Lasso
from sklearn.model_selection import cross_val_score, GridSearchCV
from sklearn.ensemble import RandomForestRegressor

X_sm = X = sm.add_constant(X)
model = sm.OLS(y, X_sm)
model.fit().summary()

lin_model = LinearRegression()
lin_model.fit(X_train, y_train)

''' Statsmodels also helps us determine which of our variables are statistically significant 
through the p-values. If our p-value is <.05, then that variable is statistically significant. 
This is a useful tool to tune your model.'''

np.mean(cross_val_score(lin_model, X_train, y_train, scoring='neg_mean_absolute_error', cv=3))
# Obtained a mean of -20.7677 thousand dollars meaning that the matrix is higly sparse maybe 
# due to less data etc. So we'll now try to use other models that can normalize those values eg. Lasso.

# E: Lasso model 
lin_model_lasso = Lasso(alpha = 0.13)
lin_model_lasso.fit(X_train, y_train)
np.mean(cross_val_score(lin_model_lasso, X_train, y_train, scoring='neg_mean_absolute_error', cv=3))
# Obtained a mean of -21.0943 thousand dollars without alpha=0.13 and -19.2576 with alpha = 0.13

alpha = []
error = []

for i in range(1, 100):
    alpha.append(i/100)
    lml = Lasso(alpha=(i/100))
    error.append(np.mean(cross_val_score(lml, X_train, y_train, scoring='neg_mean_absolute_error', cv=3)))
print('alpha:', alpha)
print('error:', error)

plt.plot(alpha, error)

# Find out for which alpha value we get highest error
err = tuple(zip(alpha, error))
df_err = pd.DataFrame(err, columns = ['alpha', 'error'])
df_err[df_err.error == max(df_err.error)]
# Obtained alpha = 0.13 for error = -19.25768

# F: Random forest model
rf_model = RandomForestRegressor()

np.mean(cross_val_score(rf_model, X_train, y_train, scoring='neg_mean_absolute_error', cv=3))
# Mean value of almost -15.0136 which is better than prev models

# G: Tune the models using Gridsearchcv
parameters = {'n_estimators':range(10,300,10), 'criterion':('mse','mae'), 'max_features':('auto','sqrt','log2')}

gs_model = GridSearchCV(rf_model,parameters,scoring='neg_mean_absolute_error',cv=3)
gs_model.fit(X_train,y_train)

gs_model.best_score_
# -14.8137 score
gs_model.best_estimator_

# H: Test ensembles
tpred_linear_model = lin_model.predict(X_test)
tpred_linear_model_lasso = lin_model_lasso.predict(X_test)
tpred_rf_model = gs_model.best_estimator_.predict(X_test)

mean_absolute_error(y_test, tpred_linear_model) #18.85362
mean_absolute_error(y_test, tpred_linear_model_lasso) #19.66525
mean_absolute_error(y_test, tpred_rf_model) #11.11507

mean_absolute_error(y_test, (tpred_rf_model+tpred_linear_model)/2) #14.208883


# Saving the model
import pickle

file_name = "model_file.p"
pickl = {'model': gs_model.best_estimator_}
pickle.dump(pickl, open(file_name, "wb" ))

with open(file_name, 'rb') as file:
    data = pickle.load(file)
    model = data['model']
    
model.predict(np.array(list(X_test.iloc[1,:])).reshape(1,-1))[0]

list(X_test.iloc[1,:])