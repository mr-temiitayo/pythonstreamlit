import streamlit as st
import random


if 'cpunumber' not in st.session_state:
    st.session_state.cpunumber = random.randint(1,10)

if 'userguess' not in st.session_state:
    st.session_state.userguess = 0

userguess = st.number_input("Enter guess",key='userguess')

guess = st.button('Guess',on_click=check)
restart = st.button('restart',on_click=restart)

def check():
    if st.session_state.cpunumber == st.session_state.userguess:
        st.write('correct')
    else:
        st.write('wrong')

def restart():
    st.session_state.cpunumber = random.randint(1,10)



st.write(st.session_state.cpunumber)

