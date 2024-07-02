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

menu = st.sidebar.selectbox('Menu',["Student Scores", "Database|Chart",'Student File'])


if menu == "Student Scores":
    st.subheader("Fill in students scores here")
    left,right = st.columns(2)

    with left:
        name = st.text_input("Enter student name")
        math = st.number_input("Enter student Math score",0,100,step=10)
        computer = st.number_input('Enter student Computer score',0,100,step=10)

    with right:
        year = st.selectbox("Enter student year",['Year 1','Year 2','Year 3','Year 4','Year 5','Year 6'])
        eng = st.number_input("Enter student English score",0,100,step=10)
        sci = st.number_input("Enter student Science score",0,100,step=10)

#create a total and average
#create a grading system from A to F using conditional statements
#display the result after the button is clicked like this: Jeida, Total score is: 200, Average is: 60, Grade is C

    if st.button("Submit student scores"):
        pass