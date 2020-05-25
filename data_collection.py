# -*- coding: utf-8 -*-
"""
Created on Mon May 25 00:52:34 2020

@author: Dell 1
"""

import glassdoor_scrapper as gs 
import pandas as pd 

path = "E:/Project/New folder/ds_salary_project/chromedriver.exe"

df = gs.get_jobs('data scientist',1000, False, path, 15)

df.to_csv('glassdoor_jobs.csv', index = False)

#    url = 'https://www.glassdoor.com/Job/jobs.htm?sc.keyword="' + keyword + '"&locT=C&locId=2940587&locKeyword=Bengaluru&jobType=all&fromAge=-1&minSalary=0&includeNoSalaryJobs=true&radius=100&cityId=-1&minRating=0.0&industryId=-1&sgocId=-1&seniorityType=all&companyId=-1&employerSizes=0&applicationType=0&remoteWorkType=0'
