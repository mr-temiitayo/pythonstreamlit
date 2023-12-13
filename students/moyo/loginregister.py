import streamlit as st
import pandas as pd

menu = st.sidebar.selectbox('Menu',['Register','Login'])

if menu == 'Register':
    st.sidebar.text_input("Choose your username")
    st.sidebar.text_input("Enter your middle name")
    st.sidebar.text_input("Create your password",type='password')






if menu == 'Login':
    st.sidebar.text_input("Enter your username")
    st.sidebar.text_input("Enter your password",type='password')


#create a register and login side bar to allow many people to register (username, password)
#then ask them to login checking if their credentials are correct.
#display their name after a succesful login