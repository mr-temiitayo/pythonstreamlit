import streamlit as st
#sessionstate in streamlit keeps track of your variables everywhere for a particular session
#callback function is 

# number = 5

# st.write(number)

# if st.button("Add 1"):
#     number +=1
#     st.write(number)


#classwork: create a simple app that asks users to enter a number then you can add 10 to their number


if 'number' not in st.session_state:
    st.session_state.number = 0


number = st.number_input('Enter a number',0,key='number')

if st.button("Add 10"):
    st.session_state +=10
    st.write(st.session_state.number)