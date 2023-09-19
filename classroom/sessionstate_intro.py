import streamlit as st


# number = 5

# if st.button('Add 1'):
#     number +=1

# st.write(number) 


if 'number' not in st.session_state:
    st.session_state.number = 5

st.write(st.session_state)
st.write(st.session_state.number)

def change():
    st.session_state.number +=1

if st.button('Add 1',on_click=change):
    pass
