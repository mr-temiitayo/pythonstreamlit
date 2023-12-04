import streamlit as st
import pandas as pd

csvlink = pd.read_csv("password.csv")

st.dataframe(csvlink)

#get csvlink and check the column and get the first value/data
correctpassword = csvlink['password'].iloc[0]

st.write(correctpassword)

correctpassword = csvlink['password'].iloc[0]
#Szymon should read a createa a loginfile.py
#show a database when a user login
#make sure you save the password in a CSV file