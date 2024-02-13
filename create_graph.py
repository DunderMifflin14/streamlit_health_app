

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import streamlit as st


def StreamlitMethod(df):
    st.write("StreamlitMethod function")
    # Streamlit app title
    st.title("Streamlit Health App")

    # Display a message
    st.write("Hello, Streamlit!")

    # Display head of the DataFrame
    st.write("Healthcare Project DataFrame:")
    st.write(df)

    # streamlit method - vertical graph
    st.bar_chart(df, y="value", x="geo", color="rank")

    # streamlit method - horizontal graph
    st.bar_chart(df, x="value", y="geo", color="rank")

    return st


def CreateGraph(df):
    # Sample data
    st.write("CreateGraph function")
    categories = df.cause
    values = df.value
    countries = df.geo
    rank = df.rank

    st.bar_chart(df, x="cause", y="value")
    return st


def Matlab(df):
    st.write("Matlab function")
    x = df.value
    y = df.geo
    countries = df.geo.unique()
    num_countries = len(countries)

    y_axis = np.arange(num_countries)

    bar_height = 0.3

    first_causes = df.loc[df.rank == 'first']
    second_causes = df.loc[df.rank == 'second']
    third_causes = df.loc[df.rank == 'third']

    fig = plt.figure(figsize=(20, 30))
    plt.barh(y_axis + bar_height, first_causes.value, height=bar_height)
    plt.barh(y_axis, second_causes.value, height=bar_height)
    plt.barh(y_axis-bar_height, third_causes.value, height=bar_height)
    # Add labels to the bars using plt.text
    for i in range(len(countries)):
        plt.text(first_causes.value.iloc[i] + 1, i + bar_height,
                 first_causes.cause.iloc[i], va='center', fontsize=14, style='italic')
        plt.text(second_causes.value.iloc[i] + 1, i,
                 second_causes.cause.iloc[i], va='center', fontsize=14, style='italic')
        plt.text(third_causes.value.iloc[i] + 1, i - bar_height,
                 third_causes.cause.iloc[i], va='center', fontsize=14, style='italic')

    plt.yticks(y_axis, countries, fontsize=16)
    plt.title("Causes of death per EU country", fontsize=30)
    plt.legend()
    st.pyplot(plt.gcf())  # global
    return st


def Scatter(df):
    st.write("Scatter function")
    st.scatter_chart(
        df,
        x='geo',
        y='cause',
        color='rank',
        size='value',
    )

    st.scatter_chart(
        df,
        y='geo',
        x='cause',
        color='rank',
        size='value',
    )

    return st


def BarChart(df):
    st.write("BarChart function")
    # streamlit method - vertical graph
    st.bar_chart(df, y="value", x="geo", color="rank")

    # streamlit method - horizontal graph
    # st.bar_chart(df, x="OBS_VALUE", y="geo", color="top_no")

