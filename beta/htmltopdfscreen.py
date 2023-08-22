import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#import pdfkit
#import tempfile  # Import tempfile module
import time  # Import time module
from PIL import Image

# Display multiline text
multiline_text = """
This is a multiline text.

It can have multiple lines.

You can format it with line breaks and whitespace as needed.

In this code:

We define a multiline text using triple quotes.
You can include line breaks and format the text as needed.

We use st.write() to display the multiline text.
Streamlit will render the text as-is, preserving the line breaks and formatting.

When you run this code, Streamlit will display the multiline text in the app.
"""

st.write(multiline_text)

# Use Chrome in headless mode (no GUI) to capture screenshots
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

# Initialize ChromeDriver
driver = webdriver.Chrome(options=chrome_options)


# Navigate to the Streamlit app (replace with your app's URL)


# Wait for the Streamlit content to load (you may need to adjust the wait time)
#time.sleep(5)  # Wait for 5 seconds (adjust as needed)

with st.form(key='download'):
    # Generate a unique timestamp for filenames
    timestamp = int(time.time())  # Using Unix timestamp for uniqueness
    st.write(timestamp)
    # Capture a screenshot
    screenshot_path = f"C:\\Users\\USER\\Documents\\screenshot_{timestamp}.png"
    # Specify the path to wkhtmltopdf executable
    #config = pdfkit.configuration(wkhtmltopdf="C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")

    # Create a button to save as PDF
    if st.form_submit_button("Save as PDF"):
        streamlit_url = "http://localhost:8503"  # Replace with your Streamlit app's URL
        driver.get(streamlit_url)
        # Capture a screenshot
        driver.save_screenshot(screenshot_path)
        # Convert the screenshot to PDF using pdfkit
        #pdf_output_path = "C:\\Users\\USER\\Documents\\screenshot.pdf"  
        #pdfkit.from_file(screenshot_path, pdf_output_path, configuration=config)
        # Display a link to download the PDF
        #st.markdown(f"**[Download this PDF](./{pdf_output_path})**")

        # Open the image file
        img = Image.open(screenshot_path)
        # Create a PDF file and add the image to it
        img.save(f'screenshot_{timestamp}.pdf', 'PDF', resolution=100.0)

        # Close the image file
        img.close()
        st.write('Done. Check Folder')

    # Close the browser
    driver.quit()
