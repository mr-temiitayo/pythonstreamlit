import streamlit as st
import pandas as pd
import plotly.express as px

# Project Objective
# Create a student scores database which can 
# -get the name
# -4 subjects
# -calculate the average
# -calculate the grade (A,B,C,D,E,F)
# -update your csv file

# What is a csv file?
# CSV files are text files where each data is separated by a comma (comma-separated values)

st.set_page_config(layout='wide')

menu = st.sidebar.selectbox('Menu',['Submit Students Scores', 'Students Database'])
df = pd.read_csv('employee.csv')

if menu == 'Submit Students Scores':
    # Your code for submitting scores goes here
    pass
elif menu == 'Students Database':
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.header(':orange[Employee DB]')
    
    # Add selectbox for filtering by gender
    gender_filter = st.sidebar.selectbox('Filter by Gender', ['All', 'Male', 'Female'])
    
    if gender_filter == 'All':
        filtered_df = df
    else:
        filtered_df = df[df['Gender'] == gender_filter]
    
    # Display filtered table
    st.table(filtered_df)

    gender= ['Male', 'Female']

    # Create a pie chart for different grade column counts
    gender_counts = filtered_df['Gender'].value_counts().reset_index()
    st.write(gender_counts)
    # grade_counts = grade_counts.rename(columns={'index': 'Grade', 'Grade': 'Count'})
    
    piechart = px.pie(gender_counts, names='Gender', values='count')
    st.plotly_chart(piechart)
