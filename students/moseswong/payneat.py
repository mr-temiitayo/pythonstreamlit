# Create a restaurant webapp
# -Add a title
# -Add a restaurant picture
# -show them the food selections
# -If they choose/select their meals, show them the total amount
# -Ask a question if you want to share the bill with others #use checkbox
# -if yes, then ask how many people want to share the bill
# -Then show the amount each person must contribute to pay the bill
#CONTRL/COMMAND / TO COMMENT A HIGHLIGHTED CODE

import streamlit as st

st.title("Moses Steak House")

st.image("https://d1csarkz8obe9u.cloudfront.net/posterpreviews/food-banner-design-template-543a83cbc11bf6bb9a048c606064e766_screen.jpg?ts=1561514352")

st.subheader("Meals Category")

bill = 0
meal1,meal2,meal3 = st.columns(3)

with meal1:
    if st.checkbox("Rice & Chicken: $15"):
        bill+=15
        st.success('Added to Menu')

with meal2:
    if st.checkbox('Pasta & Sauce: $10'):
        bill +=10
        st.success("Added to Menu")

with meal3:
    if st.checkbox("Chicken & Chips: $15"):
        bill +=15
        st.success('Added to Menu')

if st.button("Check Total Bill"):
    st.write("Your total bill is:",bill,'dollars')