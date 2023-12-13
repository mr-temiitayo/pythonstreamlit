import streamlit as st

name = 'Faisal' #string

score = 90 #int

#QUESTION??
#what is I want to store my best friends? I want to many/multiple data stored in one variable?

#I need a data collection
#DATA COLLECTION
#This is when you have more than one data stored in a variable
# -List -Tuple -Dictionary -Set

bestfriends = ['Blue','Yellow','Red']

st.write(bestfriends)

st.write(bestfriends[0]) #index position. First item position is 0 not 1

# Examples of the use of list in streamlit

#Exampe 1: SELECTBOX
# when you want to create a selectbox to show the user multiple options to select one from
#example: Ask the user to choose their best color using a selectbox

bestcolor = st.selectbox("Select your best color",['Red','Blue','Yellow'])
st.write("You selected",bestcolor)

#Example 2: SELECTBOX IN MENU
#When you want to create a menu with different pages/categories

menu = st.sidebar.selectbox("Menu",['Home','About','Find Us'])

#Example 3: RADIO

#when you want to create a radion button to show few options for the user to pick/select one

gender = st.radio("Select your gender",['Male','Female'],horizontal=True)

st.write("You are a",gender)

