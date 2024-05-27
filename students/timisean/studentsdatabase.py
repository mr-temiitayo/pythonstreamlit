#Create a page for school teachers to ask for the name of the student, grade 5 subjects scores and calculate the grade

import streamlit as st

head1, head2,head3 = st.columns([1,2,1])

with head2:
    st.subheader(":blue[Grange International School]")

col1,col2 = st.columns(2)

with col1:
    name = st.text_input("Enter student name")
    math = st.number_input("Enter student math score",0)
    science = st.number_input("Enter student science score",0)
    computer = st.number_input("Enter student computer score",0)

with col2:
    grade = st.selectbox('Choose student year',[1,2,3,4,5,6])
    english = st.number_input("Enter student English score",0)
    art = st.number_input("Enter student Art score",0)
    st.write('')
    st.write("")
    submit = st.button("Submit student score")

total = math+english+science+computer+art

average = total/5

#70-100 = A
#60-69 = C
#50-59 = P
#0-49 = F

if submit:
    if average >= 70:
        grade = 'A'
        st.success(f"{name} your total score is: {total}. Average is {average}. Grade is {grade}")
        st.balloons()

    elif average >= 60 and average < 70:
        grade = 'C'
        st.info(f"{name} your total score is: {total}. Average is {average}. Grade is {grade}")

    elif average >= 50 and average < 60:
        grade = 'P'
        st.warning(f"{name} your total score is: {total}. Average is {average}. Grade is {grade}")

    elif average < 50:
        grade = 'F'
        st.error(f"{name} your total score is: {total}. Average is {average}. Grade is {grade}")


