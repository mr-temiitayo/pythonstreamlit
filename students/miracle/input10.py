import streamlit as st
name=st.text_input('please enter your name')
num_jobs=st.number_input('how many print job is available',0)
pages_per_job=st.number_input('pages per job print',0)
total_pages=num_jobs*pages_per_job
if st.button("click here for the answer"):
    st.write('answer is',total_pages)
