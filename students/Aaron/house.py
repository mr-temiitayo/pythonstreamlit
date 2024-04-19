

import streamlit as st
import pandas as pd


readcsv = pd.read_csv('salary.csv')




page = st.sidebar.selectbox('Menu', ['Input Data', 'Database'])


if page == 'Input Data':
    st.header('Input Data Here')
    name = st.text_input('Enter Name:')
    salary = st.number_input('Input Salary: $',step=100000)


    save = st.button('Save Data')


    if save:
        st.success('Saved')
        if salary >= 499999:
            house = ('Mansion')
        elif salary >= 99999:
            house = ('Duplex')
        elif salary >= 49999:
            house = ('Bungalow')
        else:
            house = ('Apartment')
        csvdict = {'Name':[name], 'Salary':[salary], 'House_Type':[house]}
        csvdf = pd.DataFrame(csvdict)


        newtable = pd.concat([readcsv,csvdf],ignore_index=True)
        newtable.to_csv('salary.csv',index=False)
       






if page == 'Database':


    editcheckbox=st.sidebar.checkbox('Edit Data')
    if editcheckbox:
        edit_table = st.data_editor(readcsv,width=800,height=800)
        if st.sidebar.button('Save Edits'):
            editsaved = edit_table.to_csv('salary.csv',index=False)
            save1, save2 = st.sidebar.columns(2)
            with save1:
                st.success('Saved Edits!')


    else:
        salary_bins = [-float('inf'), 50000, 100000, 500000, float('inf')]
        house_types = ['Apartment', 'Bungalow', 'Duplex', 'Mansion']
        readcsv['House_Type'] = pd.cut(readcsv['Salary'], bins=salary_bins, labels=house_types)
        readcsv.to_csv('salary.csv',index=False)
        st.table(readcsv)
