import streamlit as st
import pandas as pd
st.set_page_config(layout='wide')
def code():
    st.title('Streamlit Forms & Salary Calculator')
    menu = ['Home','About']
    choice = st.sidebar.selectbox('Menu',menu)

    if choice == 'Home':
        st.subheader("Forms Tutorial")

        #Salary Calculator
        #Combine forms + columns
        with st.form(key = 'salaryform',clear_on_submit=True): #clear form is simple
            col1,col2,col3 = st.columns(3)
            with col1:
                amount = st.number_input('Hourly rate in $',0,format="%d")
            
            with col2:
                hr = st.number_input("Hours Per Week",1,168)

            with col3:
                st.text("Salary")
                submit_salary = st.form_submit_button('Calculate')
        
        if submit_salary:
            with st.expander("Results"):
                daily = [amount * 7]
                weekly = [amount * hr]
                df = pd.DataFrame({'hourly':amount,'daily':daily,'weekly':weekly})
                st.dataframe(df.T) #Transpose turns from vertical labels to horizontal

        #Method 1: Contect Manager Approach (with)
        with st.form(key='form1',clear_on_submit=True):
            firstname = st.text_input('Firstname')
            lastname = st.text_input('Lastname')
            dob = st.date_input('Date of Birth')

            submit = st.form_submit_button("Register") #very important to submit button
        
        #results can be outside or i the form
        if submit:
            st.success(f"Hello {firstname} you have created an account")

        #Method 2:
        form2 = st.form(key='form2')
        username = form2.text_input("Username")
        jobtype = form2.selectbox("Job",["Teacher",'Programmer','Accountant'])
        submit2 = form2.form_submit_button("Login")

        if submit2:
            st.write(f"{username} your job role is {jobtype}")

    else:
        st.subheader('About')

code()
