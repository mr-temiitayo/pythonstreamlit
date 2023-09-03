import streamlit as st
import random

# Streamlit app title
st.title("Math Tutor: Addition")

# Generate two random numbers for the addition problem
num1 = random.randint(1, 10)
num2 = random.randint(1, 10)

# User input for the answer
user_answer = st.number_input(f"What is {num1} + {num2}?", min_value=0)

# Calculate the correct answer
correct_answer = num1 + num2

# Check if the user's answer is correct
if user_answer == correct_answer:
    st.success("Correct! Well done.")
else:
    st.error(f"Sorry, the correct answer is {correct_answer}.")

# Provide step-by-step explanation (simplified)
st.subheader("Step-by-Step Explanation:")
st.write(f"Step 1: Start with the first number, {num1}.")
st.write(f"Step 2: Add the second number, {num2}, to the result.")
st.write(f"Step 3: The final result is {correct_answer}.")

# Offer a new problem
if st.button("New Problem"):
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    user_answer = None

# Information and instructions
st.markdown("### Instructions:")
st.write("1. Solve the addition problem and enter your answer in the input box.")
st.write("2. Click the 'New Problem' button to get a new addition problem.")
st.write("3. See if your answer is correct.")

# Disclaimer
st.markdown("### Disclaimer:")
st.write("This is a simplified math tutor app for educational purposes only.")
st.write("It covers basic addition problems.")
