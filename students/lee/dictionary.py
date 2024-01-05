import streamlit as st
import pandas as pd

#A dictionary can store many variables and data inside

students_grades = {'Name':['Nathan','Mio'],'English':[95,90],'Maths':[90,85],'Science':[89,92]}


st.write(students_grades)

students_df = pd.DataFrame(students_grades)

st.dataframe(students_df)