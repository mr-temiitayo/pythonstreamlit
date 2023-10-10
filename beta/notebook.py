import streamlit as st

# Define hardcoded password
password = "password"

# Streamlit app title
st.title("Access Notebook")

# Create a placeholder for the login page content
login_container = st.empty()

# Create two columns within the container
col1, col2 = login_container.columns([1, 1])

# Create a text input field for the password in the first column
password_input = col1.text_input("Enter the password:", type="password")

# Create a button to submit the password in the second column
login_button = col2.button("Login")

# Check if the entered password matches after clicking the button
if login_button:
    if password_input == password:
        # Clear the login page content
        login_container.empty()

        # Display the text area for the notebook
        st.write("Notebook Page")

        # Create a text area for user input
        user_notebook = st.text_area("Type your notebook content here:", "")

        # Add a button to save the notebook content to a file
        if st.button("Save Notebook"):
            with open("notebook.txt", "w") as f:
                f.write(user_notebook)
            st.success("Notebook content saved to 'notebook.txt'")
    else:
        st.warning("Password incorrect. Please try again.")
