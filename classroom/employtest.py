import streamlit as st
import pandas as pd
st.set_page_config(layout='wide')
# Main app
st.title("Employee Database App")

# Load the CSV file into a DataFrame
df = pd.read_csv("employees_database.csv")

st.write("Current Database:")
st.dataframe(df,use_container_width=True)

with st.form(key='employee',clear_on_submit=True):

    st.write("Update Employee Details:")
    name = st.text_input("Name:")
    position = st.text_input("Position:")
    salary = st.number_input("Salary:", step=1000)

    if st.form_submit_button("Add Employee"):
        if name and position and salary:
            new_df = pd.DataFrame( {"Name": [name], "Position": [position], "Salary": [salary]})
            df = pd.concat([df, new_df], ignore_index=True)
            df.to_csv("employees_database.csv", index=False)
            st.success("Employee added successfully!")
        else:
            st.warning("You need to fill all the boxes")

