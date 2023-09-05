import streamlit as st
import pandas as pd

# Create a quiz
# Store user details, score, and grade in a CSV file

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
    st.write(f"You scored {st.session_state.score} out of {st.session_state.length} questions.")

def previous():
    st.session_state.index -= 1

def next():
    st.session_state.index += 1

def restart():
    st.session_state.score = 0
    st.session_state.index = 0
    st.session_state.correctly_answered = {}
    st.session_state.user_answers = {}

# Streamlit app title
st.title("Quiz App")
col1, col2, col3, col4 = st.columns(4)

# Display the current question
question_data = quiz_data.iloc[st.session_state.index]
st.session_state.length = len(quiz_data)  # Update the total number of questions
st.subheader(f"Question {st.session_state.index+1} of {st.session_state.length}:")
st.write(question_data["question"])

# Display answer options as radio buttons with the user's previous selection
selected_option = st.radio("Select an answer:", question_data["options"].split(';'), key=st.session_state.index, index=None if st.session_state.index not in st.session_state.user_answers else st.session_state.user_answers[st.session_state.index])
correct_answer = question_data["correct_answer"]

# Store the user's answer for the current question
st.session_state.user_answers[st.session_state.index] = selected_option

# Check if the answer is correct and has not been previously marked as correct
if selected_option == correct_answer and st.session_state.index not in st.session_state.correctly_answered:
    st.session_state.score += 1
    st.session_state.correctly_answered[st.session_state.index] = correct_answer

with col1:
    if st.session_state.index > 0:
        st.button('Previous Question', on_click=previous)

with col3:
    if st.session_state.index < st.session_state.length - 1:
        st.button('Next Question', on_click=next)

with col4:
    st.button('Restart', on_click=restart)

# Display quiz results
if st.session_state.index == st.session_state.length - 1:
    st.button("Submit", on_click=submit)

st.write('index:', st.session_state.index, 'score:', st.session_state.score)
