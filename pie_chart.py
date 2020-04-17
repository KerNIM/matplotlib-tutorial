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
df_can.columns = list(map(str, df_can.columns))
df_can.set_index('Country', inplace=True)
df_can['Total'] = df_can.sum(axis=1)
years = list(map(str, range(1980, 2014)))
df_can.sort_values(['Total'], ascending=False, axis=0, inplace=True)

# group countries by continents and apply sum() function
df_continents = df_can.groupby('Continent', axis=0).sum()

# note: the output of the groupby method is a `groupby' object.
# we can not use it further until we apply a function (eg .sum())
print(type(df_can.groupby('Continent', axis=0)))

df_continents.head()
# autopct create %, start angle represent starting point
df_continents['Total'].plot(kind='pie',
                            figsize=(15, 10),
                            autopct='%1.1f%%',  # add in percentages
                            startangle=90,  # start angle 90° (Africa)
                            shadow=True,  # add shadow
                            )

plt.title('Immigration to Canada by Continent [1980 - 2013]')
plt.axis('equal')  # Sets the pie chart to look like a circle.

plt.savefig('pie_continent.png')

colors_list = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'lightgreen', 'pink']
explode_list = [0.1, 0, 0, 0, 0.1, 0.1]  # ratio for each continent with which to offset each wedge.

df_continents['Total'].plot(kind='pie',
                            figsize=(15, 10),
                            autopct='%1.1f%%',
                            startangle=90,
                            shadow=True,
                            labels=None,  # turn off labels on pie chart
                            pctdistance=1.2,
                            colors=colors_list,  # add custom colors
                            explode=explode_list  # 'explode' lowest 3 continents
                            )

# scale the title up by 12% to match pctdistance
plt.title('Immigration to Canada by Continent [1980 - 2013]', y=100)
plt.axis('equal')

# add legend
plt.legend(labels=df_continents.index, loc='upper left')
plt.savefig('pie_exploded.png')

explode_list = [0.1, 0, 0, 0, 0.1, 0.2]  # ratio for each continent with which to offset each wedge.
df_continents['2013'].plot(kind='pie',
                           figsize=(15, 10),
                           autopct='%1.1f%%',
                           startangle=90,
                           shadow=True,
                           labels=None,  # turn off labels on pie chart
                           pctdistance=1.12,  # the ratio between the pie center and start of text label
                           explode=explode_list  # 'explode' lowest 3 continents
                           )
plt.title('Immigration to Canada by Continent in 2013', y=1.12)
plt.axis('equal')
# add legend
plt.legend(labels=df_continents.index, loc='upper left')
plt.savefig('pie_2013.png')
