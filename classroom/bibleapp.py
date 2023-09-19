import streamlit as st
import streamlit.components as stc

import pandas as pd
import neattext.functions as nfx

import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import altair as alt

@st.cache_data
def load_bible(data):
    df = pd.read_csv(data)
    return df

def code():
    st.title("Bible App")
    menu = st.sidebar.selectbox('Menu',['Bible Verse','About'])
    df = load_bible('KJV_Bible.csv')
    #st.dataframe(df)

    if menu =='Bible Verse':
        st.subheader("Bible Verse Search")

        book_list = df['book'].unique().tolist() #create unique values from book columns, removes diplicates
        book_name = st.sidebar.selectbox('Book',book_list)
        chapter = st.sidebar.number_input('Chapter',1)
        verse = st.sidebar.number_input('Verse',1)
        bible_df = df[df['book'] == book_name]
        #st.dataframe(bible_df) #this will only show df of selected bible_chapter

        col1,col2 = st.columns([2,1])

        with col1:
            try: #some verses might not be there, this will help know what to do
                selected_passage = bible_df[(bible_df['chapter'] == chapter) & (bible_df['verse'] == verse)]
                st.write(selected_passage)
                passage_details = f'{book_name} Chapter::{chapter} Verse::{verse}'
                st.info(passage_details)
                passage = '{}'.format(selected_passage['text'].values[0])
                st.write(passage)
            except Exception as e:
                raise e







code()