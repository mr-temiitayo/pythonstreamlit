import streamlit as st
#streamlit is used to create a web page for your python app


st.title("This is a big title")

st.header("This is a small header")

st.subheader("This is a smaller subheader")

st.write("This is the smallest write")

st.success("Success: Green bar")

st.error("Error: Red bar")

st.warning("Warning: Orange bar")

st.info("Info: Blue bar")

name = st.text_input("Enter your name here")

score = st.number_input("Enter your number here")