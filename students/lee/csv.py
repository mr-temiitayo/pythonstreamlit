#we will learn how to open csv files with python

#what is csv file?
#csv file are text files that each data is separated by a comma (comma separated values)

import streamlit as st
import pandas as pd #this will help open and read your CSV files then convert to a table (dataframe)

st.set_page_config(layout='wide')

df = pd.read_csv('grades.csv') #pd will help me read the csv file

st.dataframe(df) #show the dataframe

# classwork: create a csv file named scores.csv and read it using pandas, and display it with streamlit