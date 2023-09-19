#Project Objective
# Create a student scores database which can 
# -get the name
# -4 subjects
# -calculate the average
# -calculate the grade (A,B,C,D,E,F) using the average
# -save and update your csv file

import streamlit as st
import pandas as pd #this is what we use to read csv files and convert to a table (dataframe)

# what is CSV file?
#A CSV file is a text file that each data is separated by a comma (comma separated values)

df = pd.read_csv("scores.csv") #read CSV file
st.dataframe(df) #show CSV as dataframe