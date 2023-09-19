#Project Objective
# Create a student scores database which can 
# -get the name
# -4 subjects
# -calculate the average
# -calculate the grade (A,B,C,D,E,F)
# -update your csv file

#what is csv file?
#csv file are text files that each data is separated by a comma (comma separated values)

import streamlit as st

import pandas as pd #this is used to read csv files and convert to a table (dataframe)

st.set_page_config(layout='wide')

st.title('Students Scores Database')

#read a csv file
df=pd.read_csv('studentsdb.csv') #pandas should read this csv file
st.dataframe(df,use_container_width=True) #streamlit should display as dataframe