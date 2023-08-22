print("Here is a github tutorial of Streamlit")

import streamlit as st

st.write("This is my github pandas dataframe work")
import pandas as pd

# Display data as a dataframe dynamic, can sort, scroll
df = pd.read_csv(r'C:/Users/USER\Desktop/PythonVSCODE/names.csv')
#st.dataframe(df,200,300) #width,height

#static table, cant clict, sort or move
st.table(df)

#adding colors from pandas
st.dataframe(df.style.highlight_max(axis=0)) #highlights max cells values

#display code as a codebox
mycode = """
def sayhello():
    print("Hello Streamlit Lovers)
"""
st.code(mycode, language='python')

