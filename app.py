import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu

st.set_page_config(layout="wide")

# Hide streamlit default menu and footer from the template
hide_st_style = """
    <style>
    #MainMenu {visibility: hidden}
    footer {visibility: hidden}
    </style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

data = pd.read_csv('Barcelona_rent_price.csv')

with st.sidebar:
    st. title("Bascelona Rental Analysis")
    nav_menu = option_menu("Main Menu", ["Dashboard", "Analyzer"], 
        icons=['clipboard-data', 'map', 'gear'], menu_icon="cast", default_index=0)
    
st.dataframe(data)