"""
-Add a restaurant picture
-Create a restaurant app that welcomes users and shows them the food selections
-If they choose/select their meals, show them the total amount
-Ask a question if you want to share the bill with others #use checkbox
-if yes, then ask how many people want to share the bill
-Then show the amount each person must contribute to pay the bill
"""

import streamlit as st
st.set_page_config(layout='wide')
bill = 0
st.title("Welcome to Pay N Eat Restaurant")
st.image("https://cdn.pixabay.com/photo/2017/09/23/12/40/catering-2778755_1280.jpg")

st.subheader("We have these meals available. Pick your choice")

st.title("Pasta")
#create 4 columns for pasta
pasta1,pasta2,pasta3,pasta4 = st.columns(4)

with pasta1:
    if st.checkbox("Spaghetti & Sauce: $30"):
        bill +=30
        st.success("Added to menu")

    if st.checkbox("Jollof & Chicken: $65"):
        bill +=65
        st.success("Added to menu")

with pasta2:
    if st.checkbox("Ofada rice & Sauce: $50"):
        bill += 50
        st.success("Added to menu")

