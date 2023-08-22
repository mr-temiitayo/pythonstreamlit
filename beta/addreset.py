import streamlit as st

# Streamlit app title
st.title("Add Number App")

# Input box for user input
user_input = st.text_input("Enter a number:", value="", key="user_input")

# Define a predefined number to add
add_number = 5

# Convert the user input to an integer (if valid)
try:
    user_number = int(user_input)
except ValueError:
    user_number = 0

# Calculate the sum and display the answer
sum_result = user_number + add_number
st.write(f"Adding {add_number} to your input: {user_number} + {add_number} = {sum_result}")

# Button to update the input box with the sum result
if st.button("Update Input"):
    user_input = str(sum_result)

# Display the updated input box
st.text_input("Enter a number:", value=user_input, key="updated_user_input")
