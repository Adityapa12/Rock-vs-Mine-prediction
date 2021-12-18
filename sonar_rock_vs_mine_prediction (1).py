# -*- coding: utf-8 -*-
"""SONAR  Rock vs Mine prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YysW0do6WBC1LlvBXkRdJLNTLLKJ58OH

Impoting the dependencies
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

"""Data collection and Data pre processing"""

# loading the dataset to pandas dataset
# (header = none cause there is no column name, we have to mention in pandas dataframe)
sonar_data  = pd.read_csv('/content/sonar data.csv',header = None)

sonar_data.head()

#  number of rows and column
sonar_data.shape

sonar_data.describe()  # describe()----> statistical measures of data

sonar_data[60].value_counts()

"""M represents Mine

R represents Rock
"""

sonar_data.groupby(60).mean()

#  seprating data and the labels
X = sonar_data.drop(columns= 60, axis= 1)
Y = sonar_data[60]

print(X)
print(Y)

"""Training and test data"""

X_train,X_test,Y_train,Y_test= train_test_split(X,Y,test_size=0.1 ,stratify=Y, random_state=1)

print(X.shape,X_train.shape,X_test.shape)

print(X_train)
print(Y_train)

"""MODEL TRAINING ---> LOGISTIC REGRESSION"""

model = LogisticRegression()

model.fit(X_train, Y_train)

"""Model Evaluation"""

# accuracy on training data
X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction,Y_train)

print("Accuracy on training data:",training_data_accuracy)

# accuracy on test data
X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction,Y_test)

print("Accuracy on test data:",test_data_accuracy)

"""Making a predictive system"""

input_data =(0.0310,0.0221,0.0433,0.0191,0.0964,0.1827,0.1106,0.1702,0.2804,0.4432,0.5222,0.5611,0.5379,0.4048,0.2245,0.1784,0.2297,0.2720,0.5209,0.6898,0.8202,0.8780,0.7600,0.7616,0.7152,0.7288,0.8686,0.9509,0.8348,0.5730,0.4363,0.4289,0.4240,0.3156,0.1287,0.1477,0.2062,0.2400,0.5173,0.5168,0.1491,0.2407,0.3415,0.4494,0.4624,0.2001,0.0775,0.1232,0.0783,0.0089,0.0249,0.0204,0.0059,0.0053,0.0079,0.0037,0.0015,0.0056,0.0067,0.0054)
# changing the data to numpy array
input_data_as_numpy_array = np.asarray(input_data)

#  reshape the numpy array for one instnce
input_data_reshaped  = input_data_as_numpy_array.reshape(1,-1)
prediction = model.predict(input_data_reshaped)
print(prediction)

if (prediction[0]=='R'):
  print('The object is rock')
else:
  print('the object is mine')

