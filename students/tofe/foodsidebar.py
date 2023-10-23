import streamlit as st
st.set_page_config(layout='wide')
#meal, drinks, snacks, fruits
# f-string is used to place everything in a string 
# but you have to indicate variables by placing them in a curly brackets {}
#title, header,subheader,success, info, error, warning does not allow ,

bill = 0

menu = st.sidebar.subheader('Food Ordered')


meal1, meal2, meal3, meal4 = st.columns(4)

with meal1:
    st.image('https://cdn.pixabay.com/photo/2018/04/13/17/14/vegetable-skewer-3317060_1280.jpg')
    if st.checkbox('Vegetable Skewer: $15'):
        st.sidebar.image('https://cdn.pixabay.com/photo/2018/04/13/17/14/vegetable-skewer-3317060_1280.jpg',width=100)
        bill += 15



if st.button('Check My Bill'):
    st.sidebar.success(f'Total Bill is: ${bill}')    