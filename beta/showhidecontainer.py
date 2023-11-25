import streamlit as st

st.title("container check")

if 'show' not in st.session_state:
    st.session_state.show = True

def hide():
    st.session_state.show = False

container = st.container()

if st.session_state.show == True:
    with container:
        st.write("here we go")
        name = st.text_input('write name here')
        if st.button('Hide',on_click=hide):
            pass