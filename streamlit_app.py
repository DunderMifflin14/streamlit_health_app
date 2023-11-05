# ---------------------------------------------------------------------------------------------------------------------------------------------
# imports
# ---------------------------------------------------------------------------------------------------------------------------------------------

import streamlit as st
import pandas as pd
import os
import pydeck
import matplotlib.pyplot as plt
import numpy as np

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
st.title("Simple Bar Chart in Streamlit edited by Marta")

# Display a message
st.write("Hello, Streamlit!")

# Display the DataFrame
st.write("Healthcare Project DataFrame:")
st.write(df)
# ---------------------------------------------------------------------------------------------------------------------------------------------
# graph
# ---------------------------------------------------------------------------------------------------------------------------------------------
# streamlit method
st.bar_chart(df, x="OBS_VALUE", y="geo", color="top_no")

# matplotlib method
fig, ax = plt.subplots()
y = df.geo
x = df.OBS_VALUE

countries = df.geo.unique()
num_countries = len(countries)

y_axis = np.arange(num_countries)

first_causes = df.loc[df.top_no == '1']
second_causes = df.loc[df.top_no == '2']
third_causes = df.loc[df.top_no == '3']
bar_height = 0.3

plt.barh(y_axis + bar_height, first_causes.OBS_VALUE, height = bar_height)
plt.barh(y_axis, second_causes.OBS_VALUE, height = bar_height)
plt.barh(y_axis-bar_height, third_causes.OBS_VALUE, height = bar_height)

# Add labels to the bars using plt.text
for i in range(len(countries)):
    plt.text(first_causes.OBS_VALUE.iloc[i] + 1, i + bar_height, first_causes.icd10.iloc[i], va='center', fontsize=14, style = 'italic')
    plt.text(second_causes.OBS_VALUE.iloc[i] + 1, i, second_causes.icd10.iloc[i], va='center', fontsize=14, style = 'italic')
    plt.text(third_causes.OBS_VALUE.iloc[i] + 1, i - bar_height, third_causes.icd10.iloc[i], va='center', fontsize=14, style = 'italic')

plt.yticks(y_axis, countries, fontsize=16)
plt.title("Causes of death per EU country", fontsize=30)
plt.legend()
st.pyplot(fig)
