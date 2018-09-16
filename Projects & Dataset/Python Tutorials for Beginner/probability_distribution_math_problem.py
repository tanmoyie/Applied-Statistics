# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 19:00:12 2018
@author: TANMOY DAS
"""

"""
Reference: Normal Distribution
Page 294, Chapter 5, FE - IE specific
A Gaussian random variable has a mean of 1830 and standard deviation of 460
Find the probability that the variable will be greater than 2750. 
"""
# greater than
import scipy.stats
mean_normal = 1830
standard_deviation_normal = 460
probability_norm_gt = scipy.stats.norm.sf(2750, mean_normal,standard_deviation_normal) # greater than

# In[ ]:
"""
Reference: Normal Distribution
Page 235, Chapter 7, Statistical techniques in Business by Lind 
The distribution of weekly incomes follows the normal probability distribution, 
with a mean of $1,000 and a standard deviation of $100. What is the probability of 
selecting a shift foreman in the glass industry whose income is:
1. Between $790 and $1,000?
2. Less than $790?
"""
import scipy.stats
# in between
mean_normal = 1000
standard_deviation_normal = 100
probability_norm_lt = scipy.stats.norm.cdf(1000, mean_normal,standard_deviation_normal)
probability_norm_gt = scipy.stats.norm.cdf(790, mean_normal,standard_deviation_normal) # greater than
probability_in_between = probability_norm_lt - probability_norm_gt

# less than
mean_normal = 1000
standard_deviation_normal = 100
probability_norm_lt = scipy.stats.norm.cdf(790, mean_normal,standard_deviation_normal)

# In[]

#To find the variate for which the probability is given, let's say the 
#value which needed to provide a 98% probability, you'd use the 
#PPF Percent Point Function
probability_given = scipy.stats.norm.ppf(.98,100,12)