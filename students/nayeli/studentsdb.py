#Project Objective
# Create a student scores database which can 
# -get the name
# -4 subjects
# -calculate the average
# -calculate the grade (A,B,C,D,E,F)
# -save and update in a csv file

import streamlit as st

import pandas as pd #pandas will help you open your csv file and display as a table (dataframe)

st.set_page_config(layout='wide')

#What is a CSV file?
#csv file is a text file that each data is separated by a comma (comma separated values)

df = pd.read_csv('score.csv')
st.dataframe(df,use_container_width=True)

name = st.text_input("Enter the student's name: ")
maths = st.number_input("Enter the student's score for Maths: ",0,value=70,step=1)
english = st.number_input("Enter the student's score for English: ",0,value=70,step=1)
science = st.number_input("Enter the student's score for Science: ",0,value=70,step=1)
history = st.number_input("Enter the student's score for History: ",0,value=70,step=1)
geography = st.number_input("Enter the student's score for Geography: ",0,value=70,step=1)
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


#The student_df will create a dictionary and convert immediately to a dataframe

#Next we concatenate (join) the old df with the student_df. Do NOT include the index position in the CSV file

#Finally write the the new df in the csv file

if st.button("Submit Student Scores"):
  students_df = pd.DataFrame({'Name':[name],'Maths':[maths],'English':[english],"Science":[science],
                  'History':[history],'Geography':[geography],'Total':[total],'Average':[average],
                  'Grade':[grade]})
  new_df = pd.concat([df,students_df])
  new_df.to_csv('score.csv',index=False)

  st.success(f"{name}'s total score is {total}. The average is {average} and the grade is {grade}")