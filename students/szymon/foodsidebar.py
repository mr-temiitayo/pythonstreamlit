import streamlit as st

st.set_page_config(layout='wide')

st.subheader("Food & Drinks Restaurant")
#4 meal, 4 drinks, 4 fruits
bill = 0
menu = st.sidebar.subheader("Food Ordered")
side1,side2= st.sidebar.columns(2)


meal1,meal2,meal3,meal4 = st.columns(4)

with meal1:
    st.image('https://cdn.pixabay.com/photo/2015/04/08/13/13/food-712665_1280.jpg')
    if st.checkbox('Fried rice & Chicken: $10'):
        bill +=10
        with side1:
            st.image('https://cdn.pixabay.com/photo/2015/04/08/13/13/food-712665_1280.jpg')