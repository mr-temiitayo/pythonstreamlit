import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')
csvlink= pd.read_csv('employ.csv')
user_id = 'USER_' + str(len(csvlink) + 1)


menu=st.sidebar.selectbox("Select Menu",["Register","Database","Employee File"])

if menu == "Register":
    st.title(":orange[Register Here]")
    co1,co2=st.columns(2)
    with co1:
        fn=st.text_input("First Name")
        email=st.text_input("Email Address")
    with co2:
        ln=st.text_input("Last Name")
        gender=st.selectbox("Gender",["Male","Female"])
    depart=st.selectbox("Department",['Management','Accounting','Engineering','Human Resources','Security'])
    jtitle=st.selectbox("Job Title",["Board Director","CEO",'Supervisor','Senior Staff','Paid Intern', 'Unpaid Intern'])
    co3,co4=st.columns(2)
    with co3:
       status= st.selectbox("Contract Status",["Full Time", "Part time"])
    with co4:
        income=st.number_input("Monthly Income: ",100,750000)
    degree=st.selectbox("Educational degree",["Bachelor's Degree",'None','Associate Degree','Graduate Degree'])
    date=st.date_input('Employment Date:')
   
    if st.button('Submit Employee Data'):
        col5,col6,=st.columns(2)
        with col5:
            st.success("Employee Information Saved")
        dict= {"User ID": [user_id],"First Name":[fn],"Last Name":[ln],"Email":[email],'Gender':[gender],"Department":[depart], 'Job Title':[jtitle],"Contract Status":[status],"Monthly Income":[income],"Education Degree":[degree],"Employment Date":[date]}
        tab=pd.DataFrame(dict)
        table2= pd.concat([csvlink,tab],ignore_index=True)
        table2.to_csv("employ.csv",index=False)


if menu=='Database':
    st.title(":orange[Database]")
    st.table(csvlink)

    
if menu == "Employee File":
    pass