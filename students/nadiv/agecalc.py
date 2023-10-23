import streamlit as st

name = st.text_input('Enter your name')
age = st.number_input('enter your age',0)

if st.button('show me'):
    st.success(f"{name} you are {age}")