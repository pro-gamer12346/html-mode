import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('titanic.csv')

data.head(5)

data.isnull().sum()

age_q1 = np.quantile(data['Age'], 0.25)
age_q2 = np.quantile(data['Age'], 0.50)
age_q3 = np.quantile(data['Age'], 0.75)

IQR_age = age_q3 - age_q1 
print("Interquartile Range :", IQR_age)

plt.hist(data['Age'])
plt.ylabel("Count of Passengers")
plt.xlabel("Age")

fare_q1 = np.quantile(data['Fare'], 0.25)
fare_q2 = np.quantile(data['Fare'], 0.50)
fare_q3 = np.quantile(data['Fare'], 0.75)

IQR_fare = fare_q3 - fare_q1
print("Interquartile Range :", IQR_fare)

bins =np.arange(0,250,20)
plt.hist(data['Fare'], bins=np.arange(1,250, 20))
plt.ylabel("Count of Passengers")
plt.xlabel("Fare")
plt.xticks(bins)