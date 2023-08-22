import streamlit as st
import random

def reset():
    st.session_state.user_input = 0  # Reset user input to 0
    st.session_state.cpunumber = random.randint(0, 10)
    st.session_state.name = ""

def code():
    st.title("Guess My Number Game.")

    # Initialize session state variables if not present
    if 'cpunumber' not in st.session_state:
        reset()
    if 'user_input' not in st.session_state:
        st.session_state.user_input = 0
    if 'name' not in st.session_state:
        st.session_state.name = ''

    name = st.text_input("Enter your name",value = st.session_state.name)

    # Display the input field for entering a number
    st.session_state.user_input = st.text_input("Enter a number", value=st.session_state.user_input)

    if st.button("Click To Guess"):
        cpunumber = st.session_state.cpunumber
        user_input = int(st.session_state.user_input)
        if cpunumber == user_input:
            st.success(f'{name} you guessed correctly')
        else:
            st.error(f'{name} your guess is incorrect')

    if st.button("Reset"):
        reset()
        # Clear the user input field
        st.session_state.user_input = 0

    cpunumber = st.session_state.cpunumber
    rand = random.randint(0, 10)

    st.write("Computer random number is:", cpunumber)

code()
