# -*- coding: utf-8 -*-
"""
Created on Tue May  1 10:59:30 2018

@author: Prashant
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = pd.read_csv('Traffic accidents by time of occurrence 2001-2014.csv')
X = data.iloc[18,:].values

accident_time = {1:X[3],2:X[4],3:X[5],4:X[6],5:X[7],6:X[8],7:X[9],8:X[10]}
times = list(accident_time.keys())
label = ['0-3Hrs','3-6Hrs','6-9Hrs','9-12Hrs','12-15Hrs','15-18Hrs','18-21Hrs','21-24Hrs']
#no_of_accidents1 = [X[3],X[4],X[5],X[6],X[7],X[8],X[9],X[10]]
#no_of_accidents = list(accident_time.values())
plt.figure(figsize=(30,8))
#plt.bar(times,no_of_accidents)


val=[]
for i in sorted(accident_time):
    val.append(accident_time[i])

plt.figure(figsize=(10,5))

plt.bar(list(accident_time.keys()),accident_time.values())
plt.xticks([1,2,3,4,5,6,7,8],label)
plt.xlabel('Time (3-hour period)')
plt.ylabel('Total deaths')