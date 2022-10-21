import pandas as pd
import matplotlib.pyplot as plot
df=pd.read_csv(".\data.csv")
print(df.to_string())

#Show the basic statistical description about the data
print(df.describe())

#Check if the data has null values.
print(df.notnull())

# Replace the null values with the mean
c=df.fillna(value=df.mean(),inplace=False)
print(c)

#Select at least two columns and aggregate the data using: min, max, count, mean
b=df.groupby('Duration').aggregate({'Duration':['mean','min','max','count']})
d=df.groupby('Pulse').aggregate({'Pulse':['mean','min','max','count']})
print(b)
print(d)

#Filter the dataframe to select the rows with calories values between 500 and 1000.
f=c.query('Calories>=500 and Calories<=1000')
print(f)

#Filter the dataframe to select the rows with calories values > 500 and pulse < 100.
g=c.query('Calories>500 and Pulse<100')
print(g)

#. Create a new “df_modified” dataframe that contains all the columns from df except for “Maxpulse”
z='Maxpulse'
df_modified=c.loc[:,c.columns !=z]
print(df_modified)

#Delete the “Maxpulse” column from the main df dataframe
k=c.drop('Maxpulse',axis=1)
print(k)

#Convert the datatype of Calories column to int datatype.
c['Calories'] = c['Calories'].astype(int)
print(c['Calories'])
print(c.dtypes)

#Using pandas create a scatter plot for the two columns (Duration and Calories)
plotting=c.plot.scatter(x='Duration', y='Calories')
print(plotting)
plot.show()
