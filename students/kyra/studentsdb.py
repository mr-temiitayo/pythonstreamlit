#  Create a student scores database which can
#  -get the name of the student
#  -get 4 subjects score
#  -calculate the average of the subjects
#  -calculate the grade (A,B,C,D,E,F) using the average
#  -update your csv file
# What is a CSV file?
# A CSV file is a text file that each data is seperated by a comma (comma seperated values)


import streamlit as st
import pandas as pd #pandas help to open, read, and display CSV files as a table (dataframe)


st.set_page_config(layout = 'wide') # this makes our page full width


st.header("Student's Scores Database")


df = pd.read_csv('scores.csv') # here pandas will read the csv file  
st.dataframe(df,use_container_width= True)#here streamlit will display it as a table (dataframe)


inputname = st.text_input("Student name:")
engscore,matscore = st.columns(2)
with engscore:
    engscore = st.number_input("Student's score in English:")
with matscore:
    matscore = st.number_input("Student's score in Maths:")


sciscore,medscore = st.columns(2)
with sciscore:
    sciscore = st.number_input ("Student's score in Science:")
with medscore:
    medscore = st.number_input ("Student's score in Media:")
totalscore = (engscore + matscore+sciscore+medscore)
average = totalscore /4

if average >=90:
    grade ='A+'
if average >=80 and average <89:
    grade = "A"
if average >=70 and average <79:
    grade = "B"
if average >=60 and average <=69:
    grade = "C"
if average >=50 and average <=59:
    grade = "D"
if average <50:
    grade = "F"

#1this function will get the data for each new student
#2dictionary will be used to get the CSV columns names and assign it to it's variable
#Name,Maths,English,Science,Media,Total,Average,Grade
#3 next, we convert the dictionary now to a dataframe
#4 next is concatenation. Append/concatenate the new student_df to the exisiting df
#5 next is to return new_df (when you call the function, runs the new_df)
def new_student(inputname,engscore,matscore,sciscore,totalscore,average,grade,medscore,df):
    student_dict = {'Name':inputname,'Maths':matscore,'English':engscore,'Science':sciscore,
                    'Media':medscore,'Total':totalscore,'Average':average,'Grade':grade}
    student_df = pd.DataFrame([student_dict])
    new_df = pd.concat([df,student_df],ignore_index = True)
    return new_df

if st.button ("Submit student score"):
    st.write(inputname,"your total score is",totalscore,"your average is",average,"and your grade is", grade)
    new_df = new_student(inputname,engscore,matscore,sciscore,totalscore,average,grade,medscore,df)
    new_df.to_csv('scores.csv',index=False)