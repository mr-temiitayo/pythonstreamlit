import streamlit as st

st.subheader("Welcome to my age calculator")

name = st.text_input("Enter your name")

currentyear = st.number_input("Enter your current year",2023)

yearofbirth = st.number_input("Enter your year of birth",1950)

age = currentyear - yearofbirth

if st.button('Check your age'):
    st.write(name,'you are',age,'in year',currentyear)