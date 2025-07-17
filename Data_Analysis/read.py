#Test your Pandas skills with exercises from all categories:

#introduction

import pandas as pd

df = pd.read_csv('data.csv')
print(df)

# newdf = df['Value'].replace("NaN", "0")
# print(newdf)

filter = df['Value'] > 30.0
print(filter)