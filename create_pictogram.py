import streamlit as st
import matplotlib.pyplot as plt
from pywaffle import Waffle
import pandas as pd


def CreatePictogramChart():
    '''
    Displays pictogram with proportion of death causes (per 100,000 in western europe?)
    '''

    # --------------------------------------------------------------------------------------------
    # get data values to display in pictogram
    # --------------------------------------------------------------------------------------------
    # read dataset with most common death causes  per country
    df_death_causes = pd.read_csv('df_final.csv')
    df_total_per_cause = df_death_causes.groupby(
        'cause')['value'].sum().reset_index().sort_values(by='value', ascending=False)

    # now convert to proportions of total deaths per cause

    df_total_per_cause['death_prop'] = 100 * \
        (df_total_per_cause['value']/df_total_per_cause['value'].sum())

    # drop absolute values, they wont be used anymore
    df_total_per_cause.drop(columns=['value'], inplace=True)

    # convert to int to easily disply values on pictogram
    df_total_per_cause['death_prop'] = df_total_per_cause['death_prop'].astype(
        int)
    # create a dictionary with cause name and corresponding death proportion value
    dict_cause_death_prop = dict(
        zip(df_total_per_cause['cause'], df_total_per_cause['death_prop']))

    # --------------------------------------------------------------------------------------------
    # display pictogram
    # --------------------------------------------------------------------------------------------

    fig = plt.figure(
        FigureClass=Waffle,
        rows=5,
        columns=10,
        values=dict_cause_death_prop,
        icons='user',
        font_size=20,
        legend={'loc': 'upper left', 'bbox_to_anchor': (1, 1)}
    )
    # add title
    st.subheader('Proportion of Death Causes')

    # display pictogram
    st.pyplot(plt.gcf())
