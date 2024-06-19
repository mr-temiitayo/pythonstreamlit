import streamlit as st

#variable is used to store data
#input is to let the user type in something
#text is any character
#number is only numbers
name = st.text_input("Please enter your name")

yob = st.number_input('Please enter your year of birth',1940,2024)

curryear = st.number_input('Please enter your current year',2024,2050)

age = curryear - yob 

st.write(name,"is",age)


