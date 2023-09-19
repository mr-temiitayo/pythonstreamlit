import streamlit as st
from docx2pdf import convert

# Title of the Streamlit app
st.title("DOC to PDF Converter")

# File upload widget
#doc_file = st.file_uploader("Upload a DOC document", type=[".doc", ".docx"])

# Convert the DOC document to PDF
# if doc_file is not None:
#     if st.button("Convert to PDF"):
#         st.text("Converting...")
#         convert(doc_file.name, "output.pdf")
#         st.success("Conversion completed!")

convert(r'C:/Users/USER/Downloads/STREAMLIT SYLLABUS FINAL.docx', r'C:/Users/USER/Downloads/STREAMLIT SYLLABUS FINAL.pdf')