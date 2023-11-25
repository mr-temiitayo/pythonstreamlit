# -Create a restaurant app that welcomes users and shows them the food selections
# -Add a restaurant picture
# -If they choose/select their meals, show them the total amount
# -Ask a question if you want to share the bill with others
# -if yes, then ask how many people want to share the bill
# -Then show the amount each person must contribute to pay the bill

import streamlit as st

st.set_page_config(layout='wide') #this set your page to full width

st.title("Pay N Eat Restaurant")

st.image('https://cdn.pixabay.com/photo/2017/09/23/12/40/catering-2778755_1280.jpg')

st.subheader("Food Menu")

food1,food2,food3,food4 = st.columns(4) #this creates 4 columns for the food section

with food1:
    if st.checkbox("Rice & Chicken: $15"):
        st.success("Added to Menu")

    
with food2:
    if st.checkbox("Spaghetti & Sauce: $10"):
        st.success("Added to Menu")

with food3:
    if st.checkbox("Suspicious Stew: $5"):
        st.success("Added to Menu")

with food4:
    if st.checkbox("Fish & Chips: $10"):
        st.success("Added to Menu")