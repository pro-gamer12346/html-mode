import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv("weather.csv")
print ("first five draws of data set")
print (df.head())
print ("\n data set in full")
print (df.info())
plt.figure(figsize=(8,5))
sns.histplot(df[df.columns[0]], kde=True,color='skyblue')
plt.title(f"distrubution of {df.columns[0]}")
plt.show()
sns.pairplot(df)
plt.suptitle("pairplot of data set",y = 1.02)
plt.show()