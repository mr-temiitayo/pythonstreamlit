import streamlit as st
#DATA COLLECTION
# This is when you have more than one data stored in a variable
#it has many options assigned to a variable


#A variable can only store one data at a time
name = 'Tofe'
score = 98

#QUESTION???
#what if i want to store my best friends? Many data in one variable??

# I need to use a data collection!!

#1 LIST [ ]
#a LIST is used to store multiple ITEMS inside one variable

bestfriends = ['Tofe','Bob','Fashek','Jeff','Bryan']
#All the names have been stored inside a list called bestfriends

st.write(bestfriends)

#examples of the use of list in streamlit


# Example 1: SELECTBOX
# when you want to create a selectbox with many items in it
#example: asking user to choose their best color
# the selectbox shows a small box with all the items inside it, click to show all other items, you can only select one item

bestcolor = st.selectbox('Select your best color',['Red','Blue','Orange','Pink'])
#Here we created a list for the selectbox, so that users can choose any color they like the most


#Example 2 
#when you want to create a menu with different pages
#you can also use a list to create a menu variable with the different pages/sections that users could choose from

menu = st.sidebar.selectbox("Navigation",['Africa Best Chef','Barbecue Nation','The House Of Food'])


#Example 3
# when you want to create a radio button to show many options for user to pick one
# A radio button shows all options at once and you can only click one
bestfood = st.radio('Select your best food',['Jollof Rice','Eba','Amala','Ofada'])
gender = st.radio("Select your gender",['Male','Female'])

#simple classwork
#what is a list?
#mention 2 uses of a list
# give an example of a list and display it on streamlit
#give 3 ways of using a list in streamlit and tell us the function of each method you use