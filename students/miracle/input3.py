import streamlit as st
name =st.text_input('please enter your name')
favourite_book=st.text_input('please enter your favourite book')
favourite_character=st.text_input('please enter your favourite character')
favourite_part=st.text_input('please enter your favourite part')
st.write('Hi',name,'your favourite book is', favourite_book,'your favourite character is', favourite_character,'and your favourite part is', favourite_part)
