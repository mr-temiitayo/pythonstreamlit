#CLASSWORK WITH MENU
# A fashion app 
# -title
# -image
# -categories
# Men's Fashion

# Women's Fashion

# Children's Fashion

# (each category must havedifferent types of unique items and the prices like shirts(long sleeves,short, round neck, polo etc), boxers, trousers, shoes, bags etc)


#A menu is way to create separate pages and functionalites for the the same data app
#colors: blue, green, orange, red, violet.
import streamlit as st

st.set_page_config(layout='wide')

menu = st.sidebar.selectbox('Menu',['Fashion Store','About Me'])

if menu == 'Fashion Store':
    st.title(":orange[Welcome To Kyra's Fashion Store]")


if menu == 'About Me':
    st.title(':orange[This Is About My Fashion Store]')

