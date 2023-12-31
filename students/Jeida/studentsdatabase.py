import streamlit as st
import pandas as pd

#Project Objective
# Create a student scores database which can 
# -get the name
# -4 subjects
# -calculate the average
# -calculate the grade (A,B,C,D,E,F)
# -update your csv file

#what is csv file?
#csv file are text files that each data is separated by a comma (comma separated values)

st.set_page_config(layout='wide')
col1,col2,col3 = st.columns([1,2,1])
with col2:
  st.header(':orange[Student Grades Database]')
#Open a csv file
df= pd.read_csv('scores.csv')
# st.dataframe(df,use_container_width=True)


name = st.text_input("Enter the student's name: ")
col4,col5 = st.columns(2)
with col4:
  maths = st.number_input("Enter the student's score for Maths: ",0,100,value=50)
  english = st.number_input("Enter the student's score for English: ",0,100,value=50)
  geography = st.number_input("Enter the student's score for Geography: ",0,100,value=50)
with col5:
  science = st.number_input("Enter the student's score for Science: ",0,100,value=50)
  history = st.number_input("Enter the student's score for History: ",0,100,value=50)

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
  if st.button("Submit Student Scores"):
      students_df= pd.DataFrame({'Name':[name],'Maths':[maths],'English':[english],'Science':[science],
                  'History':[history],'Geography':[geography],'Total':[total],'Average':[average],'Grade':[grade]})
  
      new_df=pd.concat([df,students_df],ignore_index=True)
      new_df.to_csv('scores.csv',index=False)
      with show1:
        st.success(f"{name}'s total score is {total}. The average is {average}. And the grade is {grade}")

#adjust hospital and employ