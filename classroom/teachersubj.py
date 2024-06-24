# idea is to enter number of subjects 
# create an input for teachers to enter name of subjects
# this input is then converted to a list
# this list is shown as a multiselect box
# this is then asked to create or remove from the subjects
# then a button to create df columns from
# proceed to create submission area for the scores  
# a multiselect to delete some subjects/students or all from in the admin page
# using clearing columns or rows



import streamlit as st
import pandas as pd


menu = st.sidebar.selectbox('Menu',['School Details','Subject Selection','Subjects Scores','Database|Charts'])
if st.sidebar.button("refresh"):
    pass
subjects_csv = pd.read_csv('subjects.csv')

# subjects = [n for n in range(1,21)]
# subjects.insert(0,'Choose')


if menu == 'School Details':
    st.header("School Details here")
    col1, col2 = st.columns([2,1])

    with col1:
        logo = st.file_uploader("Upload school logo", type = ['jpeg','png', 'jpg'])
        contact = st.text_input("Enter school contact number")

    with col2:
        school_name = st.text_input("Enter school name")
        st.write("")
        country = st.selectbox('Choose country',['UAE','Nigeria'])

    address = st.text_input("Enter school address")

if menu == 'Subject Selection':


    st.header("Teachers Subjects Database")
   
    subjects_list = subjects_csv['Subjects'].to_list() #read subjects saved in csv as list
    # st.write(subjects_list) 

    col1,col2 = st.columns([1,2])
    all_subjects = st.multiselect("**Step 2:** Confirm subjects to create here",subjects_list,default=subjects_list) #display all subjects chosen
    
    cols_button = st.button('Create subject columns') #button to create columns
    if cols_button:
        for subject in all_subjects: #loop through multiselect box
            if subject not in subjects_csv.columns: #avoid duplicates
                subjects_csv[subject] = '' #column values after columns created
        subjects_csv.to_csv('subjects.csv',index=False)
        st.sidebar.success('Subjects created')


    
   
    with col1:
        subjects_name = st.text_input("**Step 1:** Enter each subject name") #enter subjects
        submit_subjects = st.button("Submit")

        if submit_subjects:
            subj_dict = {'Subjects':[subjects_name]}
            subj_df = pd.DataFrame(subj_dict)
            subj_join = pd.concat([subjects_csv,subj_df],ignore_index=True)
            subj_join.to_csv('subjects.csv',index=False)
            st.sidebar.success(f"{subjects_name} Submitted")

    


    col3, col4 = st.columns(2)
    with col3:
        del_subject = st.multiselect('Choose subject(s) to delete',subjects_list,default=subjects_list)

    with col4:
        del_student = st.text_input("Enter student ID to delete")



if menu == 'Database|Charts':
    st.header("Students Database|Charts")
    exclude_subj = subjects_csv.drop(columns=['Subject'], errors='ignore')
    st.table(exclude_subj)