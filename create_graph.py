import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import streamlit as st


def StreamlitMethod(df):
    # Streamlit app title
    st.title("Streamlit Health App")

    # Display a message
    st.write("Hello, Streamlit!")

    # Display head of the DataFrame
    st.write("Healthcare Project DataFrame:")
    st.write(df)

    # streamlit method - vertical graph
    st.bar_chart(df, y="OBS_VALUE", x="geo", color="top_no")

    # streamlit method - horizontal graph
    st.bar_chart(df, x="OBS_VALUE", y="geo", color="top_no")

    return st


def CreateGraph(df):
    # Sample data
    categories = df.icd10
    values = df.OBS_VALUE
    countries = df.geo
    rank = df.top_no

    st.bar_chart(df, x="icd10", y="OBS_VALUE")
    return st


def Matlab(df):
    df_final = df
    y = df_final.geo
    x = df_final.OBS_VALUE

    countries = df_final.geo.unique()
    num_countries = len(countries)

    y_axis = np.arange(num_countries)
    plt.figure(figsize=(8, 8))
    first_causes = df_final.loc[df_final.top_no == '1']
    second_causes = df_final.loc[df_final.top_no == '2']
    third_causes = df_final.loc[df_final.top_no == '3']
    bar_height = 0.3

    plt.barh(y_axis + bar_height, first_causes.OBS_VALUE, height=bar_height)
    plt.barh(y_axis, second_causes.OBS_VALUE, height=bar_height)
    plt.barh(y_axis-bar_height, third_causes.OBS_VALUE, height=bar_height)
    # Add labels to the bars using plt.text
    for i in range(len(countries)):
        plt.text(first_causes.OBS_VALUE.iloc[i] + 1, i + bar_height,
                 first_causes.icd10.iloc[i], va='center', fontsize=14, style='italic')
        plt.text(second_causes.OBS_VALUE.iloc[i] + 1, i,
                 second_causes.icd10.iloc[i], va='center', fontsize=14, style='italic')
        plt.text(third_causes.OBS_VALUE.iloc[i] + 1, i - bar_height,
                 third_causes.icd10.iloc[i], va='center', fontsize=14, style='italic')

    plt.yticks(y_axis, countries, fontsize=16)
    plt.title("Causes of death per EU country", fontsize=30)
    plt.legend()
    # fig = plt.figure(figsize=8)
    # plt.bar(x=df.OBS_VALUE, y=df.geo)
    # st.pyplot(fig)
    st.pyplot(plt.gcf())  # global
    return st


def AltairMethod(df):

    return st
