import streamlit as st

welcome = 'Mr. Tee'
if st.button("Test my button"):
    st.write("welcome",welcome)

#keys must be unique for each widget if not error

welcome = 'Mr. Tee'
if st.button("Test my button",key='button2'):
    st.write("welcome again",welcome)

#working with radiobuttons
status = st.radio("What is your status", ("Active", "Inactive"))

if status == "Active":
    st.success('You are Active')

elif status == "Inactive":
    st.warning("Inactive")

#working with checkbox
if st.checkbox("Show/hide"):
    st.text("Showing something")

#working with Beta Expander
if st.expander("Open Python"):
    st.success("Hello Python")

