
import streamlit as st


st.title("TJC Church Form")
correctpassword = ("12345")
password = st.text_input("Login with the church password",type = 'password')
if st.button("Login"):
    if password == correctpassword:
        col1,col2,col3 = st.columns(3)


        with col1:
            name = st.text_input("What is your name?")
       
        with col2:
            age = st.selectbox("Select your age range",['1-12','13-19','20-34','35-64','65+'])


        with col3:
            gender = st.radio("Select your gender:",['Male','Female'],horizontal =True)


        message = st.text_area("Leave us a message:")


        if st.button("Submit"):
            st.write("Thanks")

