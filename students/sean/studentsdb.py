#Project Objective
# Create a student scores database which can
# -get the name
# -5 subjects
# -calculate the average
# -calculate the grade (A,B,C,D,E,F) using the average
# -save and update your csv file


import streamlit as st
import pandas as pd #this is what we use to read csv files and convert to a table (dataframe)
st.set_page_config(layout='wide')

# what is CSV file?
#A CSV file is a text file that each data is separated by a comma (comma separated values)


df = pd.read_csv("scores.csv")
st.dataframe(df,use_container_width=True)


name = st.text_input("Enter your name: ")


math = st.number_input("Enter you math score: ",step = 1)


english = st.number_input("Enter your english score: ",step = 1)


science = st.number_input("Enter your science score: ",step = 1)


computer = st.number_input("Enter your you computer score: ",step = 1)


history = st.number_input("Enter your history score: ",step = 1)


total = math+english+science+computer+history
average = total / 5


if (average >= 90) and (average <= 100):
   grade = "A+"
elif (average >= 80) and (average < 90):
   grade = "A"
elif (average >= 70) and (average < 80):
   grade = "B"
elif (average >= 60) and (average < 70):
   grade = "C"  
elif (average >= 50) and (average < 60):
   grade = "D"
elif average < 50:
   grade = "F"
#ctrl [


#we created a function to get all the values for each students
# next we created a dict to attach the CSV variables to their variables
def new_student(name,maths,english,science,computer,history,total,average,grade,df):
   student_dict = {"Name":name,'Math':maths,'English':english,"Science":science,
                   "Computer":computer,"History":history,"Total Score":total,"Average":average,"Grade":grade}
   



if st.button("Show me my score"):
  st.success(f"Your name is {name},your total score is {total},average is {average} and grade is {grade}")



