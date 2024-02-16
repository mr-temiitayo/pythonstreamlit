import streamlit as st

st.title("My Age Calculator")

name = st.text_input("Enter your name")

yob = st.number_input("Enter your year of birth",1990,2024)
currentyear = st.number_input("Enter your current year",2024,2050)
age = currentyear - yob

if st.button("Check My Age"):
    st.write("You are",age,'in',currentyear)