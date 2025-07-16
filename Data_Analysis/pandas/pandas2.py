import pandas as pd

try:
    df = pd.read_csv('sales1_data.csv')
    print(df.head(5))
except Exception as e:
    print(e)

#Accessing from dataframe

#print(df['Product'])

# print(df.loc[0])
#
# print(df.iloc[0])
#print(df['Sales']> 600)

#Accessing specific element
print(df.head(5))
print(df.at[1,'Product'])

print(df.iat[1,1])

# Adding new column
df['Salary'] = df['Sales'] * 100
#print(df)

df.drop('Salary', axis=1, inplace=True)
print(df)

#describing the values 
print(df.describe())