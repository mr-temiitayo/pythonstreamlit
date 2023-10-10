# 1 chicken is sold for 5 dollars
# create a chicken app to ask users how many chicken they want to get
# show them the total amount

import streamlit as st

chickenprice = 5

st.write("1 Chicken cost 5 dollars")

userchicken = st.number_input('How many chicken do you want to get')

totalchickenprice = chickenprice * userchicken

if st.button('Check Chicken Price'):
    st.write("The price for",userchicken,"chickens is",totalchickenprice,'dollars')
