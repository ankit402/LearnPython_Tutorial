import pandas as pd
df =pd.read_csv("dataCard.csv")

# print(df.head(5)) # first 5 data

# print(df.tail(5)) #last 5 data

# new_df =df.dropna()

# print(df)

# x = df["Calories"].replace("", pd.NA)
# print(df.fillna(x))
#Replace Using Mean, Median, or Mode
x = df["Calories"].mode()[0]

y = df["Calories"].median()

z = df["Calories"].mean()

df.fillna({"Calories": y} , inplace=True)

print(df.to_string())

