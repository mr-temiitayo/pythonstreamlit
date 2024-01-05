import streamlit as st
import pandas as pd

database = pd.read_csv('dataframe.csv')
st.dataframe(database)

name = st.text_input("Enter your name")

gender = st.radio("Enter your best sport",['Male','Female'],horizontal=True)

game = st.selectbox('Enter your best game',['Roblox','Minecraft','Basketball','Football','Swimming','Tennis'])

if st.button('Submit'):
    st.subheader(f'Name: {name}, Gender: {gender}, Game: {game}')
    dict= {'Name':[name],'Gender':[gender],'Game':[game]}
    st.write(dict)
    dataframe = pd.DataFrame(dict)

