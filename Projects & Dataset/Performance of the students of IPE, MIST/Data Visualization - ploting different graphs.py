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
import pandas as pd
dataframe_raw = pd.read_csv("Grading of the students in the exam (IPE101) raw.csv", header=0).drop_duplicates()
dataframe_raw.dtypes
# convert the dataframe into an array/matrix

# finding NaN values
print(dataframe_raw.isna)
df_droping_na = dataframe_raw.dropna()
#df_drop_txt = df_droping_na[~df_droping_na['CT-4 (Marks: 20)'].isin(['Ma'])]

input_data = df_droping_na.values
df_droping_na['CT-4 (Marks: 20)'].astype(str).astype(float)
type(df_droping_na)
df_droping_na.dtypes
df_matrix = df_droping_na.as_matrix
"""
EDA
"""
x = input_data[:,7]
y = input_data[:,10]
plt.scatter(x,y)
plt.show()

