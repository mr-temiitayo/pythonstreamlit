'''
Create a menu for Registration and Database
Design a blood donation database that can get donor input
-Name -Contact Number (use text)
-Blood group (r selectbox) -Disease/Infection (use radio )

-Submit donor details

Next, save these in a csv file and show the database in a Database page in the menu
'''

import streamlit as st
import pandas as pd
csvfile = pd.read_csv("database.csv")
st.set_page_config(layout="wide")
menu = st.sidebar.selectbox("Menu",["Registration","Database"])




if menu == "Database":
    st.table(csvfile)


if menu == "Registration":
    st.subheader("Registration")
    colm1,colm2 = st.columns(2)
    colm3,colm4 = st.columns(2)
    with colm1: # donor name
        user_name = st.text_input("Insert name here")
    with colm2: # donor number
        user_con = st.text_input("Insert number here Ex:(123-456-7890)")
    with colm3: # options
        bloodtyp = st.selectbox("Select blood type",["A","A+","A++","B","B+",'B++'])
    with colm4: # button for result
        infection =  st.radio('Do you have any infection?',['Yes','No'],horizontal=True)
    btn = st.button("Submit Registration")
    if btn:
        st.write(user_name,"has donated blood type",bloodtyp,"There contact number is",user_con)
        blooddict = {"Name":[user_name],"Contact number":[user_con],"Blood group":[bloodtyp],'Infection':[infection]}
        bloodframe = pd.DataFrame(blooddict)
        bloodtable = pd.concat([csvfile,bloodframe],ignore_index=True)
        bloodtable.to_csv("database.csv",index=False)