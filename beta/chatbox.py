import streamlit as st

#Create a storage for chat history

if "Messages" not in st.session_state:
    st.session_state.messages = []


prompt = st.chat_input("Ask Something")

if prompt:
    with st.chat_message("user"):
        st.write(prompt)
    
    with st.chat_message("assistant"):
        st.write(prompt)

#custom
    # with st.chat_message("bot",avatar="😎"):
        # st.write(prompt)