import streamlit as st
import pandas as pd
st.set_page_config(layout='wide')
donordata=pd.read_csv('blood_donor.csv')
menu=st.sidebar.selectbox("Menu",['Registration','Database'])
if menu == 'Registration':
    st.title(':blue[Register For Blood Donation]')
    col1,col2,col3=st.columns([1.5,1,1])
    with col1:
        st.header("Personal Information")
        name=st.text_input('Input Your Full Name')
        num=st.text_input("Input Phone Number")
        age=st.number_input("Input Your Age",18,65)
        gen=st.selectbox("Select Your Gender",['Male','Female'])
    with col3:
        st.header("Health Information")
        blood=st.selectbox("Select Blood Type",['A','B','AB','O'])
        check=['Yes','No']
        ill=st.radio('Do You Have Any Medical Conditions?',check,horizontal = True)
        insured=st.radio('Do You Have Health Insurance?',check,horizontal = True)
        firstime=st.radio('Have You Donated Blood Before?',check,horizontal= True)
    colu1,colu2,colu3=st.columns([1.5,1,1])
    with colu2:
            col2a,col2b,col2c = st.columns([1,2,1])
            with col2b:
                if st.button("Save Donor Info"):
                    st.success("Donor Data Saved")
                    donordict={'Full Name':[name],'Phone Number':[num],'Donor Age':[age],'Blood Type':[blood],'Medical Condition':[ill],'Insurance Coverage':[insured],"Gender":[gen], 'Prior Donations':[firstime]}
                    donorDF=pd.DataFrame(donordict)
                    combinedata=pd.concat([donordata,donorDF],ignore_index= True)
                    combinedata.to_csv('blood_donor.csv',index=False)
if menu =='Database':
    st.header(":orange[DATABASE]")
    st.table(donordata)

