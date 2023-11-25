import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')
correctpassword = '12345Moyo'


database = pd.read_csv('employee_db.csv')

pass1,pass2 = st.sidebar.columns(2)

with pass1:
    password = st.sidebar.text_input("Enter Admin Password",type='password')
    login = st.sidebar.button("Login")


if login:
    if password:
        if password == correctpassword:
            st.dataframe(database,use_container_width=True)
        else:
            with pass1:
                st.sidebar.error("You typed in the wrong password")
    else:
        with pass1:
            st.sidebar.error("Please type in a password")


