import streamlit as st
import pandas as pd

#A list is used to store/save multiple items in one variable

studentlist = ['moyo','kyra','nadiv','szymon']

st.write(studentlist)

#A dictionary is very useful when you want to show/indicate different 
# key/variables/attributes/categories to save/store your items with

studentslist = ['moyo',75,82,90]

st.write(studentslist)

#what if i have more students to save in each category?
studentsgrade = {'Name':['moyo','kyra'],'Science':[75,82],'Maths':[82,75],'English':[90,83]}

st.write(studentsgrade)

table = pd.DataFrame(studentsgrade)

# st.dataframe(table,use_container_width=True)

st.table(table)


#classwork

# create only one dictionary of 3 football players, 
# stating they number of games played, goals scored, assist made, red cards and yellow cards
# convert this into dataframe and display it