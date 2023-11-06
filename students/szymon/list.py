import streamlit as st

#DATA COLLECTION
#This is when you have more than one data stored in a variable

#A variable can only store one data at a time
name = 'Szymon'
score = 98

#QUESTION???
#What if I want to store my best friends? Many data in one variable??

#I need to use a data collection

#1 LIST []
#A list is used to store multiple ITEMS inside one variable

bestfriends = ['Tofe','Jack','Adam','Leo']

st.write(bestfriends)

#examples of the use of list in streamlit

#Example 1: SELECTBOX
#when you want to create a selectbox with many itmes in it
#example: asking the user to choose their best color
#the selectbox shows a small box with all the items inside it, click to show all other items
#you can only select one item

bestcolor = st.selectbox("Select your best color",['Red','Blue','Green','Orange','Pink'])
#here is a list of colors we created for the selectbox, the user can choose any color they like the most

#Example 2: SELECTBOX IN MENU
#when you want to create a menu with different pages/sections
menu = st.sidebar.selectbox("Menu",['Home','About'])


#Example 3: RADIO
#when you want to create a radio button to show many options for user to pick one
gender = st.radio('Select your gender',['Male','Female'])

game = st.radio('Select your game',['Minecraft','Roblox'],horizontal=True)


# classwork:
# create a list.py file
# -tell us what a list is in python
# -create an example of a list and display it in python
# -give 3 examples of how to use a list in streamlit