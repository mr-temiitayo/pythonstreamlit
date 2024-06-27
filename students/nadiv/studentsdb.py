import streamlit as st
import pandas as pd #used to read csv files and display as dataframe (table)
import plotly.express as px #used to plot charts

st.set_page_config(layout='wide')
# st.subheader("Student Grades")

# what is a CSV file?
# This is a text file, where all the values are separated by a comma (comma separated values)


database = pd.read_csv("scores.csv")
menu = st.sidebar.selectbox('Menu',['Submit Scores', 'Database|Chart','Student File'])
studentID = 'Student_'+str(len(database)+1)
   

if menu == 'Submit Scores':

   name = st.text_input("Enter the students name: ")


   c1,c2 = st.columns(2)


   with c1:
      math = st.number_input("Enter the students math results: ",1,7)
      english = st.number_input("Enter the students english results; ",1,7)
      science = st.number_input("Enter the students science results: ",1,7)
   with c2:
      hum = st.number_input("Enter the students humanities results:",1,7)
      art = st.number_input("Enter the students art results: ",1,7)
      tech = st.number_input("Enter the students tech results: ",1,7)


   total = hum + art + science + english + math
   avg = int(total/5)


   if avg == 8:
      grade = "A+"
   elif avg == 7:
      grade = "A"
   elif avg == 6:
      grade = "B+"
   elif avg == 5:
      grade = "B"
   elif avg == 4:
      grade = "C"
   elif avg <= 3:
      grade = "F"

   # Name,Maths,English,Humanities,Science,Art,Total,Average,Grade
   if st.button("Submit student scores"):
      student_dict = {'StudentID':[studentID],'Name':[name],'Maths':[math],'English':[english],
                                       'Humanities':[hum],'Science':[science],'Art':[art],'Tech':[tech],'Total':[total],'Average':[avg],'Grade':[grade]}
      student_database = pd.DataFrame(student_dict)
      #i created a dictionary of csv columns:python variable, 
      # then converted it to a dataframe (table)
      # st.dataframe(student_database)
      new_database = pd.concat([database,student_database],ignore_index=True) #Join the old database with the new one (student_database)
      new_database.to_csv('scores.csv',index=False) #write/save the new_database to a csv file
      st.success(f"{name} total score is {total}. {name}'s average is {avg}, {name}'s final grade is {grade}")



if menu == 'Database|Chart':
   st.table(database)

   #now let's make a chart. First we need to get the subjects as a list

   subjects = ['Maths','English','Humanities','Science','Art','Tech'] #list  for all subjects
   subjectstable = database[subjects].mean().reset_index() #got the mean of all subjects
   subjectsrename = subjectstable.rename(columns={'index':'Subject', 0:'Grade'}) #renamed the columns
  
   chart = st.radio('Choose your chart',['Bar Chart','Pie Chart'],horizontal=True)

   if chart == 'Bar Chart':

      barchart = px.bar(subjectsrename, x='Subject',y='Grade') #x = categories, y = values
      st.plotly_chart(barchart) #plot the chart

   elif chart == 'Pie Chart':
      piechart = px.pie(subjectsrename, names = 'Subject', values= 'Grade')
      st.plotly_chart(piechart)
   

if menu == "Student File":
   header1, header2, header3 = st.columns(3)

   with header3:
      st.subheader("Find Student's File")
      findID = st.text_input("Enter student ID")
      findbutton = st.button("Find Student")

   if findbutton:
      if findID:
         pass