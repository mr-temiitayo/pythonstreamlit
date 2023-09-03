# Creating students scores database
# -Get info of each student (name, 4 subjects score)
# -Calculate the average of total score of each student
# -Grade the student with (A,B,C,D,E,F) -----
# -Save all data in a csv file
# -Show current csv database file


import streamlit as st
import pandas as pd
st.header('Student Database')

df=pd.read_csv('scores.csv')
st.dataframe(df)



name=st.text_input('Enter student name')

math=st.number_input('Enter your math score',0,100,value=0)
english=st.number_input('Enter your english score',0,100,value=0)
physics=st.number_input('Enter your physics score',0,100,value=0)
chemistry=st.number_input('Enter your chemistry score',0,100,value=0)

average=(math+english+physics+chemistry)/4

if average > 80:
    grade = "A"
    st.write('Your grade is A')
elif (average>=70) and (average<=80):
    grade ="B"
    st.write('Your grade is B')
elif(average>=60) and (average<70):
    grade ="C"
    st.write('Your grade is C')
elif(average>=50) and (average<60):
    grade ="D"
    st.write ('Your grade is D')
elif(average>=45) and (average<50):
    grade ="E"
    st.write('Your grade is E')
elif(average<=44):
    grade ="F"
    st.write('Your grade is F')



def new_student(name,math,english,physics,chemistry,average,grade,df):
  student_dict= {'Name':name,'Math':math,'English':english,'Physics':physics,'Chemistry':chemistry,'Average':average,'Grade':grade}
  new_df = pd.DataFrame([student_dict],columns=["Name",'Maths','English','Pyhsics','Chemistry','Average','Grade'])  
  df = pd.concat([df,new_df],ignore_index=True)
  return df 

if st.button ('Add Student score'):
  df=new_student(name,math,english,physics,chemistry,average,grade,df)
  df.to_csv('scores.csv',index=False)
  st.success('Student Scores Added')
