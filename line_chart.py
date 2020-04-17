import numpy as np  # useful for many scientific computing in Python
import pandas as pd  # primary data structure library
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.style.use(['ggplot'])

df_can = pd.read_excel(
    'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DV0101EN/labs/Data_Files/Canada.xlsx',
    sheet_name='Canada by Citizenship',
    skiprows=range(20),
    skipfooter=2)

# print(df_can.head(n=5))
# print(df_can.tail(n=5))
# print(df_can.info())
# print(df_can.index.values)

# size of dataframe (rows, columns)
# print(df_can.shape)

# in pandas axis=0 represents rows (default) and axis=1 represents columns.
df_can.drop(['AREA', 'REG', 'DEV', 'Type', 'Coverage'], axis=1, inplace=True)
# print(df_can.head(2))

df_can.rename(columns={'OdName': 'Country', 'AreaName': 'Continent', 'RegName': 'Region'}, inplace=True)
# print(df_can.columns)

df_can['Total'] = df_can.sum(axis=1)
# print(df_can.isnull().sum())

# describe データ、標準偏差など
# print(df_can.describe())

df_can.set_index('Country', inplace=True)
# tip: The opposite of set is reset. So to reset the index, we can use df_can.reset_index()

# 1. the full row data (all columns)
# print(df_can.loc['Japan'])

# alternate methods
# print(df_can.iloc[87])
# print(df_can[df_can.index == 'Japan'].T.squeeze())

# 2. for year 2013
# print(df_can.loc['Japan', 2013])

# alternate method
# print(df_can.iloc[87, 36])
# year 2013 is the last column, with a positional index of 36

# 3. for years 1980 to 1985
# print(df_can.loc['Japan', [1980, 1981, 1982, 1983, 1984, 1984]])
# print(df_can.iloc[87, [3, 4, 5, 6, 7, 8]])

df_can.columns = list(map(str, df_can.columns))
# [print (type(x)) for x in df_can.columns.values] #<-- uncomment to check type of column headers

years = list(map(str, range(1980, 2014)))

# 1. create the condition boolean series
condition = df_can['Continent'] == 'Asia'

# we can pass mutliple criteria in the same line.
# let's filter for AreaNAme = Asia and RegName = Southern Asia

print(df_can[(df_can['Continent'] == 'Asia') & (df_can['Region'] == 'Southern Asia')])

# note: When using 'and' and 'or' operators, pandas requires we use '&' and '|' instead of 'and' and 'or'
# don't forget to enclose the two conditions in parentheses
print('data dimensions:', df_can.shape)
print(df_can.columns)
df_can.head(2)

'''
haiti immigration
'''
haiti = df_can.loc['Haiti', years]  # passing in years 1980 - 2013 to exclude the 'total' column
haiti.head()
haiti.index = haiti.index.map(int)  # let's change the index values of Haiti to type integer for plotting
haiti.plot(kind='line')

plt.title('Immigration from Haiti')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')

# annotate the 2010 Earthquake.
# syntax: plt.text(x, y, label)
plt.text(2000, 6000, '2010 Earthquake')  # see note below

plt.savefig('Haiti.png')

df_CI = df_can.loc[['China', 'India'], years]
df_CI.head()
df_CI = df_CI.transpose()
df_CI.index = df_CI.index.map(int)  # let's change the index values of df_CI to type integer for plotting

df_CI.plot(kind='line')
plt.title('Immigration from China and India')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')

plt.savefig('CI.png')

df_can.sort_values(by='Total', ascending=False, axis=0, inplace=True)
df_top5 = df_can.head(5)
df_top5 = df_top5[years].transpose()
df_top5.index = df_top5.index.map(int)  # let's change the index values of df_top5 to type integer for plotting
df_top5.plot(kind='line', figsize=(14, 8))  # pass a tuple (x, y) size

plt.title('Immigration Trend of Top 5 Countries')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')

plt.savefig('Top5.png')
