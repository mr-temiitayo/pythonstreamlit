import streamlit as st
import pandas as pd

# Main app
st.title("Employee Database App")

# Load the CSV file into a DataFrame
df = pd.read_csv("employees_database.csv")

st.write("Current Database:")
st.dataframe(df)

with st.form(key='employee',clear_on_submit=True):
    # Function to add new employee data to the DataFrame
    def add_employee(name, position, salary, df):
        new_data = {"Name": name, "Position": position, "Salary": salary}
        new_df = pd.DataFrame([new_data])
        df = pd.concat([df, new_df], ignore_index=True)
        return df


    st.write("Update Employee Details:")
    name = st.text_input("Name:")
    position = st.text_input("Position:")
    salary = st.number_input("Salary:", step=1000)

    if st.form_submit_button("Add Employee"):
        if name and position and salary:
            df = add_employee(name, position, salary, df)

            # Save the updated DataFrame back to the CSV file
            df.to_csv("employees_database.csv", index=False)
            st.success("Employee added successfully!")
        else:
            st.warning("You need to fill all the boxes")

