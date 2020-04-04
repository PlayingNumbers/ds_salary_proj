# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 11:47:44 2020

@author: Ken
"""

import glassdoor_scraper as gs 
import pandas as pd 

path = "C:/Users/Ken/Documents/ds_salary_proj/chromedriver"

df = gs.get_jobs('data scientist',1000, False, path, 15)

df.to_csv('glassdoor_jobs.csv', index = False)