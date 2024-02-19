import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static


def DisplaySuicideMap(data_path='suicidal_data_west_central_europe.csv'):
    # Load your data
    df_suicidal_data_west_central_europe = pd.read_csv(data_path)

    # Prepare country level dictionary (country and suicides per 100k population)
    dict_europe_suicide_count_per100k = (
        df_suicidal_data_west_central_europe.groupby(
            'Location')['Value'].sum().astype(int).to_dict()
    )

    # Create a Folium map
    m = folium.Map(location=[50, 10], zoom_start=4, tiles=None)

    # Add choropleth layer
    folium.Choropleth(
        geo_data='https://raw.githubusercontent.com/python-visualization/folium/master/examples/data/world-countries.json',
        name='choropleth',
        data=dict_europe_suicide_count_per100k,
        columns=['Country', 'Number_of_suicides'],
        key_on='properties.name',
        fill_color='RdYlGn_r',
        fill_opacity=1,
        line_opacity=0.9,
        legend_name='Number Of Suicides per 100,000 People',
        highlight=True,
        tooltip=folium.GeoJsonTooltip(fields=['name', 'Number_of_suicides'],
                                      aliases=[
                                          'Country', 'Number_of_suicides per 100,000'],
                                      labels=True, sticky=False, toLocaleString=True)
    ).add_to(m)

    # Display the Folium map in the Streamlit app
    st.title("Suicide by Country")
    folium_static(m)
