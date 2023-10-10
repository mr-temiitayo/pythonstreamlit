#Streamlit is an API called an Application Programming Interface, used to build and use application software

import streamlit as st
import os

st.title("Welcome to my Age Calculator")

name = st.text_input("Enter your name: ")

yob = st.number_input("Enter your year of birth: ",1950)

curr = st.number_input("Enter your current year: ",2023,2050)

age = curr - yob

if st.button("Show My Age"):
  st.write(f"{name} you are {age} years old in {curr}")