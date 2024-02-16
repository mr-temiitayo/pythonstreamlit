import streamlit as st
import pandas as pd

datafile = pd.read_csv('nameage.csv')
menu = st.sidebar.selectbox("Menu", ['Enter Data', 'Database'])

if menu == 'Enter Data':
    name = st.text_input("Enter student name")
    age = st.number_input("Enter student age",3,20)

    if st.button("Submit student data"):
        datadict = {'Name':[name],'Age':[age]}
        dataDF = pd.DataFrame(datadict)
        combinedata = pd.concat([datafile,dataDF],ignore_index=True)
        combinedata.to_csv('nameage.csv',index = False)
        st.success("Information Submitted")


if menu == 'Database':
    st.table(datafile)

