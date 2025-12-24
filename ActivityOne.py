import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('titanic.csv')

print (data.head(5))

print(data.dtypes)

nominal_cat = ['Name','Ticket','Cabin']

ordinal_cat = ['Embarked','Gender']

print (data['Gender'].value_counts())

gender_categories = ['Female','Male']

data['Gender'] = pd.Catergorial(data['Gender'], gender_categories, ordered=True)

median_index = np.nanmedian(data['Gender'].cat.codes)
median_gender = gender_categories[int(median_index)]
print(median_gender)

print (data['Embarked'].value_counts())

embarked_categories = ['S','C','Q']

data['Embarked'] = pd.Categorical(data['Embarked'], embarked_categories,ordered = True)

median_index = np.median(data['Embarked'].cat.codes)
median_embarked = embarked_categories[int(median_index)]
print(median_embarked)