import streamlit as st

# number = 5
# st.write(number)

# if st.button("Add 1"):
#     number +=1

# st.write(number)


#session state is a memory (dict) in streamlit to create, update and keep variables for the session




if 'num' not in st.session_state:
    st.session_state.num = 5



if st.button("Add 1"):
    st.session_state.num +=1
    st.write(st.session_state.num)