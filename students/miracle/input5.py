import streamlit as st
name =st.text_input("please enter your name")
red_marbles =st.number_input('please enter number of red marbles')
blue_marbles =st.number_input("please enter number of blue marbles")
green_marbles =st.number_input("please enter number of green marbles")
total_marbles =red_marbles + blue_marbles + green_marbles
st.write('Hi', name, 'you have collected a total of',total_marbles, 'marbles')

