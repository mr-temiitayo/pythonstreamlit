import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')
st.sidebar.subheader("Login to see my page")

correctpassword =  '12345Szymon'

pass1,pass2 = st.sidebar.columns(2)
with pass1:

    password = st.sidebar.text_input("Enter the school password",type="password")
    login = st.sidebar.button('Login me in now')

if login:
    if password:
        if password == correctpassword:
            database = pd.read_csv("scores.csv")
            st.dataframe(database,use_container_width=True)
        else:
            st.sidebar.subheader("Password not correct")
    else:
        st.sidebar.subheader('Type in the password first')