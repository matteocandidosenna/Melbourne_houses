# -*- coding: utf-8 -*-
"""RandomForestMelbourne.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14ALcMRO5zuHZPqWT-Dzz5YNJ60MTSyTD

<h1>Random Forest Regressor

In this code, Matheus will use the Random Forest Regressor algorithm at predicting prices of houses in Melbourne
"""

#Mounting drive
from google.colab import drive
drive.mount('/content/drive')

#Importing and Reading data
import pandas as pd
melbourne = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/data_csv/melb_data.csv')

#Analyzing columns
print(melbourne.dtypes)
melbourne_filt = melbourne.dropna(axis = 0)
print(list(melbourne))

#Atributes
y = melbourne_filt['Price']
atributos = ['Rooms', 'Bathroom', 'Landsize', 'BuildingArea', 'YearBuilt', 'Lattitude', 'Longtitude']
x = melbourne_filt[atributos]


#The RandomForest model is born!
from sklearn.ensemble import RandomForestRegressor
melbourne_model = RandomForestRegressor()
melbourne_model.fit(x, y)


#Creating Prediction
from sklearn.model_selection import train_test_split
#Split data into training and validation data, for both features and target
#The split is based on a random number generator. Supplying a numeric value to
#The random_state argument guarantees we get the same split every time we
#Run the Script
train_x, val_x, train_y, val_y = train_test_split(x, y, random_state = 0)
melbourne_model = RandomForestRegressor()
print('O algoritmo foi criado!')
melbourne_model.fit(train_x, train_y)

from sklearn.metrics import mean_absolute_error
#Prediction
pred = melbourne_model.predict(val_x)
print(mean_absolute_error(val_y, pred))

"""This model (RandomForestRegressor) did better to evaluate this situation than DecisionTreeRegressor(presnt in another repository of mine). This obtained MAE of 191958, while DecisionTreeRegressor, 262978."""
