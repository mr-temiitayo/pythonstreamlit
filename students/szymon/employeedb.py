import streamlit as st

st.set_page_config(layout='wide')

gender = st.radio('Gender',['Male','Female'],horizontal=True)

joblevel = st.selectbox('Job Level',['Beginner','Deeper In','Average','Expert'])

regdate = st.date_input("Enter registration date")