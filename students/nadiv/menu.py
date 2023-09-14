#classwork
# create different haircut/ hairdo categories with prices only to show on the men salon page
# the create the about us page to make
import streamlit as st

st.set_page_config(layout='wide')

menu = st.sidebar.selectbox('Menu',['Men Salon','About Us'])

st.image("image adress",width= 150)

if menu == 'Men Salon':
    st.header("Welcome To Our Salon")









if menu == 'About Us':
    st.header('Our About Us Page')




