import streamlit as st
import pandas as pd #read csv and show as table

st.set_page_config(layout='wide')

database = pd.read_csv('scores.csv') 

st.dataframe(database,use_container_width=True)

name = st.text_input("Enter name")

sub1,sub2 = st.columns(2)

#variables Maths, English, Art, History, Total, Average, Grade
with sub1:
   Math = st.number_input("Enter the student's score for math",0,100)
   English = st.number_input("Enter the student's score for english",0,100)

with sub2:
   Art = st.number_input("Enter the student's score for art",0,100)
   History = st.number_input("Enter the student's score for history",0,100)


total = Art+History+Math+English


average = total/4

if average >=90:
   grade = "A+"
elif average >=80 and average <=89:
   grade = "A"
elif average >=65 and average <=88:
   grade = "B"
elif average >=55 and average <=87:
   grade = "C"
elif average >=35 and average <=86:
   grade = "D"
elif average >=0 and average <=85:
   grade = "F"


# Name,Maths,English,Art,History,Total,Average,Grade
sub1,sub2 = st.columns(2)
with sub1:
     if st.button("Submit Student score"):
          st.success(f'{name}, your total score is: {total}. The average is: {average}. The grade is: {grade}')
          student_dict = {'Name':[name],'Maths':[Math],'English':[English],'Art':[Art],'History':[History],
                              'Total':[total],"Average":[average],'Grade':[grade]}
          student_table = pd.DataFrame(student_dict)
          new_database = pd.concat([database,student_table],ignore_index=True) #join the old database with the new database
          new_database.to_csv('scores.csv',index=False) #save the database in a file
          
