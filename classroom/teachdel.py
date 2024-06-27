import streamlit as st
import pandas as pd

# Load the CSV file
try:
    df = pd.read_csv('subjects.csv')
except FileNotFoundError:
    st.error('subjects.csv file not found.')
    df = pd.DataFrame()

# Extract subject names from the "Subjects" column
subject_names = df['Subjects'].tolist()

# Create a dictionary to store subject scores
subject_scores = {}

col1, col2 = st.columns(2)
# Create columns for each subject
for i, subject in enumerate(subject_names):
    
    if i % 2 == 0:
        with col1:
            score = st.number_input(f'Enter student score for {subject}', min_value=0, max_value=100, step=10, key=subject)
    else:
        with col2:
            score = st.number_input(f'Enter student score for {subject}', min_value=0, max_value=100, step=10, key=subject)
    subject_scores[subject] = score

# Display the scores
st.write('Subject Scores:')
st.write(subject_scores)
