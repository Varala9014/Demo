# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 16:36:28 2023

@author: Yashwanth Reddy
"""

import pandas as pd
import matplotlib.pyplot as plt
#%matplotlib inline
# read file into dataframe and print
df_gdp = pd.read_excel("Popular Indicators.xlsx")
print(df_gdp)
print()
# line plots
plt.figure()
# plot the four countries with labels
plt.plot(df_gdp["YEAR"], df_gdp["Algeria"], label="Algeria")
plt.plot(df_gdp["YEAR"], df_gdp["Indonesia"], label="Indonesia")
plt.plot(df_gdp["YEAR"], df_gdp["Ireland"], label="Ireland")
#plt.plot(df_gdp["Year"], df_gdp["United States"], label="USA")
# set labels and show the legend
plt.xlabel("YEAR")
plt.ylabel("GDP")
plt.legend()
plt.show()