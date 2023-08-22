import random
import streamlit as st
cpunumber = 2
def clear():
    st.session_state["userkey"] = 0

usernumber = st.number_input("type a number: ",value=0,format="%d",key="userkey")

if st.button("Click to guess:", on_click=clear):
    usernumber+=1
    st.write(usernumber)