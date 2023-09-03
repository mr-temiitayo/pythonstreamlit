import streamlit as st
import pandas as pd
import time

# Load quiz data from the CSV file
@st.cache  # Use Streamlit's caching for better performance
def load_quiz_data():
    quiz_data = pd.read_csv('quiz_data.csv')
    return quiz_data

# Initialize variables to keep track of the quiz state
quiz_data = load_quiz_data()
quiz_index = 0
score = 0
timer_duration = 30  # Set the timer duration in seconds
start_time = 0

# Streamlit app title
st.title("Quiz App")

# Countdown timer function
def countdown_timer():
    remaining_time = max(timer_duration - int(time.time() - start_time), 0)
    return remaining_time

# Display the current question
if quiz_index < len(quiz_data):
    question_data = quiz_data.iloc[quiz_index]
    st.subheader(f"Question {quiz_index + 1}:")
    st.write(question_data["question"])

    # Display answer options as radio buttons
    selected_option = st.radio("Select an answer:", question_data["options"].split(';'))

    # Start the timer when the question is displayed
    if start_time == 0:
        start_time = time.time()

    # Display the countdown timer
    remaining_time = countdown_timer()
    st.write(f"Time remaining: {remaining_time} seconds")

    # Check if the selected option is correct
    if st.button("Submit") or remaining_time == 0:
        if selected_option == question_data["correct_answer"]:
            score += 1

        # Move to the next question and reset the timer
        quiz_index += 1
        start_time = 0

# Display quiz results
else:
    st.subheader("Quiz Results")
    st.write(f"You scored {score} out of {len(quiz_data)} questions.")

# Reset the quiz
if st.button("Restart Quiz"):
    quiz_index = 0
    score = 0
    start_time = 0
