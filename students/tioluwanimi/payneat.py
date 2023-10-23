"""
-Add a restaurant picture
-Create a restaurant app that shows users the food selections
-After they choose/select their meals, show them the total amount
-Ask a question if you want to share the bill with others #use checkbox
-if yes, then ask how many people want to share the bill
-Then show the amount each person must contribute to pay the bill
"""

import streamlit as st
st.set_page_config(layout='wide') #this makes your page full width

bill = 0
st.header("Pay N Eat Food Menu")

st.subheader("Meals Selection")

meal1,meal2,meal3,meal4 = st.columns(4) #creating 4 columns for meal category

with meal1:
    st.image("https://cdn.pixabay.com/photo/2014/11/05/15/57/salmon-518032_1280.jpg")
    if st.checkbox('Pasta & Salad: $12'):
        bill+=12
        st.write('Added')