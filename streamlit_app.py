# ---------------------------------------------------------------------------------------------------------------------------------------------
# imports
# ---------------------------------------------------------------------------------------------------------------------------------------------

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt # comment out for now as it triggers error
import os
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
st.title("Streamlit Health App")

# Display a message
st.write("Hello, Streamlit!")

# Display head of the DataFrame
st.write("Healthcare Project DataFrame:")
st.write(df)
# ---------------------------------------------------------------------------------------------------------------------------------------------
# graph
# ---------------------------------------------------------------------------------------------------------------------------------------------
# streamlit method - vertical graph
st.bar_chart(df, y="OBS_VALUE", x="geo", color="top_no")

# streamlit method - horizontal graph
st.bar_chart(df, x="OBS_VALUE", y="geo", color="top_no")


# ----------------------------------------------------------------------------------------------------------------------------------------------
# matplotlib graph
# ----------------------------------------------------------------------------------------------------------------------------------------------

# '''comment out for now as strealit triggers error when the module is imported'''
# # matplotlib method
# fig, ax = plt.subplots()
# y = df.geo
# x = df.OBS_VALUE

# countries = df.geo.unique()
# num_countries = len(countries)


# first_causes = df.loc[df.top_no == '1']
# second_causes = df.loc[df.top_no == '2']
# third_causes = df.loc[df.top_no == '3']
# bar_height = 0.3

# ax.barh(y_axis + bar_height, first_causes.OBS_VALUE, height = bar_height)
# ax.barh(y_axis, second_causes.OBS_VALUE, height = bar_height)
# ax.barh(y_axis-bar_height, third_causes.OBS_VALUE, height = bar_height)

# # # Add labels to the bars using plt.text
# # for i in range(len(countries)):
# #     ax.text(first_causes.OBS_VALUE.iloc[i] + 1, i + bar_height, first_causes.icd10.iloc[i], va='center', fontsize=14, style = 'italic')
# #     ax.text(second_causes.OBS_VALUE.iloc[i] + 1, i, second_causes.icd10.iloc[i], va='center', fontsize=14, style = 'italic')
# #     ax.text(third_causes.OBS_VALUE.iloc[i] + 1, i - bar_height, third_causes.icd10.iloc[i], va='center', fontsize=14, style = 'italic')

# # ax.yticks(y_axis, countries, fontsize=16)
# ax.barh(x, y, 0.5)
# # ax.title("Causes of death per EU country", fontsize=30)
# # ax.legend()
# st.pyplot(fig)


# df_head = df.head()
# st.write(df_head)





# ax.barh(y_axis + bar_height, first_causes.OBS_VALUE, height = bar_height)
# ax.barh(y_axis, second_causes.OBS_VALUE, height = bar_height)
# ax.barh(y_axis-bar_height, third_causes.OBS_VALUE, height = bar_height)
# =======
# y_axis = np.arange(num_countries)






# ---------------------------------------------------------------------------------------------------------------------------------------------
# graph
# ---------------------------------------------------------------------------------------------------------------------------------------------
# stworzyc nowy file i sie odwolac tylko do niej w streamlit_app.py

# # ---------------------------------------------------------------------------------------------------------------------------------------------
# # graph
# # ---------------------------------------------------------------------------------------------------------------------------------------------


# Sample data
categories = ['Category 1', 'Category 2', 'Category 3', 'Category 4']
values = [10, 15, 7, 12]


plt.bar(categories, values)


plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Simple Bar Plot')


plt.show()

