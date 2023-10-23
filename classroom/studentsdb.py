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
st.header('Student Scores Database')


#Open a csv file
df= pd.read_csv('scores.csv')
st.dataframe(df,use_container_width=True)

name = st.text_input("Enter the student's name: ")
col1,col2=st.columns(2)
with col1:
  maths = st.number_input("Enter the student's score for Maths: ",0,value=70,step=1)
  english = st.number_input("Enter the student's score for English: ",0,value=70,step=1)
  science = st.number_input("Enter the student's score for Science: ",0,value=70,step=1)
with col2:
  
  history = st.number_input("Enter the student's score for History: ",0,value=70,step=1)
  geography = st.number_input("Enter the student's score for Geography: ",0,value=70,step=1)
total = maths + english + science + history + geography
average = total / 5


if average <= 100 and average >= 95:
  grade = "A+"
elif average < 95 and average <= 90:
  grade = "A" 
elif average < 90 and average >= 80:
  grade = "B"
elif average < 80 and average >=75:
  grade = "B-"
elif average <= 70 and average >= 60:
  grade = "C"
elif average < 60 and average >= 50:
  grade = "D"
elif average < 50 and average >= 40:
  grade = "E"
elif average < 40:
  grade = "F"


with col2:
  st.write('')
  st.write('')
  if st.button("Submit Student Scores"):
    student_df = pd.DataFrame({'Name':[name],'Maths':[maths],'English':[english],'Science':[science],
                    'History':[history],'Geography':[geography],'Total':[total],'Average':[average],'Grade':[grade]})
    df = pd.concat([df,student_df],ignore_index=True)
    df.to_csv('scores.csv',index=False)
    st.success(f"{name}'s total score is {total}. The average is {average}. And the grade is {grade}")
