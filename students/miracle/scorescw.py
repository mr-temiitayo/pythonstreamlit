#classwork: using the age calc example, create a program that will ask
#the user for the name and his score in maths and his score in english, then add the two scores together

import streamlit as st

name = st.text_input("please enter your name,")
ms = st.number_input('please enter your math score')
es = st.number_input('please enter your english score')
ts = ms + es 

if st.button("Check"): #colon is used to create a condition
    st.write(name, 'scored', ts) #indentatation
