# -*- coding: utf-8 -*-
"""
Created on Tue May  1 17:40:46 2018

@author: Prashant
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
dataset = pd.read_csv("Accidents0515.csv")


time1=dataset['Time']
time=dataset['Time'].values

t=[]
j=0
for i in time:
    t.append((i))
    j+=1
x = []
for i in range(len(t)):
    s = t[i]
    x.append(s[0:2])
import math
j=0
for i in x:
    x[j] = math.ceil(int(i)/3)
    j+=1

accident_time = {}
for i in x:
    if i in accident_time:
        accident_time[i]+=1
    else:
        accident_time[i]=1
accident_time[1]+=accident_time[0]
del(accident_time[0])

val=[]
for i in sorted(accident_time):
    val.append(accident_time[i])

plt.figure(figsize=(10,5))
label = ['12am-3am','3am-6am','6am-9am','9am-12pm','12pm-3pm','3pm-6pm','6pm-9pm','9pm-12am']
plt.bar(list(accident_time.keys()),accident_time.values())
plt.xticks([1,2,3,4,5,6,7,8],label)
plt.xlabel('Time (3-hour period)')
plt.ylabel('Total deaths')


day_of_week = dataset['Day_of_Week'].values
day_freq = {}
for i in day_of_week:
    if(math.isnan(i)):
        pass
    elif int(i) not in day_freq:
        day_freq[int(i)]=1
    else:
        day_freq[int(i)]+=1

labels = 'Monday', 'Tuesday', 'Wednesday', 'Thursday','Friday','Saturday','Sunday'
sizes = [day_freq[1],day_freq[2],day_freq[3],day_freq[4],day_freq[5],day_freq[6],day_freq[7]]
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()


#for i in X:

