import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dataset=pd.read_csv('student_scores.csv')
type(dataset)
dataset.shape
dataset.ndim
features=dataset['Hours'].values
labels=dataset['Scores'].values

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features, labels)

