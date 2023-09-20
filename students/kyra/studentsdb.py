#  Create a student scores database which can 
#  -get the name of the student
#  -get 4 subjects score
#  -calculate the average of the subjects
#  -calculate the grade (A,B,C,D,E,F) using the average
#  -update your csv file

# what is a CSV file?
# A CSV file is a text file that each data is separated by a comma (comma separated values)

import streamlit as st
import pandas as pd #pandas helps to open, read and display CSV files as a table (dataframe)

st.set_page_config(layout='wide') #this makes our page full width

st.header("Student's Scores Database")

df = pd.read_csv('scores.csv') #here pandas will read the csv file
st.dataframe(df,use_container_width=True) #here streamlit with display it as a table (dataframe)

#classwork
# create your own scores csv File
# open and read using pandas
# display your csv as a table