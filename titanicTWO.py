import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns

data = pd.read_csv('titanic.csv')

data.head()

mean_age = np.mean(data['Age'])
print("mean age of passengers is - ",mean_age)

mean_fare = np.mean(data['fare']
                    )
print ("mean fare is - ",mean_fare)