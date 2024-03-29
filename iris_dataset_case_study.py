# -*- coding: utf-8 -*-
"""Iris dataset case study.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1W9w0RHDcFInDLiHZQJ3WDOQqMQnvI51F

The **Iris dataset** was used in R.A. Fisher's classic 1936 paper, The Use of Multiple Measurements in Taxonomic Problems, and can also be found on the UCI Machine Learning Repository.

It includes three iris species with 150 samples each as well as some properties about each flower. One flower species is linearly separable from the other two, but the other two are not linearly separable from each other.

The columns in this dataset are:

* Id
* SepalLengthCm
* SepalWidthCm
* PetalLengthCm
* PetalWidthCm
* Species
"""

import sklearn
print(sklearn.__version__)

# import pandas, matplotlib.pyplot
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

from google.colab import drive
drive.mount('/content/drive')

# Load dataset
#names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/AIML-2022 LAB/DataSet-2022/Iris.csv',index_col=0)

#dispaly first 5 records from the dataset
dataset.head()

#dispaly size of the dataset
dataset.shape

#provide statistical detailed description of dataset
dataset.describe()

#dispaly information about dataset/summary of datset
dataset.info()

#Display different species in the dataset
dataset['Species'].unique()

#display species type wise count/ number of records
dataset['Species'].value_counts()

# Split-out validation dataset
arr = dataset.values
#print(type(arr))
X = arr[:,0:4]
y = arr[:,4]
#split 80% for training and 20% for testing 
X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.20, random_state=1, shuffle=True)

"""##Support Vector Machine

https://scikit-learn.org/stable/modules/classes.html#module-sklearn.svm

##Support Vector Classifier (SVC)

**kernel{‘linear’, ‘poly’, ‘rbf’, ‘sigmoid’, ‘precomputed’}, default=’rbf’**

Specifies the kernel type to be used in the algorithm. It must be one of ‘linear’, ‘poly’, ‘rbf’, ‘sigmoid’, ‘precomputed’ or a callable.

<font color='red'>If none is given, **‘rbf’** will be used.</font>

If a callable is given it is used to pre-compute the kernel matrix from data matrices; that matrix should be an array of shape (n_samples, n_samples).


**gamma{‘scale’, ‘auto’} or float, default=’scale’**

Kernel coefficient for ‘rbf’, ‘poly’ and ‘sigmoid’.

if gamma='scale' (default) is passed then it uses 1 / (n_features * X.var()) as value of gamma,

if ‘auto’, uses 1 / n_features.

**Accuracy-score:** 
* Accuracy score means how accurate our model is. 
* To find accuracy most popular ways are classification report and confusion matrix. 
* The matrix is a 2X2 matrix which tells about correct and wrong predictions as the form of positive and negative. 
* Accuracy is the addition of all the truly positive and truly negative predictions divided by the addition of all the numbers in the matrix.

The **comfusion matrix** has four columns as shown below:

![cf.png](data:image/png;base64,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)
 


**accuracy = (truely_positive+truely_negative)  /  (truely_positive+truely_negative+falsely_positive+falsely_negative)**

Here,

**truely_positive** = case was positive and the model predicted it positive

**truely_negative** = case was positive and the model predicted it negative

**falsely_negative** = case was negative but the model predicted it positive

**falsely_positive** = case was positive but the model predicted it negative
"""

# Make predictions on validation dataset
#default kernal is 'rbf'

model = SVC(gamma='auto')
model.fit(X_train, Y_train)
predictions = model.predict(X_test)

from sklearn.metrics import classification_report
print("For classification report:")
print(classification_report(Y_test , predictions))

from sklearn.metrics import confusion_matrix
print("For confusion matrix")
print(confusion_matrix(Y_test , predictions))

# Evaluate accuracy
from sklearn.metrics import accuracy_score
print("Accuracy score")
print(accuracy_score(Y_test, predictions))

"""===========================================================================

"""

import pickle

# Saving model to disk
pickle.dump(model, open('model.pkl','wb'))

# Loading model to compare the results
load_model = pickle.load(open('model.pkl','rb'))
print(load_model.predict([[5.6,	2.3,	3.9,	1.1]]))