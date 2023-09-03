# Create a restaurant webapp
# -Add a title
# -Add a restaurant picture
# -shows them the food selections
# -If they choose/select their meals, show them the total amount
# -Ask a question if you want to share the bill with others #use checkbox
# -if yes, then ask how many people want to share the bill
# -Then show the amount each person must contribute to pay the bill
#CONTRL/COMMAND / TO COMMENT A HIGHLIGHTED CODE

import streamlit as st

st.set_page_config(layout='wide')

bill = 0

st.title('Pay N Eat Restaurant')

st.image('https://cdn.pixabay.com/photo/2017/09/23/12/40/catering-2778755_1280.jpg')

st.header('Meals')
meal1,meal2,meal3, meal4 = st.columns(4)

with meal1:
    if st.checkbox('Spaghetti & Sauce: $5'):
        bill +=5
        st.success("Added to Menu")

with meal2:
    if st.checkbox('Potatoes & Chicken: $4'):
        bill +=4
        st.success("Added to Menu")