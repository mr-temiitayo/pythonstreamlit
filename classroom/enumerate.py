# In coding, enumerate is a built-in Python function that allows you to loop over 
# an iterable (like a list or tuple) and have an automatic counter. 
# This counter provides the index of the current item in the iterable along with the item itself. 
# It is particularly useful when you need both the index and the value in a loop.

# This is useful for operations that depend on the position of the elements, 
# such as placing subjects in alternating columns.
import streamlit as st
subjects = ['Math', 'Science', 'History']

for i, subject in enumerate(subjects):
    print(f"Index: {i}, Subject: {subject}")
