#Objective: How to use texts and buttons in Python web

#python for our data analysis (creating and computing data)

#streamlit helps you design a page for your python project (HTML & CSS FOR PYTHON)

import streamlit as st #this is the module to get the streamlit functions

#---------------------USING TEXTS----------------------

st.title("This is a big title")

st.header("This is a big header")

st.subheader("This is a subheader")

st.text("This is a normal text")

#--------------GET USER INPUT---------------------------

#variables and data
'''
data is a useful information in python
(Moses, 13, Hong Kong, Boy)

variables are names used to store Data 
firstname = Moses
age = 13
country = Hong Kong
gender = Boy
'''

name = st.text_input("Enter your name")

age = st.number_input("Enter your age")

country = st.text_input("Enter your country")

if st.button("Show My Details"):
    st.write("Welcome")


#rules in creating variables
#if elif else

#homework
'''
create a simple python page to ask for firstname, lastname, school, age, best game, best color
then create a button to say Congratulations you are now registered 
'''