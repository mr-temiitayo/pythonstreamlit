# idea is to create an input for teachers to enter name of subjects
# this input is then converted to a list
# this list is shown as a multiselect box
# this is then asked to confirm or remove from subjects
# then a button to confirm and to create df columns from

# create a checkbox to create a multiselect delete subjects/students from
# using clearing columns or rows


import streamlit as st
import numpy as np

grade_to_point = {
    "O": 10,
    "A+": 9,
    "A": 8,
    "B+": 7,
    "B": 6,
    "C": 5,
}
grades = list(grade_to_point.keys())
# st.write(grades)


def calculate_cgpa(
    grade: np.array,
    credit: np.array,
    previous_cgpa: float = 0,
    previous_credit: float = 0,
):
    # grade = np.array([grade_to_point[g] for g in grade])
    total_credit = credit.sum() + previous_credit
    total_grade = (grade * credit).sum() + previous_cgpa * previous_credit
    return total_grade / total_credit


# -----------------------------------------------------------
number_of_subjects = st.number_input(
    label="Number of Subjects",
    help="Enter the number of subjects you are taking this semester",
    min_value=1,
    max_value=10,
    value=5,
)


grade = np.array([0] * number_of_subjects)
st.write(grade)

credit = np.array([0] * number_of_subjects)
st.write(credit)

#check here
for i in range(number_of_subjects):
    st.subheader(f"Subject #{i+1}")
    cols = st.columns(2)
    grade[i] = grade_to_point[
        cols[0].selectbox(
            label=f"Grade",
            options=grades,
            key=f"selectbox_{i}",
        )
    ]

    credit[i] = cols[1].number_input(
        label=f"Credit",
        min_value=1.0,
        max_value=10.0,
        value=4.0,
        step=0.5,
        key=f"number_input_{i}",
    )

st.write(grade)
st.write(credit)
if st.button("Calculate"):
    st.info(f"Your semester GPA is {calculate_cgpa(grade, credit):.2f}")