import streamlit as st
#order Fashion Page

st.set_page_config(layout='wide')
menu = st.sidebar.selectbox('Menu',["Men Category", "Women Category", "Children Category"])
bill = 0

if menu == "Men Category":
    
    st.header("Men Fashion Category")
    men1,men2,men3,men4 = st.columns(4)
    with men1:
        st.image("https://m.media-amazon.com/images/I/61XtfipV3qL._AC_UL320_.jpg")
        if st.checkbox("Men Complete Suit: $150"):
            bill +=150
            st.success("Added to menu")
    
    with men2:
        st.image("https://m.media-amazon.com/images/I/71kiKJpww7L._AC_UL320_.jpg")
        if st.checkbox("Men Jacket: $40"):
            bill +=40
            st.success("Added to menu")

    with men3:
        st.image("https://m.media-amazon.com/images/I/816g4QaCd6L._AC_UL320_.jpg")
        if st.checkbox("Men Hoodie: $35"):
            bill += 35
            st.success("Added to menu")

    with men4:
        st.image("https://m.media-amazon.com/images/I/61XXg9AFgNL._AC_UL320_.jpg")
        if st.checkbox("Men Shirt & Pants: $60"):
            bill +=60
            st.success('Added to menu')




if menu == "Women Category":
    st.header("Women Fashion Category")

if menu == "Children Category":
    st.header("Children Fashion Category")