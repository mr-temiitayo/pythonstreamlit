#5 things kids can do on python with an example each


import streamlit as st

#1 Display texts on python

st.title("10 Things Kids Can Do On Python")

st.header("Submit Your Scores")

#2 Ask user text questions

name = st.text_input("Enter your name:")

#3 Ask user number questions

maths = st.number_input("Enter your maths score")

english = st.number_input("Enter your english score")

#4 Add variables together

total = maths + english

#5 create a button

if st.button("Check Total Score"):
    st.success(name,"you got",total,'in total')

