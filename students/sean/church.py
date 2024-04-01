"""
#create a simple church age range database
#This will get the name, age, gender of the church memeber
#save this in a database and display on a new page (this page MUST have a register feature)
#Make sure you group members in differnt category based on their age
# (Kids(3- 12), Teens(13-19), Youth(20-35), Adult(36-64), Elders(65+) )
save all information in a csv file
"""
import streamlit as st
import pandas as pd

st.set_page_config(layout = "wide")

choice = st.sidebar.selectbox("menu",["Register Member",'Members Database'])
readcsv = ("church.csv")


if choice == "Register Member":
  name = st.text_input("Enter your name: ")
  age = st.number_input("Enter your age: ",1)
  gender = st.radio("Enter your gender: ",['Male','Female'],horizontal=True)

  if st.button("register"):
     if age > 2 and age < 13:
      klass = 'Kids'
      st.success("You have registered. You are part of the Kids")
     if age > 12 and age < 20:
      klass = 'Teens'
      st.success("You have registered. You are part of the Teens")
     if age > 19 and age < 36:
      klass = 'Youths'
      st.success("You have registered. You are part of the Youths")
     if age > 35 and age < 66:
      klass = 'Adults'
      st.success("You have registered. You are part of the Adults")
     if age > 65:
      klass = 'Elders'
      st.success("You have registered. You are part of the Elders")
      
      membersdict = {'Name':[name],'Age':[age],'Gender':[gender],'Class':[klass]}
      memberstable = pd.DataFrame(membersdict)
      newtable = pd.concat([readcsv,memberstable],ignore_index=True)
      newtable.to_csv('church.csv')


if choice == 'Member Database':
 st.table(readcsv)

