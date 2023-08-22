import streamlit as st
import pandas as pd
import os

# Streamlit app title
st.title("Variable to CSV Example")

# Input field to get a user's name
user_name = st.text_input("Enter your name:")

# Button to save the name to a CSV file
if st.button("Save Name"):
    # Create a DataFrame with the user's name
    data = {'Name': [user_name]}
    st.text(user_name)
    df = pd.DataFrame(data)

    # Check if the CSV file exists
    csv_filename = "C:\\Users\\USER\\Desktop\\streamlipython\\pythonstreamlit\\beta\\user_data.csv"
    if not os.path.exists(csv_filename):
        # If the file doesn't exist, create an empty DataFrame
        df = pd.DataFrame(columns=["Name", "Age", "City"])
        # Save the empty DataFrame to create the CSV file
        df.to_csv(csv_filename, index=False)
    else:
        # If the file exists, load its content into a DataFrame
        df = pd.read_csv(csv_filename)

    st.success(f"Name '{user_name}' saved to user_data.csv")

    # Read and display the name from the CSV file
    st.write("Name uploaded from CSV:")
    loaded_data = pd.read_csv(csv_filename)
    new_name = loaded_data['Name']
    st.text(new_name)



# try:
#     loaded_data = pd.read_csv('user_data.csv')
#     if not loaded_data.empty:
#         st.write(loaded_data['Name'][0])
# except FileNotFoundError:
#     st.write("No data saved yet.")
