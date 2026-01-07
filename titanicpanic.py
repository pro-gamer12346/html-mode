import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('titanic.csv')
data.head(5)

sns.countplot(data['Gender'], hue=data['Survived'])
sns.countplot(data['Pclass'], hue=data['Survived'])
sns.displot(data['Age'], kde=False, bins=40)
sns.countplot(data['Gender'])
sns.countplot(x='Survived', hue='Sibsp', data=data, palette="mako")
sns.countplot(x='Survived', hue='Parch', data=data, palette="mako")
sns.distplot(data['Fare'])
plt.show()
sns.boxplot(x='Pclass',y='Age',data=data,palette='winter')
sns.heatmap(data.corr())