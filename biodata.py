#!/usr/bin/env python
# coding: utf-8

# Import modules
import streamlit as st
import glob
from st_speckmol import speck_plot
import pandas as pd


# Setting titles
st.title("Dataflow design studio")
st.markdown('<p style="font-size:25px">Statistics are just <b style="color:blue">one face</b> of reality</p>', unsafe_allow_html=True)

st.subheader("")

# Example files path
ex_files = glob.glob("data/datum.xyz")
ex_files2 = glob.glob("data/data.xyz")
ex_files3 = glob.glob("data/unemployamine.xyz")

with st.sidebar:
    example_option = st.selectbox("Select data", ["Datum", "Data", "Unemployamine"])

    if example_option == "Datum":
        example_xyz = ex_files[0]
        f = open(example_xyz, "r")
        example_data = f.read()

    elif example_option == "Data":
        example_xyz = ex_files2[0]
        f = open(example_xyz, "r")
        example_data = f.read()
        
    elif example_option == "Unemployamine":
        example_xyz = ex_files3[0]
        f = open(example_xyz, "r")
        example_data = f.read()
        
        df = pd.read_csv('data/unemployment_data.csv')
        df = df.iloc[408:]
        
        
                # Define the style function to apply color based on the year
        def color_cells(x):
            styles = []
            for value in x:
                if '2023' in value:
                    styles.append('background-color: #A67CA9')
                elif '2022' in value:
                    styles.append('background-color: #C5807C')
                elif '2021' in value:
                    styles.append('background-color: #D4BCA0')
                elif '2020' in value:
                    styles.append('background-color: #AADF8D')
                elif '2019' in value:
                    styles.append('background-color: #AFCAD3')
                elif '2018' in value:
                    styles.append('background-color: #D8D697')
                elif '2017' in value:
                    styles.append('background-color: #BFAADB')
                else:
                    styles.append('')
            return styles

            # Apply the style function to the DataFrame
        st.dataframe(df.style.apply(color_cells, subset=['Date']))
        
        
        
        
        
        
width = 600
    
res = speck_plot(example_data, wbox_height="600px",wbox_width="800px", component_h = 700, scroll=False)





