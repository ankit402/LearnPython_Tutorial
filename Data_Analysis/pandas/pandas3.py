import pandas as pd
#Pandas is used to analyze data.
df = pd.read_csv('sales1_data.csv')
print(df.head(5))

#Pandas allows us to analyze big data and make conclusions based on statistical theories.

a= [1,2,3]
df = pd.Series(a, index=['a','b','c'])
print(df.head(5))
print(df['a'])

#Data sets in Pandas are usually multi-dimensional tables, called DataFrames.

datas = {
    'Calories' : [100, 200 , 300 ,400],
    'duration': [1, 2, 2.5, 4]
}

df = pd.DataFrame(datas)
print(df.head(5))
#A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.

#refer to the row index:
print(df.loc[0])

#use a list of indexes:
print(df.loc[[0,1]])

#Note: When using [], the result is a Pandas DataFrame.

#Named Indexes
data2 = {
    'Calories' : [100, 200 , 300 ,400],
        'duration': [1, 2, 2.5, 4]
}
pd.options.display.max_columns=2
df = pd.DataFrame(data2, index=["day1", "day2", "day3", "day4"])
print(df)

# #Locate Named Indexes
# df = df.loc["day2"]
# print(df)

