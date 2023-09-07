import streamlit as st
import pandas as pd

# create a quiz
# store user details and score and grade in csv file

if 'score' not in st.session_state:
    st.session_state.score = 0

if 'index' not in st.session_state:
    st.session_state.index = 0

if 'length' not in st.session_state:
    st.session_state.length = 0

if 'correctly_answered' not in st.session_state:
    st.session_state.correctly_answered = {}

if 'user_answers' not in st.session_state:
    st.session_state.user_answers = {}

# Load quiz data from the CSV file
quiz_data = pd.read_csv('quiz_data.csv')

def submit():
    st.subheader("Quiz Results")
    st.write(f"You scored {st.session_state.score} out of 3 questions.")

def previous():
    st.session_state.index -= 1

def next():
    st.session_state.index += 1

def restart():
    st.session_state.score = 0
    st.session_state.index = 0
    st.session_state.correctly_answered = {}

# Streamlit app title
st.title("Quiz App")
col1, col2, col3, col4 = st.columns(4)

# Display the current question
question_data = quiz_data.iloc[st.session_state.index]
st.subheader(f"Question {st.session_state.index+1}:")
st.write(question_data["question"])

#key=st.session_state.index,
# key=st.session_state.index, 
# index=None if st.session_state.index not in st.session_state.user_answers else st.session_state.user_answers[st.session_state.index])

# Display answer options as radio buttons
selected_option = st.radio("Select an answer:", 
        question_data["options"].split(';'),
        key=st.session_state.index,
        index=st.session_state.user_answers.get(st.session_state.index, None)
)
correct_answer = question_data["correct_answer"]


# Store the user's answer for the current question
st.session_state.user_answers[st.session_state.index] = selected_option

# Check if the answer has changed from a correct answer to a wrong answer

#if the answer (key) is in the correctly answered dict
#and if the correctly answered index (value) == correct answer
#and the current selected option is not correct
#then score -1 and del the index (key) from the corrcetly answered dict
if (
    st.session_state.index in st.session_state.correctly_answered
    and st.session_state.correctly_answered[st.session_state.index] == correct_answer
    and selected_option != correct_answer
):
    st.session_state.score -= 1
    del st.session_state.correctly_answered[st.session_state.index]


# Check if the answer has changed from a correct answer to a wrong answer
#-----
# Check if the current selected answer is the correct answer
#if the answer (key) is not in correctly answered dict
if (selected_option == correct_answer 
    and st.session_state.index not in st.session_state.correctly_answered):
    st.session_state.score += 1
    st.session_state.correctly_answered[st.session_state.index] = correct_answer

with col1:
    if st.session_state.index > 0:
        st.button('Previous Question', on_click=previous)

with col3:
    if st.session_state.index < 2:
        st.button('Next Question', on_click=next)

with col4:
    st.button('Restart', on_click=restart)

# Display quiz results
if st.session_state.index > 1:
    st.button("Submit", on_click=submit)

st.write('index:', st.session_state.index, 'score:', st.session_state.score)
