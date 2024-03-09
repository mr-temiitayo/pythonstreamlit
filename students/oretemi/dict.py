import streamlit as st
import pandas as pd

#dictionary is very useful when you have different categories of items/data to save

#classwork: talk about ronaldo, country, club, goals score, assist made

player = ['ronaldo', 'portugal', 'Al Nassr', 300, 78]

st.write(player)


playerdict = {'Name':['Ronaldo','Messi'],'Country': ['Portugal','Argentina'],'Goals':[300,400],'Assists':[85,70]}

st.write(playerdict)

playertable = pd.DataFrame(playerdict)

st.table(playertable)



#Homework: create 2 examples of list and dictionary and display them on streamlit