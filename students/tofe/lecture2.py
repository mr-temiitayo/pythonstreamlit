import streamlit as st

subjects = ['Maths', 'Science', 'History']
scores = {}

for subject in subjects:
    scores[subject] = st.number_input(f"Enter your {subject} score:", value=0, step=1, format='%d')

    if st.button(f"Check {subject} Score"):
        if scores[subject] > 50:
            st.success("You passed")
        else:
            st.warning("You failed")
