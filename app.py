import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import plotly.express as px

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

#with st.sidebar:
#    st. title("Bascelona Rental Analysis")
#    nav_menu = option_menu("Main Menu", ["Dashboard", "Analyzer"], 
#        icons=['clipboard-data', 'map', 'gear'], menu_icon="cast", default_index=0)

st.subheader("Barcelona house rental analysis")
enable_district_filter = st.checkbox('Enable filter with Year')

if enable_district_filter:

    col_heatmap_chart, col_summary = st.columns([2,1])

    with col_heatmap_chart:


        options_for_year = data['Year'].unique().tolist()
        selected_options_year = st.multiselect('Select Year(You can modify defailt selection)',options_for_year, default=options_for_year[0:5])
        filter_data = data.query('Year == @selected_options_year')

        fig = px.treemap(filter_data, path=[px.Constant("all"), 'Year', 'Trimester', 'District'], values='Price')
        fig.update_traces(root_color="lightgrey")
        fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))

        st.plotly_chart(fig, theme="streamlit")

    with col_summary:
        col_1, col_2 = st.columns(2)

        with col_1:
            total_rental_count = filter_data['Price'].value_counts().sum()
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.metric(label = 'Total rental record', value= total_rental_count)

        with col_2:
            sum_of_rental_amount = filter_data['Price'].sum()
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")        
            st.metric(label = 'Total rental amount in EURO', value= sum_of_rental_amount)



###############
else:
    
    col_heatmap_chart_dist, col_summary_dist = st.columns([2,1])

    with col_heatmap_chart_dist:


        options_for_district = data['District'].unique().tolist()
        selected_options_district = st.multiselect('Select Year(You can modify defailt selection)',options_for_district, default=options_for_district[0:5])
        filter_data_district = data.query('District == @selected_options_district')

        fig = px.treemap(filter_data_district, path=[px.Constant("all"), 'Year', 'Trimester', 'District'], values='Price')
        fig.update_traces(root_color="lightgrey")
        fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))

        st.plotly_chart(fig, theme="streamlit")

    with col_summary_dist:
        col_1, col_2 = st.columns(2)

        with col_1:
            total_rental_count = filter_data_district['Price'].value_counts().sum()
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.metric(label = 'Total rental record', value= total_rental_count)

        with col_2:
            sum_of_rental_amount = filter_data_district['Price'].sum()
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")        
            st.metric(label = 'Total rental amount in EURO', value= sum_of_rental_amount)

st.subheader("Data Source")
st.dataframe(data)