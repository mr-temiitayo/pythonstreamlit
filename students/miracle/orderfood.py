import streamlit as st

st.header("Food Order App")

st.image('https://cdn.pixabay.com/photo/2023/09/05/12/44/mug-8235059_1280.jpg')

#categories: Food, Drinks, Fruits,

st.subheader("Food Category")

col1, col2, col3 = st.columns(3) #create columns to place your items inside

with col1:
    if st.checkbox("Rice and Chicken: #7,000"):
        st.write("OK Done")
    
    if st.checkbox("Porridge Yam: #3,000"):
        st.write("OK Done")


with col2:
    if st.checkbox('Beans and Yam:#8,000'):
        st.write('ok Done')

    if st.checkbox("pounded yam:#5,000"):
        st.write("ok Done")

with col3:
    if st.checkbox("Jollof rice:#10,000"):
       st.write("ok Done")

    if st.checkbox("Fried rice:#12,000"):
        st.write("ok Done")



st.subheader('Drinks Category')

col4, col5,col6 = st.columns(3)

with col4:
    if st.checkbox('fanta:#1,000'):
        st.write("ok Done")

    if st.checkbox("sprite:#1,000"):
        st.write("ok Done")


with col5:
    if st.checkbox("coke:#2,000"):
        st.write("ok Done")

    if st.checkbox('american cola:#2,000'):
       st.write("ok Done")

with col6:
     if st.checkbox("pepsi:#1,000"):
        st.write('ok Done')

     if st.checkbox("mirinda:#1,000"):
        st.write("ok Done")

st.subheader("fruit category")
col7, col8, col9 =st.columns(3)

with col7:
    if st.checkbox("apple:#1,000"):
        st.write("ok Done")

    if st.checkbox("water melon:#3,000"):
        st.write('ok Done')

with col8:
    if st.checkbox('orange:#2,000'):
        st.write('ok Done')

    if st.checkbox("pine apple:#4,000"):
        st.write('ok Done')

with col9:
    if st.checkbox("grapes:#3,000"):
        st.write("ok Done")

    if st.checkbox("carrot:#2,000"):
        st.write("ok Done")












if st.button("Calculate bill"):
    st.write("Thank You!")