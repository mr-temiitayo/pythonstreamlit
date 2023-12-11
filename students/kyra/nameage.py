#Create a python program to ask the name on the left column and the age on the right column
#Save this in a CSV file and display the database

import streamlit as st
import pandas as pd #this will help us read, add to and display your CSV file as a table (dataframe)

csvfile = pd.read_csv('nameage.csv')
st.dataframe(csvfile)


namecol,agecol = st.columns(2)

with namecol:
    name = st.text_input("Enter your name")

with agecol:
    age = st.number_input("Enter your age",0)

if st.button("Save Information"):
    st.write(name,'you are',age)
    newdict = {'Name':[name],'Age':age}
    st.write(newdict)

#create a new python program
#create a csvfile and display is using streamlit
#Ask user for their best game and best movie using two columns
#create a dictionary from their response and display is as a dataframe