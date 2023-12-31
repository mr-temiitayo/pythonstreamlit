import streamlit as st
import pandas as pd
st.set_page_config(layout='wide')
df=pd.read_csv('employeedb1.csv')
employee_id = 'User' + str(len(df) + 1)
menu = st.sidebar.selectbox('Employee',['Register Here','Employee data base','Employee File'])
if menu == 'Register Here':
    st.header('Register Here')
    firstn, lastn = st.columns(2)
    with firstn:
        firstname = st.text_input('Enter your firstname')
        email = st.text_input('Enter your email')
        el = st.selectbox("Education level",["Masters","Bacherlors","OND","HND"])
        department = st.selectbox('Department',['Security','Cleaning','IT','Sales','Finance','Purchasing','Accounting','Operations','Marketing','Researsh and development','Production','General management','Administration'])
        date = st.date_input('Enter the Employment date')
    with lastn:
        lastname = st.text_input('Enter your lastname')
        gender=st.radio("Gender",["Male","Female"],horizontal=True)
        salary = st.number_input('Enter your monthly salary',0)
        jobtitle = st.selectbox('Job title',['Entry','Individual Contributor','Manager','Director','Vice chief','Chief','Chairperson'])
        employeestatus = st.selectbox('Employee status',['Part time','Full time'])
    Registration = st.date_input('Enter the Registration date')
    if st.button('Add Employee Data'):
        employee_df = pd.DataFrame({'User ID':[employee_id],'Firstname':[firstname],'Lastname':[lastname],'email': [email],'gender':[gender],'education level':[el],
                    'salary':salary,'department':[department],'job title':[jobtitle],'employment date':[date],'employee status':[employeestatus],'Registration':[Registration]})
        new_df = pd.concat([df,employee_df],ignore_index=True)
        new_df.to_csv('employeedb1.csv',index=False)
        st.success('New Employee Added')
if menu == 'Employee File':
    s1,s2,s3 = st.columns(3)
    with s3:
        st.header('Find Employee')
        EmployeeID = st.text_input('Search Employee Details')
        Search = st.button('Find Employee')
    if Search:
        if EmployeeID:
            search_result = df[df['User ID'] == EmployeeID]
            st.write(search_result)


if menu ==('Employee data base'):
    st.dataframe(df,use_container_width=True)