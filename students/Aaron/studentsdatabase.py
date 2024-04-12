import streamlit as st #this is the webpage for our python projects
import pandas as pd #this helps to read, write CSV files, and convert them to a table 
import plotly.express as px #helps us to plot charts

# submit students information (student name, scores) DONE
# The computer will calc the (total, average, grade of student) DONE
# save each submitted info into a CSV file (appear and fade singular table)
# create a database with chart and with filter
# download the database
# teacher can edit the database
# search students file
# computer send a mail
#edit database page should have clear data button



#CSV file is a text file that has all it's data separated by a comma (COMMA SEPARETED VALUES)

readcsv = pd.read_csv('scores.csv',dtype={'Average': str}) #pandas reads CSV file


menu = st.sidebar.selectbox('Menu',['Submit Scores',  'Students Database','Scores Charts', 'Search Student'])


if menu == 'Submit Scores':
    st.header('Submit Students Scores Here')
    name = st.text_input("Enter the student's name")




    subject1, subject2 = st.columns(2)




    with subject1:
        maths = st.number_input("Enter student's score for Maths",0,100,step=10,value=50)
        science = st.number_input("Enter student's score for Science",0,100,step=10,value=50)
        art = st.number_input("Enter student's score for Art",0,100,step=10,value=50)




    with subject2:
        english = st.number_input("Enter student's score for English",0,100,step=10,value=50)
        history = st.number_input("Enter student's score for History",0,100,step=10,value=50)
        geography = st.number_input("Enter student's score for Geography",0,100,step=10,value=50)




    totalscore = maths + science + art + english + history + geography




    average = totalscore /6
    average = round(average,2)



    #st.success, error, warning, info
    if average >= 90:
        grade = ("A+")
    elif average >= 85:
        grade = ("A")
    elif average >= 80:
        grade = ("A-")
    elif average >= 75:
        grade = ("B+")
    elif average >= 70:
        grade = ("B")
    elif average >= 65:
        grade = ("C+")
    else:
        grade = ("FAIL")


    savebutton = st.button("Save Students Scores")


    if savebutton:
        if grade != ("FAIL"):
            st.success(f"{name}'s total score is {totalscore} points, their average is: {average}%, and their grade is: {grade}.")
        else:
            st.error(f"{name}'s total score is {totalscore} points, their average is: {average}%, and their grade is: {grade}.")
        
    
        #Here we create the dictionary to store the key and the data, then we convert to a df using pandas
        studentsdict = {'Name':[name],'Maths': [maths],'English':[english],'Science':[science],'Art':[art],
                        'Geography':[geography],'History':[history],'Total Score':[totalscore],'Average':[average],'Grade':[grade]}
        # st.write(studentsdict)
        studentsdf = pd.DataFrame(studentsdict) #converts to dataframe
        # st.table(studentsdf)
        newtable = pd.concat([readcsv,studentsdf],ignore_index=True) #joins the 2 tables together. old + new
        newtable.to_csv('scores.csv',index=False) #saves the newtable into the csv file
        #Next we join the existing df with the new df and save it on the csv file
        

if menu == "Students Database":
    editcheckbox=st.sidebar.checkbox('Edit Database')
    if editcheckbox:
        edit_table = st.data_editor(readcsv,width=800,height=800)

        if st.sidebar.button("Save Database"):
            saved_edit = edit_table.to_csv('scores.csv',index=False)
            save1, save2 = st.sidebar.columns(2)
            with save1:
                st.sidebar.success('Edits Saved')
    else:
        st.table(readcsv) #streamlit displays the csv file

    

if menu == 'Scores Charts':
    #what if teach wants to see gender based score chart?

    radio1, radio2 = st.columns(2)

    with radio1:
        selectchart = st.radio('Choose Preferred Chart to Plot', ['Bar Chart', 'Pie Chart'],horizontal=True)
    #now let's plot the bar chart
    subjects = ['Maths','English','Science','Art','Geography','History'] #subjects for new table to plot
    subjectstable = readcsv[subjects].mean().reset_index() #displays only the 5 columns on the table
    renamedcolumns = subjectstable.rename(columns = {'index': 'Subject', 0: "Score"})
    # st.table(renamedcolumns)

    if selectchart == 'Bar Chart':
        barchart = px.bar(renamedcolumns, x = 'Subject', y = 'Score')
        st.plotly_chart(barchart)

    elif selectchart == 'Pie Chart':
        piechart = px.pie(renamedcolumns, names='Subject', values='Score')
        st.plotly_chart(piechart)



# if menu == 'Edit Database':
#     edit_table = st.data_editor(readcsv)