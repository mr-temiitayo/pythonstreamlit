#Project Objective
# Create a student scores database which can 
# -get the name
# -4 subjects
# -calculate the average
# -calculate the grade (A,B,C,D,E,F) using the average
# -save and update your csv file

import streamlit as st
import pandas as pd #used to read a csv file and convert to a table (dataframe)

#What is a CSV file?
#A CSV file is a text file that each data is separated by a comma (comma separated values)

df = pd.read_csv('scores.csv')
st.dataframe(df)