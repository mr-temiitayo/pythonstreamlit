import streamlit as st
import pandas as pd
st.set_page_config(layout='wide')

correctpassword = 'Nayel1DB'

pass1, pass2 = st.sidebar.columns([1,2])

with pass1:
    password = st.sidebar.text_input("Please enter admin password",type='password')

    login = st.sidebar.button("Login")



if login:
    if password:
        if password == correctpassword:
            csvlink = pd.read_csv("employee.csv")
            st.dataframe(csvlink,use_container_width=True)
        else:
       
            st.sidebar.error("Password is incorrect")
    else:
       
        st.sidebar.error("Please enter password")

