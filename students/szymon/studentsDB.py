import streamlit as st
import pandas as pd


menu = st.sidebar.selectbox("Menu",['Submit Scores','Database|Charts','Student File'])


if menu == 'Submit Scores':
    st.header("Submit Student Scores")
    

    left,right = st.columns(2)

    with left:
        name = st.text_input("Enter Student name")
        math = st.number_input("Enter Student Math score",0,100)
        sci = st.number_input("Enter Student Science score",0,100)

    with right:
        skills = st.multiselect("Choose Student Best Skills",['Very Creative','Thinker','Artistic','Reading','Accuracy','Speed'])
        eng = st.number_input("Enter Student English score",0,100)
        art = st.number_input("Enter Student Art score",0,100)

    totalscore = math + eng
    average = totalscore/5

    if st.button("Submit Student Score"):
        st.success(f'{name} scored {totalscore} in total, Average: {average}')