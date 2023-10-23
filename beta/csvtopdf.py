import streamlit as st
import pandas as pd
import tabula
from io import BytesIO

# Title of the Streamlit app
st.title("CSV to PDF Converter")

# File upload widget
csv_file = st.file_uploader("Upload a CSV file", type=[".csv"])

# Convert the CSV file to PDF
if csv_file is not None:
    if st.button("Convert to PDF"):
        st.text("Converting...")

        # Read the CSV file into a DataFrame
        df = pd.read_csv(csv_file)

        # Create a BytesIO buffer to store the PDF content
        pdf_buffer = BytesIO()

        # Convert the DataFrame to PDF using tabula
        tabula.convert_into(df, pdf_buffer, output_format="pdf", pages="1")

        # Display the PDF
        st.text("Conversion completed!")
        st.write(pdf_buffer.getvalue())

        # Offer the PDF as a download link
        st.markdown(get_binary_file_downloader_html(pdf_buffer, "output.pdf", "Download PDF"), unsafe_allow_html=True)

# Function to create a download link for a binary file
def get_binary_file_downloader_html(bin_file, file_label, button_label):
    with open(bin_file.name, "wb") as f:
        f.write(bin_file.read())
    href = f'<a href="data:application/octet-stream;base64,{bin_file.getvalue().hex()}" download="{file_label}">{button_label}</a>'
    return href
