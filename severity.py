# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
# Importing the dataset
dataset = pd.read_csv('Data_Final.csv')
X = dataset.iloc[:,:].values
X = np.delete(X,2,axis=1)
X = np.delete(X,1,axis=1)
X = np.delete(X,0,axis=1)
names = (dataset.columns.values)
names = names[3:]

from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values='NaN',strategy="most_frequent",axis=0)
imputer = imputer.fit(X[:,:])
X[:,:] =  imputer.transform(X[:,:])
data_new = pd.DataFrame(data=X,columns=names)

imputer = Imputer(missing_values=-1,strategy="most_frequent",axis=0)
imputer = imputer.fit(X[:,:])
X[:,:] =  imputer.transform(X[:,:])
data_new = pd.DataFrame(data=X,columns=names)



plt.figure(figsize=(30,8))

sns.countplot(x='LIGHT_CONDITION', hue='SEVERITY',data=data_new)
sns.countplot(x='SEVERITY',hue='ALCOHOLTIME',data=data_new)
sns.countplot(x='LIGHT_CONDITION',hue='ALCOHOLTIME',data=data_new)
sns.countplot(x='SEVERITY',hue='SPEED_ZONE',data=data_new)
sns.countplot(x='POLICE_ATTEND',hue='SPEED_ZONE',data=data_new)
sns.countplot(x='FEMALES',hue='SEVERITY',data=data_new)