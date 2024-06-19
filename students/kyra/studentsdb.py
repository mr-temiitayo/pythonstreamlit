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


import streamlit as st #streamlit creates a page for your python app

st.header(':blue[Enter Student Scores]')

col1, col2 = st.columns([2,1])

with col1:
    name = st.text_input('Please enter student name')

with col2:
    grade = st.selectbox('Please choose student grade',['Grade 1', 'Grade 2','Grade 3','Grade 4','Grade 5','Grade 6'])


sub1, sub2 = st.columns(2)

with sub1:
    math = st.number_input("Please enter student Math score ",0,100,step=10)
    art = st.number_input("Please enter student Art score",0,100,step=10)
    comp = st.number_input("Please enter student Computer score",0,100,step=10)




with sub2:
    eng = st.number_input("Please enter student English score",0,100,step=10)
    sci = st.number_input("Please enter student Science score",0,100,step=10)
    french = st.number_input("Please enter student French score",0,100,step=10)


#homework: create a total and and average variables
#and display after the submit button is clicked
