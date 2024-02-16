import streamlit as st
import pandas as pd


st.set_page_config(layout='wide')

st.title("Data Editor App")

upload_csv = st.file_uploader("Upload CSV File")

if upload_csv:
    csv_file = pd.read_csv(upload_csv)
    edit_csv = st.data_editor(csv_file)

if st.button("Seve The File"):
    pass