# standard libraries
import streamlit as st
import pandas as pd
import os


def CreateMap(df):
    # ---------------------------------------------------------------------------------------------------------------------------------------------
    # manipulate data
    # ---------------------------------------------------------------------------------------------------------------------------------------------
    countries = []
    countries = df.geo.unique()
    # ---------------------------------------------------------------------------------------------------------------------------------------------
    # Streamlit app
    # ---------------------------------------------------------------------------------------------------------------------------------------------

    st.write("")
form = st.form(key="form_settings")
col1, col2, col3 = form.columns([3, 1, 1])

address = col1.text_input(
    "Country you want to check",
    key="address",
)
radius = col2.slider(
    "Radius (meter)",
    100,
    1500,
    key="radius",
)
style = col3.selectbox(
    "Pick a number",
    options=list([1,2,3]),
    key="number",
)

# style = col3.selectbox(
#     "Color theme",
#     options=list(STYLES.keys()),
#     key="style",
# )

expander = form.expander("Customize map style")
col1style, col2style, _, col3style = expander.columns([2, 2, 0.1, 2])

bg_buffer = col1style.slider(
    "Background Size",
    min_value=0,
    max_value=50,
    help="How much the background extends beyond the figure.",
    key="bg_buffer",
)

col1style.markdown("---")
contour_color = col1style.color_picker(
    "Map contour color",
    key="contour_color",
)
contour_width = col1style.slider(
    "Map contour width",
    0,
    30,
    help="Thickness of contour line sourrounding the map.",
    key="contour_width",
)

name_on = col2style.checkbox(
    "Display title",
    help="If checked, adds the selected address as the title. Can be customized below.",
    key="name_on",
)
custom_title = col2style.text_input(
    "Custom title (optional)",
    max_chars=30,
    key="custom_title",
)
font_size = col2style.slider(
    "Title font size",
    min_value=1,
    max_value=50,
    key="font_size",
)
font_color = col2style.color_picker(
    "Title font color",
    key="font_color",
)
text_x = col2style.slider(
    "Title left/right",
    -100,
    100,
    key="text_x",
)
text_y = col2style.slider(
    "Title top/bottom",
    -100,
    100,
    key="text_y",
)
text_rotation = col3style.slider(
    "Title rotation",
    -90,
    90,
    key="text_rotation",
)

# if style != st.session_state["previous_style"]:
#     st.session_state.update(get_colors_from_style(style))
# draw_settings = copy.deepcopy(STYLES[style])
# for lc_class in st.session_state.lc_classes:
#     picked_color = col3style.color_picker(lc_class, key=lc_class)
#     if "_" in lc_class:
#         lc_class, idx = lc_class.split("_")
#         draw_settings[lc_class]["cmap"][int(idx)] = picked_color  # type: ignore
#     else:
#         draw_settings[lc_class]["fc"] = picked_color

form.form_submit_button(label="Submit")