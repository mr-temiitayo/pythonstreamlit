# -Add a restaurant picture
# -Create a restaurant app that shows the food selections
# -If they choose/select their meals, show them the total amount
# -Ask a question if you want to share the bill with others #use checkbox
# -if yes, then ask how many people want to share the bill
# -Then show the amount each person must contribute to pay the bill
#create a sidebar menu, full width page


import streamlit as st
st.set_page_config(layout='wide') #this sets your page to full width

bill = 0
st.title("Pay N Eat Restaurant")
st.image("https://cdn.pixabay.com/photo/2017/09/23/12/40/catering-2778755_1280.jpg")


menu = st.sidebar.selectbox('Menu',['Food Menu','About Us'])


if menu == 'Food Menu':
    st.subheader('Meal')
    m1,m2,m3,m4 = st.columns(4) #creating 4 columns

    with m1:
        if st.checkbox('Ofada Rice & Sauce: #5,000'):
            bill+=5000
            st.success("Added to Menu")
    with m2:
        if st.checkbox('Pasta & Sauce: #4,500'):
            bill +=4500
            st.success("Added to Menu")