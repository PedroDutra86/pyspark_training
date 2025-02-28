import streamlit as st
from streamlit_folium import st_folium
import folium

st.set_page_config(page_title='Netflix', page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)


st.title = 'netflixDados'

st.write('Hello World!')

add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone"))

st.write(add_selectbox)
options = st.multiselect(
    "What are your favorite colors",
    ["Rio de Janeiro", "Yellow", "Red", "Blue"],
    ["Yellow", "Red"],
)
st.header("One", divider=True)

m = folium.Map(location=[39.949610, -75.150282], zoom_start=16)
folium.Marker(
    [39.949610, -75.150282], popup="Liberty Bell", tooltip="Liberty Bell"
).add_to(m)

st_data = st_folium(m, width=725)