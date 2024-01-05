import streamlit as st

st.title("TJC Church Form")

correctpassword = '12345Kyra'

password = st.text_input("Login with the church password",type='password')
if st.button("Login"):

    if password == correctpassword:
        col1,col2,col3 = st.columns(3)

        with col1:
            name = st.text_input('Enter your name here')

        with col2:
            age = st.selectbox('Select your age range',['1-12','13-19','20-34','35-64','65+'])


        with col3:
            gender = st.radio("Select your gender",['Male','Female'],horizontal=True)

        message = st.text_area("Leave us a message")

        if st.button('Submit'):
            st.write("Thanks")
    else:
        st.write('Sorry try again')


#homework: create a simple church form that has a name, age range and gender on 3 columns
#then a text area to ask for other additional message
#create a login feature to let them in if they enter the correct password