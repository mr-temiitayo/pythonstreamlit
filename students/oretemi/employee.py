import streamlit as st
import pandas as pd
st.set_page_config(layout="wide")

csvfile = pd.read_csv("SDatabase.csv")
menu = st.sidebar.selectbox("Menu",["Register Staff","Staff Database","Staff File"])

userid = 'USER_' + str(len(csvfile)+1)

if menu == "Register Staff":  #staff registration
    st.subheader("Registration")
    colm1,colm2 = st.columns(2)
    colm3,colm4 = st.columns(2)
    colm5,colm6 = st.columns(2)
    colm7,colm8 = st.columns(2)


    with colm1:#user_fn
        user_fn = st.text_input("First Name")
    with colm2:#user_ln
        user_ln = st.text_input("Last Name")
    with colm3:#user_email
        user_email = st.text_input("Email Address")
    with colm4:#user_gen
        user_gen = st.selectbox("Gender",["Male","Female"])
    with colm7:#user_dep
         user_dep = st.selectbox("Department",["Management","Accounting","Engineering"
                                               ,"Security","Medical","Transportation"])
    with colm8:#user_jt
        user_jt = st.selectbox("Job Title",["Board Of Directors","Supervisor","Senior Staff",
                                            "Junior Staff","Paid Intern","Unpaid Intern"])
    with colm5:#user_cs
        user_cs = st.selectbox("Contract Status",["Full Time",'Half Time'])
    with colm6:#user_mi
        user_mi = st.number_input("Monthly Income",1000,step=1000)
    user_ed = st.selectbox("Educational Degree",["None","Associate Degree","Bachelor Degree"
                                                 ,"Graduate Degree","Professional Degree","Doctoral Degree"])
    user_empd = st.date_input("Emploment Date")


    btn = st.button("Submit Employee Data")


    if btn:
        colm9,colm10 = st.columns(2)
        with colm9:
            st.success("Employee Information has been saved.")
        with colm10:
            st.write("")
        btndict = {"User ID":[userid],"First Name":[user_fn],"Last Name":[user_ln],"Email":[user_email] #full btn list
                   ,"Gender":[user_gen],"Department":[user_dep],"Job Title":[user_jt]
                   ,"Contract Status":[user_cs],"Monthly Income":[user_mi]
                   ,"Educational Degree":[user_ed],"Employment Date":[user_empd]}
        stafftable = pd.DataFrame(btndict)
        staff = pd.concat([csvfile,stafftable],ignore_index=True)
        staff.to_csv("SDatabase.csv",index=False)


if menu == "Staff Database":
    st.table(csvfile)


if menu == 'Staff File':
    colma1,colma2,colma3 = st.columns(3)


    with colma3:
        st.subheader("Find Employee Details")
        find1,find2 = st.columns([2,1])
        with find1:
            find = st.text_input("Insert Employee's ID")
            findemp = st.button("Find Employee")
    if findemp: #if button clicked
        if find: #if data in variable
            searchresult = csvfile[csvfile['User ID'] == find]
            st.table(searchresult)
            getfn = searchresult['First Name'].iloc[0] #extract column values using index positions
            getln = searchresult['Last Name'].iloc[0]



        else: #no data in variable
            with find1: #put result in button column
                st.error('Please enter a User ID')


