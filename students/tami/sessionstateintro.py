#sessionstate in streamlit helps to store, updtae and keep track of your variables in a sessionstate dictionary
#callback function is used to code python to start a function first before reading the other code
import streamlit as st

# number = 5 #all variables refresh. back again to refresh var to 5

# st.write(number)

# if st.button('Add 1'):
#     number +=1

# st.write(number) #is adds 1= 6


# st.write(st.session_state)

if 'number' not in st.session_state:
    st.session_state.number = 0

number = st.number_input('Enter your number:',key = 'number')

st.write(st.session_state.number) #6


def add(): #call back function
    st.session_state.number +=1

if st.button('Add 1',on_click=add):
    pass


def subtract():
    st.session_state.number -=1


if st.button('Subtract 1',on_click=subtract):
    pass


