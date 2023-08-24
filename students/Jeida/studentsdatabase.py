import streamlit as st
import pandas as pd #used to create tables

#Project Objective
# Create a student scores database which can 
# -get the name
# -4 subjects
# -calculate the average
# -calculate the grade (A,B,C,D,E,F)
# -update your csv file

#what is csv file?
#csv file are text files that each data is separated by a comma (comma separated values)

st.set_page_config(layout='wide')

st.title('Student Scores Database')
#Open a csv file
df= pd.read_csv('scores.csv')
st.dataframe(df)

