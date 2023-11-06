import streamlit as st

#DATA COLLECTION

#This is when you have more than one data store in a variable

#VARIABLE
#A variable can only store one data at a time

name = 'Nathan'
score = 100

#QUESTION???
#What if i wnat to store my best friends?
#I want to store many names/data in one variable?

#I need to use a data collection

#1 LIST []
#a LIST is used to store multiple ITEMS inside one variable

bestfriends = ['Johny','Damian','Ethan','Omar']

st.write(bestfriends)

#examples of the use of list in streamlit

#EXAMPLE 1: SELECTBOX
#when you want to create a selectbox with many items in it
#example: let us ask a user to choose their best color

bestcolor = st.selectbox("Select your best color",['Red','Orange','Blue','Pink'])

st.write(bestcolor)

#EXAMPLE 2: SIDEBAR MENU
#when you want to create a menu with different pages/sections

menu = st.sidebar.selectbox('Menu',['Home','About Us'])


#EXAMPLE 3: RADIO BUTTON
#when you want to create a radio button to show many options for the user to pick one

gender = st.radio('Select your gender',['Male','Female'])


#classwork
#1 what is a list?
#2 mention 2 uses of a list
#3 give an example of a list and display it on streamlit
#4 give 3 ways of using a list in streamlit and tell us the function of each method you use