import streamlit as st
name=st.text_input('please write your name')
# =('how many mangoes were sold',0)
number_of_good_mangoes=('how many mangoes are good',0)
number_of_bad_mangoes=('how many mangoes are bad',0)
total_mangoes=number_of_good_mangoes-number_of_bad_mangoes
if st.button('check here for final answer'):
    st.write('final answer is',total_mangoes)
