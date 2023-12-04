import streamlit as st
import pandas as pd

correctpassword = 'Tofe12345'

password = st.text_input("Enter the admin password",type='password')

if st.button("Login"):
    if password == correctpassword:
        csvlink = pd.read_csv('homework.csv')
        st.dataframe(csvlink,use_container_width=True)
    else:
        st.error("Wrong Password")