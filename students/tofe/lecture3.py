import streamlit as st

# Define the subjects and their score ranges
subjects = ['English', 'Maths', 'Science']
score_ranges = {
    'A+': (90, 100),
    'A': (80, 89),
    'B': (70, 79),
    'C': (60, 69),
    'D': (50, 59),
    'F': (0, 49)
}

# Initialize session state variables
current_subject_index = st.session_state.get('current_subject_index', 0)
scores = st.session_state.get('scores', {})

# Main loop to iterate through subjects
if current_subject_index < len(subjects):
    current_subject = subjects[current_subject_index]
    st.write(f"Enter your {current_subject} score:")
    scores[current_subject] = st.number_input(f"{current_subject} Score", value=0, step=1, format='%d')

    if st.button("Check Score"):
        min_score, max_score = score_ranges['F']
        for grade, (min_range, max_range) in score_ranges.items():
            if min_range <= scores[current_subject] <= max_range:
                min_score, max_score = min_range, max_range
                break
        
        result = f"Your {current_subject} score is {scores[current_subject]}."
        if min_score <= scores[current_subject] <= max_score:
            result += f" You got a grade {grade}."
        
        st.write(result)
        current_subject_index += 1
        st.session_state.current_subject_index = current_subject_index
        st.session_state.scores = scores

    st.write(f"Current subject: {current_subject}")
else:
    st.write("All subjects checked. Thank you!")

