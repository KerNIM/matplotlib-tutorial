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
# finally, let's create a list of years from 1980 - 2013
# this will come in handy when we start plotting the data
years = list(map(str, range(1980, 2014)))
df_can.sort_values(['Total'], ascending=False, axis=0, inplace=True)

# Iceland
df_iceland = df_can.loc['Iceland', years]
# step 2: plot data
df_iceland.plot(kind='bar', figsize=(10, 6), rot=90)

plt.xlabel('Year')  # add to x-label to the plot
plt.ylabel('Number of immigrants')  # add y-label to the plot
plt.title('Icelandic immigrants to Canada from 1980 to 2013')  # add title to the plot
# Annotate arrow
plt.annotate('',  # s: str. Will leave it blank for no text
             xy=(32, 70),  # place head of the arrow at point (year 2012 , pop 70)
             xytext=(28, 20),  # place base of the arrow at point (year 2008 , pop 20)
             xycoords='data',  # will use the coordinate system of the object being annotated
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3', color='blue', lw=2)
             )

plt.annotate('2008 - 2011 Financial Crisis',  # text to display
             xy=(28, 30),  # start the text at at point (year 2008 , pop 30)
             rotation=72.5,  # based on trial and error to match the arrow
             va='bottom',  # want the text to be vertically 'bottom' aligned
             ha='left',  # want the text to be horizontally 'left' aligned.
             )
plt.savefig('iceland_bar_chart.png')

# Top 15 countries
df_can.sort_values(by='Total', ascending=True, inplace=True)
df_top15 = df_can['Total'].tail(15)
df_top15.plot(kind='bar', figsize=(20, 20), color='steelblue')

plt.xlabel('Year')  # add to x-label to the plot
plt.title('Top15 Countries immigrants to Canada from 1980 to 2013')  # add title to the plot
for index, value in enumerate(df_top15):
    label = format(int(value), ',')  # format int with commas

    # place text at the end of bar (subtracting 47000 from x, and 0.1 from y to make it fit within the bar)
    plt.annotate(label, xy=(value - 47000, index - 0.10), color='white')

plt.savefig('top15_bar_chart.png')
