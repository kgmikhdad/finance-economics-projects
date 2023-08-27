import streamlit as st
import folium
import geopandas as gpd
from streamlit_folium import folium_static

# Set the layout of the Streamlit app to wide mode
st.set_page_config(layout="wide")

# Load the world map data
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Calculate GDP per capita
world['gdp_per_capita'] = world['gdp_md_est'] / world['pop_est']

# Create a map object with a larger width and height
m = folium.Map(location=[20,0], zoom_start=2, width='100%', height='100%')

# Add the data to the map
folium.Choropleth(
    geo_data=world,
    name='choropleth',
    data=world,
    columns=['name', 'gdp_per_capita'],
    key_on='feature.properties.name',
    fill_color='YlGnBu',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='GDP per Capita by Country'
).add_to(m)

folium.LayerControl().add_to(m)

# Display the map in Streamlit
folium_static(m)

