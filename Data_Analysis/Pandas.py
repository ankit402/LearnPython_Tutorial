#Series for 1-D array
#Dataframe for multidimensional Array

#widely use for data analysis and data cleaning, powerful data manipulation library in python

import pandas as pd

# arr= [1,2,3,4,5]  #1-D array
# series = pd.Series(arr)
# print("Series\n", series)
#
# #create series using dictionary
#
# dic_data = { 'Name' : 'ankit', 'age' : 32 , 'mobile' : '0564240153'}
# series2= pd.Series(dic_data)
# print("Series\n", series2)
#
# #data and index
# data= [10,20,30,40,50]
# index=['a','b', 'c','d','e']
# series= pd.Series(data, index=index)
# print("Series\n", series)
#
# #dataframe is multidimensional array like table in database with labels column name
#
# #create dataframe using dictionary
#
# data= {
#     'Name': ['ankit', 'suraj', 'suresh', 'krish'],
#     'Age' : [30, 32, 34, 45],
#     'City':['Shj' , 'Ban', 'Ind', 'Sin']
# }
#
# df = pd.DataFrame(data)
# print("DataFrame\n", df)


#Read CSV file for data analysis

df = pd.read_csv('myresult.csv')
#print(df.head(10))
#condition
#filtered_df = df[df['status'] == 'Failed']
#filtered_df= df[df['user'].str.contains('javed') or [df['status'] == 'Failed']]
filtered_df = df[(df['user'].str.contains('javed', case=False, na=False)) & (df['status'] == 'Success')]
print(filtered_df)

#Accessing data from dataframe
#print(df['user'].head())

#print(df.iloc[0])




