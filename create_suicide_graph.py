
# standard libraries
import streamlit as st
import pandas as pd
import os


def CreateSuicideGraph():
    # ---------------------------------------------------------------------------------------------------------------------------------------------
    # get data
    # ---------------------------------------------------------------------------------------------------------------------------------------------
    folder_path = os.getcwd()
    file_name = "suicidal_data_west_central_europe.csv"
    full_path = os.path.join(folder_path, file_name)

    data = pd.read_csv(full_path)
    df = pd.DataFrame(data)

    # ---------------------------------------------------------------------------------------------------------------------------------------------
    # manipulate data
    # ---------------------------------------------------------------------------------------------------------------------------------------------

    df_male_fem_only = df[df['Dim1'].isin(['Male', 'Female'])]

    # get total values suicide figure for gender per country

    df_suicide_gender_country = df_male_fem_only.groupby(
        ['Location', 'Dim1'])['Value'].sum().reset_index()

    # represent gender (male and fem value) as 2 separate columns each holding vals for male and fem
    df_suicide_gender_country_pivoted = df_suicide_gender_country.pivot(
        index='Location', columns='Dim1', values='Value').reset_index()

    # Remove the name of the index column
    df_suicide_gender_country_pivoted = df_suicide_gender_country_pivoted.rename_axis(
        None, axis=1)

    # ---------------------------------------------------------------------------------------------------------------------------------------------
    # Streamlit app
    # ---------------------------------------------------------------------------------------------------------------------------------------------

    # Allow the user to select the gender to display
    selected_gender = st.selectbox('Select Gender:', ['Female', 'Male'])

    # Filter DataFrame based on user selection
    selected_column = 'Female' if selected_gender == 'Female' else 'Male'
    selected_df = df_suicide_gender_country_pivoted.loc[:, [
        'Location', selected_column]]

    # Bar chart
    # By default, when creating a bar chart in Streamlit, the x-axis of the bar chart is determined by the df index
    st.bar_chart(selected_df.set_index('Location'))
