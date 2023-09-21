# Create an employee database, that shows the name of employee, date of employment (use st.date),
#salary, gender, position/role, education level, contract status (full/part)



import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')
menu = st.sidebar.selectbox('Menu',['Registration','Employee File','Database']) #menu bar


df = pd.read_csv("employee_db.csv")

employee_id = 'USER' + str(len(df) +1)

def new_employee(employee_id,firstname,lastname,email,education,dept,date,gender,salary,job,emp_status,df):
    employee_dict = {"Employee ID":employee_id,"Firstname":firstname,"Email" : email,"Education":education,"Dept":dept,"Registrationdate": date,"Lastname" : lastname,"Gender" : gender,"Salary" :salary,"Job" : job,"Employee" : emp_status}
    employee_df = pd.DataFrame([employee_dict])
    df = pd.concat([df,employee_df],ignore_index = True)
    return df


if menu == 'Registration':


    st.title ("Register Here")
    row1,row2 = st.columns(2)
    with row1:
        firstname = st.text_input("Enter in your firstname")
        email = st.text_input("Enter in your email")
        education = st.selectbox("Education level",["Masters","Bacherlors","OND","HND"])
        dept = st.selectbox("Department",["Department","Manegment","Acounting Dept","Engineering Dept","HumanResources Dept","Security","Medical Dept","Transportation"]) #dropdown
        date = st.date_input('Enter the Employment date')


    with row2:
        lastname = st.text_input("Enter in your lastname")
        gender=st.radio("Gender",["Male","Female"],horizontal=True) #Select toogle
        salary = st.number_input("Enter in your monthly salary",value=1000, step = 100, format = "%d")
        job = st.selectbox("Job title",["Intern","Junior","Senior"])
        emp_status = st.selectbox("Employee Status",["Part time", "Full Time"])
    date = st.date_input('Enter the Registration date')
    if st.button("Add Employee Data"):
        if firstname and email and education and dept and date and lastname and gender and salary and job and emp_status:
            df = new_employee(employee_id,firstname,email,education,dept,date,lastname,gender,salary,job,emp_status,df)
            df.to_csv("employee_db.csv",index = False)
            st.success("You have been successfully added")


        else:
            st.error("You need to fill in the boxes")



if menu == 'Database':
    st.title('Employee Database')


    st.dataframe(df,use_container_width=True)
 

if menu == 'Employee File':
    col1,col2,col3 = st.columns([2,2,1])
    with col3:
        employeesearch = st.text_input("Enter Employee",label_visibility='collapsed',placeholder='Enter Employee ID')