import streamlit as st
from datetime import datetime
import pandas as pd
today = datetime.today()
today_date = today.strftime("%d-%b-%Y")
#st.subheader("Savings App")

menu = st.sidebar.selectbox('Menu',['Summary','Add Money','Withdraw'])
space = ''
df = pd.read_csv('savings.csv')
if menu == 'Add Money':
    b1,b2,b3 = st.sidebar.columns(3)
    with b2:
        st.sidebar.write("**Enter savings**")    
    with b3:
        save = st.sidebar.text_input('save',label_visibility='collapsed')
        if st.sidebar.button('Save'):
            pass


    a1,a2,a3,a4=st.columns(4)
    with a2:
        st.header('**#45,000,000**')
    space


    space
   
    # st.subheader("**Savings History**")
    # c1,c2,c3,c4=st.columns(4)
    # with c2:
    #     st.write(today_date)
    # with c3:
    #     st.write('**#20,000**')