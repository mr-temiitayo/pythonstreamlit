import streamlit as st
import pandas as pd #used to read CSV and display as dataframe (table)

st.set_page_config(layout="wide")
st.header("Student's Grades Database")

db = pd.read_csv("scores.csv") #read the CSV file
st.dataframe(db,use_container_width=True) #display CSV as table 

#variables to show in CSV = Name,Maths,English,Science,History,Total,Average,Grade
n1,n2 = st.columns(2)
with n1:
    name=st.text_input("Enter the student's name: ")


mathscol,engcol=st.columns(2)


with mathscol:
 mathscore=st.number_input("Enter the student's score for Maths: ",0,100)


with engcol:
 englishscore=st.number_input("Enter the student's score for English: ",0,100)


sciencecol,histcol=st.columns(2)


with sciencecol:
 sciencescore=st.number_input("Enter the student's score for Science: ",0,100)


with histcol:
 historyscore=st.number_input("Enter the student's score for History: ",0,100)


totalscore=mathscore+englishscore+sciencescore+historyscore
averagescore=totalscore/4


if averagescore>=90:
  grade='A+'
 
elif averagescore>=80:
  grade='A'


elif averagescore>=70:
  grade='B'


elif averagescore>=60:
  grade='C'


elif averagescore>=50:
  grade='D'


elif averagescore<50:
 grade='F'

# Name,Maths,English,Science,History,Total,Average,Grade
sub1,sub2 = st.columns(2)
with sub1:
    if st.button("Submit student scores"):
        st.success(f"{name} your Total score is: {totalscore}, Average score is: {averagescore}, your Grade is: {grade}")
        student_database = pd.DataFrame({'Name':[name],'Maths':[mathscore],'English':[englishscore],'Science':[sciencescore],
                                 'History':[historyscore],'Total':[totalscore],'Average':[averagescore],'Grade':[grade]})
        st.dataframe(student_database)
        new_database = pd.concat([db,student_database],ignore_index=True) #join the old db to the student database
        new_database.to_csv('scores.csv',index=False) #write the new new database (concat) in the file


