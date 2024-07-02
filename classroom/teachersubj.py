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


menu = st.sidebar.selectbox('Menu',['School Details','Subject Selection','Submit Scores','Database|Charts'])
if st.sidebar.button("refresh"):
    pass
subjects_csv = pd.read_csv('subjects.csv')
subjectscores_csv = pd.read_csv('subjectscores.csv')

subjects_list = subjects_csv['Subjects'].to_list() #read subjects saved in csv as list
# st.write(subjects_list) 

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


    st.header("Create Your Database Headers")
   
    col1,col2 = st.columns([1,2])
    with col1:
        subjects_name = st.text_input("**Step 1:** Enter each subject name") #enter subjects
        submit_subjects = st.button("Submit")

    with col2:
        student_year = st.radio("Add student year (optional)",['No','Yes'],horizontal=True)
        st.sidebar.write(student_year)
        if submit_subjects:
            subj_dict = {'Subjects':[subjects_name]}
            subj_df = pd.DataFrame(subj_dict)
            subj_join = pd.concat([subjects_csv,subj_df],ignore_index=True)
            subj_join.to_csv('subjects.csv',index=False)
            st.sidebar.success(f"{subjects_name} Submitted")


    
    all_subjects = st.multiselect("**Step 2:** Confirm subjects to create here",subjects_list,default=subjects_list) #display all subjects chosen
    
    cols_button = st.button('Create subject columns') #button to create columns
    
    if cols_button:
        for subject in all_subjects: #loop through multiselect box
            if subject not in subjectscores_csv.columns: #avoid duplicates
                subjectscores_csv[subject] = '' #column values after columns created
                
        # Delete the column named 'Subjects'
        if 'Subjects' in subjectscores_csv.columns:
            subjectscores_csv.drop(columns=['Subjects'], inplace=True)
        subjectscores_csv.to_csv('subjectscores.csv',index=False)
        st.sidebar.success('Subjects created')


#------------DELETE SUBJECTS     
    # col3, col4 = st.columns(2)
    # with col3:
    #     del_subject = st.multiselect('Choose subject(s) to delete',subjects_list,default=subjects_list)

    # with col4:
    #     del_student = st.text_input("Enter student ID to delete")

if menu == 'Submit Scores':
    st.header('Submit Student Scores')
    col1, col2 = st.columns(2)

    name = st.text_input("Enter student name")

    # create a dictionary to store the student's scores with default name
    student_data = {'Name': name}

    # Create columns for each subject
    for i, subject in enumerate(subjects_list):
        if i % 2 == 0:
            with col1:
                score = st.number_input(f'Enter student score for {subject}', min_value=0, max_value=100, step=10, key=subject)
        else:
            with col2:
                score = st.number_input(f'Enter student score for {subject}', min_value=0, max_value=100, step=10, key=subject)

        #add the subject loop in the dictionary
        student_data[subject] = score

    if st.button("Save Student Scores"):
        student_df = pd.DataFrame(student_data)
        student_join = pd.concat([subjectscores_csv,student_df],ignore_index=True)
        student_join.to_csv('scores.csv')
        st.success()

if menu == 'Database|Charts':
    st.header("Students Database|Charts")
    # exclude_subj = subjectscores_csv.drop(columns=['Subjects'], errors='ignore')
    st.table(subjectscores_csv)


