#streamlit is a web page built to display your python project

import streamlit as st

st.title("Here is my first project")

st.header("A header")

st.subheader("A subheader")

st.write("This is the small write")

st.success("This is a text with a green bar")

st.error("This is a text with a red bar") #others: st.warning, st.info

if st.button("Click me"):
    st.write("Yaay you did!!!!")