# ---------------------------------------------------------------------------------------------------------------------------------------------
# imports
# ---------------------------------------------------------------------------------------------------------------------------------------------

# standard libraries
import streamlit as st
import pandas as pd
import matplotlib as plt  # comment out for now as it triggers error
import os
import numpy as np
# import folium
# from streamlit_folium import folium_static
# from pywaffle import Waffle


# custom modules
from create_graph import CreateGraph, Matlab, Scatter, BarChart, Map
from create_suicide_graph import CreateSuicideGraph
from intro import IntroPage

from settings_tab import SettingsTab


# from suicide_data_map import DisplaySuicideMap
# from create_pictogram import CreatePictogramChart


# ---------------------------------------------------------------------------------------------------------------------------------------------
# data
# ---------------------------------------------------------------------------------------------------------------------------------------------
folder_path = os.getcwd()
file_name = "df_final.csv"
full_path = os.path.join(folder_path, file_name)

data = pd.read_csv(full_path)
df = pd.DataFrame(data)

# ---------------------------------------------------------------------------------------------------------------------------------------------
# streamlit
# ---------------------------------------------------------------------------------------------------------------------------------------------

# Streamlit app title
st.title("Streamlit Health App")

# Display a message
st.write("Hello, Streamlit!")

# Display head of the DataFrame
st.write("Healthcare Project DataFrame:")


# ----------------------------------------------------------------------------------------------------------------------------------------------
# matplotlib graph
# ----------------------------------------------------------------------------------------------------------------------------------------------
IntroPage()
# call the function here
BarChart(df)
# Matlab(df)
Scatter(df)

# Map(df) # triggers an error


# Map2() # triggers an error

# SettingsTab() # trigers an error

# # ----------------------------------------------------------------------------------------------------------------------------------------------
# # suicide graph and map
# # ----------------------------------------------------------------------------------------------------------------------------------------------

CreateSuicideGraph()

# DisplaySuicideMap()

