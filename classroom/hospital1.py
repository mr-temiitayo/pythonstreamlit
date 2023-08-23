import streamlit as st
import pandas as pd
st.set_page_config(layout='wide')

# create menu
# create form
# create df
# create numbers as strings
# retain leading zeros in numbers
# create unique ids to search or phone numbers if patient dont remember ID
#using qr code for website


def code():
    zerostr = {'ID': str,"Home Phone": str,"Work Phone":str,"Postcode":str,"Mobile Phone":str}
 
     #Load the employee CSV file as a dataframe
    
    df = pd.read_csv("patientrecords.csv",dtype=zerostr)

    patient_id = "USER_" + str(len(df) + 1) #generate user id 


    def new_patient(patient_id,selected_title,reg,firstname,lastname,dob,secondname,prefer,
                    selected_gender,homephone,workphone,city,mobilephone,email,postcode,df): #func to process each patient data

        patient_dict = {"Patient ID":patient_id,"Title":selected_title,"Registration":reg,"First Name":firstname,"Last Name":lastname,
                        "Date of Birth":dob,"Second Name":secondname,"Prefer":prefer,
                        "Gender":selected_gender,"Home Phone":homephone,"Work Phone":str(workphone),"City":city,
                        "Mobile Phone":str(mobilephone),"Email":email,"Postcode":str(postcode)} #create a dict for each student data
        patient_df = pd.DataFrame([patient_dict]) #convert the dict to a df
        df = pd.concat([df,patient_df], ignore_index = True) #append new df above to the exisiting df (df)
        #ignore means if dupplicate data then overwrite existing one
        return df


    menu= ['Register','Patient File','Patients Database','About'] #list for menu options
    choice = st.sidebar.selectbox('Menu',menu) #create list for menu options

    if choice =='Register':
        col1, col2,col3 = st.columns([1.5,4, 0.5])
        with col2:
            st.title(":orange[Hospital Patient Registration]") #colors: blue, green, orange, red, violet.

        with st.form(key ='personal',clear_on_submit=True):
           
            #-----------------1ST SECTION-------------------------
            st.subheader(":orange[PATIENT PERSONAL DETAILS]")
            
            col1a,col1b = st.columns(2)
            with col1a:
                title = ["Mr", "Mrs", "Miss", "Ms"]
                selected_title = st.radio('Select Title',title,horizontal=True)
                st.write(selected_title)

            with col1b:
                reg = st.date_input('Date of Registration')
            
            col2a,col2b = st.columns(2)
            with col2a:
                firstname = st.text_input("First Name")
                lastname = st.text_input("Last Name")
                dob = st.date_input('Date of Birth')

            with col2b:
                secondname = st.text_input("Second Name")
                prefer = st.text_input("Preferred Name")
                gender = ['Male','Female']
                selected_gender = st.radio('Select',gender,horizontal=True)
            
            st.write("")      #breakline
            
            #-----------------2ND SECTION-------------------------
            st.subheader(':orange[PATIENT CONTACT DETAILS]')
           
            col3a,col3b = st.columns(2)
            with col3a:
                homephone = st.text_input('Home Phone')
                workphone = st.text_input('Work Phone')
                city = st.text_input('City||Town')

            with col3b:
                mobilephone = st.text_input('Mobile Phone')
                email = st.text_input('Email')
                postcode = st.text_input('Postcode')
            if st.form_submit_button('Register'):
#                if all([selected_title,reg,firstname,lastname,dob,secondname,prefer,
#            selected_gender,homephone,workphone,city,mobilephone,email,postcode]):
                df = new_patient(patient_id,selected_title,reg,firstname,lastname,dob,secondname,prefer,
        selected_gender,homephone,workphone,city,mobilephone,email,postcode,df)
                df.to_csv("patientrecords.csv", index= False)
                st.success('DONE')
                # else:
                #     st.error('Fill all boxes')

    if choice == 'Patients Database':
        col4,col5,col6=st.columns([1.5,4,0.5])
        with col5:
            st.title(":orange[Patient Records]")
        st.dataframe(df) # display df on streamlit 

    if choice == 'Patient File':
        col7,col8,col9 = st.columns([1.5,2,1])
        with col7:
            st.title(":orange[Patient File]")
        with col9:
            st.text_input("Enter patient user ID")

    if choice == 'Buy Drugs':
        
        pass
code()