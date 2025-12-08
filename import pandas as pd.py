import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

HouseDF=pd.read_csv('D:\pythorn/USA_Housing.csv')

print (HouseDF.head())

print (HouseDF.info())

print (HouseDF.describe())

print (HouseDF.columns)

print (sns.pairplot(HouseDF))

print (plt.show())

print (sns.heatmap(HouseDF.corr(),annot=True))

print (plt.show())