import streamlit as st #webpage to display your python project

st.title("Title")
st.header("Header")
st.subheader("Subheader")
st.write("Write")
st.success("Shows in a green box")

name = st.text_input("Enter your name")

age = st.number_input('Enter your age here')

if st.button("Check Here"):
    st.success("Thank you")

if st.checkbox('Click Me'):
    st.success("Thank you")