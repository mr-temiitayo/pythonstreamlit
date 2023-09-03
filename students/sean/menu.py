import streamlit as st

#about us furniture
#"C:\Users\USER\Downloads\about us furniture.png"
st.set_page_config(layout='wide')

menu = st.sidebar.selectbox('Menu',['Furnitures','About Us']) #name of menu, menu options to click

if menu == 'Furnitures':
    st.header(':orange[Welcome To The Furniture Store]')



if menu == 'About Us':
    st.header('This Is About Us')