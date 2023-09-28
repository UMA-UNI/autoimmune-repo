# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 12:07:51 2023

@author: Uma R
"""
import streamlit as st

# Create text inputs
text_input1 = st.text_input('Input 1', key='input1')
text_input2 = st.text_input('Input 2', key='input2')

# Create a button to clear the inputs
def clear_text():
    
    # Clear the input values
    st.session_state['input1'] = ""
    st.session_state['input2'] = ""

# Display the input values
st.button("Clear Text Input", on_click=clear_text)
st.write('Input 1 value:', text_input1)
st.write('Input 2 value:', text_input2)
