import streamlit as st
from PIL import Image #This is used to process images

menu = st.sidebar.selectbox('Menu',['Upload Files','About Us'])


if menu == 'Upload Files':
    st.header('Upload Files Here')

#------------HOW TO LET USERS UPLOAD IMAGES-----------------------
    image_file = st.file_uploader('Upload your image',type=['png','jpg','jpeg'])

    if image_file is not None:
        st.image(Image.open(image_file))

        