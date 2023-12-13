import streamlit as st
import pandas as pd


correctpassword = 'Nathan12345'

password = st.text_input("Enter the admin password",type='password')


if st.button('Login'):
    if password:
        if password == correctpassword:

            csvlink = pd.read_csv('scores.csv')

            st.dataframe(csvlink)
        else:
            st.write("The password is incorrect!")
    else:
        st.write('Enter password')