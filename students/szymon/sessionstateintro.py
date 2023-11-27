import streamlit as st

# number = 5
# st.write(number)

# if st.button("Add 1"):
#     number +=1

# st.write(number)


#session state is a memory (dict) in streamlit to create, update and keep variables for the session



if 'number' not in st.session_state:
    st.session_state.number = 5

st.write(st.session_state)
st.write(st.session_state.number)

if st.button("Add 1"):
    st.session_state.number +=1


if st.button('Subtract 1'):
    st.session_state.number -=1
