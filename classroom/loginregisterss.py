import streamlit as st

menu = st.sidebar.selectbox('menu',['Register','Login'])

if 'showregister' not in st.session_state:
    st.session_state.showregister = True

if 'username' not in st.session_state:
    st.session_state.username = ''

if 'password' not in st.session_state:
    st.session_state.password = ''

if 'passwordcheck' not in st.session_state:
    st.session_state.passwordcheck = ''


def hideregister():
    if username and password and passwordcheck:
        if password == passwordcheck:
            st.session_state.showregister = False

if menu == 'Register':
    userdetails = st.sidebar.container()
    if st.session_state.showregister == True:
        with userdetails:
            username = st.sidebar.text_input('Enter your username',key='username')
            password = st.sidebar.text_input("Enter your password",type='password',key='password')
            passwordcheck = st.sidebar.text_input("Enter your password again",type='password',key='passwordcheck')
            submit = st.sidebar.button('Register',on_click=hideregister)

    if st.session_state.showregister == False:
        if st.session_state.username and st.session_state.password and st.session_state.passwordcheck:
            if st.session_state.password == st.session_state.passwordcheck:
                
                st.title('Hello you are registered')
                
            else:
                st.sidebar.error("Password do not match")

        else:
            st.sidebar.error("Kindly Fill In All Boxes")

if menu == 'Login':
        st.session_state.showregister = True
        loginusername = st.sidebar.text_input('Enter your username',value='')
        loginpassword = st.sidebar.text_input("Enter your password",type='password',value='')
        submit = st.sidebar.button('Login')

        if submit:
            if loginusername and loginpassword:
                if loginusername == username and loginpassword == password:
                    # userdetails.empty()
                    st.title('Hello you are logged in')
                    
                else:
                    st.sidebar.error("Password do not match")

            else:
                st.sidebar.error("Kindly Fill In All Boxes")
