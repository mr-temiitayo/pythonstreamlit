import streamlit as st

name = 'Temi' #this variable can only store one data at a time

#we can create a list to store multiple items/data in just one variable
bestfriends = ['Ore','Ebun','Jason','Jane']

# st.write(bestfriends)

#using lists in streamlit

# 1 SELECTBOX: Create dropdown options

#create a dropdown for users to pick a color
colors = ['blue','orange','yellow', 'green']

colors[1] = 'grey'
colors.append('red')
st.write(colors)

pickcolor = st.selectbox("Pick a color",['blue','orange','yellow', 'green'])


# 2 RADIO: Create options users can from 

gender = st.radio("Select your gender",['Male','Female'])


#3 SIDEBAR SELECTBOX: Create separate sections in a page

menu = st.sidebar.selectbox('Menu',['Home','Contact','About'])