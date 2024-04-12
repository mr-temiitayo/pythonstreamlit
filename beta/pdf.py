import streamlit as st
from fpdf import FPDF

st.title('image pdf convert')

# Function to generate PDF
def generate_pdf():
    # Create instance of FPDF class
    pdf = FPDF()

    # Add a page
    pdf.add_page()

    # Set font for the entire document
    pdf.set_font("Arial", size=12)

    # Define the positions for the columns
    column1_x = 10
    column2_x = 150 # Adjust this value based on the width of column 1 and any padding desired

    # Define the width of each column
    column_width = 90  # Adjust this value as needed



 # Add image to the PDF in a specific column
    pdf.image("employee.png", x=column1_x, y=120, w=50)  # Adjust the image path and size as needed

    # Add content to the PDF in different columns
    pdf.set_font(family='Arial', size=16, style='B')
    pdf.set_xy(column1_x, 20)
    pdf.cell(column_width, 10, txt="New Column 1, Row 1", ln=True, align="L") #width/height


    # Add a divider
    pdf.set_line_width(0.5)  # Set the width of the line
    pdf.line(12, 30, 70, 30)  # Draw a line from start x,y stop x,y
    
    # pdf.line(10, 100, 200, 100)  # Draw a line from (10, 100) to (200, 100)


    
    pdf.set_font(family='Arial', size=12, style='')
    pdf.set_xy(column2_x, 20)
    pdf.cell(column_width, 10, txt="Column 2, Row 1", ln=True, align="L")

    pdf.set_font(family='Arial', size=12, style='')
    pdf.set_xy(column1_x, 40)
    pdf.cell(column_width, 10, txt="Column 1, Row 2", ln=True, align="L")

    pdf.set_font(family='Arial', size=12, style='')
    pdf.set_xy(column2_x, 40)
    pdf.cell(column_width, 10, txt="Column 2, Row 2", ln=True, align="L")

    # Save the PDF
    pdf_file = "example.pdf"
    pdf.output(pdf_file)
    return pdf_file

# Generate the PDF
pdf_file_path = generate_pdf()

# Read the generated PDF as binary data
with open(pdf_file_path, "rb") as f: #properly open and closed using the read binary mode
    pdf_data = f.read() #reads as binary to be processed/downloaded

# Display the download button
st.download_button(label='Download PDF', data=pdf_data, file_name='pdfexample.pdf', mime='application/pdf')
