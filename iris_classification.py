# -*- coding: utf-8 -*-
"""Iris_Classification.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Y1v6H7hKgmWTzwOaQGCePP2yD1YWTOLh

#LODING THE LIBRARIES
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import seaborn as sns

data=pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", names=["Sepal Length","Sepal Width","Petal Length","Petal Width","Class"])

data

data.shape

data.isnull().sum()

data['Class'].unique()

data['Class']=data['Class'].map({'Iris-setosa':0,'Iris-versicolor':1,'Iris-virginica':2})

data

"""# DATA VISUVALIZATION"""

sns.pairplot(data)

X=data.drop('Class',axis=1)

X

y=data['Class']

y

"""# TRAINING THE MODEL"""

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)

llr=LogisticRegression()

llr.fit(X_train,y_train)

"""# FINDING ACCURACIES """

from sklearn.metrics import accuracy_score

Prediction=llr.predict(X_test)

accuracy_score(y_test,Prediction)

