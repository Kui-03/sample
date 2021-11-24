#!usr/bin/env py39

# Import packages
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import folium
from streamlit_folium import folium_static
import geopandas as gpd
import warnings
warnings.filterwarnings('ignore')

url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQA6M-Yz2TNQ72HokTQgVOU2-Ybph5QwztMlMILs70Sd4-G99PyizCjQuw2n3n0u3Y85-Q&usqp=CAU"


pages = ["Introduction", "Objectives", "Methodology", "Exploratory Data Analysis", "Cluster Analysis", "Conclusions", "Recommendations"]
nav = st.sidebar.radio('Page Navigation', pages)

df = pd.read_csv("data/2016-2019-voter-data.csv")

if nav == 'Introduction':
    st.title("Background of the Study")
    st.text("Insert introduction here..")
elif nav == "Cluster Analysis":
    st.title("Cluster Analysis of the Data")
    st.header("K-means clustering")
    st.text("In order to determine the different levels of data, we perfomed K-means clustering analysis on our data..")
    st.image(url) 
elif nav == 'Results':
    st.title("Data")
    st.header("2016-2019 Philippine Voter Dataset")
    if st.checkbox('Show data', value = True):
        st.subheader('Data')
        data_load_state = st.text('Loading data...')
        st.write(df.head(20))
        data_load_state.markdown('Loading data...**done!**')