#Prior to starting ensure that the pandas library has been downloaded

from tabulate import tabulate
import pandas as pd

########################################################################################################################
# Cleaning the Data for University Rankings Dataset
########################################################################################################################
df_csv = pd.read_csv(
    'C:/Users/rinke/OneDrive/Desktop/Uni/2022/Sem 1/Busan 300/A5 - Project/Dataset/timesData.csv')  # reads the csv file and puts it into a table format, change path based on where file is

# drop any record if teaching, international or citation is empty
df_csv = df_csv.drop(df_csv[(df_csv.teaching == "-")].index)  # drops row if the record has a - as a value for teaching
df_csv = df_csv.drop(df_csv[(df_csv.research == "-")].index)
df_csv = df_csv.drop(df_csv[(df_csv.citations == "-")].index)
df_csv = df_csv.dropna(
    subset=['teaching', 'research', 'citations'])  # drops any records in which teaching, research or citations is null

df_csv.loc[
    df_csv.citations == "-", 'international'] = 0  # if the record has a - for its citation value then change to a 0
df_csv.loc[df_csv.income == "-", 'income'] = 0  # if the record has a - for its income value then change to a 0
df_csv.loc[pd.isnull(
    df_csv.citations), 'international'] = 0  # if the record has a nan for its citation value then change to a 0
df_csv.loc[pd.isnull(df_csv.income), 'income'] = 0  # if the record has a nan for its income value then change to a 0

# for loop used to find all empty total scores and replace them with an estimated total score
for x in range(len(df_csv['total_score'].values)):
    # the following code will calculate the total score if the total score is empty and the calculation is done based on the University Rankings performance weights
    # it rounds the total to 1dp and i used the df_csv.info to check for the object data type and converted it to float if needed
    if df_csv['total_score'].values[x] == '-' or pd.isnull(df_csv['total_score'].values[x]):
        df_csv['total_score'].values[x] = (round(
            (df_csv['teaching'].values[x] * 0.3) +
            (df_csv['research'].values[x] * 0.3) +
            (df_csv['citations'].values[x] * 0.3) +
            (float(df_csv['international'].values[x]) * 0.075) +
            (float(df_csv['income'].values[x]) * 0.025), 1
        ))

# print(df_csv.info())
# print(tabulate(df_csv, headers='keys', tablefmt='psql'))  # prints the csv data in the format of a table

########################################################################################################################
# Cleaning the Data for the world GDP dataset
########################################################################################################################
df_json = pd.read_json(
    'C:/Users/rinke/OneDrive/Desktop/Uni/2022/Sem 1/Busan 300/A5 - Project/Dataset/GDPfinal.json')  # reads json file and converts into a panda dataframe

del df_json['Anthem']  # drops the anthem property
del df_json['Government']  # drops the government property
del df_json['2020 Population Rank']
del df_json['2020 World Percentage']
del df_json['2020 Growth Rate']
del df_json['Capital City']
del df_json['Land Area']
del df_json['Area']

df_json = df_json.drop(
    df_json.index[df_json['GDP Per Capita'] == "-"])  # removes any gdp per capita record which is empty
df_json = df_json.dropna(subset=['GDP Per Capita'])

# print(df_json.info())
# print(tabulate(df_json, headers='keys', tablefmt='psql'))  #prints the json data in the format of a table
########################################################################################################################
# Merging#
########################################################################################################################
# check if all the countries in University Rankings are present in the gdp dataset
"""
csv_countryList = []  # list for all of the countries in the University Ranking database
for i in df_csv['country'].unique():
    csv_countryList.append(i)
csv_countryList.sort()
print(csv_countryList)

json_countryList = []  # list for all of the countries in the GDP database
for i in df_json['Country'].unique():
    json_countryList.append(i)
json_countryList.sort()
print(json_countryList)


#Code to find countries not in JSON databse
for i in csv_countryList:
    if i not in json_countryList:
        print("Not in JSON dataset: " + i)

for i in json_countryList:
    if i not in csv_countryList:
        print("Not in CSV dataset: " + i)
"""

for x in range(len(
        df_csv['country'].values)):  # change the name of countries in University Ranking Dataset to match GDP dataset
    if df_csv['country'].values[x] == "Republic of Ireland":
        df_csv['country'].values[x] = "Ireland"

    elif df_csv['country'].values[x] == "Russian Federation":
        df_csv['country'].values[x] = "Russia"

    elif df_csv['country'].values[x] == "Unisted States of America":
        df_csv['country'].values[x] = "United States"

    elif df_csv['country'].values[x] == "United States of America":
        df_csv['country'].values[x] = "United States"

    elif df_csv['country'].values[x] == "Unted Kingdom":
        df_csv['country'].values[x] = "United Kingdom"

df_csv = df_csv.drop(df_csv[(df_csv.country == "Hong Kong")].index)  # drop any records of Universities from Hong Kong
df_csv = df_csv.drop(df_csv[(df_csv.country == "Macau")].index)  # drop any records of Universities from Macau

df_csv = df_csv.drop(df_csv[(df_csv.year == 2011)].index)
df_csv = df_csv.drop(df_csv[(df_csv.year == 2012)].index)
df_csv = df_csv.drop(df_csv[(df_csv.year == 2013)].index)
df_csv = df_csv.drop(df_csv[(df_csv.year == 2014)].index)
df_csv = df_csv.drop(df_csv[(df_csv.year == 2015)].index)

# Code to change the female to male ration format from ff:mm to ff - mm
for x in range(len(df_csv["female_male_ratio"].values)):
    if not pd.isna(df_csv["female_male_ratio"].values[x]) and df_csv["female_male_ratio"].values[x] != "-":
        df_csv["female_male_ratio"].values[x] = (df_csv["female_male_ratio"].values[x].split(':')[0] + "-" +
                                                 df_csv["female_male_ratio"].values[x].split(':')[1])

# Merged database will merge via inner join meaning that the values in the resulting dataset are values insuring that all universities from the edited set of data are present
result_dataset = pd.merge(df_csv, df_json, left_on='country', right_on='Country')
del result_dataset['Country']

result_dataset.to_csv('C:/Users/rinke/OneDrive/Desktop/Uni/2022/Sem 1/Busan 300/A5 - Project/Dataset/finalDataset.csv',
                      encoding='utf-8', index=False)
# print(tabulate(result_dataset))
