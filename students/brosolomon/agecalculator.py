#Project: Create an Age Calculator

import streamlit as st

st.header("Age Calculator Project")

name = st.text_input('Enter your name')

yob = st.number_input('Enter your year of birth',1950,2023) 

curr = st.number_input('Enter your current year',2023)

age = curr - yob

if st.button("Check My Age"):
    st.subheader(f'{name} you are {age} years old in {curr}')

# f-string: This will convert all variables to a string (statement).
# indicate variables by placing them in a curly brackets {}

#bars to use: st.success, warning, info, error