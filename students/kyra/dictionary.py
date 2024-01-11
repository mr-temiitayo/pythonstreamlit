import streamlit as st
import pandas as pd #pandas helps us to convert a dictionary to a table

#A dictionary allows you to store multiple variables and data

students = {'Name':['Kyra','Erin'],'English':[90,76],'Maths':[86,82],'Science':[95,65]}


st.write(students)

table = pd.DataFrame(students) #convert/change dictionary to a table. import pandas as pd

st.dataframe(table) #tells streamlit to view this as a table

#classwork
#create one dictionary of 3 movies in 2023. Give categories of their Name, Producer, Main Character, Rating
#convert this to a table and display