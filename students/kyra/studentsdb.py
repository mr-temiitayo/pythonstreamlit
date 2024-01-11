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
st.table(df)#here streamlit will display it as a table


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
elif average >=80 and average <89:
    grade = "A"
elif average >=70 and average <79:
    grade = "B"
elif average >=60 and average <=69:
    grade = "C"
elif average >=50 and average <=59:
    grade = "D"
elif average <50:
    grade = "F"

but1,but2 = st.columns(2)
# Name,Maths,English,Science,Media,Total,Average,Grade
with but1:
    if st.button ("Submit Student score"):
        st.success(f'{inputname} your total score is {totalscore} your average is {average} and your grade is {grade}')
        # f-string is used to print all data in variables as a string.All variables must be in a curly/dict brackets
        #create a dictionary that stores the variable names and the data inside
        studentdict = {'Name':[inputname],'Maths':[matscore],'English':[engscore],'Science':[sciscore],'Media':[medscore],'Total':[totalscore]}


