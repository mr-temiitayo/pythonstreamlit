import streamlit as st #this is the framework to build the page for your program

#Task: create an age calculator and build a web page for your program

#to run, open your terminal and type: streamlit run nameofproject

st.title("Welcome to my age calculator")

name = st.text_input("Enter your name")

currentyear = st.number_input('Enter your current year',2023)

yob = st.number_input("Enter your year of birth",1950,2023)

age = currentyear - yob


checkage = st.button("Check my age")

if checkage:
    st.write(name,'you will be',age,'in',currentyear)

s = [1,2,3,4]

s.