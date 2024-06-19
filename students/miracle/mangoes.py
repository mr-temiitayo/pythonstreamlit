#A boy went to the market to buy some mangoes but some were bad. 
# Can you find out the remainging good ones? ask the boy the following questions
#-ask the boy for his name
#ask how many mangoes he bought 
#ask how many mangoes were bad
#then calculate the mangoes that were good
import streamlit as st
name = st.text_input('please input your name')
nm = st.number_input('number of mangoes')
nbm = st.number_input("number of bad mangoes")
ngm = nm-nbm

st.write (name, 'good mangoes is', ngm)





