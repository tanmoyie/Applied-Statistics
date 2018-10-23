# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 22:00:35 2018
@author: Tanmoy Das
"""
# This code has been run on Sypder IDE of Anaconda distribution (Python 3.6)
import pandas
# import statsmodels.api as sm # https://www.statsmodels.org/stable/index.html
from statsmodels.regression.linear_model import OLS
import matplotlib.pyplot as plt
# Excel file with no header
dataframe_no_header = pandas.read_excel(open('CommViolPredUnnormalizedData.xlsx','rb'),
                       sheetname=0, header=None) # Dataset is extracted from https://archive.ics.uci.edu/ml/datasets/Communities+and+Crime+Unnormalized

# In[]:
x = dataframe_no_header[5].values # accessing 6th column
y = dataframe_no_header[147-18].values # accessing 18th column from the last
# draw a Scatter Plot 
plt.scatter(x,y) 
plt.show()
 
# Modeling
simple_linear_regression_model = OLS(y,x)
simple_linear_regression_model_fit = simple_linear_regression_model.fit()
# Estimating Model Coefficient
print(simple_linear_regression_model_fit.params)






# In[ ]: 
x_multi = dataframe_no_header[[5,6,7,8]].values
y = dataframe_no_header[147-18].values
multiple_linear_regression_model = OLS(y,x_multi)
multiple_linear_regression_model_fit = multiple_linear_regression_model.fit()
# Estimating Model Coefficient
print(multiple_linear_regression_model_fit.params)