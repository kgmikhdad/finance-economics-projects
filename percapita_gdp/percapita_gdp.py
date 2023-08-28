import streamlit as st
import folium
import geopandas as gpd
from streamlit_folium import folium_static

st.set_page_config(layout="wide")

world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

world['gdp_per_capita'] = world['gdp_md_est'] / world['pop_est']

m = folium.Map(location=[20,0], zoom_start=2, width='100%', height='100%')

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

folium_static(m)

