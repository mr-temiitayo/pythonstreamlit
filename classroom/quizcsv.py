import streamlit as st
import pandas as pd

# create a quiz
# store user details and score and grade in csv file

if 'score' not in st.session_state:
    st.session_state.score = 0

if 'index' not in st.session_state:
    st.session_state.index = 0

if 'lenght' not in st.session_state:
    st.session_state.lenght = 0

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

# Streamlit app title
st.title("Quiz App")
col1, col2, col3, col4 = st.columns(4)

# Display the current question
question_data = quiz_data.iloc[st.session_state.index]
st.subheader(f"Question {st.session_state.index+1}:")
st.write(question_data["question"])

# Display answer options as radio buttons
selected_option = st.radio("Select an answer:", question_data["options"].split(';'))
if selected_option == question_data["correct_answer"]:
    st.session_state.score +=1

with col1:
    if st.session_state.index > 0:
        st.button('Previous Question',on_click=previous)
            

with col3:    
    if st.session_state.index < 2:
        st.button('Next Question',on_click=next)
            

with col4:
    st.button('Restart',on_click=restart)


# Display quiz results
if st.session_state.index >1:
    st.button("Submit",on_click = submit)


st.write('index:',st.session_state.index,'score:',st.session_state.score)