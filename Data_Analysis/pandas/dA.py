#Data Manipulation and data analysis key task of Data Science.
#Clean Transform  & Extract insight data

import pandas as pd

# df = pd.read_csv('DataCard.csv')
# print(df)
# # first 5 rows
# df = df.head(5)
# print(df)
# # last 5 rows
# df = df.tail(5)
# print(df)
# df = df.dtypes
# print(df)

df = pd.read_excel('Book1.xlsx')
#print("Available columns:", df.columns)


df['Lines of Source code'] = pd.to_numeric(df['Lines of Source code'])
df['Lines of Executable code'] = pd.to_numeric(df['Lines of Executable code'])
print("Total Lines of Source code:", df['Lines of Source code'].sum())
print("Total Lines of Executable code:", df['Lines of Executable code'].sum())


#handling missing values
# df= df.isnull().any(axis =1)

# df =df.isnull().sum()
# print(df.columns)

# df['Depth of Inheritance'] = df['Depth of Inheritance'].fillna(df['Depth of Inheritance'].mean())
# print(df)


# df = df.rename['Lines of Source code', ""]
