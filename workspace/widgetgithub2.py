import streamlit as st

#select/multiple select

my_lang = ["Python","CSS","HTML","C++","JAVA"]

choice = st.selectbox("Choose a language",my_lang)

st.write("You selected",choice)

#mulitple select
spoken_lang = ("English","French","Spanish","Chinese")
my_spoken_lang = st.multiselect("Spoken language",spoken_lang) #default ="Eng;ish"

#slider (numbers int/float only)
age = st.slider("Age",1,100) #5 is range

#sliders any data type
color = st.select_slider("Choose language",options = my_lang)

