
import streamlit as st
from pywaffle import Waffle
import matplotlib as plt


def CreatePictogramChart():
    # # Streamlit app
    # st.title("PyWaffle Example")

    # # Data
    # data = {'Category A': 30, 'Category B': 20, 'Category C': 50}

    # # Create a Waffle chart
    # fig = Waffle(
    #     data=data,
    #     rows=5,  # Number of rows in the chart
    #     columns=10,  # Number of columns in the chart
    #     colors=["#232066", "#983D3D", "#DCB732"],  # Colors for each category
    #     legend={'loc': 'upper left', 'bbox_to_anchor': (1, 1)}
    # )

    # # Display the Waffle chart in Streamlit
    # st.pyplot(fig)

    fig = plt.figure(
        FigureClass=Waffle,
        rows=5,
        values=[30, 16, 4],
        colors=["#FFA500", "#4384FF", "#C0C0C0"],
        icons=['sun', 'cloud-showers-heavy', 'snowflake'],
        font_size=20,
        icon_style='solid',
        icon_legend=True,
        legend={
            'labels': ['Sun', 'Shower', 'Snow'],
            'loc': 'upper left',
            'bbox_to_anchor': (1, 1)
        }
    )
    st.pyplot(fig)
