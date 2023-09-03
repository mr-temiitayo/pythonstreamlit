import streamlit as st
#File processing pkgs
from PIL import Image
import pandas as pd
import docx2txt #to open doc files
#textract #also to open doc files
#from PyPDF2 import PdfFileReader #pdfreader
import pdfplumber #also to read pdf

#load images
@st.cache


def code():
    st.title("Converting Files with Python")

    menu= ['Home','Dataset','Document Files','About']
    choice = st.sidebar.selectbox('Menu',menu)

    if choice =='Home':
        st.subheader('Home')
        image_file = st.file_uploader("Upload Images", type = ["png","jpg","jpeg"])
        if image_file is not None:
            #st.write(type(image_file)) #image attr
            #st.write(dir(image_file)) #image attr
            image_details = {"filename":image_file.name,"filetype":image_file.type,"filesize":image_file.size} 
            st.write(image_details)
            st.image(Image.open(image_file),250,250) #open the image uploaded


    elif choice =='Dataset':
        st.subheader('Dataset')
        csv_file = st.file_uploader("Upload CSV", type=["csv"])
        if csv_file is not None:
            #st.write(type(data_file))
            csv_details = {'filename': csv_file.name, 'filetype':csv_file.type,'filesize':csv_file.size}
            st.write(csv_details)
            df = pd.read_csv(csv_file)
            st.dataframe(df)

    elif choice =='Document Files':
        st.subheader('Document Files')
        doc_file = st.file_uploader("Upload Document",type=['pdf','docx','txt'])
        if st.button('Process'):
            if doc_file is not None:
                doc_details = {'filename': doc_file.name, 'filetype':doc_file.type,'filesize':doc_file.size}
                st.write(doc_details)
                if doc_file.type == "text/plain":
                    doc_text = str(doc_file.read(), 'utf-8') #uses txt formatting
                    st.write(doc_text)
                    st.subheader("method 2") 
                    st.text(doc_text)  #no formatting
                elif doc_file.type == "application/pdf": #if file is pdf format
                    try:
                        with pdfplumber.open(doc_file) as pdf:
                            pages = pdf.pages[0] #read first page
                            st.write(pages.extract_text())
                    except:
                        st.write('None')
                else:
                    raw_doc = docx2txt.process(doc_file)
                    st.write(raw_doc)




    else:
        st.subheader('About')



code()