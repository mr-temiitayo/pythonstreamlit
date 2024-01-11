import streamlit as st
import pandas as pd #pandas helps to convert a dictionary to a table. also read/write csv files

#A dictionary allows you sto store multiple variables and data

#A list can only have data/single/independent items
studentslist = ['Aisha',100,80,90,75]


#A dictionary can have variables attached to the data/items
students = {'Name':['Faisal','Jason','Aisha'],'Science':[100,85,90],'Arabic':[75,96,80],'Computer':[86,89,86]}

cars = {'Name':'Benz','Year':2022,'Country':'Germany'}

st.write(students)
st.write(cars)


students_table = pd.DataFrame(students)

st.table(students_table)