# submit students information (student name, scores) DONE
# The computer will calc the (total, average, grade of student) DONE
# save each submitted info into a CSV file (appear and fade singular table) DONE
# create a database with chart and with filter DONE
# teacher can edit the database DONE
# download the database csv file DONE
#how to make sure scores edited will be recalculated DONE
#sort database scores by grade DONE
#edit database page should have clear data button for all db or just one student
# search students file
# computer send a mail

import streamlit as st
import pandas as pd #pandas help to open, read, and display CSV files as a table (dataframe)


readcsv = pd.read_csv('scores.csv') #read csv file

menu = st.sidebar.selectbox('Menu',['Submit Scores','View Database'])


if menu == 'Submit Scores':    
    inputname = st.text_input("Student name:")
    engscorecol,matscorecol = st.columns(2)
    with engscorecol:
        engscore = st.number_input("Student's score in English:",0)
    with matscorecol:
        matscore = st.number_input("Student's score in Maths:",0)


    sciscorecol,medscorecol = st.columns(2)
    with sciscorecol:
        sciscore = st.number_input ("Student's score in Science:",0)
    with medscorecol:
        medscore = st.number_input ("Student's score in Media:",0)
    totalscore = (engscore + matscore+sciscore+medscore)




    average = totalscore/4
    if average >= 90:
        grade = "A+"
    elif average >=80:
        grade = "A"
    elif average >=70:
        grade = "B"
    elif average >=60:
        grade = "C"
    elif average >=50:
        grade = "D"
    elif average <50:
        grade = "F"


    if st.button ("Check your overall score:"):
        st.write (f"Your total score is {totalscore} and your average is {average} and your grade is {grade}")
        #dictionary, dataframe, join the old and new dataframe, then save combined dataframe
        studentdict = {'Name':[inputname],'Math':[matscore],'English':[engscore],'Science':[sciscore],'Media':[medscore],'Total':[totalscore],'Average':[average],'Grade':[grade]}
   

if menu == 'View Database':
    st.table(readcsv)