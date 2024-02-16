""""
-title
-image
-categories
Men's Fashion

Women's Fashion

Children's Fashion

(each category must havedifferent types of unique items and the prices 
like shirts(long sleeves,short, round nexk, polo etc), boxers, trousers, shoes, bags etc)

Show the total bill
"""  

import streamlit as st

st.set_page_config(layout='wide')

menu = st.sidebar.selectbox('Menu',['Men Category', 'Women Category', 'Children Category'])

if menu == 'Men Category':
    st.subheader("Welcome To Men's Category")








if menu == 'Women Category':
    st.subheader("Welcome To Women's Category")







if menu == 'Children Category':
    st.subheader("Welcome To Children's Category")






