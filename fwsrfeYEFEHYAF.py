import pandas as pd
import numpy as np

exam_date = {'name': ['anastasia','dima',' 𓀛 𓀜 𓀝 𓀞 𓀟', 'james', 'josh', 'emily', 'micheal', 'matthew', 'scott', 'laura', 'kevin', 'jonas the thrid, duke of wellington' ],
             'score':[12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
             'attempts':[1, 3, 2, 3, 2, 3, 1, 1, 2, 1,]
             'qualify':['yes', 'no', 'yes', 'yes','no', 'no','yes', 'no','no', 'no','yes', 'yes',]

             }
lables = ['a','b','c','d','e','f','g','h','i','j']

df = pd.DataFrame(exam_data , index=lables)
print("summary of the basic information about this dataframe and its data:")
print(df.info())