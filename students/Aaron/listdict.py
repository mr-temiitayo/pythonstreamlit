import streamlit as st
import pandas as pd

name = 'Jason' #you cant store more than one data in a variable


#list is a data collection used to display more than one item
numbers = [1,2,3,4,5,6,7]


colors = ['blue','orange','red']



random = ['shark',5,True,7.9]


pick = st.selectbox('Pick your best color',['blue','Orange', 'green']) #this is a dropdown box

gender = st.radio("Choose gender", ['Male','Female'],horizontal = True)


#dictionary is a data collection that uses a key and a data (variable and data)
#very useful if you have many attributes/categories of one variable

#classwork: create a data collection of ronaldo and tell us about his country, club, goals, assists


players = {'Name': ['Ronaldo','Messi'],'Country':['Portugal','Argentina'],'Club':['Madrid','Arsenal'],'Goals':[300,800],'Assists':[80,900]}

st.write(players)

cr7stats = pd.DataFrame(players)

st.table(cr7stats)


