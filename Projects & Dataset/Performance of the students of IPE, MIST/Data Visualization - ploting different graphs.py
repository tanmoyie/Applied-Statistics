# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 22:19:27 2018

@author: TANMOY DAS
"""



import plotly.plotly as py
import plotly.graph_objs as go

# Create random data with numpy
import numpy as np
    


"""
importing excel files
""" 
import pandas
# load the EXCEL file & read the data 
dataframe = pandas.read_excel(open('Data of Performance of students in Operations Research.xlsx','rb'),
                       sheetname=0)
# no header
dataframe_no_header = pandas.read_excel(open('Data of Performance of students in Operations Research.xlsx','rb'),
                       sheetname=0, header=None)
# if the excel file contains multiple sheet
dataframe = pandas.read_excel(open('3D76FB00.xlsx','rb'),
                       sheetname=1)
    
# convert the dataframe into an array/matrix
input_data = dataframe.values






N = 1000
random_x = np.random.randn(N)
random_y = np.random.randn(N)

# Create a trace
trace = go.Scatter(
    x = random_x,
    y = random_y,
    mode = 'markers'
)

data = [trace]

# Plot and embed in ipython notebook!
py.iplot(data, filename='basic-scatter')

