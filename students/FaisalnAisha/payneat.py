# -Add title==
#Add a restaurant picture==
# -shows them the food selections
# -After they choose/select their meals, show them the total amount
# -Ask a question if you want to share the bill with others #use checkbox
# -if yes, then ask how many people want to share the bill
# -Then show the amount each person must contribute to pay the bill

#meals, drinks, fruits, snacks
import streamlit as st

st.set_page_config(layout='wide')

st.title("Pay N Eat Restaurant")

st.image("https://cdn.pixabay.com/photo/2018/02/26/18/55/coffee-3183752_1280.jpg")

st.subheader("Meals")

meal1, meal2, meal3, meal4 = st.columns(4)


with meal1:
    if st.checkbox('Rice & Chicken: $12'):
        st.success("Added to Menu")

with meal2:
    if st.checkbox("Spag & Sauce: $10"):
        st.success("Added to Menu")


with meal3:
    if st.checkbox("Ofada rice & Sauce: $8"):
        st.success("Added to Menu")