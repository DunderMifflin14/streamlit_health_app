# --------------------------------------------------------------------------------------------
# modules for cleaning raw data
# --------------------------------------------------------------------------------------------

# imports

import pandas as pd
import matplotlib.pyplot as plt
import csv
import json
import requests
import folium
import yaml
from typing import Dict

# read config file
with open("config.yml", 'r') as file:
    config = yaml.safe_load(file)


def CleanSuicideData(raw_dataset_name: str, config_file: dict) -> None:
    """
    Description:
        - cleans raw dataset for suicide data and saves it as csv
    Input: 
        - raw_dataset: name of the raw dataset to be processed
        - config_file: parsed python dictionary with global variables 
    Returns:
        - None, rather saves cleaned csv file
    """

    df_suicidal_data = pd.read_csv(raw_dataset)
    # check st.file_uploader LATER

    df_suicidal_data_europe = df_suicidal_data[df_suicidal_data.loc[:,
                                                                    'ParentLocation'] == 'Europe']

    # URL of the JSON file
    country_geo = config["country_geo"]
    # Send a GET request to retrieve the JSON data
    response = requests.get(country_geo)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON data, also make sure we get correct dtype
        # (it will rise an error is incorrect dtype obtained)
        dict_world_countries_data_from_github: Dict[str, any] = json.loads(
            response.content)

    else:
        print("Failed to retrieve JSON data.")

    # check structure of returned dictionary
    d_keys_world_countries_data_from_github_keys = dict_world_countries_data_from_github.keys()

    # inside one of the dictionary keys (key = features) there is a list of dictionaries
    # where each dictionary contains country specific info
    list_of_country_related_dictionaries = dict_world_countries_data_from_github['features']

    # check numer of dictionaries within list
    # 177 makes sense, roughly that many countries exist
    len_list_of_country_related_dictionaries = len(
        list_of_country_related_dictionaries)

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

    # # manually matched (otherwise use string similarity libraries)

    dict_country_names_suicidal_vs_github = config['dict_country_names_suicidal_vs_github']

    # Replace country names in suicide dataframe with country names from publicly available json file from github
    # set copy to avoid SettingWithCopyWarning:
    df_suicidal_data_europe = df_suicidal_data_europe.copy()
    df_suicidal_data_europe['Location'] = df_suicidal_data_europe['Location'].replace(
        dict_country_names_suicidal_vs_github)

    # inculde only western and central european countries -> not reliable data for eastern europe
    estern_european_countries = config['estern_european_countries']

    df_suicidal_data_west_central_europe = df_suicidal_data_europe[~df_suicidal_data_europe.Location.isin(
        estern_european_countries)]

    # export data

    df_suicidal_data_west_central_europe.to_csv(
        'suicidal_data_west_central_europe.csv', index=False)


if __name__ == "__main__":

    CleanSuicideData(raw_dataset_name='suicide_data_2019.csv',
                     config_file=config)
