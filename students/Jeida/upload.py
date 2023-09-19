#Inthis class we will learn to upload files, starting from an image

import streamlit as st
from PIL import Image

st.set_page_config(layout='wide')

if 'image_file' not in st.session_state:
    st.session_state.image_file = None

menu = st.sidebar.selectbox('Menu',['Upload Files','View Files'])

if menu == "Upload Files":
    st.subheader('Upload Your Files Here')
    image_file = st.file_uploader('Upload your image',type=['png','jpg','jpeg'],key='image_file') #upload only files with these extensions



if menu == 'View Files':
    st.subheader('View Files Here')
    if st.session_state.image_file is not None: #Check if the variable is not empty
        st.image(Image.open(st.session_state.image_file)) #st.image should display after PIL Image has proccess the file
