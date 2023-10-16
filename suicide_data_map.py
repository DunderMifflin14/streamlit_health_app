'''
- 04 file
'''


import pandas as pd
import matplotlib.pyplot as plt
import csv
import json
import requests
# lib to create interactive map
import folium


df_suicidal_data_west_central_europe = pd.read_csv('suicidal_data_west_central_europe.csv')

#Prepare country level dictionary (country and suicides per 100k population)

dict_europe_suicide_count_per100k= (
    df_suicidal_data_west_central_europe.groupby('Location')['Value'].sum().astype(int).to_dict()
)


country_geo = r'https://raw.githubusercontent.com/python-visualization/folium/master/examples/data/world-countries.json'
# Create map
# Centered at latitude 50 and longitude 10
# Set tiles parameter to None to hide backgroud folium map
map = folium.Map(location=[50, 10], zoom_start=4, tiles=None)  

# Add choropleth layer
folium.Choropleth(
    geo_data=country_geo, #JSON containing coordinates for countries
    name='choropleth',
    # data=dict_github_keys_with_suicidal_data, # 
    data = dict_europe_suicide_count_per100k,

    columns=['Country', 'Number_of_suicides'], #key used to match up the data with country shapes in json (key_on)
    key_on='properties.name', # specifies how the country names should be matched to the geographic data
    fill_color='RdYlGn_r', # green-yellow-Green_reverse
    fill_opacity=1,
    line_opacity=0.9,
    legend_name='Number Of Suicides per 100,000 People',
    highlight=True,
    tooltip=folium.GeoJsonTooltip(fields=['name', 'Number_of_suicides'],
                                  aliases=['Country', 'Number_of_suicides per 100,000'],
                                  labels=True, sticky=False, toLocaleString=True)
).add_to(map)

folium.LayerControl().add_to(map)
map
