#HOW TO CREATE AND USE MENU
# A fashion app 
# -title
# -image
# -categories
# Men's Fashion

# Women's Fashion

# Children's Fashion

# (each category must havedifferent types of unique items and the prices 
# like shirts(long sleeves,short, round neck, polo etc), boxers, trousers, shoes, bags etc)

import streamlit as st

menu = st.sidebar.selectbox('Fashion Menu', ['Fashion Store', 'About Us'])

if menu == 'Fashion Store':
    st.header("Welcome to the Fashion Store")

if menu == 'About Us':
    st.header('This is About us')