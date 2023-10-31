import streamlit as st


import pandas as pd
st.set_page_config(layout='wide')
df = pd.read_csv('employee.csv')
user_id = 'USER'  +  str(len(df) + 1) 


menu = st.sidebar.selectbox('Menu',['Register here','Employee file', 'Database'])


if menu =='Register here':


    st.subheader('Register your employee')
    r1,r2 = st.columns(2)


    with r1:
       fn = st.text_input('Enter first name')
       email = st.text_input('Enter email')
       education = st.selectbox('Education level',['College','Masters degree','Bachelors degree','Post-graduate'])
       dep = st.selectbox('Department',['Sales','Engineering','Marketing','Management'])
       empdate = st.date_input('Employment date')
#intern junior senior supervisor manager
    with r2:
       ln = st.text_input('Enter last name')
       gender = st.radio('Select gender',['Male','Female'],horizontal=True)
       salary = st.number_input('Monthly salary')
       title = st.selectbox('Job title',['Intern','Junior','Senior','Supervisor','Manager'])
       status = st.selectbox('Employee status',['Part time','Full time'])
   
    date = st.date_input('Enter the registration date')


    if st.button('Submit'):
        employee_df = pd.DataFrame({"User ID":[user_id], "First name":[fn],"Last name":[ln],"Email":[email],"Gender":[gender],
                                    "Education":[education],"Salary":[salary],"Department":[dep],
                                    "Job title":[title],"Employment date":[empdate],"Employee status":[status]})
        new_df = pd.concat([df,employee_df])
        new_df.to_csv('employee.csv',index=False)
        st.success("New Employee Added")




if menu == 'Employee file':
    t1,t2,t3 = st.columns(3)
    with t3:
        st.subheader('Find an employee here')
        st.write('')
        find1, find2 = st.columns([2,0.5])
        with find1:
            employee = st.text_input('Enter Employee ID')
            findbutton = st.button('Find Employee')
            

    if findbutton:
        if employee:
            find_result = df[df['User ID'] == employee]
            # st.dataframe(find_result)
            #put a check incase user types wrong id. let it say Please enter correct Employee Id
            if not find_result.empty:

                getid = find_result['User ID'].iloc[0]
                getid = find_result['First name'].iloc[0]
                getid = find_result['Last name'].iloc[0]
                getid = find_result['Email'].iloc[0]
                getid = find_result['Gender'].iloc[0]
                getid = find_result['Education'].iloc[0]
                getid = find_result['Salary'].iloc[0]
                getid = find_result['Department'].iloc[0]
                getid = find_result['Job title'].iloc[0]
                getid = find_result['Employment date'].iloc[0]
                getid = find_result['Employee status'].iloc[0]
            








            
            else:
                st.error("Kindly Type In A Valid ID")

if menu =='Database':
    st.dataframe(df,use_container_width=True)
