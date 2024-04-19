import streamlit as st
import pandas as pd
st.set_page_config(layout='wide')
csvlink= pd.read_csv('students/FaisalnAisha/employ.csv')
menu=st.sidebar.selectbox("Select Menu",["Register","Database",'Employee File'])
userid='User_'+str(len(csvlink)+1)
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
            st.success("ok")
        dict= {"User ID":[userid],"First Name":[fn],"Last Name":[ln],"Email":[email],'Gender':[gender],"Department":[depart], 'Job Title':[jtitle],"Contract Status":[status],"Monthly Income":[income],"Education Degree":[degree],"Employment Date":[date]}
        tab=pd.DataFrame(dict)
        table2= pd.concat([csvlink,tab],ignore_index=True)
        table2.to_csv("employ.csv",index=False)
space=' '
if menu=='Database':
    st.title(":orange[Database]")
    st.table(csvlink)


if menu == "Employee File":
    side1,side2,side3= st.columns(3)
    with side3:
        st.subheader("Find Employee Details")
        find= st.text_input('Find Employee ID')
        but=st. button("Find")
 
    if but:
        if find:
                try:
                    result=csvlink[csvlink['User ID'].str.lower()== find.lower() ]
                    #st.table(result)
                    nfm=result['First Name'].iloc[0]
                    nlm=result['Last Name'].iloc[0]
                    st.title(f':violet[{nfm}{space}{nlm}]')
                    st.subheader('Personal Information')
                    st.divider()
                    nemail=result['Email'].iloc[0]
                    ngen=result['Gender'].iloc[0]
                    ned=result['Education Degree'].iloc[0]
                    dis1,dis2,dis3=st.columns(3)
                    with dis1:
                        st.write("Email")
                        st.write(f':blue[{nemail}]')
                    with dis2:
                        st.write('Gender')
                        st.write(f':blue[{ngen}]')
                    with dis3:
                        st.write('Educational Level')
                        st.write(f':blue[{ned}]')
                    st.divider()
                    st.subheader('Job Information')
                    st.divider()
                    dis4,dis5,dis6=st.columns(3)
                    ndepart=result['Department'].iloc[0]
                    njb=result['Job Title'].iloc[0]
                    ncs=result['Contract Status'].iloc[0]
                   
                    st.divider()
                    with dis4:
                        st.write("Department")
                        st.write(f':blue[{ndepart}]')
                    with dis5:
                        st.write("Job Title")
                        st.write(f':blue[{njb}]')
                    with dis6:
                        st.write("Contract Status")
                        st.write(f':blue[{ncs}]')
                   
                    nmi=result['Monthly Income'].iloc[0]
                    ned=result['Education Degree'].iloc[0]
                    nedt=result['Employment Date'].iloc[0]
                    dis7,dis8,dis9=st.columns(3)
                    with dis7:
                        st.write("Monthly Income")
                        st.write(f':blue[${nmi}]')
                    with dis8:
                        st.write("Education Degree")
                        st.write(f':blue[{ned}]')
                    with dis9:
                        st.write("Employment Date")
                        st.write(f':blue[{nedt}]')


                except IndexError:
                        st.success('The UserID cannot be found')
        else:
            st.error("Please input value...")
            #change made



