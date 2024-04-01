import pandas as pd
import streamlit as st

# Function to load the employee data
def load_data():
    return pd.read_csv("employee_data.csv")

# Function to save the employee data
def save_data(df):
    df.to_csv("employee_data.csv", index=False)

# Function to add a new employee
def add_employee(df, user_id, first_name, last_name, gender, email, department, seniority_level, contract_status, education, salary):
    new_employee = pd.DataFrame({
        "UserID": [user_id],
        "FirstName": [first_name],
        "LastName": [last_name],
        "Gender": [gender],
        "MailAddress": [email],
        "Department": [department],
        "SeniorityLevel": [seniority_level],
        "ContractStatus": [contract_status],
        "Education": [education],
        "Salary": [salary]
    })
    df = df.append(new_employee, ignore_index=True)
    save_data(df)
    st.success("Employee added successfully!")
    return df

# Function to search for an employee by UserID
def search_employee_by_id(df, user_id):
    result = df[df['UserID'] == user_id]
    return result

def main():
    st.title("Employee Database")

    df = load_data()

    # Sidebar for adding a new employee
    st.sidebar.title("Add New Employee")
    user_id = st.sidebar.text_input("UserID")
    first_name = st.sidebar.text_input("First Name")
    last_name = st.sidebar.text_input("Last Name")
    gender = st.sidebar.selectbox("Gender", ["Male", "Female", "Other"])
    email = st.sidebar.text_input("Email")
    department = st.sidebar.text_input("Department")
    seniority_level = st.sidebar.text_input("Seniority Level")
    contract_status = st.sidebar.selectbox("Contract Status", ["Full-time", "Part-time", "Contract"])
    education = st.sidebar.text_input("Education")
    salary = st.sidebar.number_input("Salary", min_value=0)

    if st.sidebar.button("Add Employee"):
        df = add_employee(df, user_id, first_name, last_name, gender, email, department, seniority_level, contract_status, education, salary)

    # Main section for searching employees
    st.header("Search Employee")
    search_user_id = st.text_input("Enter UserID to search")
    if st.button("Search"):
        search_result = search_employee_by_id(df, search_user_id)
        if not search_result.empty:
            st.write(search_result)
        else:
            st.warning("No matching employee found.")

    # Display current employee data
    st.header("Current Employee Data")
    st.write(df)

if __name__ == "__main__":
    main()
