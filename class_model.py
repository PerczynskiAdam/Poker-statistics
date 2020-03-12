# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 11:36:26 2019

@author: Adam
"""
import pandas as pd
import numpy as np

from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm

features = pd.read_csv(r'C:\Users\Adam\Desktop\Python\Master\features.csv')
targets = pd.read_csv(r'C:\Users\Adam\Desktop\Python\Master\targets.csv')
# Splitting data into training and testing
from sklearn.model_selection import train_test_split
# Split into 70% training and 30% testing set
X_train, X_test, y_train, y_test = train_test_split(features, targets, test_size = 0.3, random_state = 42)

print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)





#scaling variables 
scaler = MinMaxScaler(feature_range=(0, 1))



#fit and transform data
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test) 



# convert to array
y_train = np.array(y_train, dtype = np.float64).reshape((-1, ))
y_test = np.array(y_test, dtype = np.float64).reshape((-1, ))


clf = KNeighborsClassifier(n_jobs = 10)
clf.fit(X_train, y_train)

accuracy = clf.score(X_test, y_test)
print(accuracy)

clfsvm = svm.SVC()
clfsvm.fit(X_train, y_train)

svmacc = clf.score(X_test, y_test)
print(svmacc)

