#Homework 1:
#Read any csv file and display as a dataframe


#Project Objective
# Create a student scores database which can
# -get the name
# -4 subjects
# -calculate the average
# -calculate the grade (A,B,C,D,E,F) using the average
# -save and update your csv file


#import streamlit as st
#import pandas as pd #used to read a csv file and convert to a table (dataframe)


#What is a CSV file?
#A CSV file is a text file that each data is separated by a comma (comma separated values)

import streamlit as st
import pandas as pd

#settings 
st.set_page_config(layout='wide')
df = pd.read_csv('homework.csv')
st.dataframe(df,use_container_width=True)

#input statements and calculations
name = st.text_input("Pls enter student name")
math = st.number_input("How much did you get in Math",value=0)
english = st.number_input("How much did you get in english",value=0)
science = st.number_input("How much did you get in Science",value=0)
total = math + english + science
average = total / 3

#if statement for grade
if average >=0 and average <=85:
     grade = "F"
elif average >=35 and average <=86:
     grade = "D"
elif average >=55 and average <=87:
     grade = "C"
elif average >=65 and average <=88:
     grade = "B"
elif average >=80 and average <=89:
     grade = "A"
elif average >= 90:
     grade = "A+"
       
#1the function helps you get all the required data for the student
#MORE EXAMPLES OF DICT NEXT CLASS

# Name,Math,Science,English,Average,Total,Grade
def new_student(name,math,english,science,total,average,grade,df):
     student_dict ={'Name':name,'Maths':math,'English':english,
                    "Science":science,"Total":total,"Average":average,'Grade':grade}#this connects the CSV columns to their variables
     student_df = pd.DataFrame([student_dict]) #this converts the dictionary to a dataframe
     new_df = pd.concat([df,student_df],ignore_index=False) #this will concatenate (join) the old df to the student df
     return new_df #when i call my function, run and show me my new df



if st.button("Submit Student Scores"):
    st.success(f"{name}'s total score is {total}. The average is {average}. And the grade is {grade}.")
    new_df = new_student(name,math,english,science,total,average,grade,df)
    new_df.to_csv('homework.csv',index=False)