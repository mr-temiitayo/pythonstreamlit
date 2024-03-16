import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')
csvlink= pd.read_csv('employ.csv')
user_id = 'USER_' + str(len(csvlink) + 1)


menu=st.sidebar.selectbox("Select Menu",["Register","Database","Employee File"])
space = ' '
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
    top1,top2,top3 = st.columns(3)

    with top3:
        st.subheader("Find Employee Details")
        search = st.text_input("Find Employee ID")
        find = st.button("Find Employee")
# User ID,First Name,Last Name,Email,Gender,Department,
# Job Title,Contract Status,Monthly Income,Education Degree,Employment Date

    if find: #check if button clicked
        if search: #check if data is in the variable
            try:
                search_result = csvlink[csvlink['User ID']== search]  #USER4
                #above, we created a filtered table from the original table, 
                #1 using the ID column and 2. now looking for search input text from the column
                st.table(search_result)
                newfn = search_result['First Name'].iloc[0] #get table,check column and extract first item!
                newln = search_result['Last Name'].iloc[0]
                st.subheader(f':orange[{newfn}  {space}  {newln}]')
            
            except IndexError:
                st.error("I can't find that USER ID")




        else:
            st.error("Please enter a user ID")





#1 how do i ensure it shows the result of the button
#on the full page to the left?
            
#2 how do i ensure it informs you if nothing is in 
# the box but you clicked the button?