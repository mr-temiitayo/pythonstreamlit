#moyo homework, add grades in the last column using the average A+, B...F
import streamlit as st

st.set_page_config(layout='wide') #this makes your page full width

st.title('Welcome to Pay N Eat Restaurant')

st.image('https://cdn.pixabay.com/photo/2017/09/23/12/40/catering-2778755_1280.jpg')

st.subheader('We have these food menu. Click to pick your choice')

cost = 0

st.title("Local Meals")

#create 4 columns for Local Meals
meal1,meal2,meal3,meal4 = st.columns(4)

with meal1:
    if st.checkbox('Jollof rice & Chicken: $15'):
        cost += 15
        st.success("Added to your menu")
    
    if st.checkbox("Pounded yam & Ogbono soup: $20"):
        cost +=20
        st.success("Added to your menu")

with meal2:
    pass


st.title("Drinks")
drink1,drink2,drink3,drink4 = st.columns(4)
with drink1:
    pass