import streamlit as st #this is used to build a page for my python project

st.title("My Age Calculator")

name = st.text_input('What is your name')

yob = st.number_input("what is your year of birth")

current = st.number_input("What is the current year")

age = current - yob

st.write('Your age is',age,'years old')