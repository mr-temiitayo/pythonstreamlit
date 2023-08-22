#cofig of page must be the fist set of code
import streamlit as st

#method 1: normal
st.set_page_config(page_title ='Hello',
                   page_icon='😎',layout='wide', #favicon title
                   initial_sidebar_state='collapsed') #expanded or auto

#method 2: dictionary
#page_config = {"page_title": "Streamlit Page","page_icon": "😀","layout": "centered"}
#st.set_page_config(**page_config)

#update streamlit use pip3 install streamlit -U
def main():
    st.title("Welcome to the Config Page")
    st.sidebar.success("Menu")


main()