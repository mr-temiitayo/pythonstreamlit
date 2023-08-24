import streamlit as st
import pandas as pd

# Load the CSV file
patientsrecord = 'https://raw.githubusercontent.com/mr-temiitayo/pythonstreamlit/main/classroom/patientrecords.csv'
df = pd.read_csv(patientsrecord)

# Streamlit app title
st.title("Search Patient Record CSV File")

# Input field to get the search query from the user
search_query = st.text_input("Enter patient ID to search:")

# Button to perform the search
if st.button("Search"):
    # Filter the DataFrame based on the search query
    search_result = df[df['Patient ID'].str.contains(search_query, case=False)]

    # Use separate variables for each matching row
    if not search_result.empty:
        # Access specific values without converting to lists
        firstname = search_result['First Name'].iloc[0]
        lastname = search_result['Gender'].iloc[0]
        st.write(f'First Name: {firstname}, Last Name: {lastname}')

        # Add more columns as needed    
    else:
        # If no matching records found, initialize empty variables
        firstname = ""
        lastname = ""
        # Initialize additional variables if needed

    # Now, you have separate variables for each matching data column
