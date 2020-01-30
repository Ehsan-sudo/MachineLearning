import pandas as pd

# series for a one-d array type data
"""data = [[1,2,3,4,5,6], ['ehsan'], [1,2,3]]
ser = pd.Series(data)
print(ser)"""
#changin the default index indecator value
"""data = [[1,2,3,4,5,6], ['ehsan'], [1,2,3]]
ser = pd.Series(data, index=['a','b','c'])
print(ser)"""
#accessing series object's element using index indecators
"""data = [[1,2,3,4,5,6], ['ehsan'], [1,2,3]]
ser = pd.Series(data, index=['a','b','c'])
print(ser['b':'c'])"""
#converting dectionary to series (keys are indeces, values are values)
"""data = {'a':1, 'b':2, 'c':3, 'd':4}
ser = pd.Series(data)
print(ser)"""


#data frame for 2-d tabular type of data (mutable size, different data type cell, labeled access)
"""data = [1,2,3,4,5,6]
df = pd.DataFrame(data)
print(df)"""
#converting 2-d list to dataframe
"""data = [[1,2,3], [4,5], [6,7,8]]
df = pd.DataFrame(data)
print(df)"""
# converting 2-d dictionary to datafram (both inner lists should be of same size)
"""data = {'a':[1,2,3], 'b':[4,5,6]}
df = pd.DataFrame(data)
print(df)"""
# converting 2-d dictionary of differnect data types to dataframe
"""data = {'fruit':['apple','banana','mango'], 'count':[13,44,12]}
df = pd.DataFrame(data)
print(df)"""
# converting series object to dataframe
"""ser2 = pd.Series([12,2], index=['a','b'])
df = pd.DataFrame(ser2)
print(df)"""
#changing dataframe column and row index names
"""data = [1,2]
df = pd.DataFrame(data)
df.rename(index={0:'a', 1:'b'}, inplace=True)
df.columns=['a']
print(df.columns)"""
# concatination of two or more dataframes (axis=1 means add column, 0 means add row in concatination)
"""data1 = [[1,2,3,4],[5,6,7,8]]
data2 = [['ehsan','popal'],['aryan', 'atal']]
df1 = pd.DataFrame(data1)
df1.columns=['a','b','c','d']
df2 = pd.DataFrame(data2)
df3 = pd.DataFrame()
df3 = pd.concat([df1,df2], axis=1) 
print(df3)"""
# reading csv file
"""file = pd.read_csv('./data.csv')
print(file.head())"""
# type cast of a csv file column (astype(int) means cast the type to int)
"""file = pd.read_csv('./data.csv')
file.Period = file.Period.astype(int)
print(file.Period)"""
# information of dataframe counting null values
"""file = pd.read_csv('./data.csv')
file.info()"""

"""file = pd.read_csv('./data.csv')
print(file.isnull().sum())"""

#calculating data frame's data despersion
"""file = pd.read_csv('./data.csv')
print(file.describe())"""



#filling missing values NaN
"""file = pd.read_csv('./data.csv')
file['Period'] = file['Period'].fillna(19.5)
print(file.head())"""
#filling missing values with mean
"""file = pd.read_csv('./data.csv')
file['Period'] = file['Period'].fillna(file['Period'].mean())
print(file.head())"""
#filling the missing values with average of above and belove number
"""file = pd.read_csv('./data.csv')
file['Period'] = file['Period'].fillna(file['Period'].interpolate())
print(file.head())"""
#deleting the whole record with contains missing values
"""file = pd.read_csv('./data.csv')
file = file.dropna()
print(file.head())"""



# droping columns
"""file = pd.read_csv('./data.csv')
file = file.drop(columns=['STATUS'])
print(file.head())"""
# sorting the data by column name
"""file = pd.read_csv('./data.csv')
file = file.sort_values(by='Data_value')
print(file.head(10))"""
# filtering the records (will return a true false dataframe), we can provide multiple conditions for filter
"""file = pd.read_csv('./data.csv')
file = file.head(10)
filter = file['Data_value']<645
print(file[filter])"""
