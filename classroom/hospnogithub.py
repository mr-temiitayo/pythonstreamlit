import streamlit as st
import pandas as pd
from PIL import Image
import requests
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
 
    df = pd.read_csv('patientrecords.csv',dtype=zerostr)

    patient_id = "USER_" + str(len(df) + 1) #generate user id 

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
                mobilephone = st.text_input('Mobile Phone')
                homephone = st.text_input('Home Phone')
                city = st.text_input('City||Town')

            with col3b:
                address = st.text_input('Address')
                email = st.text_input('Email')
                postcode = st.text_input('Postcode')

            if st.form_submit_button('Register'):
                patients_df = pd.DataFrame({"Patient ID":[patient_id],"Title":[selected_title],"Registration":[reg],"First Name":[firstname],"Last Name":[lastname],
                        "Date of Birth":[dob],"Second Name":[secondname],"Prefer":[prefer],
                        "Gender":[selected_gender],"Mobile Phone":[mobilephone],"Home Phone":[str(homephone)],"City":[city],
                        "Address":[address],"Email":[email],"Postcode":[str(postcode)]})
                new_df = pd.concat([df,patients_df],ignore_index=False)
                new_df.to_csv(df, index= False)
                st.success('DONE')
                # else:
                #     st.error('Fill all boxes')


#-----------------------------------PATIENTS DATABASE----------------------------------
    if choice == 'Patients Database':
        col4,col5,col6=st.columns([1.5,4,0.5])
        with col5:
            st.title(":orange[Patient Records]")
        st.dataframe(df) # display df on streamlit 
        
        #DOWNLOAD THE FILE
        with open('patientrecords.csv','rb') as file:
            data = file.read() #read the content
        st.download_button(label='Download Patients Database CSV',data=data,file_name='Patients Database.csv')



#------------------------------PATIENTS FILE --------------------------------------
    if choice == 'Patient File':
#        with st.form(key='search',clear_on_submit=True):

            col7,col8,col9 = st.columns([1.5,2,1])
            with col7:
                st.title(":orange[Patient File]")
            with col9:
                usersearch=st.text_input("Enter patient user ID")
                search = st.button('Search Patient') #deleted form button here
                if search:
                    # Filter the DataFrame based on the search query
                    search_result = df[df['Patient ID'].str.contains(usersearch, case=False)]
                    
                    if not search_result.empty:
                        # Access specific values without converting to lists
                        getfirstname = search_result['First Name'].iloc[0]
                        
                        getlastname = search_result['Last Name'].iloc[0]
                        getgender = search_result['Gender'].iloc[0]
                        getdob = search_result['Date of Birth'].iloc[0]
                        getcontact = search_result['Mobile Phone'].iloc[0]
                        getemail = search_result['Email'].iloc[0]
                        getaddress = search_result['Address'].iloc[0]
                        getid = search_result['Patient ID'].iloc[0]




                        #st.write(f'First Name: {firstname}, Last Name: {lastname}')
  
                    else:
                        # If no matching records found, initialize empty variables
                        getfirstname = ""
                        getlastname = ""
                        # Initialize additional variables if needed
            if search:
                container1 = st.container()
                with container1:
                    t11,t12,t13 = st.columns([1.5,3.5,2])
                    with t12:
                        st.header('LASTH MEDICAL RECORDS REQUEST')
                    t21,t22,t23,t24 = st.columns([0.5,2.5,2,2])
                    with t22:
                        #logo = Image.open(r'C:/Users/USER/Downloads/logo2.png') for local image
                        #st.image(logo,50,50) #to use full width
                        # Corrected image URL
                        
                        image_url = "https://raw.githubusercontent.com/mr-temiitayo/pythonstreamlit/main/beta/logo2.png"

                        # Load and display the image directly
                        st.image(image_url, width=50)  # Adjust width and add a caption if needed
                        st.write('**LASTH TEACHING HOSPITAL**')

                    with t24:
                        
                        st.write('327a,coporation drive, Ikoyi')
                        st.write('Lagos. Nigeria')
                        st.write('teeakintoye@yahoo.com')
                        st.write('+2348162644554')
                        
                    st.write('')
                st.write('')
                t31,t32,t33 = st.columns([1.5,2,1])
                with t32:
                    st.subheader("PATIENT'S INFORMATION")
                info1,info2,info3,info4 = st.columns([1.5,2,2,0.5])
                with info2:
                    st.write('Name of Patient')
                    st.write('Gender')
                    st.write('Date of Birth')
                    st.write('Contact Number')
                    st.write('Email Address')
                    st.write('Home Address')

                with info3:
                    st.write(f'**{getfirstname} {getlastname}**')
                    st.write(f'**{getgender}**')
                    st.write(f'**{getdob}**')
                    st.write(f'**{getcontact}**')
                    st.write(f'**{getemail}**')
                    st.write(f'**{getaddress}**')
                    st.write('')
                    st.write('')
                t41,t42,t43 = st.columns([1,2,0.5])
                with t42:
                    st.subheader("MEDICAL RECORDS REQUEST FORM")
                info11,info22,info33,info44 = st.columns([1.5,2,2,0.5])
                with info22:
                    st.write('Request Date')
                    st.write('Medical Records Number')
                with info33:
                    st.write('**2023-08-28**')
                    st.write(f'**{getid}**')
                    



code()

