""""
-title
-image
-categories
Men's Fashion

Women's Fashion

Children's Fashion

(each category must havedifferent types of unique items and the prices like shirts(long sleeves,short, round nexk, polo etc), boxers, trousers, shoes, bags etc)
"""  

import streamlit as st

st.set_page_config(layout="wide")

bill = 0
st.title('Cute Fashion Store')

st.image('https://cdn.pixabay.com/photo/2016/11/22/19/08/hangers-1850082_1280.jpg')

st.header("Men's Categories")

men1,men2,men3,men4 = st.columns(4)

with men1:
    if st.checkbox('Long sleeves for men: $10'):
        bill +=10
        st.success('Added to List')
        