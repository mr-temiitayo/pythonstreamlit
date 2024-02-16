#create a fashion page for men, women and children categories (use columns here)
#use a menu to separate the categories


import streamlit as st
st.set_page_config(layout='wide')

menu = st.sidebar.selectbox('Fashion Menu',['Men Category','Women Category','Chidren Category'])

if menu == 'Men Category':
    st.title("Men Fashion Category")

    men1,men2,men3,men4 = st.columns(4)

    with men1:
        st.image("https://m.media-amazon.com/images/I/616R16Ga0oL._AC_UL320_.jpg")
        if st.checkbox("Men Suit: $500"):
            st.success("Added to Menu")

    with men2:
        st.image("https://m.media-amazon.com/images/I/51crUk19QRL._AC_UL320_.jpg")
        if st.checkbox("Men Tracksuit: #350"):
            st.success("Added to Menu")

    with men3:
        st.image("https://m.media-amazon.com/images/I/71s1Di2E0qL._AC_UL320_.jpg")
        if st.checkbox("Men shirt & pants: $200"):
            st.success("Added to Menu")

    with men4:
        st.image("https://m.media-amazon.com/images/I/71KI2MZQLeS._AC_UL320_.jpg")
        if st.checkbox("Men Jeans: $50"):
            st.success("Added to Menu")