import streamlit as st

st.title("My Age Calculator")

name = st.text_input("Enter your name")

yearofbirth = st.number_input("Enter your year of birth",1950,2023)

currentyear = st.number_input("Enter your current year",2023)

age = currentyear - yearofbirth


if st.button("Check My Age"):
    st.write(name,'you are',age,'in',currentyear)