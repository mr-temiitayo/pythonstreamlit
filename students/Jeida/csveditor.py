import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')
st.title('Data Editor App')

col1,col2 = st.columns(2)

with col1:
    upload_csv= st.file_uploader("Upload CSV File",type=['csv'])

    st.divider()
    st.write("")

if upload_csv:
    csv_file = pd.read_csv(upload_csv)
    edit_csv = st.data_editor(csv_file,use_container_width=True)

    if st.button("Save Edited CSV"):    
        st.success("Edited CSV File Saved")
        new_csvname = f'{upload_csv.name}'
        saved_csv = edit_csv.to_csv(new_csvname,index=False)

#what if you want to edit and save a copy, not overwrite the original data??


