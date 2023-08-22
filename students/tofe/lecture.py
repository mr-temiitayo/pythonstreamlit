#A lecturer in the university wants you as programmer to create a software to mark students scores
#Ask the students for their scores in english, maths and science
#If the total score is above 90, give the student A+
#If the total score is between 80-89, give the student A
#If the total score is between 70-79, give the student B
#If the total score is between 60-69, give the student C
#If the total score is between 50-59, give the student D
#If the total score is below 50, give the student F


import streamlit as st

#check if subject == none to show maths button
subject = st.session_state.get('subject', 'maths')

if subject == 'maths':
    maths = st.number_input("Enter your maths score:", value=0, step=1, format='%d')

    if st.button("Check Maths Score"):
        if maths > 50:
            st.success("You passed")
        else:
            st.warning("You failed")
        subject = 'science'
        st.session_state.subject = subject

#check if maths button has been clicked to show science button
if subject == 'science':
    science = st.number_input("Enter your Science score:", value=0, step=1, format='%d')

    if st.button("Check Science Score"):
        if science > 50:
            st.success("You passed")
        else:
            st.warning("You failed")
        subject = 'history'
        st.session_state.subject = subject
#check if science button has been clicked to show history button
if subject == 'history':
    history = st.number_input("Enter your History score:", value=0, step=1, format='%d')

    if st.button("Check History Score"):
        if history > 50:
            st.success("You passed")
        else:
            st.warning("You failed")