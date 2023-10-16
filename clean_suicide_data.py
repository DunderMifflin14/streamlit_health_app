'''
- 03 file
'''


import pandas as pd
import matplotlib.pyplot as plt
import csv
import json
import requests
import folium
from typing import Dict


df_suicidal_data = pd.read_csv('suicide_data_2019.csv')


df_suicidal_data_europe = df_suicidal_data[df_suicidal_data.loc[:, 'ParentLocation'] == 'Europe']



# URL of the JSON file
country_geo = 'https://raw.githubusercontent.com/python-visualization/folium/master/examples/data/world-countries.json'

# Send a GET request to retrieve the JSON data
response = requests.get(country_geo)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON data, also make sure we get correct dtype 
    # (it will rise an error is incorrect dtype obtained)
    dict_world_countries_data_from_github: Dict[str, any] = json.loads(response.content)
    
else:
    print("Failed to retrieve JSON data.")


# check structure of returned dictionary
d_keys_world_countries_data_from_github_keys = dict_world_countries_data_from_github.keys()



# inside one of the dictionary keys (key = features) there is a list of dictionaries
# where each dictionary contains country specific info
list_of_country_related_dictionaries = dict_world_countries_data_from_github['features']

# check numer of dictionaries within list
# 177 makes sense, roughly that many countries exist
len_list_of_country_related_dictionaries = len(list_of_country_related_dictionaries)

list_of_countries_from_github_json = []

for inx in range(len_list_of_country_related_dictionaries):
    country = list_of_country_related_dictionaries[inx]['properties']['name']
    list_of_countries_from_github_json.append(country)


'''
Note, we are intending to use the data to represent interactive map. For creating map, 
we will use a json file from public github repo with country names and geographical coordinates. 
The problem is, country names in suicide data do not match country names in json file from public 
github repo. we must map / convert country names in suicide dataset with country names from json file. 

'''

# manually matched (otherwise use string similarity libraries)
dict_country_names_suicidal_vs_github = {
  'Iceland'               : 'Iceland',
  'Malta'                 : 'Malta',
  'Armenia'               : 'Armenia',
  'Ireland'               : 'Ireland',
  'Greece'                : 'Greece',
  'Cyprus'                : 'Cyprus',
  'Italy'                 : 'Italy',
  'Serbia'                : 'Republic of Serbia',
  'Türkiye'               : 'Turkey',
  'Albania'               : 'Albania',
  'Azerbaijan'            : 'Azerbaijan',
  'Romania'               : 'Romania',
  'Georgia'               : 'Georgia',
  'Portugal'              : 'Portugal',
  'Spain'                 : 'Spain',
  'Slovakia'              : 'Slovakia',
  'Latvia'                : 'Latvia',
  'France'                : 'France',
  'Slovenia'              : 'Slovenia',
  'Turkmenistan'          : 'Turkmenistan',
  'Belarus'               : 'Belarus',
  'Switzerland'           : 'Switzerland',
  'Germany'               : 'Germany',
  'Croatia'               : 'Croatia',
  'Denmark'               : 'Denmark',
  'Uzbekistan'            : 'Uzbekistan',
  'Belgium'               : 'Belgium',
  'Bulgaria'              : 'Bulgaria',
  'Norway'                : 'Norway',
  'Kazakhstan'            : 'Kazakhstan',
  'Netherlands'           : 'Netherlands',
  'Montenegro'            : 'Montenegro',
  'Bosnia and Herzegovina': 'Bosnia and Herzegovina',
  'Sweden'                : 'Sweden',
  'Kyrgyzstan'            : 'Kyrgyzstan',
  'Russian Federation'    : 'Russia',
  'Finland'               : 'Finland',
  'Tajikistan'            : 'Tajikistan',
  'Czechia'               : 'Czech Republic',
  'Lithuania'             : 'Lithuania',
  'Austria'               : 'Austria',
  'Poland'                : 'Poland',
  'Hungary'               : 'Hungary',
  'Luxembourg'            : 'Luxembourg',
  'Republic of Moldova'   : 'Moldova',
  'Estonia'               : 'Estonia',
  'Ukraine'               : 'Ukraine',
  'The former Yugoslav Republic of Macedonia'            : 'Macedonia',
  'United Kingdom of Great Britain and Northern Ireland' : 'United Kingdom'
}



# Replace country names in suicide dataframe with country names from publicly available json file from github

df_suicidal_data_europe['Location'] = df_suicidal_data_europe['Location'].replace(dict_country_names_suicidal_vs_github)


# inculde only western and central european countries -> not reliable data for eastern europe
estern_european_countries = [
    'Armenia', 'Azerbaijan', 'Georgia', 'Turkmenistan', 'Belarus',
    'Uzbekistan', 'Kazakhstan', 'Russia',
    'Tajikistan', 'Kyrgyzstan', 'Moldova', 'Ukraine', 'Turkey', 'Israel'
]


df_suicidal_data_west_central_europe = df_suicidal_data_europe[~df_suicidal_data_europe.Location.isin(estern_european_countries)]


# export data 

df_suicidal_data_west_central_europe.to_csv('suicidal_data_west_central_europe.csv', index=False)
