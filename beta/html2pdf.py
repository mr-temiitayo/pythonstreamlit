import streamlit as st
import pdfkit

def main():
    st.title("Save Web Page as PDF")

    # Input field for the user to enter the URL of the page to convert to PDF
    page_url = st.text_input("Enter the URL of the web page:")

    if st.button("Convert to PDF"):
        if page_url:
            try:
                # Define a file name for the PDF output
                pdf_file_name = "output.pdf"

                # Specify the path to the wkhtmltopdf executable
                # Replace 'path_to_wkhtmltopdf' with the actual path on your system
                wkhtmltopdf_path = r"C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe"

                # Configure pdfkit to use the specified wkhtmltopdf executable
                config = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_path)
                pdfkit.from_url(page_url, pdf_file_name, configuration=config)

                # Display a success message and a link to download the PDF
                st.success(f"Web page converted to PDF. [Download PDF](./{pdf_file_name})")
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
        else:
            st.warning("Please enter the URL of the web page to convert.")

if __name__ == '__main__':
    main()
