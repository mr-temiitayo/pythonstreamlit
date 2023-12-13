#we want to learn to save our login in a csv file

import streamlit as st
import pandas as pd

passwordlink = pd.read_csv('password.csv')

correctpassword = passwordlink['password'].iloc[0]

st.dataframe(passwordlink)
st.write(correctpassword)

#create a register and login side bar to allow many people to register (create their username, password)
#then another page to login checking if their credentials are correct. (login with your username, password)
#display their username after a succesful login