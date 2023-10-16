'''
- 05 file
- DRAFT ONLY
'''

import pandas as pd
import numpy as np
import folium

data = {
    'Country': ['Poland', 'Austria'],
    'Value': ['xxx', 'yyy']
}

df = pd.DataFrame(data)


# Create a sample DataFrame
data = {
    'X': [1, 2, 3],
    'Y': [2, 4, 6],
    'weights': [0.5, 1.0, 0.7]
}

df = pd.DataFrame(data)

# Calculate the weighted Pearson correlation coefficient manually
weighted_x_mean = np.average(df['X'], weights=df['weights'])
weighted_y_mean = np.average(df['Y'], weights=df['weights'])
weighted_covariance = np.average((df['X'] - weighted_x_mean) * (df['Y'] - weighted_y_mean), weights=df['weights'])
weighted_x_std = np.sqrt(np.average((df['X'] - weighted_x_mean) ** 2, weights=df['weights']))
weighted_y_std = np.sqrt(np.average((df['Y'] - weighted_y_mean) ** 2, weights=df['weights']))
weighted_pearson_correlation = weighted_covariance / (weighted_x_std * weighted_y_std)

print("Weighted Pearson Correlation Coefficient:", weighted_pearson_correlation)



european_geo = r'https://raw.githubusercontent.com/python-visualization/folium/master/examples/data/world-countries.json'

# Create map
# Centered at latitude 50 and longitude 10
map = folium.Map(location=[50, 10], zoom_start=4, tiles=None, background_color='#e0ffe0')

# use the folium.GeoJson function to add a GeoJson layer to the map.
folium.GeoJson(
    data=european_geo,
    # The style_function sets the styling properties for the countries (borders) when 
    # they are not being hovered over.
    style_function=lambda feature: {
        'fillOpacity': 1,  # Set to 0 do erase backgorund countries to be coloured
        'color': 'black',  # Country border color
        'weight': 2,  # Border line width
        'fillColor': '#9ecae1',  # colour of 'background countries'
    },
    # highlight_function sets the styling properties for the countries when they are being hovered over.
    highlight_function=lambda x: {
        'weight': 3,  # Border line width on hover
        'fillOpacity': 0.8,  # Fill opacity on hover
        'fillColor': '#3182bd',  # colour of country on hover
    },
    # The tooltip parameter specifies the field that will be shown as a tooltip when hovering over a country.
    tooltip=folium.GeoJsonTooltip(fields=['name'], aliases=['country'])
).add_to(map)

# folium.LayerControl().add_to(map)
folium.LayerControl().add_to(map)

# Display the map
map
