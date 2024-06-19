import streamlit as st
name=st.text_input ('please enter your name')
animal_stickers=st.number_input('please enter the number of  animal sticker')
superhero_sticker=st.number_input('please enter the number of super hero sticker')
star_sticker=st.number_input('please enter the number of star sticker')
total_sticker=animal_stickers+superhero_sticker+star_sticker
st.write("hi",name,'you have collected the total of',total_sticker,'sticker')












