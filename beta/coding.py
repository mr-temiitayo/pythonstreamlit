import streamlit as st
import subprocess

# Streamlit app title
st.title("Coding Practice Platform")

# Text area for entering Python code
code = st.text_area("Enter Python code:")

# Button to execute the code
if st.button("Execute"):
    try:
        # Create a temporary Python file to store the code
        with open("temp_code.py", "w") as file:
            file.write(code)

        # Execute the code and capture the output
        output = subprocess.check_output(["python", "temp_code.py"], stderr=subprocess.STDOUT, text=True)

        # Display the code output
        st.code(output, language="python")
    except subprocess.CalledProcessError as e:
        st.error(f"Error executing the code:\n{e.output}")

# Information and instructions
st.markdown("### Instructions:")
st.write("1. Enter your Python code in the text area above.")
st.write("2. Click the 'Execute' button to run the code.")
st.write("3. The code output will be displayed below.")

# Disclaimer
st.markdown("### Disclaimer:")
st.write("This is a simplified coding practice platform for educational purposes only.")
st.write("Avoid running untrusted or malicious code in this environment.")
