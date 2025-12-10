import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings ('ignore')

df = pd.read_csv('heart.csv')

print (df.head())

print (df.shape)

print (df.columns)

print (df.describe())

print (df.isnull().sum())

print(df.info())

plt.figure(figsize=(20,10))
sns.heatmap(df.corr(), annot=True, cmap='terrain')
print (plt.show())