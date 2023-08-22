import streamlit as st
from PIL import Image

#working with meadi files (videos/images/audio)
img = Image.open(r'C:/Users/USER/Desktop/streamlipython/pythonstreamlit/media/Golfcart Robot.jpg')
st.image(img, use_column_width=True) #to use full width

#from url
st.image("https://cdn.pixabay.com/photo/2016/11/14/04/45/elephant-1822636_1280.jpg")

#how to display videos
