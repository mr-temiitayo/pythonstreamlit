import streamlit as st

# Define the quiz questions and answers
quiz_data = [
    {
        "question": "What is the capital of France?",
        "options": ["London", "Berlin", "Paris", "Madrid"],
        "correct_answer": "Paris",
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Mars", "Jupiter", "Venus", "Saturn"],
        "correct_answer": "Mars",
    },
    {
        "question": "What is the largest mammal?",
        "options": ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"],
        "correct_answer": "Blue Whale",
    },
]

def submit():
        if selected_option == quiz_data[st.session_state.quiz_index]["correct_answer"]:
            st.session_state.score += 1

        # Move to the next question
        st.session_state.quiz_index += 1

def restart():
    st.session_state.quiz_index = 0
    st.session_state.score = 0

if 'quiz_index' not in st.session_state:
    st.session_state['quiz_index'] = 0

if 'score' not in st.session_state:
    st.session_state.score = 0

# Streamlit app title
st.title("Quiz App")

# Display the current question
if st.session_state.quiz_index < 3:
    st.subheader(f"Question {st.session_state.quiz_index + 1}:")
    st.write(quiz_data[st.session_state.quiz_index]["question"])

    # Display answer options as radio buttons
    selected_option = st.radio("Select an answer:", quiz_data[st.session_state.quiz_index]["options"])

    # Check if the selected option is correct
    st.button("Submit",on_click=submit)

# Display quiz results
else:
    st.subheader("Quiz Results")
    st.write(f"You scored {st.session_state.score} out of {len(quiz_data)} questions.")

# Reset the quiz
st.button("Restart Quiz",on_click=restart)