import pandas as pd

df = pd.read_json('data.json')

# pd.options.display.max_rows = 20
# print(df)

df = pd.DataFrame(df)

print(df)

#Viewing the Data
df =df.head(5)
print(df)

#tail
df =df.tail(169)
print(df)

#info

#The info() method also tells us how many Non-Null values there are present in each column, and in our data set it seems like there are 164 of 169 Non-Null values in the "Calories" column.
print(df.info())


'''Data Cleaning
Data cleaning means fixing bad data in your data set.

Bad data could be:

Empty cells
Data in wrong format
Wrong data
Duplicates
In this tutorial you will learn how to deal with all of them.'''

#Remove Rows
df =pd.read_json('data.json')
ndf = df.dropna()
# print(ndf)

data = {
    "Car" : ["Model1", "Model2", "Model3", "Model4", "Model5"],
    "Year":[2012, 2013,2014,2015,2016],
    "Make":["Chev", "Nissan", "Toyota", "K", "K"]
}

df =pd.DataFrame(data)
df['Make'] = df['Make'].replace("K", pd.NA)
print(df)