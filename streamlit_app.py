# ---------------------------------------------------------------------------------------------------------------------------------------------
# imports
# ---------------------------------------------------------------------------------------------------------------------------------------------

import streamlit as st
import pandas as pd
import matplotlib
from matplotlib import pyplot
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------------------------------------------------------------------------
# data
# ---------------------------------------------------------------------------------------------------------------------------------------------

# Create a DataFrame
data = {
    'Category': ['A', 'B', 'C', 'D'],
    'Values'  : [10, 20, 15, 30]
}
df = pd.DataFrame(data)



# ---------------------------------------------------------------------------------------------------------------------------------------------
# streamlit
# ---------------------------------------------------------------------------------------------------------------------------------------------


# Streamlit app title
st.title("Simple Bar Chart in Streamlit")

# Display a message
st.write("Hello, Streamlit!")

# Display the DataFrame
st.write("Sample DataFrame:")
st.write(df)

# Create an interactive slider to set the maximum y-axis value
st.sidebar.header("Set Y-Axis Max Value")
max_y_value = st.sidebar.slider("Max Y-Axis Value", 0, 50, max(df['Values']))


# ---------------------------------------------------------------------------------------------------------------------------------------------
# graph
# ---------------------------------------------------------------------------------------------------------------------------------------------


# Create a simple bar chart
st.write("Bar Chart:")
fig, ax = plt.subplots()
ax.bar(df['Category'], df['Values'])
ax.set_ylim(0, max_y_value)  # Set the y-axis limit
st.pyplot(fig)
