import streamlit as st
import pandas as pd
import os

# Streamlit app title
st.title("Variable to CSV Example")
csv_filename = "C:\\Users\\USER\\Desktop\\streamlipython\\pythonstreamlit\\beta\\user_data.csv"
df = pd.read_csv(csv_filename)  # Load the CSV file

# Input fields to get user's information
user_name = st.text_input("Enter your name:")
city = st.text_input("Enter your city:")
age = st.number_input("Enter your age:")
dob = st.date_input('Date')

# Button to save the information to the CSV file
if st.button("Save Information"):
    # Create a DataFrame with the user's information
    data = {'Name': [user_name], 'City': [city], 'Age': [age],'Date':[dob]}
    df = pd.DataFrame(data,columns=['Name','City','Age','Date'])

    # Save the DataFrame to the CSV file
    df.to_csv(csv_filename, index=False)

    st.success(f"Information saved to user_data.csv")

    #OR create a function to overwrite it when need be
    # Create a DataFrame with the user's information
    #data = {'Name': [user_name], 'City': [city], 'Age': [age],'Date':[dob]}
    #df = pd.DataFrame(data,columns=['Name','City','Age','Date'])



    # Save the DataFrame to the CSV file
    df.to_csv(csv_filename, index=False)

# Button to extract and display the information from the CSV file
if st.button("Extract Information"):
    loaded_data = pd.read_csv(csv_filename)
    if not loaded_data.empty:
        extracted_name = loaded_data['Name'].iloc[0] #wxtract from the first row
        extracted_city = loaded_data['City'].iloc[0]
        extracted_age = loaded_data['Age'].iloc[0]
        st.write(f"Name: {extracted_name}, City: {extracted_city}, Age: {extracted_age}, Date: {dob}")
    else:
        st.write("No data saved yet.")

