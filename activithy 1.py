import pandas as pd 
import matplotlib.pyplot as plt 

countries_df = pd.read_csv('countries.csv')
countries = countries_df
print (countries.head(3))

c_52 = countries.loc[countries['year'] == 1952]
c_52.head()

names = ['China', 'India', 'United states', 'Indonesia', 'Brazil', 'Pakistan', 'Bangladesh', ' Nigeria', 'Mexico', 'Philippines']
pop_grow = (o_merge('population_growth') / 10**6)

plt.figure(figsize=(15,9))
plt.bar(names,pop_grow,width=0.6)
plt.xlabel('Country')
plt,ylabel('Population Growth ')