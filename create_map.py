# standard libraries
import streamlit as st
import pandas as pd

import numpy as np

# def get_aoi():



def Map():
    import os
    folder_path = os.getcwd()
    file_name = "df_final.csv"
    full_path = os.path.join(folder_path, file_name)

    data = pd.read_csv(full_path)
    df = pd.DataFrame(data)

    st.write("")
    form = st.form(key="form_settings")
    col1, col2, col3 = form.columns([2, 2, 1]) 

    address = col1.text_input(
        "Country you want to check",
        key="address",
    )

    sex = col2.selectbox(
        "Pick the ranked cause you want to view",
        options=list([1,2,3]),
        key="ranked_cause",
    )
    expander = form.expander("Customize map style")
    col1style, col2style, _, col3style = expander.columns([2, 2, 0.1, 2])
    
    form.form_submit_button(label="Submit")
    
    df_map = pd.DataFrame(
        np.random.randn(100000, 2) / [1, 0.8] + [51.1, -1.4],
        columns=['lat', 'lon'])
    st.map(df_map) 