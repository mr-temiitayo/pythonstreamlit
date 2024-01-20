import streamlit as st

name = 'Nadiv'

score = 90

#QUESTION??
#What if I want to store my favorite colors? I want many data stored in one variable

#I need a data collection

#Types of data collection
#-List -Dictionary


colors = ['Blue','Yellow','Green','Red']

st.write(colors)

#Examples of how to use it in streamlit

#Example 1: SELECTBOX
#When you want to create a selectbox to show the user multiple options to select one from 

#example: Ask the user to choose their best color using a selectbox

bestcolor = st.selectbox('Choose your best color',['Orange','Red','Purple','Grey'])

st.write(bestcolor)

oldcolor = st.selectbox("Choose one of the old colors",colors)
st.write(oldcolor)


#Example 2: SELECTBOX IN MENU
#When you want to create a menu with different pages/categories

menu = st.sidebar.selectbox('Menu',['Home','Contact'])


#Example 3: RADIO

#When you want to create a radio button to show few options for the user to pick/select one from

gender = st.radio("Select your gender",['Male','Female'])
st.write('You are a',gender)

#classwork: create a list.py
#create 