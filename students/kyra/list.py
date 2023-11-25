import streamlit as st

#DATA COLLECTION

#This is when you have more than one data stored in a variable

name = 'kyra'

score = 95

#QUESTION??
#What if i want to store my best friends?
# I want to store multiple names/data in one variable?

#I need to use a DATA COLLECTION!!

#LIST []
#A LIST is used to store multiple ITEMS inside one variable

bestfriends = ['Kyra','Nathan','Mio','Alana','Jason']

st.write(bestfriends)

#examples of the use of list in streamlit

#EXAMPLE 1: SELECTBOX

#when you want to create a selectbox with many items in it
#example: let us ask a user to choose their best color

bestcolor = st.selectbox("Select your best color",['Red','Orange','Blue','Yellow'])

st.write("I chose",bestcolor)

#EXAMPLE 2: SIDEBAR MENU
#when you want to create a menu with different sections/pages

menu = st.sidebar.selectbox("Menu items",['Home','About','Teachers'])

#EXAMPLE 3: RADIO BUTTON
#when you want to create a radio button to show many options for the user to pick one

gender = st.radio('Select your gender',['Male','Female'])

#classwork
# -what is a list in python?
# -create 3 examples of a list
# -display all items in the 3 lists
# -display only the first item in the 3 lists


#A list is used to store multiple data in one variable

games = ['FIFA23','Roblox','Minecraft','Basketball']
st.write(games)
st.write(games[0])