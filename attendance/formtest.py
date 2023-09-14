import streamlit as st
import pandas as pd

# Load the existing attendance data from CSV
attendance_df = pd.read_csv("attendance.csv")

# Sidebar menu
menu = st.sidebar.selectbox('Menu', ['Attendance', 'Students Database'])

if menu == 'Attendance':
    col1, col2, col3, col4 = st.columns([2, 1, 2, 1])

    with st.form(key='attendance_form', clear_on_submit=True):
        with col1:
            name_search = st.text_input('Enter name to search', placeholder="Search Student", label_visibility='collapsed')

        with col2:
            search_submit = st.form_submit_button('Search')

        with col3:
            new_student = st.text_input("Add new student", placeholder="Add New Student", label_visibility='collapsed')

        with col4:
            add_student = st.form_submit_button('Add Student')

        if add_student and new_student.strip() != "":
            # Add a new column with the student's name to the attendance DataFrame
            attendance_df[new_student] = ''

            # Save the updated DataFrame back to the CSV file
            attendance_df.to_csv('attendance.csv', index=False)

            st.success(f"{new_student} added")

        if search_submit:
            # Filter the columns in the DataFrame that contain the name_search text
            matching_columns = [col for col in attendance_df.columns if name_search.lower() in col.lower()]

            # Display the matching column names
            if matching_columns:
                st.success(f"Matching column names: {', '.join(matching_columns)}")
            else:
                st.warning("No matching column names found.")

if menu == 'Students Database':
    st.dataframe(attendance_df)
