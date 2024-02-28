#Project Objective
# Create a student scores database which can
# -get the name done
# -4 subjects done
# -calculate the average
# -calculate the grade (A,B,C,D,E,F)
# -update your csv file




#what is csv file?
#csv file are text files that each data is separated by a comma (comma separated values)




import streamlit as st #for the python webpage
import pandas as pd #this is used to read csv files and convert to a table (dataframe)
import plotly.express as px #this is used for the charts


st.set_page_config(layout='wide')    
df=pd.read_csv('Studentdb.csv') #pandas should read this csv file
menu = st.sidebar.selectbox('Menu',['Student Score Input','Student Data Base'])




if menu == 'Student Score Input':
    n = st.text_input("Name:")
    N,E = st.columns(2)
    with N:
       
        m = st.number_input("Math Score",0,100)
        c = st.number_input("Computer Score",0,100)
    with E:
        e = st.number_input("English Score",0,100)
        s = st.number_input("Science Score",0,100)


    st.write(" ")
    st.write(" ")
    submit = st.button("Submit")


    total = e+m+s+c
    average = total/4
    if average <=100 and average >90:
        grade = ("A")
    if average <=90 and average >80:
        grade = ("B")
    if average <=80 and average >70:
        grade = ("C")
    if average <=70 and average >60:
        grade = ("D")
    if average <=60 and average >50:
        grade = ("E")
    if average <=50:
        grade = ("Fail")
    def new_student(n,e,m,s,c,total,average,grade,df):
        student_df = pd.DataFrame({'Name':[n],'English':[e],'Maths':[m],'Science':[s],'Computer':[c],'Total':[total],'Average':[average],'Grade':[grade]})
        new_df = pd.concat([df,student_df],ignore_index=True)
        new_df.to_csv('Studentdb.csv',index=False)
        return new_df


    if submit:
        st.success(f'Your total is {total} mark, average is {average} mark, your grade is {grade}')
        new_df = new_student(n,e,m,s,c,total,average,grade,df)
        new_df.to_csv('score.csv',index=False)


if menu == 'Student Data Base':
    st.title('Students Scores Database')
    st.table(df) #streamlit should display as dataframe


    subjects = ['English','Maths','Science','Computer'] #these are the subjects i want to plot
    subjects_ave = df[subjects].mean().reset_index() #this will create a new df with just 4 columns and the average score
    subjects_rename = subjects_ave.rename(columns = {'index': 'Subject', 0: 'Average'})
    st.table(subjects_rename)


    barchart = px.bar(subjects_rename, x = 'Subject', y= 'Average')

    st.plotly_chart(barchart)


   
