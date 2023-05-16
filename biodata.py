#!/usr/bin/env python
# coding: utf-8

# Import modules
import streamlit as st
import glob
from st_speckmol import speck_plot


# Setting titles
st.title("Dataflow design studio")
st.markdown('<p style="font-size:25px">Statistics are just <b style="color:blue">one face</b> of reality</p>', unsafe_allow_html=True)

st.subheader('Eclate l\'invisible')

# Example files path
ex_files = glob.glob("data/datum.xyz")
ex_files2 = glob.glob("data/data.xyz")

with st.sidebar:
    example_option = st.selectbox("Select data", ["Datum", "Data"])

    if example_option == "Datum":
        example_xyz = ex_files[0]
        f = open(example_xyz, "r")
        example_data = f.read()

    elif example_option == "Data":
        example_xyz = ex_files2[0]
        f = open(example_xyz, "r")
        example_data = f.read()
        
width = 800
    
res = speck_plot(example_data, wbox_height="600px",wbox_width="800px", component_h = 700, scroll=False)
