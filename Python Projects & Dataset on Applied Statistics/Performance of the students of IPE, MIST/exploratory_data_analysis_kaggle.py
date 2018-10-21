# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 23:11:11 2018

@author: TANMOY Das
"""
# In[2]:
# https://github.com/tanmoyie/Applied-Statistics

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory
import os
print(os.listdir("../input"))
# ploting related libraries
import matplotlib.pyplot as plt
import plotly.plotly as plty
import plotly.graph_objs as go
#modeling
from sklearn import datasets, linear_model
# load the EXCEL file & read the data 
dataframe1 = pd.read_csv("../input/Grading of the students in the exam (OR).csv")
print(dataframe1)
print(dataframe1.dtypes)
input_data = dataframe1.values
input_data_asMatrix = dataframe1.as_matrix()
# Examine the properties of the dataset
# print the statistics
print(dataframe1['Final Mark'].describe())

# In[2]:
# Replacing NaN values
input_adding_roll = dataframe1.iloc[3,10]
print(input_adding_roll)
dataframe1.iloc[3,10] = 15
print(dataframe1.values)


# In[2]:
# Develop a Scatter plot of Attendance vs the mark of final exam
print("-------------Draw a Scatter Plot: Attendance vs Total Mark -----------")
x = input_data[:,7] # independent variable
y = input_data[:,12] # dependent variable
plt.scatter(x,y) # Scatter plot for Attendance vs Final exam mark
plt.show() 
# Develop a Scatter plot of class test vs the mark of final exam
print("-------------Draw a Scatter Plot: Class Test vs Total Mark -----------")
#y_final_exam_sum = input_data['']+input_data[:,11]
x_ct = input_data[:,6] # independent variable
y_final_exam = input_data[:,12] # dependent variable
plt.scatter(x_ct, y_final_exam) # Scatter plot for Attendance vs Final exam mark
plt.show() 
# basic plot
dataframe1.boxplot()
# https://pandas.pydata.org/pandas-docs/version/0.23/generated/pandas.DataFrame.hist.html
dataframe1.hist()
