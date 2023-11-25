import streamlit as st
#sessionstate in streamlit keeps track of your variables everywhere for a particular user's session

# number = 5
# st.write(number)
# if st.button('Add 1'):
#     number +=1

# st.write(number)

st.write(st.session_state)
if 'number' not in st.session_state:
    st.session_state.number = 5

st.write(st.session_state.number)
if st.button('Add 1'):
    st.session_state.number +=1
    st.write(st.session_state.number )

if st.button('Remove 1'):
    st.session_state.number -=1
    st.write(st.session_state.number )