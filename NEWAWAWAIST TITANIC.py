import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd .read_csv('iris.csv')
data.head(5)
data.isnull().sum()

data.describe()
labels = ['Id','SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm',]
print('Distribution of', Lebel)
sns.heatmap(data.corr())
