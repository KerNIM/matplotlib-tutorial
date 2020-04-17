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

df_can.drop(['AREA', 'REG', 'DEV', 'Type', 'Coverage'], axis=1, inplace=True)
df_can.rename(columns={'OdName': 'Country', 'AreaName': 'Continent', 'RegName': 'Region'}, inplace=True)
# let's view the first five elements and see how the dataframe was changed
print(df_can.head())

df_can.columns = list(map(str, df_can.columns))

# let's check the column labels types now
print(all(isinstance(column, str) for column in df_can.columns))
df_can.set_index('Country', inplace=True)

# let's view the first five elements and see how the dataframe was changed
print(df_can.head())

df_can['Total'] = df_can.sum(axis=1)

# let's view the first five elements and see how the dataframe was changed
print(df_can.head())

# finally, let's create a list of years from 1980 - 2013
# this will come in handy when we start plotting the data
years = list(map(str, range(1980, 2014)))
df_can.sort_values(['Total'], ascending=False, axis=0, inplace=True)

# get the top 5 entries
df_top5 = df_can.head()

# transpose the dataframe
df_top5 = df_top5[years].transpose()
df_top5.index = df_top5.index.map(int)  # let's change the index values of df_top5 to type integer for plotting
df_top5.plot(kind='area',
             stacked=False,
             figsize=(20, 10),  # pass a tuple (x, y) size
             )

plt.title('Immigration Trend of Top 5 Countries')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')

plt.savefig('top5_area_unstacked.png')

df_top5.plot(kind='area',
             stacked=True,
             figsize=(20, 10),  # pass a tuple (x, y) size
             )

plt.title('Immigration Trend of Top 5 Countries')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')

plt.savefig('top5_area_stacked.png')

df_top5.plot(kind='area',
             alpha=0.25,  # 0-1, default value a= 0.5
             stacked=False,
             figsize=(20, 10),
             )

plt.title('Immigration Trend of Top 5 Countries')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')

plt.savefig('top5_area_alpha.png')

df_least5_script = df_can.tail()
df_least5_script = df_least5_script[years].transpose()
df_least5_script.head()
df_least5_script.index = df_top5.index.map(int)  # let's change the index values of df_top5 to type integer for plotting
df_least5_script.plot(kind='area',
               alpha=0.45,
               figsize=(20, 10),  # pass a tuple (x, y) size
               )

plt.title('Immigration Trend of Least 5 Countries')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')

plt.savefig('bottom5_area_stacked_scripting.png')

df_least5_art = df_can.tail(5)
df_least5_art = df_least5_art[years].transpose()
df_least5_art.head()
df_least5_art.index = df_top5.index.map(int)  # let's change the index values of df_top5 to type integer for plotting
ax = df_least5_art.plot(kind='area', alpha=0.55, stacked=False, figsize=(20, 10))

ax.set_title('Immigration Trend of Least 5 Countries')
ax.set_ylabel('Number of Immigrants')
ax.set_xlabel('Years')

plt.savefig('bottom5_area_stacked_artist.png')
