import streamlit as st
import pandas as pd
import plotly.express as px #to plot graphs/charts


# submit score -
# add percentage ####
# database with chart with filter
# edit the database
# search students file
# download the database
# send mail

st.set_page_config(layout='wide')

menu = st.sidebar.selectbox('Menu',['Submit Scores','Search Student','Students Database','Edit Database'])
df= pd.read_csv('scores.csv', dtype= {'Average':str})


if menu == "Submit Scores":
  col1,col2,col3 = st.columns([1,2,1])
  with col2:
    st.header(':orange[Submit Students Scores Here]')
  with st.form(key = 'scores', clear_on_submit=True):
    name = st.text_input("Enter the student's name: ")
    col4,col5 = st.columns(2)
    with col4:
        maths = st.number_input("Enter the student's score for Maths: ",0,100,value=50,step=10)
        english = st.number_input("Enter the student's score for English: ",0,100,value=50,step=10)
        geography = st.number_input("Enter the student's score for Geography: ",0,100,value=50,step=10)
    with col5:
        science = st.number_input("Enter the student's score for Science: ",0,100,value=50,step=10)
        history = st.number_input("Enter the student's score for History: ",0,100,value=50,step=10)

    total = maths + english + science + history + geography
    average = total / 5

    if average >= 95:
        grade = "A+"
    elif average >= 90 and average < 95:
        grade = "A" 
    elif average >= 80 and average < 90:
        grade = "B"
    elif average >= 70 and average <80:
        grade = "B-"
    elif average >= 60 and average < 70:
        grade = "C"
    elif average >= 50 and average < 60:
        grade = "D"
    elif average >= 40 and average < 50:
        grade = "E"
    elif average < 40:
        grade = "F"

    show1,show2 = st.columns(2)
    with col5:
        st.write('')
        st.write('')
    if st.form_submit_button('Submit Student Scores'):
        students_df= pd.DataFrame({'Name':[name],'Maths':[maths],'English':[english],'Science':[science],
                    'History':[history],'Geography':[geography],'Total':[total],'Average':[average],'Grade':[grade]})
    
        new_df=pd.concat([df,students_df],ignore_index=True)
        new_df.to_csv('scores.csv',index=False)
        with show1:
          st.success(f"{name}'s total score is {total}. The average is {average}. And the grade is {grade}")


if menu == 'Students Database':
  
  cola, colb, col3c = st.columns(3)
  
  
  col1,col2,col3 = st.columns([1,2,1])
  with col2:
    st.header(':orange[Student Grades Database]')
  #Open a csv file
  
  st.table(df)

  with open('scores.csv','rb') as file: #with ensures it opens and closes properly
    data = file.read() #read the file content above and stores in var data
    st.download_button(label='Download Students Database CSV',data=data,file_name='Students Database.csv')



  subjects = ['English','Science','History','Geography']

  subjects_scores = df[subjects].mean().reset_index()
  subjects_scores = subjects_scores.round(2)
  subjects_renamed = subjects_scores.rename(columns={'index': 'Subject', 0: 'Total'})
  # st.write(subjects_renamed)

  barchart = px.bar(subjects_renamed, x='Subject',y='Total')

  st.plotly_chart(barchart, use_container_width=True)

  # Create a pie chart for different grade column counts
#   grade_counts = df['Grade'].value_counts().reset_index()
#   st.write(grade_counts)
  # grade_counts = grade_counts.rename(columns={'index': 'Grade', 'Grade': 'Count'})
  # st.write(grade_counts)

#   piechart = px.pie(grade_counts, names='Grade', values='count')
#   st.plotly_chart(piechart)
  
