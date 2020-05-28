# -*- coding: utf-8 -*-
"""
Created on Thu May 28 23:06:26 2020

@author: Dell 1
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('eda_data.csv')

# Tasks to be done
# A: Choose relevant columns
df.columns
df_model = [['Rating', 'Size', 'Type of ownership', 'Industry', 'Sector', 'Revenue', 'num_comp', '']]

# B: Get dummy data (separate cols for caregorical values)
# C: Train test split
# D: Multilinear regression model
# E: Lasso model
# F: Random forest model
# G: Tune the models using Gridsearchcv
# H: Test ensembles