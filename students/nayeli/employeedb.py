import streamlit as st

menu = st.sidebar.selectbox('Menu',['Register Here','Employee File','Database'])

if menu =='Register Here':
    st.subheader('Register your employee')
    gender = st.radio('Select Gender',['Male','Female'],horizontal=True)
    education = st.selectbox('Education Level',['College','University'])

    regdate = st.date_input("Registration date")


if menu == 'Employee File':
    st.subheader('Find an employee here')



if menu == 'Database':
    st.subheader('View all employee')