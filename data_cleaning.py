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
#Remove the rating float present in the company name column
df['company'] = df.apply(lambda x: x['Company Name'] if x['Rating'] < 0 else x['Company Name'][:-3], axis = 1)

#state in which company is located
df['company_state'] = df['Location'].apply(lambda x: x.split(',')[1])
df.company_state.value_counts()

#Check if the job is in the HQ
df['same_state'] = df.apply(lambda x: 1 if x.Location == x.Headquarters else 0, axis = 1)

#company age
df['age'] = df.Founded.apply(lambda x: 2020-x if x != -1 else -1)

#job desc
#Python
df['python'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
df.python.value_counts()

#r_studio
df['r'] = df['Job Description'].apply(lambda x: 1 if 'r studio' in x.lower() or 'r-studio' in x.lower() else 0)
df.r.value_counts()

#spark 
df['spark'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
df.spark.value_counts()

#aws
df['aws'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
df.aws.value_counts()

#excel
df['excel'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)
df.excel.value_counts()

#Drop useless columns
df.columns
df_out = df.drop(['Unnamed: 0'], axis=1)

df_out.to_csv('salary_data_cleaned.csv', index=False)