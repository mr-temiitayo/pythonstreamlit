#what is csv file?
#csv file is a text file that each data is separated by a comma (comma separated values)
#you can read a csv file and display it as a table 

import streamlit as st
import pandas as pd #this will help to read the csv file

csvlink = pd.read_csv('scores.csv') #here is where pandas read the csv file
st.table(csvlink)

#create your csv file for 5 phones and their prices. 
# read the csv file using pandas and display it usgin streamlit



#homework: create a csv file of 5 states and capitals in Nigeria and display the csv file as a table
