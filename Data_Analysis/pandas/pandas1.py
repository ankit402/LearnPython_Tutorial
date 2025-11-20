import pandas as pd

data = [1,2,3,4,5]
index = ('a', 'b', 'c', 'd', 'e')
series = pd.Series(data, index=index)
print(series)

#dictionary
data2 = {'a':1 , 'b':2 , 'c':3 , 'd':4 , 'e':5 }
series = pd.Series(data2)
print(series)

#dataframe --> 2D Dimenstional
dataf= {
    'Name': ['Krish', 'Ankit', 'TEST'],
    'Age': [12,23,34],
    'Gender':['Male', 'Male' , 'Female']
}
df = pd.DataFrame(dataf)
print(df)
print(type(df))

data2 = [{'Name' : 'X', 'Age' : 23},
         {'Name' : 'Y', 'Age' : 34},
         {'Name' : 'Z', 'Age' : 45}]
df = pd.DataFrame(data2)
print(df)