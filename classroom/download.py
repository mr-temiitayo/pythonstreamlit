import streamlit as st

# Define the file path
download_file = 'patientrecords.csv'

# Create a download button
with open(download_file, 'rb') as file:
    data = file.read()
st.download_button(label='Download CSV', data=data, file_name='patientrecords.csv', key='download_csv')


# By opening the file in binary read mode, you can read the contents of the CSV file as binary data, 
# which is necessary for creating a download button in Streamlit. 
# Streamlit's st.download_button function expects the file data to be in binary format 
# to create a downloadable link. 
# The with statement ensures that the file is properly closed after reading its contents.
# binary read binary ('rb') and read its contents into the data variable.
#  It ensures that the file's contents are read without any interpretation or modification.

# .read(): This is a method of the file object (file) that is used to read the entire contents of the file.
# .read() is used for reading text data from a file opened in text mode ('r'),