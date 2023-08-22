import streamlit as st
import random

def reset():
    st.session_state.cpunumber = random.randint(0, 10)
    st.session_state.guess = 0

def main():
    st.title("Guess The Number Game")

    if 'reset_button' not in st.session_state:
        st.session_state.reset_button = False

    if st.session_state.reset_button:
        reset()
        st.session_state.reset_button = False

    name = st.text_input("Enter your game name")

    if 'guess' not in st.session_state:
        st.session_state.guess = 0

    if 'cpunumber' not in st.session_state:
        reset()

    guess = st.number_input("Guess my number from 1-10", 0, 10, value=st.session_state.guess)

    cpunumber = st.session_state.cpunumber

    st.write("Computer random number is:", cpunumber)

    if st.button("Click To Guess"):
        if guess == cpunumber:
            st.success(f'{name} your guess is correct')
        else:
            st.error('Your guess is incorrect')

    if st.button("Reset"):
        st.session_state.reset_button = True

if __name__ == "__main__":
    main()
