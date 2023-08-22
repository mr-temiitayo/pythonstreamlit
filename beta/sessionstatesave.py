# Import the Streamlit library
import streamlit as st

# Define the main function that runs the app
def main():
    # Initialize the number variable with a value of 5
    number = st.session_state.get('number', 5)

    # Create a button labeled "Add 1"
    if st.button("Add 1"):
        # When the button is clicked, increase the number by 1
        number += 1
        # Update the session state to remember the new number value
        st.session_state.number = number

    # Display the current value of the number
    st.write(f"Number: {number}")

# Call the main function to start the Streamlit app
main()
