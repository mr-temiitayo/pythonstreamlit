import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')

st.sidebar.subheader('Login to see my page')

correctpassword= '1234Jeida'

pass1,pass2 = st.sidebar.columns(2)

with pass1:
    password = st.sidebar.text_input("Enter the school password",type='password')
    database = pd.read_csv('employeedb1.csv')
    passwordbutton = st.sidebar.button("Login")

if passwordbutton:
    if password:
        if password == correctpassword:
            st.dataframe(database,use_container_width=True)
            if st.button('click me'):
                st.write("hi")
        else:
            st.sidebar.error("Error! Wrong password")
    else:
        st.sidebar.error('Input Password!')