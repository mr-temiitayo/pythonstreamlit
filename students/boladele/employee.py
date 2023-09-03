import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')

employeedb = 'employeedb.csv'
df = pd.read_csv(employeedb)


#,columns=["First Name","Last Name","Email","Gender","Job Title","Department","Employment Date","Job Status","Reg Date"]
def new_employee(first,last,email,selectedgender,jtitle,jdept,doe,jstatus,reg,df):
    employee_dict = {'First Name':first,'Last Name':last,'Email':email,'Gender':selectedgender,
                    'Job Title':jtitle,'Department':jdept,'Employment Date':doe,'Job Status':jstatus,'Reg Date':reg}
    employee_df = pd.DataFrame([employee_dict]) 
    df = pd.concat([df,employee_df],ignore_index=True)
    return df

menu = ['Register Staff','Staff Database']
choice = st.sidebar.selectbox('Menu',menu)


if choice =='Register Staff':

    with st.form('Register',clear_on_submit=True):

        name1,name2=st.columns(2)
        with name1:
            first=st.text_input('First')
        with name2:
            last=st.text_input('Last')


        eg1,eg2=st.columns(2)


        with eg1:
            email=st.text_input('Email')
        with eg2:
            gender=['Male','Female']
        selectedgender=st.radio('Select Gender',gender,horizontal=True)


        stat1,stat2=st.columns(2)
        with stat1:
            title=['Board  of Director','Supervisor','Senior staff','Junior staff', 'Intern']
            jtitle=st.selectbox('Job Title',title)


        with stat2:
            department=['Accounting Dept','Engineering Dept','Human Resources','Security Dept','Medical Dept','Tranportation Dept']
            jdept=st.selectbox('Department',department)


        sd1,sd2=st.columns(2)
        with sd1:
            doe=st.date_input('Date of Employment')
        with sd2:
            status=['Part time','Full time']
            jstatus=st.selectbox('Status',status)

        reg=st.date_input('Registration Date')

        if st.form_submit_button('Register'):
            df=new_employee(first,last,email,selectedgender,jtitle,jdept,doe,jstatus,reg,df)
            df.to_csv(employeedb,index=False)
            st.success('Information Saved')

if choice == 'Staff Database':
    st.dataframe(df)