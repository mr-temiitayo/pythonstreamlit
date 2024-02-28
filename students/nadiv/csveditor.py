import streamlit as st
import pandas as pd


st.set_page_config(layout='wide')

st.title("Data Editor App")

upload_csv = st.file_uploader("Upload CSV File")

if upload_csv:
    csv_file = pd.read_csv(upload_csv)
    edit_csv = st.data_editor(csv_file)

# new_database.to_csv('scores.csv',index=False)
if st.button("Save The File"):
    saved_csv = edit_csv.to_csv(upload_csv.name,index=False)
    st.success("Your Edited File Has Been Saved")

