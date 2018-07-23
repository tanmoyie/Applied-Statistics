# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 22:19:27 2018

@author: TANMOY DAS
"""
#import plotly.plotly as plty
#import plotly.graph_objs as go
import numpy as np
import matplotlib.pyplot as plt

"""
importing CSV files
""" 
import pandas
dataframe_csv = pandas.read_csv("Grading of the students in the exam (OR).csv")
dataframe_csv.dtypes
# convert the dataframe into an array/matrix
input_data = dataframe_csv.values


"""
EDA
"""
x = input_data[:,7]
y = input_data[:,12]
plt.scatter(x,y)
plt.show()
