# Creating students scores database
# -Get info of each student (name, 4 subjects score)
# -Calculate the average of total score of each student
# -Grade the student with (A,B,C,D,E,F) -----
# -Save all data in a csv file
# -Show current csv database file

import streamlit as st

st.title('Students Database')

name = st.text_input('Enter your name')
maths = st.number_input('Enter Maths score')
science = st.number_input('Enter Science score')
history = st.number_input('Enter History score')