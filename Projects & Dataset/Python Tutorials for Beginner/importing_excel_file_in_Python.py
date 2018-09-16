# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 00:37:43 2018

@author: TANMOY
"""

"""
importing excel files
""" 
import pandas
# load the EXCEL file & read the data 
dataframe1 = pandas.read_excel(open('Data of Performance of students in Operations Research.xlsx','rb'),
                       sheetname=0)
# no header
dataframe_no_header = pandas.read_excel(open('Data of Performance of students in Operations Research.xlsx','rb'),
                       sheetname=0, header=None)
# if the excel file contains multiple sheet
dataframe_2nd_sheet = pandas.read_excel(open('3D76FB00.xlsx','rb'),
                       sheetname=1)
    
# convert the dataframe into an array/matrix
input_data = dataframe1.values

