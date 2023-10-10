import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')

menu = ['Register Staff','Staff Database','Staff File']
choice = st.sidebar.selectbox('Menu',menu)

df= pd.read_csv('employee.csv')
userid = 'USER' + str(len(df) + 1)

if choice == 'Staff Database':
    st.dataframe(df,use_container_width=True)

    #creating user ID for employees
    

if choice == 'Register Staff':
 st.subheader("Employee's Name")
 fn,ln = st.columns(2)
 with fn:
     name = st.text_input("First Name: ")
 with ln:
     name2 = st.text_input("Last Name: ")
 mail,gender = st.columns(2)
 with mail:
     mail = st.text_input("Email Adress: ")
 with gender:
     gender = st.selectbox(
         'Gender',
         ('Male', 'Female', 'Other'))
     
 department = st.selectbox(
    'Department',
    ('Management', 'Accounting', 'Engineering', 'Human Resources', 'Security', 'Medical', 'Transportation')) 

 jobttle = st.selectbox(
    'Job Title',
    ('Board Of Directors', 'Supervisor', 'Senior Staff', 'Junior Staff', 'Paid Intern', 'Unpaid Intern'))
 
 tmspent,salary = st.columns(2)
 with tmspent:
     timespent = st.selectbox(
         'Contract Status',
         ('Full Time', 'Part Time'))
 with salary:
     salary = st.number_input("Monthly Income: ",0,value=10000,step=100)

 edulevel = st.selectbox(
     'Educational Degree',
     ('None', 'Associate Degree', 'Bachelor Degree', 'Graduate Degree', 'Professional Degree', 'Doctoral Degree'))
 
 date = st.date_input("Employememt Date")
 
 df= pd.read_csv('employee.csv')
 def add_employ(userid,name,name2,date,salary,gender,mail,department,jobttle,edulevel,timespent,df):
  employ_dict = {'User ID':userid,'First Name':name,'Last Name':name2,'Date of Employment':date,'Salary':salary,'Gender':gender,'Mail Address':mail,'Department':department,
                  'Seniority Level':jobttle,'Education Level':edulevel,'Contract Status':timespent}
  employ_df = pd.DataFrame([employ_dict]) 
  df = pd.concat([df,employ_df],ignore_index=True) 
  return df

 if st.button("Submit Employee Data"):
     if (name and name2 and date and salary and gender and mail and department and jobttle and edulevel and timespent):
        df = add_employ(userid,name,name2,date,salary,gender,mail,department,jobttle,edulevel,timespent,df)
        df.to_csv('employee.csv',index=False)
        st.success('Employee Data Saved')
     else:
         st.error('Kindly fill all the boxes')

if choice == 'Staff File':
   st.subheader("Find Employee Details")
   space1,space2,finder = st.columns([2,2,1.5])
   with finder:
        find = st.text_input("Enter Employee ID ")
        if st.button("Find Employee"):
            if find:
                findresult = df[df['User ID'] == find ] #new df to filter ID with search only
                st.write(findresult)
                getfirstname = findresult['First Name'].iloc[0] #iloc is the index position of dataframes'
                getlastname = findresult['Last Name'].iloc[0]
                st.subheader(getlastname)
                st.write(getfirstname)
