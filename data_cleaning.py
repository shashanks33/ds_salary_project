# -*- coding: utf-8 -*-
"""
Created on Mon May 25 23:14:51 2020

@author: Dell 1
"""

import pandas as pd

df = pd.read_csv("glassdoor_jobs.csv")

#salary parse

#Create a new col for the salaries with hourly rates
df['hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)

#Same with employer provided
df['employer_provided_salary'] = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary:' in x.lower() else 0)

#Salary estimate has -1 values instead of actual salaries
#So let us remove all the rows that contain the value -1 for the salary estimate col
df = df[df['Salary Estimate'] != '-1'] 
#Total rows changes from 956 to 742

#Remove the text from the salary estimate column (Glassdoor est)
#We can use either regular exp or lambda
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])

#Remove the K in salary 
remove_k = salary.apply(lambda x: x.replace('K', '').replace('$', ''))

#Remove the per hour 
remove_hr = remove_k.apply(lambda x: x.lower().replace('employer provided salary:', '').replace('per hour', ''))

#Make new cols for minimum salary and max salary and average salary
df['min_salary'] = remove_hr.apply(lambda x: int(x.split('-')[0]))
df['max_salary'] = remove_hr.apply(lambda x: int(x.split('-')[1]))
df['avg_salary'] = (df.min_salary + df.max_salary)/2

#comp name only
#state
#company age
#job desc