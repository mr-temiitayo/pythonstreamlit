import streamlit as st
import pandas as pd

csvlink = pd.read_csv('password.csv')

st.dataframe(csvlink)

#get csvlink and check the column, and get th first value/data

correctpassword = csvlink['password'].iloc[0]

st.write(correctpassword)

#Jeida should create a a loginfile.py
#make sure the correct password is saved in a CSV file
#show a database when a user login
